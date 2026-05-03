# NetUID 127 — Astrid (`𑀅`)

## Overview

The capital axis for Bittensor.

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5FU4uxAdrZsaWaezWwXEK93MwPX5gw2566BQK2WwrGUudfSH`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

# Astrid Validator - Subnet 127

A production-ready Bittensor subnet validator daemon for Subnet 127 (Astrid). This validator connects to the Astrid coordination service, executes trading strategy simulations in isolated Docker environments, and manages Bittensor weight commitments.

---

## Prerequisites

- Node.js 20+
- Docker and Docker Compose
- Redis 7+ (included in docker-compose.yml)
- Bittensor validator identity (mnemonic phrase)

---

## Installation

```bash

---

# Install dependencies

npm install

---

# Validator identity (Polkadot/Substrate mnemonic or secret seed)

VALIDATOR_MNEMONIC="your twelve word seed phrase goes here"
VALIDATOR_SECRET_SEED="0x..."

---

# Validator display name

VALIDATOR_DISPLAY_NAME=Validator Name

---

### Validator fails to register

- Verify `API_URL` is correct and accessible
- Check that `VALIDATOR_MNEMONIC` or `VALIDATOR_SECRET_SEED` is valid
- Ensure network connectivity to the coordinator


*README source used for excerpts: `https://raw.githubusercontent.com/astridintelligence/sn-127/master/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


The capital axis for Bittensor.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://www.astrid.global/](https://www.astrid.global/)
- **GitHub:** [https://github.com/astridintelligence/sn-127](https://github.com/astridintelligence/sn-127)
- **Logo URL:** [https://cdn.prod.website-files.com/68b07769f32da8fcc36dc172/69f2325c06235848691480b7_Astrid%20Square.png](https://cdn.prod.website-files.com/68b07769f32da8fcc36dc172/69f2325c06235848691480b7_Astrid%20Square.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.004237083 |
| 8103738 | 0.00423707 |
| 8103786 | 0.004236963 |
| 8103834 | 0.004236954 |
| 8103882 | 0.004236932 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Astrid Intelligence PLC
- **Fetched from:** [https://www.astrid.global/](https://www.astrid.global/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

