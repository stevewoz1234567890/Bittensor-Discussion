#!/usr/bin/env python3
"""Generate one Markdown file per subnet under subnets/.

Pulls chain identity + hyperparameters + short alpha price samples, optionally
TAOStats historical pool prices and GitHub README “requirements” excerpts.

Usage (from repo root, with bittensor installed):
    python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements-catalog.txt
    .venv/bin/python scripts/generate_subnet_pages.py
    TAOSTATS_API_KEY=… .venv/bin/python scripts/generate_subnet_pages.py   # add daily history
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from bittensor import Subtensor
from bittensor.utils.balance import Balance

ROOT_OVERVIEW = """The **root network** (NetUID 0) is Bittensor’s top-level coordination layer. TAO holders delegate stake to root validators, who set **weights** on other subnets. Those weights help determine how network **emissions** are allocated across subnets. Root is not an application or “task” subnet like higher netuids; it is the mechanism through which the protocol routes incentive and security across the rest of the network."""

README_SECTION_KEYS = frozenset(
    (
        "require",
        "prereq",
        "hardware",
        "validator",
        "miner",
        "compute",
        "comput",
        "spec",
        "gpu",
        "cuda",
        "vram",
        "memory",
        "infra",
        "install",
        "setup",
        "recommended",
        "minimum",
    )
)


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


def _fetch_text(url: str, timeout: float = 12.0, max_bytes: int = 750_000) -> str | None:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Bittensor-Discussion-catalog/1.0 (documentation)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read(max_bytes).decode("utf-8", errors="ignore")
    except (urllib.error.URLError, OSError, ValueError):
        return None


def _fetch_site_excerpt(url: str, timeout: float = 8.0, max_bytes: int = 200_000) -> tuple[str | None, str | None]:
    text = _fetch_text(url, timeout=timeout, max_bytes=max_bytes)
    if not text:
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


def _github_repo_raw_readme_candidates(repo_https: str) -> list[str]:
    u = repo_https.strip().rstrip("/")
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?$", u, re.I)
    if not m:
        return []
    org, repo = m.group(1), m.group(2)
    out: list[str] = []
    for br in ("main", "master"):
        out.append(f"https://raw.githubusercontent.com/{org}/{repo}/{br}/README.md")
        out.append(f"https://raw.githubusercontent.com/{org}/{repo}/{br}/readme.md")
    return out


def _extract_readme_spec_sections(markdown_body: str, max_chars: int = 5_500) -> str | None:
    chunks: list[str] = []
    for m in re.finditer(
        r"(^#{1,4}[ \t]+.+?$)(.*?)(?=^#{1,4}[ \t]|\Z)",
        markdown_body,
        re.MULTILINE | re.DOTALL,
    ):
        heading = m.group(1).strip()
        inner = heading.lstrip("#").strip().lower()
        if any(k in inner for k in README_SECTION_KEYS):
            body = m.group(2).strip()
            if body:
                chunks.append(heading + "\n\n" + body)
    if not chunks:
        return None
    joined = "\n\n---\n\n".join(chunks).strip()
    if len(joined) > max_chars:
        joined = joined[: max_chars - 1] + "…"
    return joined


def _readme_specs_from_github(repo_url: str) -> tuple[str | None, str | None]:
    candidates = _github_repo_raw_readme_candidates(repo_url)
    sources: list[str] = []
    for raw_url in candidates:
        text = _fetch_text(raw_url, timeout=10.0, max_bytes=800_000)
        if text and len(text) > 80:
            ex = _extract_readme_spec_sections(text)
            if ex:
                return ex, raw_url
            sources.append(raw_url)
    return None, None


def chain_price_recent_rows(
    st: Subtensor, netuid: int, head: int, *, step: int, max_offset: int
) -> list[tuple[int, float]]:
    rows: list[tuple[int, float]] = []
    off = 0
    while off <= max_offset:
        b = head - off
        try:
            p = st.get_subnet_price(netuid, block=b)
            rows.append((b, float(p.tao)))
        except Exception:
            break
        off += step
    return sorted(rows, key=lambda t: t[0])


def fetch_taostats_pool_history_daily(
    api_key: str, netuid: int, *, limit: int = 56, timeout: float = 25.0
) -> tuple[list[dict] | None, str | None]:
    q = urllib.parse.urlencode(
        {
            "netuid": netuid,
            "frequency": "by_day",
            "limit": min(limit, 200),
            "order": "timestamp_desc",
        }
    )
    url = f"https://api.taostats.io/api/dtao/pool/history/v1?{q}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", api_key)
    req.add_header("User-Agent", "Bittensor-Discussion-catalog/1.0")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8", errors="ignore"))
    except urllib.error.HTTPError as e:
        try:
            err_body = e.read().decode("utf-8", errors="ignore")[:300]
        except Exception:
            err_body = str(e.reason)
        return None, f"HTTP {e.code}: {err_body}"
    except Exception as e:
        return None, str(e)

    data = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(data, list):
        return None, "Unexpected JSON payload from TAOStats"
    return data, None


def format_chain_ops(st: Subtensor, netuid: int, block: int) -> str:
    hp = st.get_subnet_hyperparameters(netuid, block=block)
    si = st.get_subnet_info(netuid, block=block)
    if hp is None and si is None:
        return "*Could not query subnet hyperparameters or info via RPC.*\n"

    lines: list[str] = []

    lines.append(
        "**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, "
        "weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs "
        "(see the next section when GitHub excerpts are available).\n"
    )

    lines.append("### Topology & economics (`SubnetInfo` snapshot)\n")
    if si:
        lines.append(f"- **`max_n` (max registered UIDs):** {si.max_n}")
        lines.append(f"- **`subnetwork_n`:** {si.subnetwork_n}")
        lines.append(f"- **Max validators allowed (`max_allowed_validators`):** {si.max_allowed_validators}")
        lines.append(f"- **Min weights per neuron (`min_allowed_weights`):** {si.min_allowed_weights}")
        lines.append(f"- **`max_weights_limit` (consensus-encoded cap):** {si.max_weight_limit}")
        lines.append(f"- **`tempo` (blocks between epoch advances):** {si.tempo}")
        lines.append(f"- **`scaling_law_power`:** {si.scaling_law_power}")
        lines.append(f"- **`modality` ID:** `{si.modality}`")
        lines.append(f"- **`emission_value` (display field):** {si.emission_value}")
        lines.append(f"- **`difficulty` (PoW field on info view):** {si.difficulty}")
        lines.append(f"- **`immunity_period` (blocks):** {si.immunity_period}")
        lines.append(f"- **Registration recycle cost snapshot (`burn`):** {si.burn}")
        lines.append(f"- **Owner SS58 (`owner_ss58`):** `{si.owner_ss58}`")

        if si.connection_requirements:
            lines.append("- **Subnet connection graph (`connection_requirements`, peer NetUID → weight multiplier):**")
            for nid, wt in sorted(
                si.connection_requirements.items(), key=lambda x: int(str(x[0]))
            ):
                lines.append(f"  - NetUID `{nid}` → {wt}")

    lines.append("")
    lines.append("### Consensus hyperparameters (`SubnetHyperparameters` snapshot)\n")
    if hp:
        lines.append(f"- **Registration allowed:** `{hp.registration_allowed}`")
        lines.append(f"- **`min_burn` / `max_burn` (RAO envelope):** {Balance.from_rao(hp.min_burn)} / {Balance.from_rao(hp.max_burn)}")
        lines.append(
            f"- **PoW `difficulty` + bounds:** `{hp.difficulty}` (min `{hp.min_difficulty}`, max `{hp.max_difficulty}`)"
        )
        lines.append(f"- **`target_regs_per_interval`:** `{hp.target_regs_per_interval}`")
        lines.append(f"- **`immunity_period`:** `{hp.immunity_period}` blocks")
        lines.append(f"- **`max_regs_per_block`:** `{hp.max_regs_per_block}`")
        lines.append(f"- **`serving_rate_limit`:** `{hp.serving_rate_limit}`")
        lines.append(f"- **`weights_rate_limit`:** `{hp.weights_rate_limit}`")
        lines.append(f"- **`activity_cutoff`:** `{hp.activity_cutoff}` blocks")
        lines.append(f"- **`commit_reveal_weights_enabled`:** `{hp.commit_reveal_weights_enabled}`")
        lines.append(f"- **`commit_reveal_period`:** `{hp.commit_reveal_period}`")
        lines.append(f"- **`liquid_alpha_enabled`:** `{hp.liquid_alpha_enabled}`")
        lines.append(f"- **`user_liquidity_enabled` (subnet pool):** `{hp.user_liquidity_enabled}`")
        lines.append(f"- **`bonds_reset_enabled` / `bonds_moving_avg`:** `{hp.bonds_reset_enabled}` / `{hp.bonds_moving_avg}`")
        lines.append(f"- **`subnet_is_active`:** `{hp.subnet_is_active}`")
        lines.append(f"- **`yuma_version`:** `{hp.yuma_version}`")
        lines.append(
            f"- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** {hp.alpha_sigmoid_steepness}, "
            f"`{hp.alpha_high}`, `{hp.alpha_low}`"
        )

    lines.append("")
    lines.append(
        "- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)"
    )
    lines.append("")
    return "\n".join(lines)


def format_readme_specs_block(
    readme_excerpt: str | None,
    readme_source_url: str | None,
    github_field: str,
) -> str:
    gh = github_field.strip() if github_field else ""
    if readme_excerpt and readme_source_url:
        src = f"\n\n*README source used for excerpts: `{readme_source_url}`.*"
        return (
            readme_excerpt.strip()
            + "\n"
            + src
            + "\n\n*Headings were selected heuristically (hardware / miner / validator / requirements). "
            "Always read the full README in the repo.*\n"
        )
    if gh.startswith("https://github.com"):
        return (
            f"No matching README sections were auto-detected for [{gh}]({gh}). "
            "Open the repository for miner/validator machine requirements, dependencies, and cloud sizing.\n"
        )
    return (
        "No GitHub URL is registered on-chain for this subnet, so README-based hardware notes were not fetched. "
        "Use the website or community links above when available.\n"
    )


def format_price_block(
    st: Subtensor,
    netuid: int,
    head: int,
    *,
    chain_step: int,
    chain_max_offset: int,
    taostats_key: str | None,
    taostats_limit: int,
    taostats_delay: float,
) -> str:
    lines: list[str] = []

    rows = chain_price_recent_rows(
        st, netuid, head, step=chain_step, max_offset=chain_max_offset
    )
    lines.append("### Short window — on-chain α price (public RPC state retention)\n")
    if netuid == 0:
        lines.append("Root uses TAO directly; protocol surfaces **1 τ per root weight unit** for pricing helpers.\n")
    if rows:
        lines.append(
            "Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but "
            f"**very short** slice of history (samples every **{chain_step}** blocks out to roughly **{chain_max_offset}** blocks)."
        )
        lines.append("| Block | α price (TAO) |")
        lines.append("|------:|----------------:|")
        for b, px in rows:
            lines.append(f"| {b} | {px:.12g} |")
        lines.append("")
    else:
        lines.append("*Could not sample historical blocks (RPC returned no usable state).*")
        lines.append("")

    if netuid == 0:
        return "\n".join(lines)

    lines.append("### Extended history — TAOStats pool price (daily)\n")
    if taostats_key:
        hist, err = fetch_taostats_pool_history_daily(
            taostats_key, netuid, limit=taostats_limit
        )
        time.sleep(taostats_delay)
        if err or not hist:
            lines.append(f"*TAOStats fetch failed:* `{err}`\n")
            return "\n".join(lines)

        lines.append(
            "Daily pool **`price`** (TAO per α) via [TAOStats `GET /api/dtao/pool/history/v1`](https://docs.taostats.io/reference/get-historical-subnet-pools) "
            f"(`frequency=by_day`, last **{len(hist)}** rows returned in this snapshot).\n"
        )
        lines.append("| Timestamp (UTC) | Block | Pool price |")
        lines.append("|-----------------|------:|-----------:|")

        chronological = sorted(
            hist,
            key=lambda x: (
                x.get("block_number") or 0,
                str(x.get("timestamp") or ""),
            ),
        )
        for row in chronological[-min(56, len(chronological)) :]:
            ts = row.get("timestamp") or ""
            bn = row.get("block_number")
            px = row.get("price") or ""
            lines.append(f"| {ts} | {bn} | {px} |")
        lines.append("")
    else:
        lines.append(
            "Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** "
            "cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate "
            "automatically.\n"
        )

    return "\n".join(lines)


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
    *,
    fetch_web: bool,
    delay_s: float,
    st: Subtensor,
    readme_excerpt: str | None,
    readme_raw_url: str | None,
    taostats_key: str | None,
    taostats_limit: int,
    taostats_delay: float,
    chain_price_step: int,
    chain_price_max_offset: int,
    skip_specs_readme: bool,
) -> str:
    netuid = d.netuid
    name = getattr(d, "subnet_name", "") or f"netuid-{netuid}"
    sym = getattr(d, "symbol", "") or ""
    sid = getattr(d, "subnet_identity", None)

    desc = ""
    additional = ""
    gh_ident = ""
    if sid:
        desc = (sid.description or "").strip()
        additional = (sid.additional or "").strip()
        gh_ident = (sid.github_repo or "").strip()

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

    readme_block = "*README hardware excerpt skipped (`--no-readme-specs`).*\n\n"
    if not skip_specs_readme:
        readme_block = "## Miner / validator compute notes (README excerpts)\n\n"
        readme_block += format_readme_specs_block(readme_excerpt, readme_raw_url, gh_ident)

    lines: list[str] = [
        title,
        "",
        "## Overview",
        "",
        _overview_for_subnet(netuid, name, desc, additional, fetch_title, fetch_desc),
        "",
        "## Operational parameters — registration, limits, economics (chain)\n",
        "",
        format_chain_ops(st, netuid, block),
        readme_block.rstrip(),
        "",
        "## On-chain identity — description\n",
        "",
    ]

    lines.append(desc if desc else "*Empty — no description bytes set in `SubnetIdentity`.*")
    lines.extend(
        [
            "",
            "## On-chain identity — additional field\n",
            "",
            additional if additional else "*Empty — no additional field set, or identity missing.*",
            "",
            "## Registered contact & links\n",
            "",
            _links_markdown(sid),
            "",
        ]
    )

    lines.extend(
        [
            "## Alpha price vs TAO (history)\n",
            "",
            format_price_block(
                st,
                netuid,
                block,
                chain_step=chain_price_step,
                chain_max_offset=chain_price_max_offset,
                taostats_key=taostats_key,
                taostats_limit=taostats_limit,
                taostats_delay=taostats_delay,
            ),
            "",
        ]
    )

    if fetch_title or fetch_desc:
        lines.extend(
            [
                "## Web crawl (supplementary)\n",
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
            f"*Snapshot: Subtensor `{network}`, head block **{block}**, {snapshot_utc}. Regenerate via "
            "`scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is "
            "heuristic; TAOStats history requires API access.*",
            "",
        ]
    )

    while len(lines) > 3 and lines[-1] == "" and lines[-2] == "":
        lines.pop()
    return "\n".join(lines) + ("\n" if lines and lines[-1] != "\n" else "")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--network", default="finney")
    ap.add_argument("--out-dir", default="subnets")
    ap.add_argument(
        "--fetch-all-websites",
        action="store_true",
        help="Always fetch marketing/GitHub landing HTML for supplementary meta",
    )
    ap.add_argument(
        "--no-supplement-web",
        action="store_true",
        help="Skip supplementary HTML crawling",
    )
    ap.add_argument("--web-thin-chars", type=int, default=400)
    ap.add_argument("--delay", type=float, default=0.25, help="Delay between miscellaneous HTTP hits")
    ap.add_argument(
        "--chain-price-step",
        type=int,
        default=48,
        help="Spacing (blocks) between on-chain historical price probes",
    )
    ap.add_argument(
        "--chain-price-max-offset",
        type=int,
        default=576,
        help="Maximum look-back (blocks) for on-chain probes before RPC discards state",
    )
    ap.add_argument(
        "--taostats-api-key",
        default=os.environ.get("TAOSTATS_API_KEY", ""),
        help="TAOStats Authorization token (daily pool history)",
    )
    ap.add_argument(
        "--taostats-limit",
        type=int,
        default=56,
        help="Max rows requested from TAOStats history per subnet (<=200)",
    )
    ap.add_argument(
        "--taostats-delay",
        type=float,
        default=0.21,
        help="Cooldown between TAOStats API calls",
    )
    ap.add_argument(
        "--no-readme-specs",
        dest="readme_specs",
        action="store_false",
        default=True,
        help="Skip GitHub README heuristic extraction",
    )
    args = ap.parse_args()

    st = Subtensor(network=args.network)
    subs = sorted(st.all_subnets() or [], key=lambda x: x.netuid)
    block = st.get_current_block()
    snapshot_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    taostats_key = (args.taostats_api_key or "").strip() or None

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    index_lines = [
        "# Subnet pages (one file per NetUID)",
        "",
        f"Generated from `{args.network}` at block **{block}** ({snapshot_utc}).",
        "",
        "Each page now adds **chain registration/limit tables**, heuristic **README hardware/miner excerpts** from GitHub, "
        "**short-window on-chain alpha price samples**, plus optional **TAOStats daily prices** (`TAOSTATS_API_KEY`).",
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
            do_fetch = bool(netuid > 0 and supplemental_target and combined < args.web_thin_chars)

        readme_excerpt = None
        readme_raw_url = None
        if args.readme_specs and github_candidate:
            readme_excerpt, readme_raw_url = _readme_specs_from_github(gh_raw)
            time.sleep(args.delay)

        body = render_page(
            d,
            block,
            args.network,
            snapshot_utc,
            fetch_web=do_fetch,
            delay_s=args.delay,
            st=st,
            readme_excerpt=readme_excerpt,
            readme_raw_url=readme_raw_url,
            taostats_key=taostats_key,
            taostats_limit=args.taostats_limit,
            taostats_delay=args.taostats_delay,
            chain_price_step=args.chain_price_step,
            chain_price_max_offset=args.chain_price_max_offset,
            skip_specs_readme=not args.readme_specs,
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
            "Regenerate: `python scripts/generate_subnet_pages.py` · optional `TAOSTATS_API_KEY=…` · "
            "`--no-readme-specs` / `--no-supplement-web` to reduce HTTP traffic.",
            "",
        ]
    )
    (out / "README.md").write_text("\n".join(index_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
