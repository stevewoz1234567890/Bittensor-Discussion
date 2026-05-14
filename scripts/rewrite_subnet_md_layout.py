#!/usr/bin/env python3
"""Rewrite existing subnets/*.md layout: TAOStats + SubnetInfo + hyperparams → tables; pool history table → Mermaid chart.

Idempotent for files already rewritten. Does not require bittensor.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


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


def _markdown_kv_table_from_bullet_lines(bullet_lines: list[str]) -> str | None:
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


def _strip_leading_heading_chunk_if_duplicate_readme_intro(heading_chunks: str, readme_intro: str) -> str:
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
        return "\n\n---\n\n".join(p.strip() for p in parts[1:] if p.strip()).strip()
    return heading_chunks


def _readme_intro_until_first_section(readme_plain: str) -> str | None:
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
    return snippet if len(snippet) >= 140 else None


def _dedupe_targon_style_hardware(text: str) -> str:
    """Remove leading README duplicate under Miner hardware when it matches Repository README excerpt."""
    m_repo = re.search(
        r"(### Repository README excerpt[^\n]*\n\n)([\s\S]*?)(\n### Supplementary site crawl|\n### Topology & economics|\n## Miner)",
        text,
    )
    if not m_repo:
        return text
    readme_body = m_repo.group(2)
    intro = _readme_intro_until_first_section(readme_body)
    if not intro:
        return text

    def repl_hw(m: re.Match[str]) -> str:
        hdr = m.group(1)
        body = m.group(2)
        stripped = _strip_leading_heading_chunk_if_duplicate_readme_intro(body, intro)
        if not stripped:
            return hdr + "*Same content as **Overview → Repository README excerpt** above; see repo for full runbooks.*\n\n"
        return hdr + stripped + "\n\n"

    return re.sub(
        r"(#### Sections matched by heading \(miner / validator / hardware / requirements\)\n\n)([\s\S]*?)(?=\n#### CPU / GPU / RAM lines|\n\*Primary README URL)",
        repl_hw,
        text,
        count=1,
    )


def _convert_taostats_subsection(text: str) -> str:
    """Replace #### Liquidity pool / #### Subnet activity bullet blocks with tables."""

    def repl_pool(m: re.Match[str]) -> str:
        hdr = m.group(1)
        body = m.group(2).rstrip("\n")
        if "| Field | Value |" in body:
            return m.group(0)
        lines = [ln for ln in body.splitlines() if ln.strip().startswith("- ")]
        tab = _markdown_kv_table_from_bullet_lines(lines)
        if not tab:
            return m.group(0)
        return hdr + "\n" + tab

    text = re.sub(
        r"(#### Liquidity pool \(TAOStats\)\n\n)([\s\S]*?)(?=\n#### Subnet activity \(TAOStats\))",
        repl_pool,
        text,
    )
    text = re.sub(
        r"(#### Subnet activity \(TAOStats\)\n\n)([\s\S]*?)(?=\n### |\n## |\Z)",
        repl_pool,
        text,
    )
    return text


def _convert_topology_consensus(text: str) -> str:
    def repl_topo(m: re.Match[str]) -> str:
        hdr = m.group(1)
        body = m.group(2).rstrip("\n")
        if "| Field | Value |" in body:
            return m.group(0)
        lines = [ln for ln in body.splitlines() if ln.strip().startswith("- ")]
        tab = _markdown_kv_table_from_bullet_lines(lines)
        if not tab:
            return m.group(0)
        return hdr + "\n" + tab + "\n"

    text = re.sub(
        r"(### Topology & economics \(`SubnetInfo` snapshot\)\n\n)([\s\S]*?)(?=\n### Consensus hyperparameters)",
        repl_topo,
        text,
    )

    def repl_hp(m: re.Match[str]) -> str:
        hdr = m.group(1)
        body = m.group(2).rstrip("\n")
        if "| Field | Value |" in body:
            return m.group(0)
        lines = []
        for ln in body.splitlines():
            s = ln.strip()
            if s.startswith("- **Docs:**"):
                continue
            if s.startswith("- "):
                lines.append(ln)
        tab = _markdown_kv_table_from_bullet_lines(lines)
        if not tab:
            return m.group(0)
        docs = "\n- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)\n"
        return hdr + "\n" + tab + docs

    text = re.sub(
        r"(### Consensus hyperparameters \(`SubnetHyperparameters` snapshot\)\n\n)([\s\S]*?)(?=\n## Miner|\n## SubnetIdentity|\n## Alpha price|\Z)",
        repl_hp,
        text,
    )
    return text


