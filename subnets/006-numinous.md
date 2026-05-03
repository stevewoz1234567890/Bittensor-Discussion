# NetUID 6 — Numinous (`ζ`)

## Overview

**Numinous** (NetUID **6**) (`ζ`).

Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `196`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ10,473.595853438. **Alpha liquidity in pool (`alpha_in`)** = ‎2,220,301.960126186ζ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,551,438.663492240ζ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004724448`** *(also **moving-average price** `0.004702520556747913` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎595,615.073981515ζ‎`. **Owner hotkey / coldkey (chain):** `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA` / `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA`.
- **Subnet registered at block:** `3219949` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎147.464285099ζ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ζ‎` · α-in `‎0.000000000ζ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004729466`
- **Market cap:** `21922620167845.56710651`
- **Liquidity:** `20974435517595`
- **Total τ:** `10479184493058`
- **Total α:** `4771665623618426`
- **α in pool:** `2219119669014892`
- **α staked:** `2416207060862343`
- **Price Δ 1h:** `0.334408001522369992`
- **Price Δ 1d:** `1.606138305220201925`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `138`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `245297887`

### On-chain declared purpose *(SubnetIdentity)*

Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters.

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Numinous**



[Discord](https://discord.gg/qKPeYPc3) • [Dashboard](https://app.hex.tech/1644b22a-abe5-4113-9d5f-3ad05e4a8de7/app/Numinous-031erYRYSssIrH3W3KcyHg/latest) • [Website](https://numinouslabs.io/) • [Twitter](https://x.com/numinous_ai) •
[Network](https://taostats.io/subnets/6/chart)
---

</div>

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** Numinous

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
- **`immunity_period` (blocks):** 50400
- **Registration recycle cost snapshot (`burn`):** τ0.211091415
- **Owner SS58 (`owner_ss58`):** `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.200000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `50400` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `6000` blocks
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

## 🏗 System Architecture

The Numinous subnet operates on a strictly defined lifecycle: **Code Submission $\to$ Sandbox Execution $\to$ Resolution $\to$ Weight Setting.**

Validators spin up parallel sandboxes where miners are evaluated on batches of events. Agents operate inside Docker containers with a secure proxy gateway to access external tools.

---

### For Miners

Develop and deploy forecasting agents that compete for the daily reward pool.

  * [**Miner Setup Guide**](docs/miner-setup.md) – Installation, wallet registration, and deployment.
  * [**Gateway Guide**](docs/gateway-guide.md) – How to use the Desearch and Chutes APIs.

---

### For Validators

Run the physical infrastructure that executes and scores the agents.

  * [**Validator Setup Guide**](docs/validator-setup.md) – Hardware requirements and node configuration.

-----

---

#### CPU / GPU / RAM lines (automatic grep)

- Agents must adhere to the interface defined in the architecture. Code size is limited to **2MB**.


*Primary README URL used: `https://raw.githubusercontent.com/numinouslabs/numinous/main/README.md`*

## On-chain identity — description


Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://numinouslabs.io/](https://numinouslabs.io/)
- **GitHub:** [https://github.com/numinouslabs/numinous](https://github.com/numinouslabs/numinous)
- **Discord (handle / invite hint):** `amedeo_ma`
- **Logo URL:** [https://numinouslabs.io/numinous-logo.svg](https://numinouslabs.io/numinous-logo.svg)
- **Contact:** marc@infinitemech.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104037 | 0.004703498 |
| 8104085 | 0.004705218 |
| 8104133 | 0.004705116 |
| 8104181 | 0.004729289 |
| 8104229 | 0.004721511 |
| 8104277 | 0.004724448 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.008984536 |
| 2026-03-10T23:59:48Z | 7718257 | 0.009480982 |
| 2026-03-11T23:59:48Z | 7725455 | 0.009877234 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.009158631 |
| 2026-03-13T23:59:48Z | 7739841 | 0.008730463 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.008245094 |
| 2026-03-15T23:59:48Z | 7754226 | 0.007492773 |
| 2026-03-16T23:59:48Z | 7761426 | 0.007860998 |
| 2026-03-17T23:59:48Z | 7768619 | 0.006863681 |
| 2026-03-18T23:59:48Z | 7775819 | 0.006835757 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00600969100285708853 |
| 2026-03-20T23:59:48Z | 7790201 | 0.006306765 |
| 2026-03-21T23:59:48Z | 7797398 | 0.007061777 |
| 2026-03-22T23:59:48Z | 7804598 | 0.00693054 |
| 2026-03-23T23:59:48Z | 7811798 | 0.006277038 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00649646965948086573 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005364923 |
| 2026-03-26T23:59:48Z | 7833396 | 0.005789895 |
| 2026-03-27T23:59:48Z | 7840596 | 0.006020822 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.006431395 |
| 2026-03-29T23:59:48Z | 7854902 | 0.006456341 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.00646621 |
| 2026-03-31T23:59:48Z | 7869291 | 0.00661928 |
| 2026-04-01T23:59:48Z | 7876474 | 0.006005148 |
| 2026-04-02T23:59:48Z | 7883622 | 0.006036096 |
| 2026-04-03T23:59:48Z | 7890794 | 0.005722253 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.005964957 |
| 2026-04-05T23:59:48Z | 7905188 | 0.0058867 |
| 2026-04-06T23:59:48Z | 7912388 | 0.005826127 |
| 2026-04-07T23:59:48Z | 7919588 | 0.0063164 |
| 2026-04-08T23:59:48Z | 7926788 | 0.006167052 |
| 2026-04-09T23:59:48Z | 7933987 | 0.005354492 |
| 2026-04-10T23:59:48Z | 7941184 | 0.005078246 |
| 2026-04-11T23:59:48Z | 7948384 | 0.005204051 |
| 2026-04-12T23:59:48Z | 7955584 | 0.005150969 |
| 2026-04-13T23:59:48Z | 7962784 | 0.005175425 |
| 2026-04-14T23:59:48Z | 7969979 | 0.005314113 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.005081231 |
| 2026-04-16T23:59:48Z | 7984379 | 0.005005984 |
| 2026-04-17T23:59:48Z | 7991579 | 0.005260479 |
| 2026-04-18T23:59:48Z | 7998779 | 0.005411483 |
| 2026-04-19T23:59:48Z | 8005979 | 0.005198359 |
| 2026-04-20T23:59:48Z | 8013179 | 0.005154425 |
| 2026-04-21T23:59:48Z | 8020376 | 0.005134581 |
| 2026-04-22T23:59:48Z | 8027562 | 0.005201061 |
| 2026-04-23T23:59:48Z | 8034762 | 0.005157768 |
| 2026-04-24T23:59:48Z | 8041962 | 0.005207059 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004928556 |
| 2026-04-26T23:59:48Z | 8056274 | 0.0049339 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004937626 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004957731 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004896487 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004766501 |
| 2026-05-01T23:59:48Z | 8092168 | 0.00474537 |
| 2026-05-02T23:59:48Z | 8099357 | 0.00468624 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004729466 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

