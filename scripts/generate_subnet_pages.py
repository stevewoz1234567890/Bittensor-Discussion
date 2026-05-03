#!/usr/bin/env python3
"""Generate one Markdown file per subnet under subnets/.

Pulls full on-chain identity from Subtensor, optionally fetches a short excerpt
from the subnet website when the URL looks usable.

Usage (from repo root, with bittensor installed):
    python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements-catalog.txt
    .venv/bin/python scripts/generate_subnet_pages.py
    .venv/bin/python scripts/generate_subnet_pages.py --fetch-all-websites   # slower; every URL
"""

from __future__ import annotations

import argparse
import html as html_lib
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from bittensor import Subtensor

ROOT_OVERVIEW = """The **root network** (NetUID 0) is Bittensor’s top-level coordination layer. TAO holders delegate stake to root validators, who set **weights** on other subnets. Those weights help determine how network **emissions** are allocated across subnets. Root is not an application or “task” subnet like higher netuids; it is the mechanism through which the protocol routes incentive and security across the rest of the network."""


def _slugify(name: str) -> str:
    s = (name or "subnet").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-") or "subnet"
    return s[:72].rstrip("-")


def _normalize_site_url(raw: str) -> str | None:
    u = (raw or "").strip()
    if not u:
        return None
    if u.startswith("www."):
        u = "https://" + u
    if not u.startswith(("http://", "https://")):
        return None
    return u


