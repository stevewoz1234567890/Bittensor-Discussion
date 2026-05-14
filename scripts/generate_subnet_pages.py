#!/usr/bin/env python3
"""Generate one Markdown file per subnet under subnets/.

Pulls chain **`DynamicInfo`** for a richer **Overview**, `SubnetHyperparameters`, GitHub README preface excerpt
and hardware scrape, and optional crawl / TAOStats pool history.

Usage (from repo root, with bittensor installed):
    python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements-catalog.txt
    .venv/bin/python scripts/generate_subnet_pages.py
    Optional: create repo-root `.env` with `TAOSTATS_API_KEY=…` (see `.env.example`) for TAOStats index + history.
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from bittensor import Subtensor
from bittensor.utils.balance import Balance
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
TAOSTATS_API_BASE = "https://api.taostats.io"

ROOT_OVERVIEW = """The **root network** (NetUID 0) is Bittensor’s top-level coordination layer. TAO holders delegate stake to root validators, who set **weights** on other subnets. Those weights help determine how network **emissions** are allocated across subnets. Root is not an application or “task” subnet like higher netuids; it is the mechanism through which the protocol routes incentive and security across the rest of the network."""

README_SECTION_KEYS = frozenset(
    (
        "require",
        "prereq",
        "hardware",
        "hardware class",
        "validator",
        "mining",
        "miner",
        "compute",
        "comput",
        "spec",
        "gpu",
        "cuda",
        "vram",
        "memory",
        "infra",
        "resources",
        "install",
        "setup",
        "recommended",
        "minimum",
        "system",
        "machine",
        "environment",
        "dependencies",
        "docker",
        "ubuntu",
        "pytorch",
        "instance",
        "aws",
        "gcp",
        "azure",
        "runpod",
    )
)


# Matches concrete hardware sizing / accelerators — used for a README-wide grep (not headings).
_HARDWARE_PATTERN = re.compile(
    r"(?is)"
    r"(\d[\d.,]{0,6}\s*(?:gb|tb|mb|mib|gib|tib)\b)"
    r"|(\d+\s*(?:mhz|ghz)\b)"
    r"|(\d+\s*(?:vcpu|cores?|threads?))\b"
    r"|\b(?:gpu|graphics|accelerator|nvidia|cuda|cuda\s*toolkit|cudnn|vram|tensor\s*core|nvlink|sm_\d+)\b"
    r"|\b(?:rtx|gtx|geforce|quadro|tesla)\s*[a-z0-9]+\b|\b(?:h100|h200|a100|a10(?:g)?|l40(?:s)?|t4|v100|k80|h800)\b"
    r"|\b(?:cpu|processor|xeon|epyc|ryzen|threadripper|intel|amd\b|apple\s+m[0-9])\b"
    r"|\b(?:ram|dram|ssd|nvme)\b|\b\d+x\s*h100\b"
)


HW_GREP_EMPTY_STUB = """#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*

