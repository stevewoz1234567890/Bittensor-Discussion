# NetUID 10 — Swap (`κ`)

## Overview

**Swap** (NetUID **10**) (`κ`).

Swap is onboarding users to Bittensor.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `138`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ15,769.448415334. **Alpha liquidity in pool (`alpha_in`)** = ‎2,685,838.373859430κ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,268,821.353708658κ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005874865`** *(also **moving-average price** `0.005910578416660428` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎810,836.320946089κ‎`. **Owner hotkey / coldkey (chain):** `5EvNESR7DfSMmdwJ3crtBW1ENAhq3f99X4FCbTi1hDUNCWAW` / `5GbcimKjp17QPUoS568DBSMNqV2pmDetBf3xyC15vh4bTFE1`.
- **Subnet registered at block:** `2869647` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎104.116489742κ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000κ‎` · α-in `‎0.000000000κ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005874865`
- **Market cap:** `26725246169214.6895117`
- **Liquidity:** `31548386273567`
- **Total τ:** `15769448712458`
- **Total α:** `4954646727568088`
- **α in pool:** `2685838323282275`
- **α staked:** `1863244280184305`
- **Price Δ 1h:** `0.012274128792212108`
- **Price Δ 1d:** `-0.801893705815726039`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `15`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `15`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Swap is onboarding users to Bittensor.

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Swap** <!-- omit in toc -->

[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** The financial layer for decentralized AI.

**Fetched document title:** Pool | TaoFi

## Operational parameters — registration, limits, economics (chain)


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
- **`immunity_period` (blocks):** 12600
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GbcimKjp17QPUoS568DBSMNqV2pmDetBf3xyC15vh4bTFE1`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `12600` blocks
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
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Prerequisites

Install `uv` for fast Python package management:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### Install

```bash
git clone https://github.com/Swap-Subnet/swap-subnet/
cd swap-subnet
uv pip install -e .
```

For development dependencies:
```bash
uv pip install -e ".[dev]"
```

---

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/Swap-Subnet/swap-subnet/main/README.md`*

## On-chain identity — description


Swap is onboarding users to Bittensor.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.taofi.com/pool](https://www.taofi.com/pool)
- **GitHub:** [https://github.com/Swap-Subnet/swap-subnet](https://github.com/Swap-Subnet/swap-subnet)
- **Logo URL:** [https://www.taofi.com/images/SN10-Swap-Dark.png](https://www.taofi.com/images/SN10-Swap-Dark.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8103976 | 0.005874139 |
| 8104024 | 0.005874138 |
| 8104072 | 0.005874134 |
| 8104120 | 0.005874871 |
| 8104168 | 0.005874868 |
| 8104216 | 0.005874865 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

