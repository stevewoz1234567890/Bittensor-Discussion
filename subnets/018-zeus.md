# NetUID 18 — Zeus (`σ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Zeus** (NetUID **18**) (`σ`).

Pushing weather forecasts beyond state-of-the-art



#### SubnetIdentity `additional` *(chain)*



Powered by Ørpheus AI

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `5`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ12,270.834399471. **Alpha liquidity in pool (`alpha_in`)** = ‎1,879,625.631661728σ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,809,537.910949517σ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006538968`** *(also **moving-average price** `0.006551199359819293` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎735,305.386166034σ‎`. **Owner hotkey / coldkey (chain):** `5HdrwVQQbMa8Wh271PDzvMHmM44wYM5wfnXCW3o97gDisuaY` / `5DHwWLjtpwnZQUQKKXE2N5Gdy2N8PpqhgjLUuzgSB7yuGZkF`.
- **Subnet registered at block:** `1604679` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎3.756906159σ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000σ‎` · α-in `‎0.000000000σ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104430`
- **Liquidity constant `k`:** `23064574859122139146694145888`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Zeus` |
| Symbol (API) | `σ` |
| Rank | `35` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.006554875` |
| Market cap | `29630120057552.57454575` |
| Market cap Δ 1d | `1.631658795012948997` |
| Liquidity | `24591527175510` |
| Total τ | `12285878879075` |
| Total α | `4688930542611245` |
| α in pool | `1877327683050487` |
| α staked | `2642990409598507` |
| Price Δ 1h | `0.158897366267368083` |
| Price Δ 1d | `1.511221965991620944` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `18` |
| Owner SS58 (API) | `5DHwWLjtpwnZQUQKKXE2N5Gdy2N8PpqhgjLUuzgSB7yuGZkF` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `1604679` |
| Registration wall time | `2023-10-30T14:06:36.007Z` |
| Registration cost snapshot | `0` |
| Active keys | `257` |
| Active validators | `11` |
| Active miners | `20` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `257` |
| Validator slots (metadata) | `11` |
| Max validators (API) | `64` |
| Neuron reg. cost | `999999999` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <img src="static/zeus-icon.png" alt="Zeus Logo" width="150"/>
</p>
<h1 align="center">SN18: Zeus Environmental Forecasting Subnet<br><small>Ørpheus AI</small></h1>


![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Welcome to the Zeus Subnet! This repository contains all the necessary information to get started, understand our subnet architecture, and contribute.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Orpheus AI is a company that operates at the intersection of weather and energy markets.

**Fetched document title:** Orpheus AI

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 257 |
| `subnetwork_n` | 257 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 65535 |
| Registration recycle cost snapshot (`burn`) | τ0.999999999 |
| Owner SS58 (`owner_ss58`) | `5DHwWLjtpwnZQUQKKXE2N5Gdy2N8PpqhgjLUuzgSB7yuGZkF` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.999999999 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `65535` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `5` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
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

## Predicting future environmental variables within a decentralized framework

**Overview:**
The Zeus Subnet leverages advanced AI models within the Bittensor network to forecast environmental data. This platform is engineered on a decentralized, incentive-driven framework to enhance trustworthiness and stimulate continuous technological advancement. The datasource for this subnet consists of ERA5 reanalysis data from the Climate Data Store (CDS) of the European Union's Earth observation programme (Copernicus). This comprises the largest global environmental dataset to date, containing hourly measurements from 1940 until the present across a multitude of hundreds of variables. Validators can stream data from this data source in real-time, allowing miners to be queried on terabytes of data.

**Purpose:**
Traditionally, environmental forecasting is achieved through physics-based numerical weather/environmental prediction (NWP). While this allows for very accurate predictions, it is also highly cost-ineffective, requiring large amounts of computing power for a single forecast. Furthermore, predictions are time expensive to obtain, since the simulation process of these NWP algorithms can take multiple hours to finish. Currently, there is a lot of ongoing research into the development of intelligent, data-driven algorithms for environmental prediction. Such algorithms can potentially be much faster, more accurate, at a fraction of the cost and carbon emissions. This subnet incentives the development of novel and groundbreaking architectures for environmental data prediction. Through the continuous evolution of this subnet, we are able to allow miners to tackle increasingly difficult problems over time.

**Features:**

- **Short- and long-horizon forecasts:** Validators issue both **short-range** challenges (hourly steps from the current hour through **+48 hours**, 49 timesteps) and **long-range** challenges (the same grid through **+360 hours**, i.e. 15 days, 361 timesteps). Each ERA5 variable is evaluated on both horizons; see [constants](zeus/validator/constants.py) for windows and weights.
- **Model Evolution:** Our platform continuously integrates the latest research and developments in AI to adapt to evolving generative techniques.

**Core Components:**

- **Miners:** Tasked with running forecasting algorithms that predict environmental variables at specific locations and timestamps.
  - **Research Integration:** We systematically update our detection models and methodologies in response to emerging academic research. Through the global ERA5 dataset, we are able to provide validators and miners with near infinite amounts of environmental data, which can also be used for training their models. All data is publicly available to everyone.
- **Validators:** Responsible for challenging miners with a subsets of environmental data and evaluating miner performance on heldout data. Validation uses a commit–reveal flow; see the [Validator Guide](docs/Validating.md#validator-phases) for phases and timing.
  - **Resource Expansion:** We continuously add new environmental challenges and data modalities to our subnet in order to evolve our subnet and solve a multitude of distinct problems.

---









#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/Orpheus-AI/Zeus/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.zeussubnet.com/](https://www.zeussubnet.com/)
- **GitHub:** [https://github.com/Orpheus-AI/Zeus](https://github.com/Orpheus-AI/Zeus)
- **Discord (handle / invite hint):** `wouter_orpheusai`
- **Logo URL:** [https://raw.githubusercontent.com/Orpheus-AI/Zeus/refs/heads/main/static/zeus-icon.png](https://raw.githubusercontent.com/Orpheus-AI/Zeus/refs/heads/main/static/zeus-icon.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.006554877 |
| 8104244 | 0.006554854 |
| 8104292 | 0.006538998 |
| 8104340 | 0.006538975 |
| 8104388 | 0.006538973 |
| 8104436 | 0.006538968 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.006274987 --> 0.008504104
    line [0.007199587, 0.007126919, 0.007464864, 0.007227748, 0.007050819, 0.006620559, 0.006428719, 0.006624743, 0.006575675, 0.006459718, 0.00662488438874, 0.006553407, 0.006689179, 0.007060043, 0.007509693, 0.00723362627543, 0.007368414, 0.007040594, 0.007325161, 0.007016954, 0.007169008, 0.007586905, 0.007624239, 0.007425438, 0.008083527, 0.008211056, 0.008350372, 0.008095473, 0.008129751, 0.007892282, 0.007753025, 0.007558498, 0.007097638, 0.007039756, 0.006931206, 0.007070496, 0.007103269, 0.007007058, 0.006924776, 0.006959371, 0.006940486, 0.006975734, 0.007101283, 0.007088044, 0.00714923, 0.007342912, 0.00696888, 0.006827515, 0.006816038, 0.006828173, 0.006962801, 0.006922797, 0.006872558, 0.006863967, 0.00650079, 0.006554875]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