"""

OVERVIEW_README_INTRO_CHARS = 14_000


def _markdown_kv_table_from_bullet_lines(bullet_lines: list[str]) -> str | None:
    """Turn `- **Label:** value` lines into a two-column Markdown table."""
    rows: list[tuple[str, str]] = []
    for ln in bullet_lines:
        stripped = ln.strip()
        if not stripped.startswith("- "):
            continue
        m = re.match(r"- \*\*(.+?):\*\*\s*(.+)$", stripped)
        if not m:
            continue
        rows.append((m.group(1).strip(), m.group(2).strip()))
    if not rows:
        return None
    out = ["| Field | Value |", "| --- | --- |"]
    for k, v in rows:
        out.append(f"| {k} | {v} |")
    return "\n".join(out) + "\n"


def _strip_leading_heading_chunk_if_duplicate_readme_intro(
    heading_chunks: str, readme_intro: str | None
) -> str:
    """Drop the first README heading-section chunk when it repeats the Overview README preface."""
    if not heading_chunks or not readme_intro:
        return heading_chunks
    intro = readme_intro.strip()
    if len(intro) < 120:
        return heading_chunks
    parts = heading_chunks.split("\n\n---\n\n")
    if not parts:
        return heading_chunks
    first = parts[0].strip()
    intro_n = re.sub(r"\s+", " ", intro)
    first_n = re.sub(r"\s+", " ", first)
    n = min(len(first_n), len(intro_n), 360)
    if n < 80:
        return heading_chunks
    if first_n[:n] == intro_n[:n] or first_n.startswith(intro_n[: min(200, len(intro_n))]):
        rest = "\n\n---\n\n".join(p.strip() for p in parts[1:] if p.strip()).strip()
        return rest
    return heading_chunks


def _mermaid_xychart_decimal(x: float, *, places: int = 14) -> str:
    """Format floats for Mermaid xychart on GitHub: fixed-point only (no `e` exponent)."""
    if not math.isfinite(x):
        return "0.0"
    s = format(float(x), f".{places}f").rstrip("0").rstrip(".")
    if not s or s in ("-", "-0"):
        return "0.0"
    if "." not in s:
        s += ".0"
    return s


def _taostats_pool_hist_to_mermaid_xychart(rows: list[dict], *, max_points: int = 56) -> str:
    """Mermaid xychart-beta for daily pool price (GitHub-flavored Markdown)."""
    chronological = sorted(
        rows,
        key=lambda x: (int(x.get("block_number") or 0), str(x.get("timestamp") or "")),
    )
    if not chronological:
        return ""
    take = min(max_points, len(chronological))
    slice_ = chronological[-take:]
    labels: list[str] = []
    ys: list[float] = []
    for row in slice_:
        ts = str(row.get("timestamp") or "")
        lab = ts.split("T")[0] if "T" in ts else (ts[:10] if len(ts) >= 10 else ts or "?")
        labels.append(lab.replace('"', "'"))
        try:
            ys.append(float(row.get("price")))
        except (TypeError, ValueError):
            ys.append(0.0)
    if not ys:
        return ""
    lo, hi = min(ys), max(ys)
    lo = max(0.0, lo)
    hi = max(lo, hi)
    span = (hi - lo) or 1e-9
    y_lo = lo - span * 0.08
    y_hi = hi + span * 0.08
    y_lo = max(0.0, y_lo)
    if y_hi <= y_lo:
        y_hi = y_lo + max(1e-18, abs(y_lo) * 1e-12, span * 1e-6)
    lbl_joined = "[" + ", ".join(f'"{lab}"' for lab in labels) + "]"
    nums_joined = "[" + ", ".join(_mermaid_xychart_decimal(max(0.0, y)) for y in ys) + "]"
    return (
        "\n```mermaid\n"
        "xychart-beta\n"
        '    title "TAOStats daily pool price (τ per α)"\n'
        f"    x-axis {lbl_joined}\n"
        f'    y-axis "Price" in {_mermaid_xychart_decimal(y_lo)} --> {_mermaid_xychart_decimal(y_hi)}\n'
        f"    line {nums_joined}\n"
        "```\n"
    )


def _title_line_subnet(name: str, netuid: int, sym: str) -> str:
    frag = f"**{name}** (NetUID **{netuid}**)"
    if sym:
        frag += f" (`{sym}`)"
    return frag + "."


def _subnet_narrative_markdown(name: str, netuid: int, sym: str, desc: str, additional: str) -> str:
    """Full SubnetIdentity description + optional additional — primary operator-facing prose."""
    title = _title_line_subnet(name, netuid, sym)
    dd = (desc or "").strip()
    aa = (additional or "").strip()
    if dd:
        core = dd
        placeholder_used = False
    else:
        core = (
            "*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, "
            "**Topology / hyperparameters** further down this page, and outbound links."
        )
        placeholder_used = True
    blocks = [title, core]
    if aa and aa.lower() != dd.lower():
        blocks.extend(["", "#### SubnetIdentity `additional` *(chain)*", "", aa])
    elif placeholder_used and aa and len(aa) > 20:
        # Only additional when description empty
        blocks.extend(["", "#### SubnetIdentity `additional` *(chain)*", "", aa])

    inner = "\n\n".join(blocks)
    return f"### Subnet narrative *(full `SubnetIdentity` text)*\n\n{inner}"


def _dynamicinfo_deep_lines(dyn) -> list[str]:
    """Optional `DynamicInfo` fields omitted from the main snapshot list."""
    lines: list[str] = []
    candidates = (
        ("`last_step` (block)", "last_step"),
        ("Liquidity constant `k`", "k"),
    )
    seen: set[int] = set()
    for label, key in candidates:
        if not hasattr(dyn, key):
            continue
        v = getattr(dyn, key)
        if callable(v):
            continue
        oid = id(v)
        if oid in seen:
            continue
        seen.add(oid)
        lines.append(f"- **{label}:** `{v}`")
    return lines


def _readme_intro_until_first_section(readme_plain: str | None, *, max_chars: int) -> str | None:
    """Return README body up to first `## `-level heading (exclusive), skipping fenced ``` blocks."""
    if not readme_plain or len(readme_plain.strip()) < 120:
        return None
    out: list[str] = []
    in_fence = False
    for ln in readme_plain.splitlines():
        stripped = ln.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith("##") and not stripped.startswith("###"):
            break
        out.append(ln.rstrip())

    snippet = "\n".join(out).strip()
    if len(snippet) < 140:
        return None
    if len(snippet) > max_chars:
        snippet = snippet[: max_chars - 3].rstrip() + "…"
    return snippet


def _taostats_request_json(
    api_key: str, path: str, query: dict[str, str | int], *, timeout: float = 38.0
) -> tuple[dict | None, str | None]:
    q = urllib.parse.urlencode({str(k): str(v) for k, v in query.items() if v is not None})
    url = f"{TAOSTATS_API_BASE}{path}?{q}"
    stripped = api_key.strip()
    auth_seq = [stripped]
    if not stripped.lower().startswith("bearer "):
        auth_seq.append(f"Bearer {stripped}")
    last_err: str | None = None
    for auth in auth_seq:
        req = urllib.request.Request(url)
        req.add_header("Authorization", auth)
        req.add_header("User-Agent", "Bittensor-Discussion-catalog/1.0")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read().decode("utf-8", errors="ignore")
                return json.loads(raw), None
        except urllib.error.HTTPError as e:
            try:
                body = e.read().decode("utf-8", errors="ignore")[:420]
            except Exception:
                body = str(e.reason)
            last_err = f"HTTP {e.code}: {body}"
            if e.code not in (401, 403):
                return None, last_err
        except Exception as e:
            return None, str(e)
    return None, last_err


def prefetch_taostats_index_maps(
    api_key: str, *, delay_s: float
) -> tuple[dict[int, dict], dict[int, dict], str | None]:
    """Paged [subnet/latest](...) and [pool/latest](...) into netuid-keyed maps (minimal HTTP)."""

    def pull(endpoint: str, order: str) -> dict[int, dict]:
        accum: dict[int, dict] = {}
        page = 1
        while page <= 120:
            payload, err = _taostats_request_json(api_key, endpoint, {"page": page, "limit": 1024, "order": order})
            time.sleep(delay_s)
            if err or not isinstance(payload, dict):
                break
            rows = payload.get("data")
            if not isinstance(rows, list) or not rows:
                break
            for r in rows:
                if not isinstance(r, dict):
                    continue
                nu = r.get("netuid")
                if nu is None:
                    continue
                try:
                    accum[int(nu)] = r
                except (TypeError, ValueError):
                    continue
            pag = payload.get("pagination") if isinstance(payload.get("pagination"), dict) else {}
            np = pag.get("next_page")
            if np in (None, ""):
                break
            try:
                nxt = int(np)
            except (TypeError, ValueError):
                break
            if nxt == page:
                break
            page = nxt
        return accum

    subnets = pull("/api/subnet/latest/v1", "netuid_asc")
    pools = pull("/api/dtao/pool/latest/v1", "netuid_asc")
    warning = (
        None
        if (subnets or pools)
        else "TAOStats index prefetch returned no rows (invalid key, outage, or empty account quota)."
    )
    return subnets, pools, warning


def format_taostats_snapshot_markdown(subnet: dict | None, pool: dict | None) -> str | None:
    """One Overview subsection when either [pool/latest](get-subnet-pools) or [subnet/latest](get-subnets-1) row exists."""

    bits: list[str] = []

    def add_block(title: str, row: dict, fields: tuple[tuple[str, str], ...]) -> None:
        bullet_lines: list[str] = []
        for label, k in fields:
            if k not in row:
                continue
            v = row.get(k)
            if v is None or v == "":
                continue
            if isinstance(v, dict) and "ss58" in v:
                v = v["ss58"]
            elif isinstance(v, dict):
                try:
                    v = json.dumps(v, separators=(",", ":"))[:520]
                except (TypeError, ValueError):
                    v = str(v)[:520]
            bullet_lines.append(f"- **{label}:** `{v}`")
        tab = _markdown_kv_table_from_bullet_lines(bullet_lines)
        if tab:
            bits.append(f"#### {title}\n{tab}")

    if isinstance(pool, dict) and pool:
        add_block(
            "Liquidity pool (TAOStats)",
            pool,
            (
                ("Subnet name (API)", "name"),
                ("Symbol (API)", "symbol"),
                ("Rank", "rank"),
                ("Block (API)", "block_number"),
                ("Time (API)", "timestamp"),
                ("Price τ/α", "price"),
                ("Market cap", "market_cap"),
                ("Market cap Δ 1d", "market_cap_change_1_day"),
                ("Liquidity", "liquidity"),
                ("Total τ", "total_tao"),
                ("Total α", "total_alpha"),
                ("α in pool", "alpha_in_pool"),
                ("α staked", "alpha_staked"),
                ("Price Δ 1h", "price_change_1_hour"),
                ("Price Δ 1d", "price_change_1_day"),
            ),
        )

    if isinstance(subnet, dict) and subnet:
        add_block(
            "Subnet activity (TAOStats)",
            subnet,
            (
                ("NetUID (API)", "netuid"),
                ("Owner SS58 (API)", "owner"),
                ("Block (API)", "block_number"),
                ("Time (API)", "timestamp"),
                ("Registration block", "registration_block_number"),
                ("Registration wall time", "registration_timestamp"),
                ("Registration cost snapshot", "registration_cost"),
                ("Active keys", "active_keys"),
                ("Active validators", "active_validators"),
                ("Active miners", "active_miners"),
                ("Active dual-role", "active_dual"),
                ("Emission", "emission"),
                ("Max neurons", "max_neurons"),
                ("Validator slots (metadata)", "validators"),
                ("Max validators (API)", "max_validators"),
                ("Neuron reg. cost", "neuron_registration_cost"),
                ("Tempo (API)", "tempo"),
                ("Min allowed weights (API)", "min_allowed_weights"),
                ("Max weights limit (API)", "max_weights_limit"),
                ("Activity cutoff", "activity_cutoff"),
            ),
        )

    if not bits:
        return None
    header = (
        "### TAOStats snapshot *(off-chain index)*\n\n"
        "Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), "
        "[pool latest](https://docs.taostats.io/reference/get-subnet-pools).\n"
    )
    return header + "\n".join(bits)


def build_detailed_overview(
    dyn,
    *,
    desc: str,
    additional: str,
    fetch_title: str | None,
    fetch_desc: str | None,
    readme_intro: str | None,
    block: int,
    taostats_subnet: dict | None = None,
    taostats_pool: dict | None = None,
) -> str:
    """Structured multi-section Overview (purpose + chain snapshot + README intro + crawler hints)."""

    netuid = dyn.netuid
    name = getattr(dyn, "subnet_name", "") or f"netuid-{netuid}"
    sym = getattr(dyn, "symbol", "") or ""

    if netuid == 0:
        prelude: list[str] = []
        if (desc or "").strip() or (additional or "").strip():
            prelude.append(_subnet_narrative_markdown(name, netuid, sym, desc, additional))

        dyn_bits = []
        dyn_bits.append(
            f"- **Root tempo:** `{dyn.tempo}` blocks between epoch strides (see [`SubnetHyperparameters`](https://learnbittensor.org/explore/concept/subnet-hyperparameters)). "
            "Validators allocate weight across subnets rather than miners competing inside a commodity task."
        )
        dyn_bits.append(f"- **`tao_in` (pool-facing TAO):** {dyn.tao_in}")
        dyn_bits.append(f"- **Root alpha bookkeeping (`alpha_in` / `alpha_out`):** {dyn.alpha_in} / {dyn.alpha_out}")
        dyn_bits.append(f"- **Reported subnet volume rolling figure:** {dyn.subnet_volume}")
        root_deep = _dynamicinfo_deep_lines(dyn)
        if root_deep:
            dyn_bits.extend(["", "#### Further numeric `DynamicInfo` fields", "", *root_deep])

        root_body = ("\n\n".join(prelude).strip() + "\n\n" if prelude else "") + ROOT_OVERVIEW.strip()
        root_body += f"\n\n### Root snapshot *(block {block})*\n\n" + "\n".join(dyn_bits) + "\n"
        ts_root = format_taostats_snapshot_markdown(taostats_subnet, taostats_pool)
        return root_body + (f"\n{ts_root}\n" if ts_root else "")

    dd = (desc or "").strip()
    aa = (additional or "").strip()
    parts: list[str] = [_subnet_narrative_markdown(name, netuid, sym, desc, additional)]

    snapshot_hdr = "### Chain & market snapshot *(from `DynamicInfo`)*\n"
    snap_lines = [
        f"- **Tempo / epoch pacing:** `{dyn.tempo}` blocks between steps; **blocks since last step:** `{dyn.blocks_since_last_step}`. "
        "**Emission allocation field:** "
        + f"`{dyn.emission}` *(protocol snapshot at block {block})*.",
        f"- **TAO routed into swap pool reserves:** **`tao_in`** = {dyn.tao_in}. **Alpha liquidity in pool (`alpha_in`)** = {dyn.alpha_in}; **`alpha_out`** (off-pool bonded/staked tally) "
        "= "
        + f"{dyn.alpha_out}.",
        f"- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`{dyn.price}`** *(also **moving-average price** `{dyn.moving_price}` used in some dashboards)*.",
        f"- **Outstanding subnet volume accumulator:** `{dyn.subnet_volume}`. "
        "**Owner hotkey / coldkey (chain):** `{0}` / `{1}`.".format(dyn.owner_hotkey, dyn.owner_coldkey),
        f"- **Subnet registered at block:** `{dyn.network_registered_at}` "
        "(see explorers for approximate wall-clock age). "
        "**Is dynamic liquidity subnet:** `{}`.".format(bool(getattr(dyn, "is_dynamic", False))),
        f"- **Pending emissions cues:** pending α emission `{dyn.pending_alpha_emission}`; pending root emission `{dyn.pending_root_emission}`.",
        f"- **Per-flow emission splits:** τ-in `{dyn.tao_in_emission}` · α-out `{dyn.alpha_out_emission}` · α-in `{dyn.alpha_in_emission}`.",
    ]
    snap_core = "\n".join(snap_lines)
    dip = _dynamicinfo_deep_lines(dyn)
    if dip:
        snap_core += "\n\n#### Further numeric `DynamicInfo` fields\n\n" + "\n".join(dip)
    snap_core += (
        f"\n\n*Values are pallet **`DynamicInfo`** at head block **{block}**. **`last_step`** anchors the most recent epoch advance. "
        "On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. "
        "**`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*"
    )

    parts.append(snapshot_hdr.rstrip() + "\n\n" + snap_core)
    ts_ov = format_taostats_snapshot_markdown(taostats_subnet, taostats_pool)
    if ts_ov:
        parts.append("")
        parts.append(ts_ov)

    readme_hdr = "### Repository README excerpt *(everything before first `##` heading)*\n"
    if readme_intro:
        intro_body = readme_intro.strip()

        redundant = dd and len(dd) > 40 and dd[:120].strip().lower() in intro_body[:800].lower()
        if redundant:
            intro_body += (
                "\n\n*(README prelude often echoes the subnet tagline — miner/validator runbooks typically live further down in-repo.)*\n"
            )
        parts.append("")
        parts.append(readme_hdr.rstrip("\n") + "\n\n" + intro_body)
    elif fetch_desc or fetch_title:
        parts.append("")
        parts.append(
            readme_hdr.rstrip("\n")
            + "\n\n"
            + "*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*"
        )

    crawler_bits: list[str] = []
    if fetch_desc:
        crawler_bits.append(f"**Landing meta / crawler:** {fetch_desc}")
    if fetch_title:
        crawler_bits.append(f"**Fetched document title:** {fetch_title}")

    if crawler_bits:
        parts.append("")
        parts.append(
            "### Supplementary site crawl *(marketing HTML)*\n\n" + "\n\n".join(crawler_bits).strip()
        )

    return "\n\n".join(p for p in parts if p.strip()).strip()


