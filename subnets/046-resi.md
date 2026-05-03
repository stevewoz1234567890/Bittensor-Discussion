# NetUID 46 — RESI (`ץ`)

## Overview

The Real Estate Oracle

Real Estate Super Intelligence

**From crawled page (site or GitHub):** RESI is the institutional-grade intelligence layer for the future of PropTech.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 256
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.100000000
- **Owner SS58 (`owner_ss58`):** `5Ft9E2ovN52AVMczVA3713uXmmBPczvUboB4YQpupu3aEYg7`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.100000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

### For Validators

See the [Validator Setup Guide](docs/VALIDATOR.md) for complete setup instructions.

---

### For Miners

See the [Miner Guide](docs/MINER.md) for complete setup instructions.

---

---

## Model Requirements

| Requirement | Specification |
|-------------|---------------|
| **Format** | ONNX (`.onnx` file) |
| **Max Size** | 200 MB |
| **License** | MIT (verified via HuggingFace metadata) |
| **Commit Age** | Must be committed ~30 days before evaluation |
| **Input** | Property features (see documentation) |
| **Output** | Predicted price in USD |

---

---

### Prerequisites

- Python >=3.11, <3.14
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager
- Docker (for validators)

---

### Install

```bash

---

# Install uv

curl -LsSf https://astral.sh/uv/install.sh | sh

---

# Clone and setup

git clone https://github.com/resi-labs-ai/RESI-models.git
cd RESI-models
uv sync


*README source used for excerpts: `https://raw.githubusercontent.com/resi-labs-ai/RESI-models/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


The Real Estate Oracle

## On-chain identity — additional field


Real Estate Super Intelligence

## Registered contact & links


- **Website:** [https://resilabs.ai](https://resilabs.ai)
- **GitHub:** [https://github.com/resi-labs-ai/RESI-models](https://github.com/resi-labs-ai/RESI-models)
- **Discord:** [https://discord.gg/9Hxmh7H6Pt](https://discord.gg/9Hxmh7H6Pt)
- **Logo URL:** [https://resi-public.nyc3.cdn.digitaloceanspaces.com/color_3_r.png](https://resi-public.nyc3.cdn.digitaloceanspaces.com/color_3_r.png)
- **Contact:** support@resilabs.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.008323072 |
| 8103690 | 0.008354354 |
| 8103738 | 0.008375227 |
| 8103786 | 0.008378165 |
| 8103834 | 0.008423842 |
| 8103882 | 0.008425076 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** RESI
- **Meta / og:description:** RESI is the institutional-grade intelligence layer for the future of PropTech.
- **Fetched from:** [https://resilabs.ai](https://resilabs.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

