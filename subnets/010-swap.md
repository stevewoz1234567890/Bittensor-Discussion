# NetUID 10 — Swap (`κ`)

## Overview

**Swap** (NetUID **10**) (`κ`).

Swap is onboarding users to Bittensor.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `200`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ15,768.766422695. **Alpha liquidity in pool (`alpha_in`)** = ‎2,685,954.465393588κ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,268,767.262174500κ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005874357`** *(also **moving-average price** `0.00590994325466454` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎810,837.002938728κ‎`. **Owner hotkey / coldkey (chain):** `5EvNESR7DfSMmdwJ3crtBW1ENAhq3f99X4FCbTi1hDUNCWAW` / `5GbcimKjp17QPUoS568DBSMNqV2pmDetBf3xyC15vh4bTFE1`.
- **Subnet registered at block:** `2869647` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎150.893435645κ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000κ‎` · α-in `‎0.000000000κ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005874865`
- **Market cap:** `26725246169214.6895117`
- **Liquidity:** `31548386273567`
- **Total τ:** `15769448712458`
- **Total α:** `4954646727568088`
- **α in pool:** `2685838323282275`
- **α staked:** `1863244280184305`
- **Price Δ 1h:** `0.012274128792212108`
- **Price Δ 1d:** `-0.801893705815726039`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `15`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `15`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Swap is onboarding users to Bittensor.

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

## On-chain identity — description


Swap is onboarding users to Bittensor.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.taofi.com/pool](https://www.taofi.com/pool)
- **GitHub:** [https://github.com/Swap-Subnet/swap-subnet](https://github.com/Swap-Subnet/swap-subnet)
- **Logo URL:** [https://www.taofi.com/images/SN10-Swap-Dark.png](https://www.taofi.com/images/SN10-Swap-Dark.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104037 | 0.005874136 |
| 8104085 | 0.005874133 |
| 8104133 | 0.00587487 |
| 8104181 | 0.005874867 |
| 8104229 | 0.005874855 |
| 8104277 | 0.005874357 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.006834335 |
| 2026-03-10T23:59:48Z | 7718257 | 0.007144869 |
| 2026-03-11T23:59:48Z | 7725455 | 0.007319578 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.007074275 |
| 2026-03-13T23:59:48Z | 7739841 | 0.006751654 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.006956675 |
| 2026-03-15T23:59:48Z | 7754226 | 0.006620784 |
| 2026-03-16T23:59:48Z | 7761426 | 0.006366769 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005924184 |
| 2026-03-18T23:59:48Z | 7775819 | 0.006024245 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00604804184944801119 |
| 2026-03-20T23:59:48Z | 7790201 | 0.006128047 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005867407 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005871909 |
| 2026-03-23T23:59:48Z | 7811798 | 0.00616962 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00628507721843416551 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005848861 |
| 2026-03-26T23:59:48Z | 7833396 | 0.005726591 |
| 2026-03-27T23:59:48Z | 7840596 | 0.005617667 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005584073 |
| 2026-03-29T23:59:48Z | 7854902 | 0.005622499 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.005687468 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005983572 |
| 2026-04-01T23:59:48Z | 7876474 | 0.006324406 |
| 2026-04-02T23:59:48Z | 7883622 | 0.00706377 |
| 2026-04-03T23:59:48Z | 7890794 | 0.006921793 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.007069473 |
| 2026-04-05T23:59:48Z | 7905188 | 0.007420248 |
| 2026-04-06T23:59:48Z | 7912388 | 0.007639721 |
| 2026-04-07T23:59:48Z | 7919588 | 0.00767369 |
| 2026-04-08T23:59:48Z | 7926788 | 0.007347438 |
| 2026-04-09T23:59:48Z | 7933987 | 0.007003339 |
| 2026-04-10T23:59:48Z | 7941184 | 0.006290475 |
| 2026-04-11T23:59:48Z | 7948384 | 0.00627169 |
| 2026-04-12T23:59:48Z | 7955584 | 0.00635893 |
| 2026-04-13T23:59:48Z | 7962784 | 0.005965908 |
| 2026-04-14T23:59:48Z | 7969979 | 0.005793388 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.005836905 |
| 2026-04-16T23:59:48Z | 7984379 | 0.005783462 |
| 2026-04-17T23:59:48Z | 7991579 | 0.005885889 |
| 2026-04-18T23:59:48Z | 7998779 | 0.005885606 |
| 2026-04-19T23:59:48Z | 8005979 | 0.006194283 |
| 2026-04-20T23:59:48Z | 8013179 | 0.006114859 |
| 2026-04-21T23:59:48Z | 8020376 | 0.006088755 |
| 2026-04-22T23:59:48Z | 8027562 | 0.006024216 |
| 2026-04-23T23:59:48Z | 8034762 | 0.006341628 |
| 2026-04-24T23:59:48Z | 8041962 | 0.006262554 |
| 2026-04-25T23:59:48Z | 8049151 | 0.006384357 |
| 2026-04-26T23:59:48Z | 8056274 | 0.006354786 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.006283378 |
| 2026-04-28T23:59:48Z | 8070646 | 0.005795889 |
| 2026-04-29T23:59:48Z | 8077790 | 0.005857838 |
| 2026-04-30T23:59:48Z | 8084984 | 0.005953018 |
| 2026-05-01T23:59:48Z | 8092168 | 0.00601745 |
| 2026-05-02T23:59:48Z | 8099357 | 0.005934427 |
| 2026-05-03T16:10:00Z | 8104202 | 0.005874865 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