def _line_looks_hardware_rich(line: str) -> bool:
    stripped = line.strip()
    if len(stripped) < 10:
        return False
    if stripped.startswith(("#", "<!--", "```", "---", "[")) and not stripped.startswith("[`"):
        return False
    if stripped.startswith("!"):
        return False
    if stripped.startswith("|") and stripped.count("|") < 3:
        return False

    low = stripped.lower()
    # Avoid generic nav lines with no specs
    noise_only = {"miner", "validator", "miner setup", "validator setup", "# miners", "## miners"}
    if stripped in noise_only:
        return False

    return bool(_HARDWARE_PATTERN.search(stripped))


def _github_parse_org_repo(repo_https: str) -> tuple[str, str] | None:
    u = repo_https.strip().rstrip("/")
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?$", u, re.I)
    if not m:
        return None
    return m.group(1), m.group(2)


def _github_extra_docs_urls(org: str, repo: str) -> list[str]:
    """Supplementary docs (tried in order; main branch first, then master)."""
    paths = (
        "docs/miner.md",
        "docs/validator.md",
        "miner/README.md",
        "validators.md",
    )
    out: list[str] = []
    for br in ("main", "master"):
        base = f"https://raw.githubusercontent.com/{org}/{repo}/{br}"
        for p in paths:
            out.append(f"{base}/{p}")
    return out


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