def _pool_table_to_mermaid(text: str) -> str:
    m = re.search(
        r"(### Extended history — TAOStats pool price \(daily\)\n\n"
        r"(?:\[TAOStats\][^\n]*\n\n)?)"
        r"(\| Timestamp[^\n]*\n\|[-|\s:]+\n(?:\|[^\n]+\n)+)",
        text,
    )
    if not m:
        return text
    prefix = m.group(1)
    anchor = m.start()
    if "```mermaid" in text[anchor : anchor + 900]:
        return text
    table = m.group(2)
    rows: list[tuple[str, int | str, float]] = []
    for ln in table.splitlines():
        if not ln.strip().startswith("|") or "Timestamp" in ln or re.match(r"^\|[\s\-:|]+\|$", ln.replace(" ", "")):
            continue
        parts = [p.strip() for p in ln.split("|")]
        parts = [p for p in parts if p]
        if len(parts) < 3:
            continue
        ts, bn, px = parts[0], parts[1], parts[2]
        try:
            price = float(px)
        except ValueError:
            continue
        try:
            block_n = int(bn)
        except ValueError:
            block_n = bn
        rows.append((ts, block_n, price))
    if len(rows) < 2:
        return text
    rows.sort(key=lambda t: (t[1] if isinstance(t[1], int) else 0, t[0]))
    labels: list[str] = []
    ys: list[float] = []
    for ts, _bn, price in rows:
        lab = ts.split("T")[0] if "T" in ts else (ts[:10] if len(ts) >= 10 else ts)
        labels.append(lab.replace('"', "'"))
        ys.append(price)
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
    chart = (
        "```mermaid\n"
        "xychart-beta\n"
        '    title "TAOStats daily pool price (τ per α)"\n'
        f"    x-axis {lbl_joined}\n"
        f'    y-axis "Price" in {_mermaid_xychart_decimal(y_lo)} --> {_mermaid_xychart_decimal(y_hi)}\n'
        f"    line {nums_joined}\n"
        "```\n\n"
    )
    return text[: m.start()] + prefix + chart + text[m.end() :]


def _fix_existing_xychart_pool_price_mermaid(text: str) -> str:
    """Rewrite numeric literals in deployed pool-price xycharts (fixes %g / scientific notation)."""

    def fix_body(body: str) -> str:
        lines_out: list[str] = []
        for ln in body.splitlines():
            t = ln.strip()
            if t.startswith("y-axis") and " in " in ln and "-->" in ln:
                mm = re.search(r"\bin\s+(\S+)\s+-->\s+(\S+)\s*$", ln)
                if mm:
                    try:
                        a, b = float(mm.group(1)), float(mm.group(2))
                        if b <= a:
                            b = a + max(1e-18, abs(a) * 1e-12)
                        a = max(0.0, a)
                        b = max(a + 1e-18, b)
                        ln = re.sub(
                            r"\bin\s+\S+\s+-->\s+\S+",
                            f"in {_mermaid_xychart_decimal(a)} --> {_mermaid_xychart_decimal(b)}",
                            ln,
                        )
                    except ValueError:
                        pass
            elif t.startswith("line ") and "[" in ln:
                mm = re.search(r"line\s+(\[[^\]]+\])", ln)
                if mm:
                    inner = mm.group(1).strip()[1:-1]
                    nums = [x.strip() for x in inner.split(",")]
                    new_nums: list[str] = []
                    for p in nums:
                        try:
                            new_nums.append(_mermaid_xychart_decimal(max(0.0, float(p))))
                        except ValueError:
                            new_nums.append(p)
                    ln = re.sub(r"line\s+\[[^\]]+\]", "line [" + ", ".join(new_nums) + "]", ln)
            lines_out.append(ln)
        return "\n".join(lines_out)

    def repl(m: re.Match[str]) -> str:
        body = m.group(1)
        fixed = fix_body(body)
        if fixed == body:
            return m.group(0)
        return "```mermaid\n" + fixed + "\n```"

    return re.sub(
        r"```mermaid\n(xychart-beta\n\s*title \"TAOStats daily pool price[^\n]*\n[\s\S]*?)\n```",
        repl,
        text,
    )


def rewrite_one(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    out = raw
    out = _dedupe_targon_style_hardware(out)
    out = _convert_taostats_subsection(out)
    out = _convert_topology_consensus(out)
    out = _pool_table_to_mermaid(out)
    out = _fix_existing_xychart_pool_price_mermaid(out)
    if out != raw:
        path.write_text(out, encoding="utf-8")
        return True
    return False


def main() -> int:
    subnets = REPO_ROOT / "subnets"
    if not subnets.is_dir():
        print("subnets/ not found", file=sys.stderr)
        return 1
    changed = 0
    for p in sorted(subnets.glob("*.md")):
        if p.name in ("README.md", "overview.md"):
            continue
        if re.match(r"^\d{3}-", p.name) and rewrite_one(p):
            changed += 1
            print("updated", p.relative_to(REPO_ROOT))
    print(f"done, {changed} files changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
