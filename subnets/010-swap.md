# NetUID 10 — Swap (`κ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Swap** (NetUID **10**) (`κ`).

Swap is onboarding users to Bittensor.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `358`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ15,768.086579532. **Alpha liquidity in pool (`alpha_in`)** = ‎2,686,070.201038039κ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,268,809.526530049κ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005873851`** *(also **moving-average price** `0.005908353487029672` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎810,837.682781891κ‎`. **Owner hotkey / coldkey (chain):** `5EvNESR7DfSMmdwJ3crtBW1ENAhq3f99X4FCbTi1hDUNCWAW` / `5GbcimKjp17QPUoS568DBSMNqV2pmDetBf3xyC15vh4bTFE1`.
- **Subnet registered at block:** `2869647` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎270.099706382κ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000κ‎` · α-in `‎0.000000000κ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104077`
- **Liquidity constant `k`:** `42354187488668723971330817748`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Swap`
- **Symbol (API):** `κ`
- **Rank:** `41`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005874865`
- **Market cap:** `26725246169214.6895117`
- **Market cap Δ 1d:** `-0.709353622637208867`
- **Liquidity:** `31548386273567`
- **Total τ:** `15769448712458`
- **Total α:** `4954646727568088`
- **α in pool:** `2685838323282275`
- **α staked:** `1863244280184305`
- **Price Δ 1h:** `0.012274128792212108`
- **Price Δ 1d:** `-0.801893705815726039`
#### Subnet activity (TAOStats)

- **NetUID (API):** `10`
- **Owner SS58 (API):** `5GbcimKjp17QPUoS568DBSMNqV2pmDetBf3xyC15vh4bTFE1`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `2869647`
- **Registration wall time:** `2024-05-02T14:38:00Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `15`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `15`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Swap** <!-- omit in toc -->

[![License:
MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** The financial layer for decentralized AI.

**Fetched document title:** Pool | TaoFi

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.taofi.com/pool](https://www.taofi.com/pool)
- **GitHub:** [https://github.com/Swap-Subnet/swap-subnet](https://github.com/Swap-Subnet/swap-subnet)
- **Logo URL:** [https://www.taofi.com/images/SN10-Swap-Dark.png](https://www.taofi.com/images/SN10-Swap-Dark.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.005874866 |
| 8104244 | 0.005874364 |
| 8104292 | 0.005874356 |
| 8104340 | 0.005873854 |
| 8104388 | 0.005873853 |
| 8104436 | 0.005873851 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

