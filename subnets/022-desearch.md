# NetUID 22 — Desearch (`χ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Desearch** (NetUID **22**) (`χ`).

Decentralized search engine

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `9`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ9,424.382430684. **Alpha liquidity in pool (`alpha_in`)** = ‎1,947,007.211258143χ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,094,529.117813379χ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004840334`** *(also **moving-average price** `0.004845665069296956` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎238,935.985677644χ‎`. **Owner hotkey / coldkey (chain):** `5CUu1QhvrfyMDBELUPJLt4c7uJFbi7TKqDHkS1Zz41oD4dyP` / `5DFuaMasyQtPhXcsuoYEyJmCVSRtzKxsTKFTA4SrpcGXBxJn`.
- **Subnet registered at block:** `2009702` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎6.798797956χ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000χ‎` · α-in `‎0.000000000χ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104426`
- **Liquidity constant `k`:** `18349340554196294016128059812`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Desearch` |
| Symbol (API) | `χ` |
| Rank | `56` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.00484038` |
| Market cap | `19867798430136.29097306` |
| Market cap Δ 1d | `1.284855020913109743` |
| Liquidity | `18848637195532` |
| Total τ | `9424427657334` |
| Total α | `5041303329071522` |
| α in pool | `1946997867563895` |
| α staked | `2157596901883192` |
| Price Δ 1h | `-0.000537145024611572` |
| Price Δ 1d | `1.168783937999272645` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `22` |
| Owner SS58 (API) | `5DFuaMasyQtPhXcsuoYEyJmCVSRtzKxsTKFTA4SrpcGXBxJn` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `2009702` |
| Registration wall time | `2023-12-26T00:06:12.001Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `14` |
| Active miners | `10` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `14` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

<img src="./docs/assets/desearch-logo.png" alt="Desearch" width="480" />

# **Subnet 22 on Bittensor**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

Welcome to **Desearch powered by Bittensor Subnet 22**! Desearch is a decentralized,
AI-powered search engine that returns unbiased and verifiable results across X, Reddit,
Arxiv, Hacker News, Wikipedia, YouTube, and the broader web. Frontend and API access are
available at [desearch.ai](https://desearch.ai).

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** AI-powered search APIs for web and Twitter/X data. Build intelligent agents with real-time search, semantic retrieval, and structured responses.

**Fetched document title:** Desearch - AI Search APIs for Web and X Data

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
| `immunity_period` (blocks) | 7200 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5DFuaMasyQtPhXcsuoYEyJmCVSRtzKxsTKFTA4SrpcGXBxJn` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `7200` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `10` |
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

### For Miners

Miners contribute search capacity and are rewarded based on result quality and volume.
Expected setup steps:

- Prepare a server with Python ≥ 3.10, PM2, and a registered hotkey on netuid 22.
- Configure credentials for OpenAI, SerpAPI, and Apify.
- Declare per-search-type concurrency in `neurons/miners/manifest.json`.
- Run the axon with PM2.

See the [Miner Setup Guide](./docs/running_a_miner.md) for full instructions.

---

### For Validators

Validators verify miner outputs and write weights on-chain. Expected setup steps:

- Prepare a server with Python ≥ 3.10, PM2, Redis, `jq`, and a registered validator hotkey.
- Configure credentials for OpenAI, Apify, ScrapingDog, and W&B.
- Generate a public API access key and run the autoupdate script.

See the [Validator Setup Guide](./docs/running_a_validator.md) for full instructions.

---









#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/datura-ai/desearch/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://desearch.ai](https://desearch.ai)
- **GitHub:** [https://github.com/datura-ai/desearch](https://github.com/datura-ai/desearch)
- **Discord:** [https://discord.gg/P44zrJmdFy](https://discord.gg/P44zrJmdFy)
- **Logo URL:** [https://desearch.ai/assets/logo-icon-C18R0lAC.png](https://desearch.ai/assets/logo-icon-C18R0lAC.png)
- **Contact:** giga@desearch.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.004840381 |
| 8104244 | 0.004840365 |
| 8104292 | 0.004840355 |
| 8104340 | 0.004840338 |
| 8104388 | 0.004840337 |
| 8104436 | 0.004840334 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

