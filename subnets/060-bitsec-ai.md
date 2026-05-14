# NetUID 60 — Bitsec.ai (`ذ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Bitsec.ai** (NetUID **60**) (`ذ`).

find and fix exploits in codebases

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `47`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,785.600057376. **Alpha liquidity in pool (`alpha_in`)** = ‎1,676,784.103657226ذ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,956,546.643194056ذ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004062505`** *(also **moving-average price** `0.0040231815073639154` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎680,983.912424123ذ‎`. **Owner hotkey / coldkey (chain):** `5CXLwkK1Scd1uiMUrXYjJUTTPxqqyH2FTJQNLp9uXQhA9rhR` / `5CXLwkK1Scd1uiMUrXYjJUTTPxqqyH2FTJQNLp9uXQhA9rhR`.
- **Subnet registered at block:** `4796992` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎35.282603286ذ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ذ‎` · α-in `‎0.000000000ذ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104388`
- **Liquidity constant `k`:** `11377986309983637477036998976`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Bitsec.ai` |
| Symbol (API) | `ذ` |
| Rank | `66` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004007786` |
| Market cap | `16922013791442.014263534` |
| Market cap Δ 1d | `2.181002081859244869` |
| Liquidity | `13505476784856` |
| Total τ | `6738966823538` |
| Total α | `4633097746851282` |
| α in pool | `1688341134311656` |
| α staked | `2533943636242963` |
| Price Δ 1h | `-0.000848341492382392` |
| Price Δ 1d | `2.059506823556734543` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `60` |
| Owner SS58 (API) | `5CXLwkK1Scd1uiMUrXYjJUTTPxqqyH2FTJQNLp9uXQhA9rhR` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4796992` |
| Registration wall time | `2025-01-27T14:33:48Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `9` |
| Active miners | `2` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Bitsec Subnet v2** <!-- omit in toc -->

[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** bitsec

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 256 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5CXLwkK1Scd1uiMUrXYjJUTTPxqqyH2FTJQNLp9uXQhA9rhR` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## In order to simplify the building of subnets, this template abstracts away the complexity of the underlying blockchain and other boilerplate code. While the default behavior of the template is sufficient for a simple subnet, you should customize the template in order to meet your specific requirements.

```python
python -m venv env; source env/bin/activate;
pip install -U pip
pip install -r requirements.txt
```

---









#### CPU / GPU / RAM lines (automatic grep)

- - Limit resources (CPU/time) to prevent hangs.


*Primary README URL used: `https://raw.githubusercontent.com/Bitsec-AI/sandbox/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://bitsec.ai](https://bitsec.ai)
- **GitHub:** [https://github.com/Bitsec-AI/sandbox](https://github.com/Bitsec-AI/sandbox)
- **Discord (handle / invite hint):** `yubo`
- **Contact:** john@bitsec.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004007564 |
| 8104292 | 0.004007555 |
| 8104340 | 0.00400754 |
| 8104388 | 0.004007528 |
| 8104436 | 0.004062504 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