def _line_table_header_or_row_probable_hardware(line: str) -> bool:
    s = line.strip()
    if not s.startswith("|") or s.count("|") < 3:
        return False
    lowered = s.lower().replace("`", "")
    if re.fullmatch(r"[|\-|:\s]+", lowered):
        return False
    return bool(
        re.search(
            r"\bgpu|accelerator|vram|cpu|tier|cores?|vcpus?|instance|hardware|compute class|memory\b",
            lowered,
        )
    )


def _extract_readme_heading_sections(markdown_body: str, max_chars: int = 4600) -> str | None:
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


def _collect_hardware_grep_lines(markdown_body: str, *, max_lines: int = 48) -> list[str]:
    """Surface CPU/GPU/RAM lines wherever they appear — prose, bullets, tables."""
    out: list[str] = []
    seen: set[str] = set()
    for ln in markdown_body.splitlines():
        if len(out) >= max_lines:
            break
        ls = ln.rstrip()
        if not ls:
            continue
        if _line_table_header_or_row_probable_hardware(ls):
            cand = ls
        elif _line_looks_hardware_rich(ls):
            cand = ls
        else:
            continue
        key = " ".join(cand.split())
        if key in seen:
            continue
        seen.add(key)
        out.append(cand)
    return out


def _format_hw_grep_block(lines: list[str]) -> str | None:
    if not lines:
        return None
    bl: list[str] = []
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if s.startswith("|"):
            bl.append(f"- `{s}`")
        else:
            bl.append(f"- {s}")
    return (
        "#### CPU / GPU / RAM lines (automatic grep)\n\n"
        + "\n".join(bl)
    )


