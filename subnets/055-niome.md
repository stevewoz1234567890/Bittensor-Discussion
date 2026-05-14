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

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.002816403 --> 0.005049298
    line [0.003667361, 0.003486701, 0.003766879, 0.003659692, 0.003499225, 0.003454483, 0.003354931, 0.003362711, 0.003279609, 0.003425203, 0.00350241031417, 0.003542836, 0.003638344, 0.003657861, 0.003677067, 0.00358585066075, 0.003309229, 0.003301626, 0.003280125, 0.003295743, 0.003340917, 0.003284359, 0.003269521, 0.003499184, 0.003434582, 0.003449451, 0.003675242, 0.003658276, 0.003750467, 0.003712836, 0.003660544, 0.002970396, 0.003292799, 0.003353013, 0.003249675, 0.003233511, 0.003137492, 0.003056504, 0.003059276, 0.003120245, 0.003164372, 0.003243454, 0.003512737, 0.003554284, 0.003459929, 0.003409112, 0.003438708, 0.004108628, 0.004221622, 0.003989303, 0.00397364, 0.004416063, 0.004682482, 0.004704999, 0.004753976, 0.004895305]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

