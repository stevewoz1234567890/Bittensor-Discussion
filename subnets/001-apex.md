# NetUID 1 — Apex (`α`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Apex** (NetUID **1**) (`α`).

Open competitions for algorithmic and agentic optimization

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `99` blocks between steps; **blocks since last step:** `38`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ28,976.282562860. **Alpha liquidity in pool (`alpha_in`)** = ‎2,724,988.794742150α‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,166,721.837975337α‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.010633980`** *(also **moving-average price** `0.010648958152160048` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎769,862.201552812α‎`. **Owner hotkey / coldkey (chain):** `5HCFWvRqzSHWRPecN7q8J6c7aKQnrCZTMHstPv39xL1wgDHh` / `5HCFWvRqzSHWRPecN7q8J6c7aKQnrCZTMHstPv39xL1wgDHh`.
- **Subnet registered at block:** `1497824` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎28.642997240α‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000α‎` · α-in `‎0.000000000α‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104397`
- **Liquidity constant `k`:** `78960045297075848694866549000`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Apex` |
| Symbol (API) | `α` |
| Rank | `24` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.010633535` |
| Market cap | `45846421640205.16196401` |
| Market cap Δ 1d | `-0.113417856530208463` |
| Liquidity | `57952546273463` |
| Total τ | `28975676553170` |
| Total α | `4891477632717487` |
| α in pool | `2725045783955564` |
| α staked | `1586448149172522` |
| Price Δ 1h | `-0.007598024626439076` |
| Price Δ 1d | `-0.217974236832119018` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `1` |
| Owner SS58 (API) | `5HCFWvRqzSHWRPecN7q8J6c7aKQnrCZTMHstPv39xL1wgDHh` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `172898` |
| Registration wall time | `2023-04-13T19:08:36Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `9` |
| Active miners | `3` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `128` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `99` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<picture>
    <source srcset="./docs/macrocosmos-white.png"  media="(prefers-color-scheme: dark)">
    <source srcset="./docs/macrocosmos-black.png"  media="(prefers-color-scheme: light)">
    <img src="macrocosmos-black.png">
</picture>

<div align="center">

