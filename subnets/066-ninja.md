# NetUID 66 — ninja (`ض`)

## Overview

Distilling software agents

**From crawled page (site or GitHub):** Contribute to unarbos/tau development by creating an account on GitHub.

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
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 6080
- **Registration recycle cost snapshot (`burn`):** τ0.018559526
- **Owner SS58 (`owner_ss58`):** `5DRtWRDDrcKfgwPBkjADBVPSFzpLSGXejzNXXRtfSCpkFKHP`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `6080` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `3`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

## Prerequisites

- Python 3.11+
- `uv`
- Docker
- A GitHub token for task generation
- An OpenRouter API key for Docker PI solves and evaluation
- A Cursor API key for Cursor solves

---

## Setup

From the `tau/` directory:

```bash
source .venv/bin/activate
uv pip install -e .
```

Create a `.env` file in `tau/` if you do not already have one:

```bash
GITHUB_TOKEN=your_github_token
OPENROUTER_API_KEY=your_openrouter_api_key
CURSOR_API_KEY=your_cursor_api_key
```

`tau` loads `.env` automatically from the project root.


*README source used for excerpts: `https://raw.githubusercontent.com/unarbos/tau/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Distilling software agents

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/unarbos/tau](https://github.com/unarbos/tau)
- **Discord (handle / invite hint):** `arbos`
- **Logo:** `🥷`
- **Contact:** tau@arbos.life

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.014205284 |
| 8103690 | 0.01422739 |
| 8103738 | 0.014262419 |
| 8103786 | 0.014270806 |
| 8103834 | 0.014285602 |
| 8103882 | 0.014265888 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** GitHub - unarbos/tau · GitHub
- **Meta / og:description:** Contribute to unarbos/tau development by creating an account on GitHub.
- **Fetched from:** [https://github.com/unarbos/tau](https://github.com/unarbos/tau)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