def _append_extra_github_hw_docs(
    org: str,
    repo: str,
    http_delay: float,
    *,
    min_total_hw_lines: int,
    existing_count: int,
) -> list[tuple[str, list[str]]]:
    """Pull a few supplementary markdown files when the main README lacks enough hardware mentions."""
    if existing_count >= min_total_hw_lines:
        return []

    gleaned: list[tuple[str, list[str]]] = []
    fetched = 0
    MAX_FILES = 4

    lines_seen = existing_count

    for url in _github_extra_docs_urls(org, repo):
        if fetched >= MAX_FILES:
            break
        if lines_seen >= min_total_hw_lines and fetched > 0:
            break
        time.sleep(http_delay)
        text = _fetch_text(url, timeout=12.0, max_bytes=600_000)
        if not text or len(text) < 50:
            continue
        glean = _collect_hardware_grep_lines(text, max_lines=36)
        if not glean:
            continue
        short = urllib.parse.urlsplit(url).path.rsplit("/", 1)[-1]
        gleaned.append((short, glean))
        lines_seen += len(glean)
        fetched += 1

    return gleaned


def _readme_specs_from_github(
    repo_url: str,
    *,
    http_delay: float,
    extract_hardware_bundle: bool = True,
) -> tuple[str | None, str | None, str | None]:
    """Return (README hardware Markdown bundle or None if skipped, raw URL, full README Markdown text)."""

    readme_text = None
    readme_url_used = None
    for raw_url in _github_repo_raw_readme_candidates(repo_url):
        text = _fetch_text(raw_url, timeout=12.0, max_bytes=800_000)
        if text and len(text.strip()) > 80:
            readme_text = text
            readme_url_used = raw_url
            break

    if not readme_text:
        return None, None, None

    if not extract_hardware_bundle:
        return None, readme_url_used, readme_text

    heading_chunks = _extract_readme_heading_sections(readme_text)
    if heading_chunks:
        heading_chunks = _strip_leading_heading_chunk_if_duplicate_readme_intro(
            heading_chunks,
            _readme_intro_until_first_section(readme_text, max_chars=OVERVIEW_README_INTRO_CHARS),
        )
    grep_primary = _collect_hardware_grep_lines(readme_text)

    bundled: list[str] = []
    if heading_chunks:
        bundled.append(
            "#### Sections matched by heading (miner / validator / hardware / requirements)\n\n" + heading_chunks
        )

    grep_block = _format_hw_grep_block(grep_primary)

    extra_sections: list[str] = []
    org_repo = _github_parse_org_repo(repo_url)
    if org_repo:
        extras = _append_extra_github_hw_docs(
            org_repo[0],
            org_repo[1],
            http_delay,
            min_total_hw_lines=22,
            existing_count=len(grep_primary),
        )
        for short_name, glines in extras:
            blk = _format_hw_grep_block(glines)
            if blk:
                extra_sections.append(f"##### Extra scrape: `{short_name}` (grep only)\n\n" + blk)

    if grep_block:
        bundled.append(grep_block)
    elif not extra_sections:
        bundled.append(HW_GREP_EMPTY_STUB)
    bundled.extend(extra_sections)

    if not bundled:
        return None, readme_url_used, readme_text

    text_out = "\n\n---\n\n".join(bundled)
    if len(text_out) > 12_500:
        text_out = text_out[: 12_400] + "…\n"
    return text_out, readme_url_used, readme_text


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
    payload, err = _taostats_request_json(
        api_key,
        "/api/dtao/pool/history/v1",
        {
            "netuid": netuid,
            "frequency": "by_day",
            "limit": min(limit, 200),
            "order": "timestamp_desc",
        },
        timeout=timeout,
    )
    if err or payload is None:
        return None, err

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

    lines.append("### Topology & economics (`SubnetInfo` snapshot)\n")
    topo_bullets: list[str] = []
    if si:
        topo_bullets.append(f"- **`max_n` (max registered UIDs):** `{si.max_n}`")
        topo_bullets.append(f"- **`subnetwork_n`:** `{si.subnetwork_n}`")
        topo_bullets.append(f"- **Max validators allowed (`max_allowed_validators`):** `{si.max_allowed_validators}`")
        topo_bullets.append(f"- **Min weights per neuron (`min_allowed_weights`):** `{si.min_allowed_weights}`")
        topo_bullets.append(f"- **`max_weights_limit` (consensus-encoded cap):** `{si.max_weight_limit}`")
        topo_bullets.append(f"- **`tempo` (blocks between epoch advances):** `{si.tempo}`")
        topo_bullets.append(f"- **`scaling_law_power`:** `{si.scaling_law_power}`")
        topo_bullets.append(f"- **`modality` ID:** `{si.modality}`")
        topo_bullets.append(f"- **`emission_value` (display field):** `{si.emission_value}`")
        topo_bullets.append(f"- **`difficulty` (PoW field on info view):** `{si.difficulty}`")
        topo_bullets.append(f"- **`immunity_period` (blocks):** `{si.immunity_period}`")
        topo_bullets.append(f"- **Registration recycle cost snapshot (`burn`):** `{si.burn}`")
        topo_bullets.append(f"- **Owner SS58 (`owner_ss58`):** `{si.owner_ss58}`")

        if si.connection_requirements:
            parts = "; ".join(
                f"NetUID `{nid}` → {wt}"
                for nid, wt in sorted(
                    si.connection_requirements.items(), key=lambda x: int(str(x[0]))
                )
            )
            topo_bullets.append(f"- **Subnet connection graph (`connection_requirements`):** {parts}")

    topo_tab = _markdown_kv_table_from_bullet_lines(topo_bullets)
    if topo_tab:
        lines.append(topo_tab.rstrip() + "\n")

    lines.append("")
    lines.append("### Consensus hyperparameters (`SubnetHyperparameters` snapshot)\n")
    hp_bullets: list[str] = []
    if hp:
        hp_bullets.append(f"- **Registration allowed:** `{hp.registration_allowed}`")
        hp_bullets.append(
            f"- **`min_burn` / `max_burn` (RAO envelope):** `{Balance.from_rao(hp.min_burn)}` / `{Balance.from_rao(hp.max_burn)}`"
        )
        hp_bullets.append(
            f"- **PoW `difficulty` + bounds:** `{hp.difficulty}` (min `{hp.min_difficulty}`, max `{hp.max_difficulty}`)"
        )
        hp_bullets.append(f"- **`target_regs_per_interval`:** `{hp.target_regs_per_interval}`")
        hp_bullets.append(f"- **`immunity_period`:** `{hp.immunity_period}` blocks")
        hp_bullets.append(f"- **`max_regs_per_block`:** `{hp.max_regs_per_block}`")
        hp_bullets.append(f"- **`serving_rate_limit`:** `{hp.serving_rate_limit}`")
        hp_bullets.append(f"- **`weights_rate_limit`:** `{hp.weights_rate_limit}`")
        hp_bullets.append(f"- **`activity_cutoff`:** `{hp.activity_cutoff}` blocks")
        hp_bullets.append(f"- **`commit_reveal_weights_enabled`:** `{hp.commit_reveal_weights_enabled}`")
        hp_bullets.append(f"- **`commit_reveal_period`:** `{hp.commit_reveal_period}`")
        hp_bullets.append(f"- **`liquid_alpha_enabled`:** `{hp.liquid_alpha_enabled}`")
        hp_bullets.append(f"- **`user_liquidity_enabled` (subnet pool):** `{hp.user_liquidity_enabled}`")
        hp_bullets.append(
            f"- **`bonds_reset_enabled` / `bonds_moving_avg`:** `{hp.bonds_reset_enabled}` / `{hp.bonds_moving_avg}`"
        )
        hp_bullets.append(f"- **`subnet_is_active`:** `{hp.subnet_is_active}`")
        hp_bullets.append(f"- **`yuma_version`:** `{hp.yuma_version}`")
        hp_bullets.append(
            f"- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** `{hp.alpha_sigmoid_steepness}`, "
            f"`{hp.alpha_high}`, `{hp.alpha_low}`"
        )

    hp_tab = _markdown_kv_table_from_bullet_lines(hp_bullets)
    if hp_tab:
        lines.append(hp_tab.rstrip() + "\n")

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
        src = f"\n\n*Primary README URL used: `{readme_source_url}`*"
        return (
            readme_excerpt.strip()
            + "\n"
            + src
            + "\n"
        )
    if gh.startswith("https://github.com"):
        return (
            f"*No miner/validator sections auto-matched.* Open [{gh}]({gh}) for requirements.\n"
        )
    return "*No GitHub URL on-chain; hardware notes not fetched automatically.*\n"


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
        lines.append("Root: protocol uses **1 τ per root weight unit** in pricing helpers.\n")
    note_rpc = (
        f"*Probes every **{chain_step}** blocks, lookback ≈ **{chain_max_offset}** blocks "
        "(bounded by typical public RPC history depth).*"
    )
    if rows:
        lines.append(note_rpc)
        lines.append("| Block | α price (TAO) |")
        lines.append("|------:|----------------:|")
        for b, px in rows:
            lines.append(f"| {b} | {px:.12g} |")
        lines.append("")
    else:
        lines.append("*No probes returned in this window.*")
        lines.append(note_rpc)
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
            f"[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** "
            f"(TAO per α), **{len(hist)}** rows in this snapshot.\n"
        )
        mermaid = _taostats_pool_hist_to_mermaid_xychart(
            hist, max_points=min(56, taostats_limit, len(hist))
        )
        if mermaid:
            lines.append(mermaid.rstrip() + "\n")
        else:
            lines.append("*Chart could not be built from TAOStats rows.*\n")
    else:
        lines.append(
            "*Daily pools from TAOStats require `TAOSTATS_API_KEY` or `--taostats-api-key` (see conventions in this folder’s README).*\n"
        )

    return "\n".join(lines)



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
    readme_intro: str | None,
    taostats_key: str | None,
    taostats_limit: int,
    taostats_delay: float,
    chain_price_step: int,
    chain_price_max_offset: int,
    skip_specs_readme: bool,
    taostats_subnet_row: dict | None,
    taostats_pool_row: dict | None,
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

    readme_block = "*README/hardware scrape skipped (`--no-readme-specs`).*\n\n"
    if not skip_specs_readme:
        readme_block = "## Miner / validator hardware (CPU/GPU/RAM)\n\n"
        readme_block += format_readme_specs_block(readme_excerpt, readme_raw_url, gh_ident)

    lines: list[str] = [
        title,
        "",
        "## Overview",
        "",
        build_detailed_overview(
            d,
            desc=desc,
            additional=additional,
            fetch_title=fetch_title,
            fetch_desc=fetch_desc,
            readme_intro=readme_intro,
            block=block,
            taostats_subnet=taostats_subnet_row,
            taostats_pool=taostats_pool_row,
        ),
        "",
        format_chain_ops(st, netuid, block),
        readme_block.rstrip(),
        "",
        "## SubnetIdentity links *(from chain)*\n",
        "",
        "*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*\n",
        "",
        _links_markdown(sid),
        "",
    ]

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

    lines.extend(
        [
            "---",
            "",
            f"*Subtensor `{network}`, block **{block}**, {snapshot_utc}. Regenerate: "
            "`scripts/generate_subnet_pages.py`.*",
            "",
        ]
    )

    while len(lines) > 3 and lines[-1] == "" and lines[-2] == "":
        lines.pop()
    return "\n".join(lines) + ("\n" if lines and lines[-1] != "\n" else "")


