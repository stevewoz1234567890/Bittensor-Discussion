# NetUID 18 — Zeus (`σ`)

## Overview

**Zeus** (NetUID **18**) (`σ`).

Pushing weather forecasts beyond state-of-the-art

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `146`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ12,285.878486044. **Alpha liquidity in pool (`alpha_in`)** = ‎1,877,327.743011935σ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,811,615.799599310σ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006554875`** *(also **moving-average price** `0.006551762344315648` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎735,290.342079461σ‎`. **Owner hotkey / coldkey (chain):** `5HdrwVQQbMa8Wh271PDzvMHmM44wYM5wfnXCW3o97gDisuaY` / `5DHwWLjtpwnZQUQKKXE2N5Gdy2N8PpqhgjLUuzgSB7yuGZkF`.
- **Subnet registered at block:** `1604679` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎109.700760898σ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000σ‎` · α-in `‎0.000000000σ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.006554875`
- **Market cap:** `29630120057552.57454575`
- **Liquidity:** `24591527175510`
- **Total τ:** `12285878879075`
- **Total α:** `4688930542611245`
- **α in pool:** `1877327683050487`
- **α staked:** `2642990409598507`
- **Price Δ 1h:** `0.158897366267368083`
- **Price Δ 1d:** `1.511221965991620944`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `257`
- **Active validators:** `11`
- **Active miners:** `20`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `257`
- **Validators (metadata):** `11`
- **Neuron reg. cost:** `999999999`

### On-chain declared purpose *(SubnetIdentity)*

Pushing weather forecasts beyond state-of-the-art



**Additional commentary (on-chain)**


Powered by Ørpheus AI

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

## Operational parameters — registration, limits, economics (chain)


### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 257
- **`subnetwork_n`:** 257
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 65535
- **Registration recycle cost snapshot (`burn`):** τ0.999999999
- **Owner SS58 (`owner_ss58`):** `5DHwWLjtpwnZQUQKKXE2N5Gdy2N8PpqhgjLUuzgSB7yuGZkF`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.999999999 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `65535` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `5`
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

## On-chain identity — description


Pushing weather forecasts beyond state-of-the-art

## On-chain identity — additional field


Powered by Ørpheus AI

## Registered contact & links


- **Website:** [https://www.zeussubnet.com/](https://www.zeussubnet.com/)
- **GitHub:** [https://github.com/Orpheus-AI/Zeus](https://github.com/Orpheus-AI/Zeus)
- **Discord (handle / invite hint):** `wouter_orpheusai`
- **Logo URL:** [https://raw.githubusercontent.com/Orpheus-AI/Zeus/refs/heads/main/static/zeus-icon.png](https://raw.githubusercontent.com/Orpheus-AI/Zeus/refs/heads/main/static/zeus-icon.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8103976 | 0.006544469 |
| 8104024 | 0.006544465 |
| 8104072 | 0.006544458 |
| 8104120 | 0.006554886 |
| 8104168 | 0.006554879 |
| 8104216 | 0.006554875 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

