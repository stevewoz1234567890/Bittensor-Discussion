# NetUID 43 — Graphite (`ע`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Graphite** (NetUID **43**) (`ע`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `30`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ15,494.077972047. **Alpha liquidity in pool (`alpha_in`)** = ‎2,433,731.000995059ע‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,570,009.109174415ע‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006364156`** *(also **moving-average price** `0.006337728817015886` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎150,237.522347823ע‎`. **Owner hotkey / coldkey (chain):** `5HjMs5JDrLH3Hknmfm1gDq7nFYAv6M7t9v3EWMctSRXJS9HC` / `5HjMs5JDrLH3Hknmfm1gDq7nFYAv6M7t9v3EWMctSRXJS9HC`.
- **Subnet registered at block:** `3408582` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎22.650336651ע‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003118700` · α-out `‎1.000000000ע‎` · α-in `‎0.490041469ע‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104405`
- **Liquidity constant `k`:** `37708417892405439089787115773`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Graphite` |
| Symbol (API) | `ע` |
| Rank | `38` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.006364209` |
| Market cap | `28029180764511.426612126` |
| Market cap Δ 1d | `0.205223986906332227` |
| Liquidity | `30981394995227` |
| Total τ | `15493414396495` |
| Total α | `5003392742432597` |
| α in pool | `2433606532835826` |
| α staked | `1970582701758988` |
| Price Δ 1h | `0.397522641548128178` |
| Price Δ 1d | `0.030979664702892284` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `43` |
| Owner SS58 (API) | `5HjMs5JDrLH3Hknmfm1gDq7nFYAv6M7t9v3EWMctSRXJS9HC` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3408582` |
| Registration wall time | `2024-07-17T23:58:24Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `5` |
| Active miners | `2` |
| Active dual-role | `0` |
| Emission | `3131384` |
| Max neurons | `256` |
| Validator slots (metadata) | `5` |
| Max validators (API) | `64` |
| Neuron reg. cost | `100000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

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
| Registration recycle cost snapshot (`burn`) | τ0.100000000 |
| Owner SS58 (`owner_ss58`) | `5HjMs5JDrLH3Hknmfm1gDq7nFYAv6M7t9v3EWMctSRXJS9HC` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.100000000 / τ100.000000000 |
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
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/GraphiteAI/Graphite-Subnet](https://github.com/GraphiteAI/Graphite-Subnet)
- **Contact:** team@graphite-ai.net

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.00636421 |
| 8104244 | 0.006364191 |
| 8104292 | 0.006364181 |
| 8104340 | 0.006364163 |
| 8104388 | 0.006364162 |
| 8104436 | 0.006364156 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

