#!/usr/bin/env python3
"""Rewrite existing subnets/*.md layout: TAOStats + SubnetInfo + hyperparams → tables; pool xychart → table.

Idempotent for files already rewritten. Does not require bittensor.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


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
        if stripped.rstrip() == body.rstrip():
            return m.group(0)
        if not stripped:
            return hdr + "*Same content as **Overview → Repository README excerpt** above; see repo for full runbooks.*\n\n"
        return hdr + stripped.rstrip() + "\n\n"

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


def _extended_history_mermaid_to_table(text: str) -> str:
    """Replace TAOStats daily pool-price Mermaid xychart with the original three-column markdown table."""

    def repl(m: re.Match[str]) -> str:
        prefix = m.group(1)
        body = m.group(2)
        ax = re.search(r"x-axis\s+(\[[^\]]+\])", body)
        line_m = re.search(r"line\s+(\[[^\]]+\])", body)
        if not ax or not line_m:
            return m.group(0)
        labels = re.findall(r'"([^"]*)"', ax.group(1))
        inner = line_m.group(1).strip()[1:-1]
        price_tokens = [x.strip() for x in inner.split(",")]
        for p in price_tokens:
            try:
                float(p)
            except ValueError:
                return m.group(0)
        n = min(len(labels), len(price_tokens))
        if n < 1:
            return m.group(0)
        out_lines = [
            "| Timestamp (UTC) | Block | Pool price |",
            "|-----------------|------:|-----------:|",
        ]
        for i in range(n):
            lab = labels[i].strip().replace('"', "'")
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", lab):
                ts = f"{lab}T23:59:48Z"
            else:
                ts = lab
            out_lines.append(f"| {ts} | — | {price_tokens[i]} |")
        return prefix + "\n".join(out_lines) + "\n\n"

    return re.sub(
        r"(### Extended history — TAOStats pool price \(daily\)\n\n"
        r"(?:\[TAOStats\][^\n]*\n\n)?)```mermaid\nxychart-beta\n([\s\S]*?)\n```\s*",
        repl,
        text,
    )


def rewrite_one(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    out = raw
    out = _dedupe_targon_style_hardware(out)
    out = _convert_taostats_subsection(out)
    out = _convert_topology_consensus(out)
    out = _extended_history_mermaid_to_table(out)
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