def main() -> None:
    load_dotenv(REPO_ROOT / ".env")
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
        default="",
        help="TAOStats Authorization header value (fallback: TAOSTATS_API_KEY from environment / `.env`)",
    )
    ap.add_argument(
        "--taostats-limit",
        type=int,
        default=120,
        help="Max rows requested from TAOStats pool history per subnet (<=200)",
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
    taostats_key = (
        (args.taostats_api_key or os.environ.get("TAOSTATS_API_KEY", "") or "").strip() or None
    )

    ts_subnet_map: dict[int, dict] = {}
    ts_pool_map: dict[int, dict] = {}
    if taostats_key:
        ts_subnet_map, ts_pool_map, ts_prefetch_warn = prefetch_taostats_index_maps(
            taostats_key, delay_s=max(0.05, args.taostats_delay)
        )
        if ts_prefetch_warn:
            print(ts_prefetch_warn, file=sys.stderr)

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    index_lines = [
        "# Subnet pages (one file per NetUID)",
        "",
        f"Generated from `{args.network}` at block **{block}** ({snapshot_utc}).",
        "",
        "Each page opens with **Subnet narrative** (full **`SubnetIdentity`** `description`/`additional`), **`DynamicInfo`** (core fields + swap/slippage helpers), **`SubnetInfo`** / **`SubnetHyperparameters`**, README preface + hardware scrape, on-chain α probes, and **TAOStats** index + optional daily history when **`TAOSTATS_API_KEY`** is set (`.env`).",
        "",
        "### Conventions (read once)",
        "",
        "- **`SubnetInfo` / `SubnetHyperparameters` blocks:** on-chain registration limits, tempo, burns, weight rules. **Miner / validator hardware:** repo scrape, not consensus.",
        "",
        "**α price — short window:** row spacing follows `--chain-price-step` / `--chain-price-max-offset` (bounded by RPC retention).",
        "",
        "**TAOStats:** prefetch fills **subnet + pool index** bullets in Overview; `--taostats-limit` caps **daily** price rows per page.",
        "",
        "---",
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
        readme_plain_text = None
        if github_candidate:
            readme_excerpt, readme_raw_url, readme_plain_text = _readme_specs_from_github(
                gh_raw, http_delay=args.delay, extract_hardware_bundle=args.readme_specs
            )
            time.sleep(args.delay)

        readme_intro = _readme_intro_until_first_section(
            readme_plain_text, max_chars=OVERVIEW_README_INTRO_CHARS
        )

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
            readme_intro=readme_intro,
            taostats_key=taostats_key,
            taostats_limit=args.taostats_limit,
            taostats_delay=args.taostats_delay,
            chain_price_step=args.chain_price_step,
            chain_price_max_offset=args.chain_price_max_offset,
            skip_specs_readme=not args.readme_specs,
            taostats_subnet_row=ts_subnet_map.get(netuid),
            taostats_pool_row=ts_pool_map.get(netuid),
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
            "Regenerate: `python scripts/generate_subnet_pages.py` · optional `.env` with `TAOSTATS_API_KEY` · "
            "`--no-readme-specs` / `--no-supplement-web` to reduce HTTP traffic.",
            "",
        ]
    )
    (out / "README.md").write_text("\n".join(index_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