def _fetch_site_excerpt(url: str, timeout: float = 8.0, max_bytes: int = 200_000) -> tuple[str | None, str | None]:
    """Return (title, description_excerpt) best-effort from HTML."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Bittensor-Discussion-catalog/1.0 (documentation; +https://github.com)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            chunk = resp.read(max_bytes)
    except (urllib.error.URLError, OSError, ValueError):
        return None, None

    try:
        text = chunk.decode("utf-8", errors="ignore")
    except Exception:
        return None, None

    title = None
    m = re.search(r"<title[^>]*>([^<]{1,200})</title>", text, re.I)
    if m:
        title = html_lib.unescape(re.sub(r"\s+", " ", m.group(1)).strip())

    desc = None
    for pattern in (
        r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:description["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']description["\']',
    ):
        m2 = re.search(pattern, text, re.I)
        if m2:
            desc = html_lib.unescape(m2.group(1).strip())
            break

    if desc and len(desc) > 800:
        desc = desc[:797] + "…"
    return title, desc


def _overview_for_subnet(
    netuid: int,
    subnet_name: str,
    desc: str,
    additional: str,
    fetch_title: str | None,
    fetch_desc: str | None,
) -> str:
    if netuid == 0:
        return ROOT_OVERVIEW

    parts: list[str] = []
    d = (desc or "").strip()
    a = (additional or "").strip()

    if d:
        parts.append(d)
    if a and a != d:
        parts.append(a)
    if fetch_desc and fetch_desc not in " ".join(parts):
        parts.append(f"**From crawled page (site or GitHub):** {fetch_desc}")
    elif fetch_title and not parts:
        parts.append(
            f"**From crawled page:** document title “{fetch_title}”. Open the links below for full detail."
        )

    if not parts:
        return (
            f"**{subnet_name}** (NetUID {netuid}) does not currently expose a long on-chain description. "
            "Use the registered links and any website excerpt below; confirm the subnet’s purpose on official channels and explorers."
        )

    return "\n\n".join(parts)


def _links_markdown(si) -> str:
    if not si:
        return "*No `SubnetIdentity` registered on-chain.*"
    lines: list[str] = []
    site = _normalize_site_url(getattr(si, "subnet_url", "") or "")
    gh = (getattr(si, "github_repo", "") or "").strip()
    logo = (getattr(si, "logo_url", "") or "").strip()
    discord = (getattr(si, "discord", "") or "").strip()
    contact = (getattr(si, "subnet_contact", "") or "").strip()

    if site:
        lines.append(f"- **Website:** [{site}]({site})")
    if gh:
        lines.append(f"- **GitHub:** [{gh}]({gh})" if gh.startswith("http") else f"- **GitHub:** `{gh}`")
    if discord:
        if discord.startswith(("http://", "https://")):
            lines.append(f"- **Discord:** [{discord}]({discord})")
        else:
            lines.append(f"- **Discord (handle / invite hint):** `{discord}`")
    if logo:
        lines.append(f"- **Logo URL:** [{logo}]({logo})" if logo.startswith("http") else f"- **Logo:** `{logo}`")
    if contact:
        lines.append(f"- **Contact:** {contact}")
    return "\n".join(lines) if lines else "*No links or contacts in chain identity.*"


def render_page(
    d,
    block: int,
    network: str,
    snapshot_utc: str,
    fetch_web: bool,
    delay_s: float,
) -> str:
    netuid = d.netuid
    name = getattr(d, "subnet_name", "") or f"netuid-{netuid}"
    sym = getattr(d, "symbol", "") or ""
    sid = getattr(d, "subnet_identity", None)

    desc = ""
    additional = ""
    if sid:
        desc = (sid.description or "").strip()
        additional = (sid.additional or "").strip()

    fetch_title: str | None = None
    fetch_desc: str | None = None
    site_url = _normalize_site_url((getattr(sid, "subnet_url", "") if sid else "") or "")
    gh = ((getattr(sid, "github_repo", "") if sid else "") or "").strip()
    fetch_url = site_url or (gh if gh.startswith("https://github.com") else None)
    if fetch_web and fetch_url and netuid > 0:
        fetch_title, fetch_desc = _fetch_site_excerpt(fetch_url)
        time.sleep(delay_s)

    title = f"# NetUID {netuid} — {name}"
    if sym:
        title += f" (`{sym}`)"

    lines: list[str] = [
        title,
        "",
        "## Overview",
        "",
        _overview_for_subnet(netuid, name, desc, additional, fetch_title, fetch_desc),
        "",
        "## On-chain description (full)",
        "",
    ]
    if desc:
        lines.append(desc)
    else:
        lines.append("*Empty — no description bytes set in `SubnetIdentity`.*")

    lines.extend(
        [
            "",
            "## On-chain additional details (full)",
            "",
        ]
    )
    if additional:
        lines.append(additional)
    else:
        lines.append("*Empty — no additional field set, or identity missing.*")

    lines.extend(
        [
            "",
            "## Registered contact & links",
            "",
            _links_markdown(sid),
            "",
        ]
    )

    if fetch_title or fetch_desc:
        lines.extend(
            [
                "## Web crawl (supplementary)",
                "",
            ]
        )
        if fetch_title:
            lines.append(f"- **Document title:** {fetch_title}")
        if fetch_desc:
            lines.append(f"- **Meta / og:description:** {fetch_desc}")
        if fetch_url:
            lines.append(f"- **Fetched from:** [{fetch_url}]({fetch_url})")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            f"*Snapshot: Subtensor network `{network}`, block **{block}**, {snapshot_utc}. "
            "Regenerate with `scripts/generate_subnet_pages.py`. On-chain fields are authoritative for registration data; "
            "website excerpts may be outdated or fail for some URLs.*",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--network", default="finney")
    ap.add_argument(
        "--out-dir",
        default="subnets",
        help="Output directory (created if missing)",
    )
    ap.add_argument(
        "--fetch-all-websites",
        action="store_true",
        help="HTTP-fetch every subnet website (slow; many requests)",
    )
    ap.add_argument(
        "--no-supplement-web",
        action="store_true",
        help="Do not fetch any websites (on-chain text only)",
    )
    ap.add_argument(
        "--web-thin-chars",
        type=int,
        default=400,
        help="Try website fetch only if description+additional shorter than this (default 400)",
    )
    ap.add_argument(
        "--delay",
        type=float,
        default=0.35,
        help="Seconds between HTTP fetches",
    )
    args = ap.parse_args()

    st = Subtensor(network=args.network)
    subs = sorted(st.all_subnets() or [], key=lambda x: x.netuid)
    block = st.get_current_block()
    snapshot_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    index_lines = [
        "# Subnet pages (one file per NetUID)",
        "",
        f"Generated from Finney/`{args.network}` at block **{block}** ({snapshot_utc}).",
        "",
        "Each file includes **full verbatim** `SubnetIdentity` sections, an **Overview** that merges chain text "
        "with optional crawled excerpts, and **registered links**. Thin subnets may fetch the marketing site or GitHub project page.",
        "",
        "## Index",
        "",
    ]

    for d in subs:
        netuid = d.netuid
        name = getattr(d, "subnet_name", "") or f"netuid-{netuid}"
        slug = _slugify(name)
        fname = f"{netuid:03d}-{slug}.md"

        sid = getattr(d, "subnet_identity", None)
        desc = ((sid.description or "").strip() if sid else "")
        additional = ((sid.additional or "").strip() if sid else "")
        combined = len(desc) + len(additional)
        site_url = _normalize_site_url((getattr(sid, "subnet_url", "") if sid else "") or "")
        gh_raw = ((getattr(sid, "github_repo", "") if sid else "") or "").strip()
        github_candidate = gh_raw.startswith("https://github.com")
        supplemental_target = site_url or (gh_raw if github_candidate else None)

        if args.no_supplement_web:
            do_fetch = False
        elif args.fetch_all_websites:
            do_fetch = bool(netuid > 0 and supplemental_target)
        else:
            do_fetch = bool(
                netuid > 0 and supplemental_target and combined < args.web_thin_chars
            )

        body = render_page(
            d,
            block=block,
            network=args.network,
            snapshot_utc=snapshot_utc,
            fetch_web=do_fetch,
            delay_s=args.delay,
        )
        (out / fname).write_text(body, encoding="utf-8")
        sym = getattr(d, "symbol", "") or ""
        sym_bit = f" `{sym}`" if sym else ""
        index_lines.append(f"- [{netuid:03d} — {name}{sym_bit}]({fname})")

    index_lines.extend(
        [
            "",
            "---",
            "",
            "Regenerate: `python scripts/generate_subnet_pages.py` (auto-fetches websites for subnets with short on-chain text). "
            "Options: `--fetch-all-websites`, `--no-supplement-web`.",
            "",
        ]
    )
    (out / "README.md").write_text("\n".join(index_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
