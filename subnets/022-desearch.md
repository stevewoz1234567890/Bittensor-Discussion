# NetUID 22 — Desearch (`χ`)

## Overview

**Desearch** (NetUID **22**) (`χ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `212`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ9,424.404958400. **Alpha liquidity in pool (`alpha_in`)** = ‎1,947,002.557080652χ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,094,375.771990870χ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004840357`** *(also **moving-average price** `0.004845922579988837` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎238,935.963149928χ‎`. **Owner hotkey / coldkey (chain):** `5CUu1QhvrfyMDBELUPJLt4c7uJFbi7TKqDHkS1Zz41oD4dyP` / `5DFuaMasyQtPhXcsuoYEyJmCVSRtzKxsTKFTA4SrpcGXBxJn`.
- **Subnet registered at block:** `2009702` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎160.148258487χ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000χ‎` · α-in `‎0.000000000χ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.00484038`
- **Market cap:** `19867798430136.29097306`
- **Liquidity:** `18848637195532`
- **Total τ:** `9424427657334`
- **Total α:** `5041303329071522`
- **α in pool:** `1946997867563895`
- **α staked:** `2157596901883192`
- **Price Δ 1h:** `-0.000537145024611572`
- **Price Δ 1d:** `1.168783937999272645`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `14`
- **Active miners:** `10`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `14`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Decentralized search engine

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
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5DFuaMasyQtPhXcsuoYEyJmCVSRtzKxsTKFTA4SrpcGXBxJn`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `10`
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

## On-chain identity — description


Decentralized search engine

## On-chain identity — additional field


*Unset.*

## Registered contact & links


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
| 8104037 | 0.004840395 |
| 8104085 | 0.004840392 |
| 8104133 | 0.004840386 |
| 8104181 | 0.004840382 |
| 8104229 | 0.004840368 |
| 8104277 | 0.004840357 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

