# NetUID 55 — NIOME (`ث`)

## Overview

**NIOME** (NetUID **55**) (`ث`).

NIOME is a decentralized AI subnet that enables privacy-safe genomic intelligence by replacing real human genomes with high-fidelity synthetic genomic profiles

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `183`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,199.325107591. **Alpha liquidity in pool (`alpha_in`)** = ‎1,673,724.112496517ث‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,898,109.641005795ث‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004895040`** *(also **moving-average price** `0.004703289130702615` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎364,314.604813849ث‎`. **Owner hotkey / coldkey (chain):** `5DJ5fT174AY8GzbYHnamYQCJd4cTcj2Zf7ogUvBhry1KfYVd` / `5GeWUxaFP6duJyNg8EUv6Jfcv6ZNkoERywAcbSw4FAuEMpDq`.
- **Subnet registered at block:** `4703386` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎137.235118549ث‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002447512` · α-out `‎1.000000000ث‎` · α-in `‎0.500000000ث‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004895305`
- **Market cap:** `21079069104094.201118975`
- **Liquidity:** `16392651479212`
- **Total τ:** `8199522390226`
- **Total α:** `4571832880936078`
- **α in pool:** `1673670810906944`
- **α staked:** `2632305855326151`
- **Price Δ 1h:** `1.263511992824494686`
- **Price Δ 1d:** `8.679136792866475075`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `10`
- **Active dual:** `0`
- **Emission:** `2447636`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

NIOME is a decentralized AI subnet that enables privacy-safe genomic intelligence by replacing real human genomes with high-fidelity synthetic genomic profiles

### Repository README excerpt *(everything before first `##` heading)*

# NIOME : Bittensor Subnet(SN55) for Privacy-Safe Genomic Inteligence

Welcome to the NIOME Subnet! This repository contains all the necessary information to get started, understand our subnet architecture, and contribute.

![niome logo image](docs/logo.png)

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Privacy-safe synthetic genomic data for pharmaceutical research. Unlimited scale. Zero privacy risk. A Bittensor subnet powering the $44B precision medicine market.

**Fetched document title:** NIOME | Privacy-Safe Synthetic Genomic Data for Pharma Research | Bittensor Subnet

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
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GeWUxaFP6duJyNg8EUv6Jfcv6ZNkoERywAcbSw4FAuEMpDq`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `2`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

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

## On-chain identity — description


NIOME is a decentralized AI subnet that enables privacy-safe genomic intelligence by replacing real human genomes with high-fidelity synthetic genomic profiles

## On-chain identity — additional field


*Unset.*

## Registered contact & links


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
| 8104024 | 0.004834231 |
| 8104072 | 0.004867708 |
| 8104120 | 0.004862572 |
| 8104168 | 0.004866531 |
| 8104216 | 0.00489504 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.003667361 |
| 2026-03-10T23:59:48Z | 7718257 | 0.003486701 |
| 2026-03-11T23:59:48Z | 7725455 | 0.003766879 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.003659692 |
| 2026-03-13T23:59:48Z | 7739841 | 0.003499225 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.003454483 |
| 2026-03-15T23:59:48Z | 7754226 | 0.003354931 |
| 2026-03-16T23:59:48Z | 7761426 | 0.003362711 |
| 2026-03-17T23:59:48Z | 7768619 | 0.003279609 |
| 2026-03-18T23:59:48Z | 7775819 | 0.003425203 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00350241031416503596 |
| 2026-03-20T23:59:48Z | 7790201 | 0.003542836 |
| 2026-03-21T23:59:48Z | 7797398 | 0.003638344 |
| 2026-03-22T23:59:48Z | 7804598 | 0.003657861 |
| 2026-03-23T23:59:48Z | 7811798 | 0.003677067 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00358585066075118068 |
| 2026-03-25T23:59:48Z | 7826196 | 0.003309229 |
| 2026-03-26T23:59:48Z | 7833396 | 0.003301626 |
| 2026-03-27T23:59:48Z | 7840596 | 0.003280125 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.003295743 |
| 2026-03-29T23:59:48Z | 7854902 | 0.003340917 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.003284359 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003269521 |
| 2026-04-01T23:59:48Z | 7876474 | 0.003499184 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003434582 |
| 2026-04-03T23:59:48Z | 7890794 | 0.003449451 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.003675242 |
| 2026-04-05T23:59:48Z | 7905188 | 0.003658276 |
| 2026-04-06T23:59:48Z | 7912388 | 0.003750467 |
| 2026-04-07T23:59:48Z | 7919588 | 0.003712836 |
| 2026-04-08T23:59:48Z | 7926788 | 0.003660544 |
| 2026-04-09T23:59:48Z | 7933987 | 0.002970396 |
| 2026-04-10T23:59:48Z | 7941184 | 0.003292799 |
| 2026-04-11T23:59:48Z | 7948384 | 0.003353013 |
| 2026-04-12T23:59:48Z | 7955584 | 0.003249675 |
| 2026-04-13T23:59:48Z | 7962784 | 0.003233511 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003137492 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.003056504 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003059276 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003120245 |
| 2026-04-18T23:59:48Z | 7998779 | 0.003164372 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003243454 |
| 2026-04-20T23:59:48Z | 8013179 | 0.003512737 |
| 2026-04-21T23:59:48Z | 8020376 | 0.003554284 |
| 2026-04-22T23:59:48Z | 8027562 | 0.003459929 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003409112 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003438708 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004108628 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004221622 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.003989303 |
| 2026-04-28T23:59:48Z | 8070646 | 0.00397364 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004416063 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004682482 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004704999 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004753976 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004895305 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

