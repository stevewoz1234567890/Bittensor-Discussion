# NetUID 29 — Coldint (`ה`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Coldint** (NetUID **29**) (`ה`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `16`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ18,448.025509365. **Alpha liquidity in pool (`alpha_in`)** = ‎1,345,289.556428242ה‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,645,990.808830417ה‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.013634453`** *(also **moving-average price** `0.013630910310894251` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎179,064.861288687ה‎`. **Owner hotkey / coldkey (chain):** `5HHHHHzgLnYRvnKkHd45cRUDMHXTSwx7MjUzxBrKbY4JfZWn` / `5HHHHHzgLnYRvnKkHd45cRUDMHXTSwx7MjUzxBrKbY4JfZWn`.
- **Subnet registered at block:** `3379782` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎12.077999999ה‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000672133` · α-out `‎1.000000000ה‎` · α-in `‎0.049296724ה‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104419`
- **Liquidity constant `k`:** `24817936054470534032121486330`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Coldint` |
| Symbol (API) | `ה` |
| Rank | `17` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.013634629` |
| Market cap | `59984730710980.506371574` |
| Market cap Δ 1d | `0.221588250323626218` |
| Liquidity | `36790235775469` |
| Total τ | `18447987854876` |
| Total α | `4991035860222206` |
| α in pool | `1345269308067952` |
| α staked | `3054170582154254` |
| Price Δ 1h | `-0.000674747946804339` |
| Price Δ 1d | `0.049978653956194601` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `29` |
| Owner SS58 (API) | `5HHHHHzgLnYRvnKkHd45cRUDMHXTSwx7MjUzxBrKbY4JfZWn` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3379782` |
| Registration wall time | `2024-07-13T23:26:48.003Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `8` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `674867` |
| Max neurons | `256` |
| Validator slots (metadata) | `8` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

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
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5HHHHHzgLnYRvnKkHd45cRUDMHXTSwx7MjUzxBrKbY4JfZWn` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `600000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/coldint/coldint_validator](https://github.com/coldint/coldint_validator)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.013634632 |
| 8104244 | 0.013634571 |
| 8104292 | 0.013634534 |
| 8104340 | 0.013634475 |
| 8104388 | 0.01363447 |
| 8104436 | 0.013634453 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.01355377 --> 0.01455708
    line [0.014325542, 0.014336827, 0.01437578, 0.014304612, 0.0142841, 0.014339973, 0.014315682, 0.014362071, 0.014387925, 0.014359686, 0.0144572632588, 0.014399393, 0.014377939, 0.014309843, 0.014371979, 0.014487886879, 0.014337459, 0.014298014, 0.01428408, 0.014274544, 0.014119468, 0.013969748, 0.014094733, 0.014125087, 0.014164083, 0.014106313, 0.014128569, 0.014122072, 0.014109879, 0.014098476, 0.014089634, 0.013971584, 0.014002836, 0.013975569, 0.013943276, 0.013932758, 0.013948998, 0.013908944, 0.01389829, 0.013929783, 0.014035898, 0.013973547, 0.013962273, 0.013945815, 0.013931256, 0.013920146, 0.013880461, 0.013845618, 0.013846929, 0.013843367, 0.013797689, 0.013739389, 0.013679012, 0.013635383, 0.013622964, 0.013634629]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

