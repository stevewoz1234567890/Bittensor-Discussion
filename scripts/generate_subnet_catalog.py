#!/usr/bin/env python3
"""Write discussions/subnet-catalog.md from live Subtensor state.

Requires: pip install bittensor (recommended in a virtual environment).

Example:
    python3 -m venv .venv && .venv/bin/pip install bittensor
    .venv/bin/python scripts/generate_subnet_catalog.py
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone

from bittensor import Subtensor


def _normalized_url(label: str, raw: str) -> str | None:
    u = (raw or "").strip()
    if not u:
        return None
    if label == "Discord" and not u.startswith(("http://", "https://")):
        return None  # Discord field is usually a username, not URL
    if label == "Website" and u.startswith("www."):
        u = "https://" + u
    return u


def _links_block(si) -> str:
    lines: list[str] = []
    if not si:
        return ""
    pairs = (
        ("Website", getattr(si, "subnet_url", "")),
        ("GitHub", getattr(si, "github_repo", "")),
        ("Discord", getattr(si, "discord", "")),
        ("Logo", getattr(si, "logo_url", "")),
    )
    for label, url_raw in pairs:
        u = _normalized_url(label, url_raw or "")
        if u:
            lines.append(f"- [{label}]({u})")
        elif label == "Discord":
            discord = (getattr(si, "discord", "") or "").strip()
            if discord:
                lines.append(f"- **Discord (handle/username):** `{discord}`")

    contact = (getattr(si, "subnet_contact", "") or "").strip()
    if contact:
        lines.append(f"- Contact: {contact}")
    add = (getattr(si, "additional", "") or "").strip()
    if add:
        lines.append(f"- Additional (on-chain): {add}")
    if not lines:
        return ""
    return "\n".join(lines)


def generate(network: str) -> str:
    st = Subtensor(network=network)
    subs = sorted(st.all_subnets() or [], key=lambda x: x.netuid)
    block = st.get_current_block()
    utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = []
    lines.append("# Bittensor subnet catalog")
    lines.append("")
    lines.append(
        "On-chain subnet names, symbols (alpha tickers where applicable), and identity "
        "descriptions copied from Subtensor **`all_subnets()`** (dynamic info + optional "
        "`SubnetIdentity`). This is documentation of what the chain stores, not an "
        "endorsement of any subnet."
    )
    lines.append("")
    lines.append(
        "**How to regenerate:** install `bittensor` (see repo `scripts/requirements-catalog.txt`), "
        "then run `python scripts/generate_subnet_catalog.py`. "
        f"Latest generation used network `{network}` at block **{block}** ({utc}). "
        "Subnets appear and change over time — verify critical details against current explorers and docs."
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    for d in subs:
        sym = getattr(d, "symbol", "") or ""
        name = getattr(d, "subnet_name", "") or f"netuid-{d.netuid}"
        heading = f"### NetUID {d.netuid} — {name}"
        if sym:
            heading += f" (`{sym}`)"
        lines.append(heading)
        lines.append("")
        sid = getattr(d, "subnet_identity", None)

        desc = ""
        if sid and (sid.description or "").strip():
            desc = (sid.description or "").strip()

        if desc:
            for para in [p.strip() for p in desc.split("\n\n") if p.strip()]:
                lines.append(para)
                lines.append("")
        elif sid:
            lines.append(
                "*(Subnet has on-chain identity fields but **no description** field was set.)*"
            )
            lines.append("")
        else:
            lines.append(
                "*(No **`SubnetIdentity`** registered on-chain for this subnet; only name/symbol/meta above are shown.)*"
            )
            lines.append("")

        link_md = _links_block(sid)
        if link_md:
            lines.append("**Registered links**")
            lines.append("")
            lines.append(link_md)
            lines.append("")

        lines.append("")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        "**Sources:** [Bittensor](https://docs.bittensor.com), "
        "`bittensor` Python `Subtensor.all_subnets()`. Explore live data via "
        "[TAOStats — Subnets](https://taostats.io/subnets)."
    )

    # Collapse trailing extra blank lines
    while lines and lines[-1] == "" and lines[-2] == "":
        lines.pop()
    return "\n".join(lines) + "\n"


def main() -> None:
    p = argparse.ArgumentParser(description="Generate subnet catalog Markdown from chain.")
    p.add_argument(
        "--network",
        default="finney",
        help="Subtensor network name (default: finney mainnet-equivalent)",
    )
    p.add_argument(
        "-o",
        "--output",
        default="discussions/subnet-catalog.md",
        help="Output path relative to repo root",
    )
    args = p.parse_args()
    text = generate(args.network)
    with open(args.output, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
