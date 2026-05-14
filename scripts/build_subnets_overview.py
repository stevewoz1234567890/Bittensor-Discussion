#!/usr/bin/env python3
"""Build subnets/overview.md from per-subnet pages (TAOStats + hardware scrape)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _title_meta(text: str) -> tuple[int, str, str]:
    m = re.search(r"^# NetUID (\d+) — (.+)$", text, re.M)
    if not m:
        return -1, "?", ""
    nu = int(m.group(1))
    rest = m.group(2).strip()
    sym_m = re.search(r"\(`([^`]+)`\)\s*$", rest)
    sym = sym_m.group(1) if sym_m else ""
    name = re.sub(r"\s*\(`[^`]+`\)\s*$", "", rest).strip()
    return nu, name, sym


def _field_value(text: str, label_needle: str) -> str:
    """Match TAOStats-style bullet or post-rewrite table row."""
    for line in text.splitlines():
        ls = line.strip()
        if "| Field | Value |" in ls or ls.startswith("| --- |"):
            continue
        if not ls.startswith("|"):
            continue
        if label_needle not in ls:
            continue
        parts = [p.strip() for p in ls.split("|")]
        parts = [p for p in parts if p]
        if len(parts) >= 2:
            key, val = parts[0], parts[1]
            if label_needle in key:
                return val.strip().strip("`").strip()
    m = re.search(rf"- \*\*[^\n]*{re.escape(label_needle)}[^\n]*:\*\* `([^`]*)`", text)
    if m:
        return m.group(1).strip()
    m = re.search(rf"- \*\*[^\n]*{re.escape(label_needle)}[^\n]*:\*\* (.+)$", text, re.M)
    if m:
        return m.group(1).strip()
    return "—"


def _miner_spec_summary(text: str) -> str:
    m = re.search(
        r"## Miner / validator hardware \(CPU/GPU/RAM\)\n\n([\s\S]*?)(?=\n## SubnetIdentity|\n## Alpha price)",
        text,
    )
    if not m:
        return "—"
    block = m.group(1)
    g = re.search(
        r"#### CPU / GPU / RAM lines \(automatic grep\)\n\n([\s\S]*?)(?=\n\*Primary README URL|\n\n## |\Z)",
        block,
    )
    if g:
        lines = [
            re.sub(r"^-\s*", "", ln.strip())
            for ln in g.group(1).splitlines()
            if ln.strip().startswith("-")
        ]
        s = "; ".join(lines[:12])
        if s:
            return s[:420] + ("…" if len(s) > 420 else "")
    block = re.sub(r"\*Primary README URL used:.*", "", block, flags=re.S)
    block = re.sub(r"^#+.*$", "", block, flags=re.M)
    one = " ".join(block.split())[:320]
    return (one + "…") if len(one) >= 320 else (one or "—")


def build_overview(subnets_dir: Path) -> str:
    rows: list[tuple[int, str, str, str, str, str, str, str]] = []
    for p in sorted(subnets_dir.glob("*.md")):
        if p.name in ("README.md", "overview.md"):
            continue
        if not re.match(r"^\d{3}-", p.name):
            continue
        raw = p.read_text(encoding="utf-8")
        nu, name, sym = _title_meta(raw)
        if nu < 0:
            continue
        reg = _field_value(raw, "Registration wall time")
        if reg == "—":
            reg = _field_value(raw, "Registration block")
        nrc = _field_value(raw, "Neuron reg. cost")
        burn = _field_value(raw, "Registration recycle cost snapshot")
        if burn == "—":
            burn = _field_value(raw, "burn")
        spec = _miner_spec_summary(raw)
        link = p.name
        sym_cell = f"`{sym}`" if sym else ""
        rows.append((nu, link, name, sym_cell, reg, spec, nrc, burn))

    rows.sort(key=lambda r: r[0])
    out: list[str] = [
        "# Subnet overview",
        "",
        "Snapshot fields are taken from each [subnet page](README.md) "
        "(**TAOStats** registration time and neuron registration cost, **SubnetInfo** burn snapshot, "
        "and the **Miner / validator hardware** scrape where present). Values reflect the block "
        "cited in each page footer when the page was last generated.",
        "",
        "| NetUID | Subnet | Sym | Registration (wall) | Miner compute spec (scrape) | Neuron reg. cost (RAO) | Reg. burn snapshot (`SubnetInfo`) |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for nu, link, name, sym_cell, reg, spec, nrc, burn in rows:
        esc = spec.replace("|", "\\|")
        out.append(
            f"| [{nu}]({link}) | {name} | {sym_cell} | {reg} | {esc} | {nrc} | {burn} |"
        )
    out.extend(["", "---", "", "Regenerate this file: `python scripts/build_subnets_overview.py`", ""])
    return "\n".join(out)


def main() -> int:
    d = REPO_ROOT / "subnets"
    if not d.is_dir():
        print("subnets/ missing", file=sys.stderr)
        return 1
    (d / "overview.md").write_text(build_overview(d), encoding="utf-8")
    print("wrote", d / "overview.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
