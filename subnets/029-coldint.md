# NetUID 29 — Coldint (`ה`)

## Overview

**Coldint** (NetUID **29**) (`ה`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `157`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ18,447.995874931. **Alpha liquidity in pool (`alpha_in`)** = ‎1,345,270.007713656ה‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,645,779.496437307ה‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.013634627`** *(also **moving-average price** `0.013630733825266361` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎179,064.742837334ה‎`. **Owner hotkey / coldkey (chain):** `5HHHHHzgLnYRvnKkHd45cRUDMHXTSwx7MjUzxBrKbY4JfZWn` / `5HHHHHzgLnYRvnKkHd45cRUDMHXTSwx7MjUzxBrKbY4JfZWn`.
- **Subnet registered at block:** `3379782` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎118.514477775ה‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000675090` · α-out `‎1.000000000ה‎` · α-in `‎0.049512908ה‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.013634629`
- **Market cap:** `59984730710980.506371574`
- **Liquidity:** `36790235775469`
- **Total τ:** `18447987854876`
- **Total α:** `4991035860222206`
- **α in pool:** `1345269308067952`
- **α staked:** `3054170582154254`
- **Price Δ 1h:** `-0.000674747946804339`
- **Price Δ 1d:** `0.049978653956194601`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `8`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `674867`
- **Max neurons:** `256`
- **Validators (metadata):** `8`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Bittensor COLaborative Destributed INcentivized Training (coldint) Subnet** <!-- omit in toc -->
[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

[coldint.io](https://coldint.io) • [Discord](https://discord.gg/bittensor) • [Network](https://x.taostats.io/subnet/29)
</div>

---

# Introduction
Bittensor subnet 29 is focused on advancing collaborative, distributed model training and research, as well as sharing of innovative ideas regarding model structure, training and evaluation.
It started as a fork of subnet 9 (pretraining), which was somewhat static and lacked the incentive to publish small improvements.
See [Macrocosmos github](https://github.com/macrocosm-os/pretraining/releases/tag/v3.2.1) for the exact starting point.

The following documentation assumes you are familiar with basic Bittensor concepts: Miners, Validators, and incentives. If you need a primer, please check out https://docs.bittensor.com/learn/bittensor-building-blocks.

The initial competition rewards miners for improving model score on the [Fineweb-edu-2 dataset](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-score-2).

Miner rewards can also be earned by contributing code, bug-fixes or key suggestions or insights; see [coldint.io](https://coldint.io) for further detais.

See the [Miner](docs/miner.md) and [Validator](docs/validator.md) docs for more information about how they work, as well as setup instructions.

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to coldint/coldint_validator development by creating an account on GitHub.

**Fetched document title:** GitHub - coldint/coldint_validator · GitHub

## Operational parameters — registration, limits, economics (chain)


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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5HHHHHzgLnYRvnKkHd45cRUDMHXTSwx7MjUzxBrKbY4JfZWn`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `600000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- Miners will need enough disk space to store the model they work on. Max size of model is defined in [constants/\_\_init\_\_.py](../constants/__init__.py), but is typically 15GB. It is recommended to have at least 100 GB of disk space.
- Miners will need enough processing power to train their model. The current models have around 7B parameters. To train such a model a single large GPU (80 GB) is required, or multiple 48GB or 24GB GPUs.

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- Validators will need enough disk space to store the models of miners being evaluated. There is a maximum model size, currently ~15GB and 6.9B parameters, defined in [constants/\_\_init\_\_.py](../constants/__init__.py) and the validator has cleanup logic to remove old models. It is recommended to have at least 1 TB of disk space.
- Validators will need enough processing power to evaluate their model, an RTX4090 (with 24GB RAM) is the minimum recommend GPU.

---

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- Miners will need enough disk space to store the model they work on. Max size of model is defined in [constants/\_\_init\_\_.py](../constants/__init__.py), but is typically 15GB. It is recommended to have at least 100 GB of disk space.
- Miners will need enough processing power to train their model. The current models have around 7B parameters. To train such a model a single large GPU (80 GB) is required, or multiple 48GB or 24GB GPUs.

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- Validators will need enough disk space to store the models of miners being evaluated. There is a maximum model size, currently ~15GB and 6.9B parameters, defined in [constants/\_\_init\_\_.py](../constants/__init__.py) and the validator has cleanup logic to remove old models. It is recommended to have at least 1 TB of disk space.
- Validators will need enough processing power to evaluate their model, an RTX4090 (with 24GB RAM) is the minimum recommend GPU.


*Primary README URL used: `https://raw.githubusercontent.com/coldint/coldint_validator/main/README.md`*

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/coldint/coldint_validator](https://github.com/coldint/coldint_validator)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8103976 | 0.013634701 |
| 8104024 | 0.013634694 |
| 8104072 | 0.013634677 |
| 8104120 | 0.013634656 |
| 8104168 | 0.013634639 |
| 8104216 | 0.013634627 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.014325542 |
| 2026-03-10T23:59:48Z | 7718257 | 0.014336827 |
| 2026-03-11T23:59:48Z | 7725455 | 0.01437578 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.014304612 |
| 2026-03-13T23:59:48Z | 7739841 | 0.0142841 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.014339973 |
| 2026-03-15T23:59:48Z | 7754226 | 0.014315682 |
| 2026-03-16T23:59:48Z | 7761426 | 0.014362071 |
| 2026-03-17T23:59:48Z | 7768619 | 0.014387925 |
| 2026-03-18T23:59:48Z | 7775819 | 0.014359686 |
| 2026-03-19T23:59:48Z | 7783014 | 0.01445726325875916671 |
| 2026-03-20T23:59:48Z | 7790201 | 0.014399393 |
| 2026-03-21T23:59:48Z | 7797398 | 0.014377939 |
| 2026-03-22T23:59:48Z | 7804598 | 0.014309843 |
| 2026-03-23T23:59:48Z | 7811798 | 0.014371979 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.01448788687897551065 |
| 2026-03-25T23:59:48Z | 7826196 | 0.014337459 |
| 2026-03-26T23:59:48Z | 7833396 | 0.014298014 |
| 2026-03-27T23:59:48Z | 7840596 | 0.01428408 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.014274544 |
| 2026-03-29T23:59:48Z | 7854902 | 0.014119468 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.013969748 |
| 2026-03-31T23:59:48Z | 7869291 | 0.014094733 |
| 2026-04-01T23:59:48Z | 7876474 | 0.014125087 |
| 2026-04-02T23:59:48Z | 7883622 | 0.014164083 |
| 2026-04-03T23:59:48Z | 7890794 | 0.014106313 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.014128569 |
| 2026-04-05T23:59:48Z | 7905188 | 0.014122072 |
| 2026-04-06T23:59:48Z | 7912388 | 0.014109879 |
| 2026-04-07T23:59:48Z | 7919588 | 0.014098476 |
| 2026-04-08T23:59:48Z | 7926788 | 0.014089634 |
| 2026-04-09T23:59:48Z | 7933987 | 0.013971584 |
| 2026-04-10T23:59:48Z | 7941184 | 0.014002836 |
| 2026-04-11T23:59:48Z | 7948384 | 0.013975569 |
| 2026-04-12T23:59:48Z | 7955584 | 0.013943276 |
| 2026-04-13T23:59:48Z | 7962784 | 0.013932758 |
| 2026-04-14T23:59:48Z | 7969979 | 0.013948998 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.013908944 |
| 2026-04-16T23:59:48Z | 7984379 | 0.01389829 |
| 2026-04-17T23:59:48Z | 7991579 | 0.013929783 |
| 2026-04-18T23:59:48Z | 7998779 | 0.014035898 |
| 2026-04-19T23:59:48Z | 8005979 | 0.013973547 |
| 2026-04-20T23:59:48Z | 8013179 | 0.013962273 |
| 2026-04-21T23:59:48Z | 8020376 | 0.013945815 |
| 2026-04-22T23:59:48Z | 8027562 | 0.013931256 |
| 2026-04-23T23:59:48Z | 8034762 | 0.013920146 |
| 2026-04-24T23:59:48Z | 8041962 | 0.013880461 |
| 2026-04-25T23:59:48Z | 8049151 | 0.013845618 |
| 2026-04-26T23:59:48Z | 8056274 | 0.013846929 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.013843367 |
| 2026-04-28T23:59:48Z | 8070646 | 0.013797689 |
| 2026-04-29T23:59:48Z | 8077790 | 0.013739389 |
| 2026-04-30T23:59:48Z | 8084984 | 0.013679012 |
| 2026-05-01T23:59:48Z | 8092168 | 0.013635383 |
| 2026-05-02T23:59:48Z | 8099357 | 0.013622964 |
| 2026-05-03T16:10:00Z | 8104202 | 0.013634629 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