# **Bittensor Subnet 1: Apex** <!-- omit in toc -->
[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docs](https://img.shields.io/badge/Docs-8A2BE2)](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex)

</div>


# Apex Guide

### [Overview](https://docs.macrocosmos.ai/subnets/subnet-1-apex)
Subnet 1 Apex subnet drives algorithmic innovation across diverse problem domains. Each pursuit of the best solution takes place within a **Competition**, which consists of multiple **Rounds** of evaluation where participants (miners) submit their Python-based algorithms through the Apex CLI and earn rewards based on their performance. Validators continuously evaluate these submissions, scoring them against benchmarks and  distributing blockchain-based rewards to miners whose solutions perform best, creating a trustless incentive mechanism that encourages innovation and optimization across various computational challenges.

### [Miner Docs](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup)

See miner docs for an overview on the [Apex CLI](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup/apex-cli) and [incentive mechanism](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/incentive-mechanism).

### [Validator Docs](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/validating)

See validator docs for an overview on validator setup.

### [Current Competitions](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup/current-competitions)

**[RL Battleship](https://docs.macrocosmos.ai/subnets/subnet-1-apex/subnet-1-current-competitions#id-1.-reinforcement-learning-battleship)**: A strategy game competition in which miners compete to sink ships on a 10x10 grid in as few turns as possible, now with reinforcement learning. Miners train and submit models that compete in the game environment.

**[Iota Simulator](https://docs.macrocosmos.ai/subnets/subnet-1-apex/subnet-1-current-competitions#id-2.-iota-simulator)**: A distributed training simulation competition where miners submit routing and balancing algorithms that orchestrate activations across a network of heterogeneous nodes. Miners are scored on how efficiently their code moves forward and backward activations through layered pipelines under realistic conditions including node churn, variable latency, and bandwidth constraints.

### Feedback, Questions, and Support
Visit the SN1 channel in the [Macrocosmos Discord server](https://discord.gg/vdyz4JZ9Ww) or the [Bittensor Discord server](https://discord.gg/GtgHWakpDs) to chat, ask questions, submit feedback, and more.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Mining intelligence

**Fetched document title:** APEX | Macrocosmos.ai

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 256 |
| Max validators allowed (`max_allowed_validators`) | 128 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 99 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 7200 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5HCFWvRqzSHWRPecN7q8J6c7aKQnrCZTMHstPv39xL1wgDHh` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `1000000000000000000`) |
| `target_regs_per_interval` | `2` |
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

### [Miner Docs](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup)

See miner docs for an overview on the [Apex CLI](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup/apex-cli) and [incentive mechanism](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/incentive-mechanism).

---

### [Validator Docs](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/validating)

See validator docs for an overview on validator setup.

---

### [Current Competitions](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup/current-competitions)

**[RL Battleship](https://docs.macrocosmos.ai/subnets/subnet-1-apex/subnet-1-current-competitions#id-1.-reinforcement-learning-battleship)**: A strategy game competition in which miners compete to sink ships on a 10x10 grid in as few turns as possible, now with reinforcement learning. Miners train and submit models that compete in the game environment.

**[Iota Simulator](https://docs.macrocosmos.ai/subnets/subnet-1-apex/subnet-1-current-competitions#id-2.-iota-simulator)**: A distributed training simulation competition where miners submit routing and balancing algorithms that orchestrate activations across a network of heterogeneous nodes. Miners are scored on how efficiently their code moves forward and backward activations through layered pipelines under realistic conditions including node churn, variable latency, and bandwidth constraints.

---









#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/macrocosm-os/apex/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://apex.macrocosmos.ai](https://apex.macrocosmos.ai)
- **GitHub:** [https://github.com/macrocosm-os/apex](https://github.com/macrocosm-os/apex)
- **Discord (handle / invite hint):** `macrocrux`
- **Logo URL:** [https://www.macrocosmos.ai/images/mc_logo_black.png](https://www.macrocosmos.ai/images/mc_logo_black.png)
- **Contact:** support@macrocosmos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.010633537 |
| 8104244 | 0.010633513 |
| 8104292 | 0.010633499 |
| 8104340 | 0.010633475 |
| 8104388 | 0.010633473 |
| 8104436 | 0.01063398 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.010756332 |
| 2026-03-10T23:59:48Z | — | 0.01069266 |
| 2026-03-11T23:59:48Z | — | 0.010680876 |
| 2026-03-12T23:59:48Z | — | 0.010723669 |
| 2026-03-13T23:59:48Z | — | 0.011259423 |
| 2026-03-14T23:59:48Z | — | 0.011322207 |
| 2026-03-15T23:59:48Z | — | 0.011024289 |
| 2026-03-16T23:59:48Z | — | 0.011719882 |
| 2026-03-17T23:59:48Z | — | 0.011408211 |
| 2026-03-18T23:59:48Z | — | 0.010914932 |
| 2026-03-19T23:59:48Z | — | 0.010845980408 |
| 2026-03-20T23:59:48Z | — | 0.011093116 |
| 2026-03-21T23:59:48Z | — | 0.011046909 |
| 2026-03-22T23:59:48Z | — | 0.011041575 |
| 2026-03-23T23:59:48Z | — | 0.011695597 |
| 2026-03-24T23:59:48Z | — | 0.0120841528346 |
| 2026-03-25T23:59:48Z | — | 0.012945534 |
| 2026-03-26T23:59:48Z | — | 0.013360591 |
| 2026-03-27T23:59:48Z | — | 0.012647623 |
| 2026-03-28T23:59:48Z | — | 0.012505982 |
| 2026-03-29T23:59:48Z | — | 0.012815964 |
| 2026-03-30T23:59:48Z | — | 0.012795353 |
| 2026-03-31T23:59:48Z | — | 0.013261963 |
| 2026-04-01T23:59:48Z | — | 0.013444394 |
| 2026-04-02T23:59:48Z | — | 0.013095972 |
| 2026-04-03T23:59:48Z | — | 0.012488581 |
| 2026-04-04T23:59:48Z | — | 0.012745189 |
| 2026-04-05T23:59:48Z | — | 0.012593235 |
| 2026-04-06T23:59:48Z | — | 0.012616593 |
| 2026-04-07T23:59:48Z | — | 0.012152708 |
| 2026-04-08T23:59:48Z | — | 0.011894017 |
| 2026-04-09T23:59:48Z | — | 0.011462284 |
| 2026-04-10T23:59:48Z | — | 0.011302083 |
| 2026-04-11T23:59:48Z | — | 0.010996662 |
| 2026-04-12T23:59:48Z | — | 0.010994696 |
| 2026-04-13T23:59:48Z | — | 0.011202567 |
| 2026-04-14T23:59:48Z | — | 0.011069211 |
| 2026-04-15T23:59:48Z | — | 0.011009014 |
| 2026-04-16T23:59:48Z | — | 0.01095797 |
| 2026-04-17T23:59:48Z | — | 0.010733284 |
| 2026-04-18T23:59:48Z | — | 0.010851988 |
| 2026-04-19T23:59:48Z | — | 0.010911549 |
| 2026-04-20T23:59:48Z | — | 0.011047039 |
| 2026-04-21T23:59:48Z | — | 0.01101258 |
| 2026-04-22T23:59:48Z | — | 0.011081943 |
| 2026-04-23T23:59:48Z | — | 0.011164112 |
| 2026-04-24T23:59:48Z | — | 0.011114072 |
| 2026-04-25T23:59:48Z | — | 0.011102956 |
| 2026-04-26T23:59:48Z | — | 0.011077471 |
| 2026-04-27T23:59:48Z | — | 0.01096515 |
| 2026-04-28T23:59:48Z | — | 0.010941149 |
| 2026-04-29T23:59:48Z | — | 0.010893296 |
| 2026-04-30T23:59:48Z | — | 0.010943509 |
| 2026-05-01T23:59:48Z | — | 0.010683822 |
| 2026-05-02T23:59:48Z | — | 0.010650877 |
| 2026-05-03T23:59:48Z | — | 0.010633535 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

