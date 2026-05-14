# NetUID 79 — MVTRX (`ي`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**MVTRX** (NetUID **79**) (`ي`).

Building a SOTA Exchange for dTAO and Beyond



#### SubnetIdentity `additional` *(chain)*



Powered by TAOS Matrix of Simulations Sandbox

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `66`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ10,164.226089947. **Alpha liquidity in pool (`alpha_in`)** = ‎1,097,779.826747900ي‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,155,150.926094220ي‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.009220840`** *(also **moving-average price** `0.00874686916358769` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎274,820.500410693ي‎`. **Owner hotkey / coldkey (chain):** `5EWwdZB7qCCMaAso5Mzcks4UUcPxKYvpAj32t5Mg1v6HSxoF` / `5Fxp7QBG81X7PLdMkAe1RLCvqqfQSw9rJC5ppEQs9FP8qez9`.
- **Subnet registered at block:** `5173967` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎49.210816984ي‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004610406` · α-out `‎1.000000000ي‎` · α-in `‎0.500000000ي‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104369`
- **Liquidity constant `k`:** `11158082356048502701893361300`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `MVTRX` |
| Symbol (API) | `ي` |
| Rank | `29` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.009165678` |
| Market cap | `36184244324603.578609278` |
| Market cap Δ 1d | `7.665237634517098302` |
| Liquidity | `20223889558582` |
| Total τ | `10132636031053` |
| Total α | `4252975032110202` |
| α in pool | `1100982767180944` |
| α staked | `2846815128905257` |
| Price Δ 1h | `-0.594609578825626018` |
| Price Δ 1d | `7.752440944215403356` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `79` |
| Owner SS58 (API) | `5Fxp7QBG81X7PLdMkAe1RLCvqqfQSw9rJC5ppEQs9FP8qez9` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5173967` |
| Registration wall time | `2025-03-21T03:07:00Z` |
| Registration cost snapshot | `254935051664` |
| Active keys | `256` |
| Active validators | `6` |
| Active miners | `207` |
| Active dual-role | `1` |
| Emission | `4582784` |
| Max neurons | `256` |
| Validator slots (metadata) | `6` |
| Max validators (API) | `64` |
| Neuron reg. cost | `4512514` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **τaos** ☯ **‪ي‬n 79**<!-- omit in toc -->
### **Decentralized Simulation of Automated Trading in Intelligent Markets:** <!-- omit in toc -->
### **Risk-Averse Agent Optimization** <!-- omit in toc -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
---


**τaos** operates as a [Bittensor](https://bittensor.com) subnet at netuid 79, where participants are incentivized to produce meaningful contributions using carefully risk-managed algorithms in a large-scale agent-based **s**imulation **o**f **a**utomated **t**rading strategies.

[![Website](https://img.shields.io/badge/website-black?logo=googlechrome
)](https://taos.im)
[![Whitepaper](https://img.shields.io/badge/whitepaper-white?logo=proton
)](https://simulate.trading/taos-im-paper)
[![Dashboard](https://img.shields.io/badge/dashboard-white?logo=grafana
)](https://taos.simulate.trading)
[![Discord](https://img.shields.io/badge/discord-black?logo=discord
)](https://discord.com/channels/799672011265015819/1353733356470276096)

---
**_taos_ (/ˈtɑos/)** : To make things out of metal by heating it until it is soft and then bending and hitting it with a hammer to create the right shape.

---
### Table of Contents
</div>

1. [Incentive Mechanism](#mechanism)
    - [Owner Role](#mechanism-owner)
    - [Validator Role](#mechanism-validator)
    - [Miner Role](#mechanism-miner)
2. [Technical Operation](#technical)
    - [Simulator](#technical-simulator)
    - [Validator](#technical-validator)
    - [Miner](#technical-miner)
3. [Requirements](#requirements)
    - [Validator](#requirements-validator)
    - [Miner](#requirements-miner)
4. [Install](#install)
    - [Validator](#install-validator)
    - [Miner](#install-miner)
    - [Docker](#install-docker)
5. [Agents](#agents)
6. [Run](#run)
    - [Validator](#run-validator)
    - [Miner](#run-miner)
---

<div style="page-break-after: always;"></div>

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Simulation of Automated Trading in Intelligent Markets (a.k.a. Sn-79)

**Fetched document title:** TAOS – Simulation of Automated Trading in Intelligent Markets (a.k.a. Sn-79)

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
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 7200 |
| Registration recycle cost snapshot (`burn`) | τ0.005719279 |
| Owner SS58 (`owner_ss58`) | `5Fxp7QBG81X7PLdMkAe1RLCvqqfQSw9rJC5ppEQs9FP8qez9` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `7200` blocks |
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

### Validator Role <span id="mechanism-validator"><span>

Validators in the subnet are responsible primarily for maintaining the state of the simulation, and rewarding agents (miners) which achieve the best results over all realizations of the simulated market.  They deploy two components:
- The C++ simulator, which handles all the computation necessary to simulate asset markets
- The Python validator, which receives state updates from the simulator, forwards these to miners, submits instructions received in response back to the simulator, and calculates miner scores based on their performance throughout the simulation.

---

### Miner Role <span id="mechanism-miner"><span>

Miners in the subnet function as trading agents in the distributed simulation; their role is to develop and host trading strategies which maximize their average risk-adjusted performance measures over all simulated market realizations, while also maintaining a sufficient level of trading activity.  There are no strict limitations on what strategies are able to be applied, but the simulation parameters and performance evaluation metrics will be continually reviewed, selected and adjusted with the intention of maximizing the utility of the output data, and promoting the use of intelligent, risk-averse and budget-constrained trading logic.

---
<div style="page-break-after: always;"></div>

---

### Validator <span id="technical-validator"><span>

The validator functions in a sense as a "proxy" which allows the C++ simulator to communicate with participants in the subnet, and handles all the Bittensor-network-related tasks involved in validator operation - authenticating and distributing requests, validating and processing responses, calculating miner scores, setting weights and, ultimately, providing access to the subnet computational resources for external queries.

---

### Miner <span id="technical-miner"><span>

Miners receive state updates from validators, and respond with instructions as to how they would like to modify their positions in the simulated orderbook realizations by placing and cancelling orders.  In this first version of the subnet, state updates are published at a parameterized interval throughout the simulation and miners are only able to submit instructions at each state publishing event - a planned future implementation will allow continuous bidirectional communication of state and instructions, in line with real exchange operation.  The state update includes all L3 messages processed since the last update, so that strategies analysing the most detailed information are still possible to apply, being limited only in the time-scale at which the algorithm is able to act.

While awaiting the validator to request and receive responses from miners, the simulation is paused such that no events are processed during this time; in order to reward efficient computation as well as agent performance, the response time of miners is used to determine the "delay" or "latency" with which their instructions will be processed by the simulator.  Longer response times thus imply more events that may take place before execution of their instructions, requiring realistic effects like price slippage to be accounted for.   This incentivizes miners to be both fast and intelligent in their trading strategy, while also carefully managing their risk across all market state realizations.  

Miner agents are otherwise treated in the simulator on the same footing as the background agents; their instructions are processed as if they would be submitted to a real exchange, with orders being traded or opened on the book in accordance with standard matching rules.  Every agent's orders will interact with those of the background agents and miners - this ensures a proper and full accounting of the performance of the miner, including their market impact.  Since agents actions directly affect the market structure, this must also be considered when making trading decisions.

---
<div style="page-break-after: always;"></div>

---

## Requirements <span id="requirements"><span>

Requirements are subject to change as the subnet matures and evolves; this section describes the recommended resources to be available for the initial simulation conditions.  We currently manage 40 orderbooks in a simulation, each having around 1000 background agents, while the aim in the near- to mid-term is to reach 1,000+ simulated orderbooks in order to achieve a meaningful level of statistical significance in the evaluation of results.

---

### Validator <span id="requirements-validato…

---





#### CPU / GPU / RAM lines (automatic grep)

- - 32GB RAM
- - 16 CORE CPU
- We hope to increase both major parameters significantly so that validators may wish to prepare a larger machine for easier expansion.  It should be noted however that increasing the CPU resources available will result in a faster progression of simulations due to multi-threaded processing of the orderbook realizations.  This should not inherently be a problem, but may cause divergences in scoring if there is a major discrepancy in resources with the other validators in the subnet.  We plan to communicate the setup employed by our validator whenever changes are made, and will enable to configure the resources allocated for simulation processing if necessary.
- There are no set requirements for miners except that the basic Bittensor package and subnet miner tools occupy ~1GB of RAM per miner instance; resources needed will depend on the complexity and efficiency of the specific strategy implementation.


*Primary README URL used: `https://raw.githubusercontent.com/taos-im/sn-79/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://taos.im](https://taos.im)
- **GitHub:** [https://github.com/taos-im/sn-79](https://github.com/taos-im/sn-79)
- **Logo URL:** [https://assets.mvtrx.fi/logo.png](https://assets.mvtrx.fi/logo.png)
- **Contact:** to@mvtrx.fi

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.009215174 |
| 8104292 | 0.009216349 |
| 8104340 | 0.009217664 |
| 8104388 | 0.009218802 |
| 8104436 | 0.009220868 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.002685163 --> 0.009645716
    line [0.003691151, 0.003649474, 0.003590706, 0.003677287, 0.003595591, 0.003606077, 0.003349596, 0.00368465, 0.003586991, 0.003574148, 0.00321463684567, 0.003333198, 0.003287595, 0.003310106, 0.003457555, 0.00341829884701, 0.003344591, 0.003286649, 0.003291027, 0.003271818, 0.003235477, 0.003431709, 0.0034002, 0.003411273, 0.003465712, 0.003384495, 0.003402478, 0.003388498, 0.003248918, 0.003247633, 0.003165201, 0.003536141, 0.004341571, 0.004068068, 0.004122484, 0.004509293, 0.005494222, 0.005116759, 0.005039406, 0.004756043, 0.004732003, 0.005152784, 0.004994444, 0.004966218, 0.004937146, 0.005027867, 0.005735082, 0.006503401, 0.007663869, 0.007500996, 0.007627128, 0.007587844, 0.007708646, 0.008154347, 0.00849097, 0.009165678]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

