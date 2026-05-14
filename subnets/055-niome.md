# NetUID 55 — NIOME (`ث`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**NIOME** (NetUID **55**) (`ث`).

NIOME is a decentralized AI subnet that enables privacy-safe genomic intelligence by replacing real human genomes with high-fidelity synthetic genomic profiles

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `42`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,271.914603747. **Alpha liquidity in pool (`alpha_in`)** = ‎1,659,243.820592734ث‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,912,593.295727047ث‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004981237`** *(also **moving-average price** `0.004717427305877209` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎364,430.730097797ث‎`. **Owner hotkey / coldkey (chain):** `5DJ5fT174AY8GzbYHnamYQCJd4cTcj2Zf7ogUvBhry1KfYVd` / `5GeWUxaFP6duJyNg8EUv6Jfcv6ZNkoERywAcbSw4FAuEMpDq`.
- **Subnet registered at block:** `4703386` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎31.496675225ث‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002490614` · α-out `‎1.000000000ث‎` · α-in `‎0.500000000ث‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104393`
- **Liquidity constant `k`:** `13725123190738003624277374298`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `NIOME` |
| Symbol (API) | `ث` |
| Rank | `53` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004895305` |
| Market cap | `21079069104094.201118975` |
| Market cap Δ 1d | `8.722430977342148914` |
| Liquidity | `16392651479212` |
| Total τ | `8199522390226` |
| Total α | `4571832880936078` |
| α in pool | `1673670810906944` |
| α staked | `2632305855326151` |
| Price Δ 1h | `1.263511992824494686` |
| Price Δ 1d | `8.679136792866475075` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `55` |
| Owner SS58 (API) | `5GeWUxaFP6duJyNg8EUv6Jfcv6ZNkoERywAcbSw4FAuEMpDq` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4703386` |
| Registration wall time | `2025-01-14T14:31:48Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `9` |
| Active miners | `10` |
| Active dual-role | `0` |
| Emission | `2447636` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# NIOME : Bittensor Subnet(SN55) for Privacy-Safe Genomic Inteligence

Welcome to the NIOME Subnet! This repository contains all the necessary information to get started, understand our subnet architecture, and contribute.

![niome logo image](docs/logo.png)

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Privacy-safe synthetic genomic data for pharmaceutical research. Unlimited scale. Zero privacy risk. A Bittensor subnet powering the $44B precision medicine market.

**Fetched document title:** NIOME | Privacy-Safe Synthetic Genomic Data for Pharma Research | Bittensor Subnet

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
| `immunity_period` (blocks) | 7200 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5GeWUxaFP6duJyNg8EUv6Jfcv6ZNkoERywAcbSw4FAuEMpDq` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `7200` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `2` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Guide for Miners and Validators

- [Miner Setup](docs/miner_guide.md) 
- [Validator Setup](docs/validator_guide.md)

---









#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/genomesio/subnet-niome/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://niome.genomes.io](https://niome.genomes.io)
- **GitHub:** [https://github.com/genomesio/subnet-niome](https://github.com/genomesio/subnet-niome)
- **Discord:** [https://discord.gg/7mJkaJZX](https://discord.gg/7mJkaJZX)
- **Logo URL:** [https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pgi-9hji1nosR-l7taHQeA.png](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pgi-9hji1nosR-l7taHQeA.png)
- **Contact:** info@genomes.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004895249 |
| 8104292 | 0.004948813 |
| 8104340 | 0.004951609 |
| 8104388 | 0.004958025 |
| 8104436 | 0.004981246 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.003667361 |
| 2026-03-10T23:59:48Z | — | 0.003486701 |
| 2026-03-11T23:59:48Z | — | 0.003766879 |
| 2026-03-12T23:59:48Z | — | 0.003659692 |
| 2026-03-13T23:59:48Z | — | 0.003499225 |
| 2026-03-14T23:59:48Z | — | 0.003454483 |
| 2026-03-15T23:59:48Z | — | 0.003354931 |
| 2026-03-16T23:59:48Z | — | 0.003362711 |
| 2026-03-17T23:59:48Z | — | 0.003279609 |
| 2026-03-18T23:59:48Z | — | 0.003425203 |
| 2026-03-19T23:59:48Z | — | 0.00350241031417 |
| 2026-03-20T23:59:48Z | — | 0.003542836 |
| 2026-03-21T23:59:48Z | — | 0.003638344 |
| 2026-03-22T23:59:48Z | — | 0.003657861 |
| 2026-03-23T23:59:48Z | — | 0.003677067 |
| 2026-03-24T23:59:48Z | — | 0.00358585066075 |
| 2026-03-25T23:59:48Z | — | 0.003309229 |
| 2026-03-26T23:59:48Z | — | 0.003301626 |
| 2026-03-27T23:59:48Z | — | 0.003280125 |
| 2026-03-28T23:59:48Z | — | 0.003295743 |
| 2026-03-29T23:59:48Z | — | 0.003340917 |
| 2026-03-30T23:59:48Z | — | 0.003284359 |
| 2026-03-31T23:59:48Z | — | 0.003269521 |
| 2026-04-01T23:59:48Z | — | 0.003499184 |
| 2026-04-02T23:59:48Z | — | 0.003434582 |
| 2026-04-03T23:59:48Z | — | 0.003449451 |
| 2026-04-04T23:59:48Z | — | 0.003675242 |
| 2026-04-05T23:59:48Z | — | 0.003658276 |
| 2026-04-06T23:59:48Z | — | 0.003750467 |
| 2026-04-07T23:59:48Z | — | 0.003712836 |
| 2026-04-08T23:59:48Z | — | 0.003660544 |
| 2026-04-09T23:59:48Z | — | 0.002970396 |
| 2026-04-10T23:59:48Z | — | 0.003292799 |
| 2026-04-11T23:59:48Z | — | 0.003353013 |
| 2026-04-12T23:59:48Z | — | 0.003249675 |
| 2026-04-13T23:59:48Z | — | 0.003233511 |
| 2026-04-14T23:59:48Z | — | 0.003137492 |
| 2026-04-15T23:59:48Z | — | 0.003056504 |
| 2026-04-16T23:59:48Z | — | 0.003059276 |
| 2026-04-17T23:59:48Z | — | 0.003120245 |
| 2026-04-18T23:59:48Z | — | 0.003164372 |
| 2026-04-19T23:59:48Z | — | 0.003243454 |
| 2026-04-20T23:59:48Z | — | 0.003512737 |
| 2026-04-21T23:59:48Z | — | 0.003554284 |
| 2026-04-22T23:59:48Z | — | 0.003459929 |
| 2026-04-23T23:59:48Z | — | 0.003409112 |
| 2026-04-24T23:59:48Z | — | 0.003438708 |
| 2026-04-25T23:59:48Z | — | 0.004108628 |
| 2026-04-26T23:59:48Z | — | 0.004221622 |
| 2026-04-27T23:59:48Z | — | 0.003989303 |
| 2026-04-28T23:59:48Z | — | 0.00397364 |
| 2026-04-29T23:59:48Z | — | 0.004416063 |
| 2026-04-30T23:59:48Z | — | 0.004682482 |
| 2026-05-01T23:59:48Z | — | 0.004704999 |
| 2026-05-02T23:59:48Z | — | 0.004753976 |
| 2026-05-03T23:59:48Z | — | 0.004895305 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

