# NetUID 18 — Zeus (`σ`)

## Overview

**Zeus** (NetUID **18**) (`σ`).

Pushing weather forecasts beyond state-of-the-art

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `208`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ12,270.865660157. **Alpha liquidity in pool (`alpha_in`)** = ‎1,879,620.850981210σ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,809,384.691630035σ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006539001`** *(also **moving-average price** `0.00655178795568645` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎735,305.354905348σ‎`. **Owner hotkey / coldkey (chain):** `5HdrwVQQbMa8Wh271PDzvMHmM44wYM5wfnXCW3o97gDisuaY` / `5DHwWLjtpwnZQUQKKXE2N5Gdy2N8PpqhgjLUuzgSB7yuGZkF`.
- **Subnet registered at block:** `1604679` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎156.285987842σ‎`; pending root emission `τ0.000000000`.
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
| 8104037 | 0.006544461 |
| 8104085 | 0.006544354 |
| 8104133 | 0.006554884 |
| 8104181 | 0.006554879 |
| 8104229 | 0.006554858 |
| 8104277 | 0.006539001 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.007199587 |
| 2026-03-10T23:59:48Z | 7718257 | 0.007126919 |
| 2026-03-11T23:59:48Z | 7725455 | 0.007464864 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.007227748 |
| 2026-03-13T23:59:48Z | 7739841 | 0.007050819 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.006620559 |
| 2026-03-15T23:59:48Z | 7754226 | 0.006428719 |
| 2026-03-16T23:59:48Z | 7761426 | 0.006624743 |
| 2026-03-17T23:59:48Z | 7768619 | 0.006575675 |
| 2026-03-18T23:59:48Z | 7775819 | 0.006459718 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00662488438873599185 |
| 2026-03-20T23:59:48Z | 7790201 | 0.006553407 |
| 2026-03-21T23:59:48Z | 7797398 | 0.006689179 |
| 2026-03-22T23:59:48Z | 7804598 | 0.007060043 |
| 2026-03-23T23:59:48Z | 7811798 | 0.007509693 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00723362627542961875 |
| 2026-03-25T23:59:48Z | 7826196 | 0.007368414 |
| 2026-03-26T23:59:48Z | 7833396 | 0.007040594 |
| 2026-03-27T23:59:48Z | 7840596 | 0.007325161 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.007016954 |
| 2026-03-29T23:59:48Z | 7854902 | 0.007169008 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.007586905 |
| 2026-03-31T23:59:48Z | 7869291 | 0.007624239 |
| 2026-04-01T23:59:48Z | 7876474 | 0.007425438 |
| 2026-04-02T23:59:48Z | 7883622 | 0.008083527 |
| 2026-04-03T23:59:48Z | 7890794 | 0.008211056 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.008350372 |
| 2026-04-05T23:59:48Z | 7905188 | 0.008095473 |
| 2026-04-06T23:59:48Z | 7912388 | 0.008129751 |
| 2026-04-07T23:59:48Z | 7919588 | 0.007892282 |
| 2026-04-08T23:59:48Z | 7926788 | 0.007753025 |
| 2026-04-09T23:59:48Z | 7933987 | 0.007558498 |
| 2026-04-10T23:59:48Z | 7941184 | 0.007097638 |
| 2026-04-11T23:59:48Z | 7948384 | 0.007039756 |
| 2026-04-12T23:59:48Z | 7955584 | 0.006931206 |
| 2026-04-13T23:59:48Z | 7962784 | 0.007070496 |
| 2026-04-14T23:59:48Z | 7969979 | 0.007103269 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.007007058 |
| 2026-04-16T23:59:48Z | 7984379 | 0.006924776 |
| 2026-04-17T23:59:48Z | 7991579 | 0.006959371 |
| 2026-04-18T23:59:48Z | 7998779 | 0.006940486 |
| 2026-04-19T23:59:48Z | 8005979 | 0.006975734 |
| 2026-04-20T23:59:48Z | 8013179 | 0.007101283 |
| 2026-04-21T23:59:48Z | 8020376 | 0.007088044 |
| 2026-04-22T23:59:48Z | 8027562 | 0.00714923 |
| 2026-04-23T23:59:48Z | 8034762 | 0.007342912 |
| 2026-04-24T23:59:48Z | 8041962 | 0.00696888 |
| 2026-04-25T23:59:48Z | 8049151 | 0.006827515 |
| 2026-04-26T23:59:48Z | 8056274 | 0.006816038 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.006828173 |
| 2026-04-28T23:59:48Z | 8070646 | 0.006962801 |
| 2026-04-29T23:59:48Z | 8077790 | 0.006922797 |
| 2026-04-30T23:59:48Z | 8084984 | 0.006872558 |
| 2026-05-01T23:59:48Z | 8092168 | 0.006863967 |
| 2026-05-02T23:59:48Z | 8099357 | 0.00650079 |
| 2026-05-03T16:10:00Z | 8104202 | 0.006554875 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

