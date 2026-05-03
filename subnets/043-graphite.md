# NetUID 43 — Graphite (`ע`)

## Overview

**Graphite** (NetUID **43**) (`ע`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `171`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ15,493.454729533. **Alpha liquidity in pool (`alpha_in`)** = ‎2,433,612.997563818ע‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,569,799.145971434ע‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006364209`** *(also **moving-average price** `0.006336122751235962` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎150,237.458471974ע‎`. **Owner hotkey / coldkey (chain):** `5HjMs5JDrLH3Hknmfm1gDq7nFYAv6M7t9v3EWMctSRXJS9HC` / `5HjMs5JDrLH3Hknmfm1gDq7nFYAv6M7t9v3EWMctSRXJS9HC`.
- **Subnet registered at block:** `3408582` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎129.105740160ע‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003132419` · α-out `‎1.000000000ע‎` · α-in `‎0.492192963ע‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.006364209`
- **Market cap:** `28029180764511.426612126`
- **Liquidity:** `30981394995227`
- **Total τ:** `15493414396495`
- **Total α:** `5003392742432597`
- **α in pool:** `2433606532835826`
- **α staked:** `1970582701758988`
- **Price Δ 1h:** `0.397522641548128178`
- **Price Δ 1d:** `0.030979664702892284`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `5`
- **Active miners:** `2`
- **Active dual:** `0`
- **Emission:** `3131384`
- **Max neurons:** `256`
- **Validators (metadata):** `5`
- **Neuron reg. cost:** `100000000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

### Repository README excerpt *(everything before first `##` heading)*

<a id="top"></a>

<h1 align="center">G R A P H I T E</h1>

<img src="./static/banner.png" alt="Graphite Banner" style='width: 100%; height: auto;'>

<p align="center";><i>A decentralized network for solving graph optimization problems, built on Bittensor, the foremost decentralised AI network.</i></p>

![Version](https://img.shields.io/badge/Version-0.0.0-blue)
![Language](https://img.shields.io/badge/Language-python-blue)
![License](https://img.shields.io/badge/License-MIT-blue)

![Last Commit](https://img.shields.io/github/last-commit/GraphiteAI/Graphite-Subnet)
![Issues](https://img.shields.io/github/issues/GraphiteAI/Graphite-Subnet)
![Contributors](https://img.shields.io/github/contributors/GraphiteAI/Graphite-Subnet)

![Stars](https://img.shields.io/github/stars/GraphiteAI/Graphite-Subnet)
![Forks](https://img.shields.io/github/forks/GraphiteAI/Graphite-Subnet)

<!-- [![Discord](https://img.shields.io/badge/Discord-7289DA?logo=discord&logoColor=white)](https://discord.com/invite/yourdiscordlink)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yourlinkedinprofile)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/c/youryoutubechannel)
[![X](https://img.shields.io/badge/X-000000?logo=x&logoColor=white)](https://twitter.com/yourtwitterhandle) -->

Website: https://graphite-ai.net/
<!-- ![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)&nbsp;&nbsp;-->
[![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://x.com/Graphite_AI)&nbsp;&nbsp;
<!-- ![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)&nbsp;&nbsp; -->

[![Discord](https://dcbadge.limes.pink/api/server/https://discord.gg/sN5NU32M)](https://discord.gg/dZQrRtGv)


<hr>

> [!WARNING]
> The Graphite AI team is still actively developing and updating on this subnet. There may potentially be breaking changes along the way, so please join our <a href="https://discord.gg/sN5NU32M">Discord</a> chat to stay up-to-date with the latest updates.
> If there are any bugs you have discovered or contribute to this subnet, please refer to
    <a href="./CONTRIBUTING.md">Contribute</a> for a list of guidelines on how to contribute.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Awesome repository for Bittensor's Subnet 43. Join us in graphing the future. - GraphiteAI/Graphite-Subnet

**Fetched document title:** GitHub - GraphiteAI/Graphite-Subnet: Awesome repository for Bittensor's Subnet 43. Join us in graphing the future. · GitHub

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
- **Registration recycle cost snapshot (`burn`):** τ0.100000000
- **Owner SS58 (`owner_ss58`):** `5HjMs5JDrLH3Hknmfm1gDq7nFYAv6M7t9v3EWMctSRXJS9HC`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.100000000 / τ100.000000000
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
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Installation 🛠️

Here at Graphite, we aim to make the installation process as seamless as possible, regardless of your technical knowledge. To get you started, we have crafted step-by-step guides and tutorials:

- Basic Installation Guide: [Installation Guide](./docs/installation.md)
- For Miners: [Miner Installation Guide](./docs/miner.md)
- For Validators: [Validator Installation Guide](./docs/validator.md)

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/GraphiteAI/Graphite-Subnet/main/README.md`*

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/GraphiteAI/Graphite-Subnet](https://github.com/GraphiteAI/Graphite-Subnet)
- **Contact:** team@graphite-ai.net

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.006364383 |
| 8104072 | 0.006364223 |
| 8104120 | 0.006364217 |
| 8104168 | 0.006364212 |
| 8104216 | 0.006364209 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.006477788 |
| 2026-03-10T23:59:48Z | 7718257 | 0.006457389 |
| 2026-03-11T23:59:48Z | 7725455 | 0.006437679 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.00643704 |
| 2026-03-13T23:59:48Z | 7739841 | 0.00637243 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.006416791 |
| 2026-03-15T23:59:48Z | 7754226 | 0.006377982 |
| 2026-03-16T23:59:48Z | 7761426 | 0.006331496 |
| 2026-03-17T23:59:48Z | 7768619 | 0.006122146 |
| 2026-03-18T23:59:48Z | 7775819 | 0.006132959 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00614500756096564673 |
| 2026-03-20T23:59:48Z | 7790201 | 0.006131546 |
| 2026-03-21T23:59:48Z | 7797398 | 0.006128796 |
| 2026-03-22T23:59:48Z | 7804598 | 0.006141599 |
| 2026-03-23T23:59:48Z | 7811798 | 0.006156394 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00608471415400913027 |
| 2026-03-25T23:59:48Z | 7826196 | 0.006039125 |
| 2026-03-26T23:59:48Z | 7833396 | 0.006007395 |
| 2026-03-27T23:59:48Z | 7840596 | 0.006002986 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005977519 |
| 2026-03-29T23:59:48Z | 7854902 | 0.005978061 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.00602566 |
| 2026-03-31T23:59:48Z | 7869291 | 0.006077924 |
| 2026-04-01T23:59:48Z | 7876474 | 0.006100049 |
| 2026-04-02T23:59:48Z | 7883622 | 0.006172923 |
| 2026-04-03T23:59:48Z | 7890794 | 0.006154752 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.00618676 |
| 2026-04-05T23:59:48Z | 7905188 | 0.006184419 |
| 2026-04-06T23:59:48Z | 7912388 | 0.006179829 |
| 2026-04-07T23:59:48Z | 7919588 | 0.006177922 |
| 2026-04-08T23:59:48Z | 7926788 | 0.006212066 |
| 2026-04-09T23:59:48Z | 7933987 | 0.006161661 |
| 2026-04-10T23:59:48Z | 7941184 | 0.006166391 |
| 2026-04-11T23:59:48Z | 7948384 | 0.006155343 |
| 2026-04-12T23:59:48Z | 7955584 | 0.006140042 |
| 2026-04-13T23:59:48Z | 7962784 | 0.006180228 |
| 2026-04-14T23:59:48Z | 7969979 | 0.006265859 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.006256069 |
| 2026-04-16T23:59:48Z | 7984379 | 0.006220651 |
| 2026-04-17T23:59:48Z | 7991579 | 0.00621646 |
| 2026-04-18T23:59:48Z | 7998779 | 0.006215949 |
| 2026-04-19T23:59:48Z | 8005979 | 0.00620811 |
| 2026-04-20T23:59:48Z | 8013179 | 0.006201767 |
| 2026-04-21T23:59:48Z | 8020376 | 0.006151613 |
| 2026-04-22T23:59:48Z | 8027562 | 0.006159428 |
| 2026-04-23T23:59:48Z | 8034762 | 0.006155489 |
| 2026-04-24T23:59:48Z | 8041962 | 0.006147581 |
| 2026-04-25T23:59:48Z | 8049151 | 0.006168907 |
| 2026-04-26T23:59:48Z | 8056274 | 0.006186973 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.006228093 |
| 2026-04-28T23:59:48Z | 8070646 | 0.006271903 |
| 2026-04-29T23:59:48Z | 8077790 | 0.00628592 |
| 2026-04-30T23:59:48Z | 8084984 | 0.006241041 |
| 2026-05-01T23:59:48Z | 8092168 | 0.006205951 |
| 2026-05-02T23:59:48Z | 8099357 | 0.006376536 |
| 2026-05-03T16:10:00Z | 8104202 | 0.006364209 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

