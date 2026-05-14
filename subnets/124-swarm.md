# NetUID 124 — Swarm (`𑀁`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Swarm** (NetUID **124**) (`𑀁`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `111`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ9,282.552925735. **Alpha liquidity in pool (`alpha_in`)** = ‎1,166,079.650853858𑀁‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,450,838.849894637𑀁‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007934655`** *(also **moving-average price** `0.008023520931601524` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎178,647.333616307𑀁‎`. **Owner hotkey / coldkey (chain):** `5GZPtUjyp5d4j7aWWV9774caQAxxbsxNNM3nuaJYDPAEDjmt` / `5HKYqfJrUFKYPMRFZZ7kfhUNEyHUbY2ZyEjQqKJf2RKVpeXM`.
- **Subnet registered at block:** `5813454` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎81.611618146𑀁‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003868073` · α-out `‎1.000000000𑀁‎` · α-in `‎0.487490989𑀁‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104324`
- **Liquidity constant `k`:** `10824196074673526868812235630`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Swarm` |
| Symbol (API) | `𑀁` |
| Rank | `46` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.007934804` |
| Market cap | `22985566067442.71825302` |
| Market cap Δ 1d | `-0.254028887837676229` |
| Liquidity | `18533360895479` |
| Total τ | `9281737127341` |
| Total α | `3616571728691498` |
| α in pool | `1165954920643047` |
| α staked | `1730848335926708` |
| Price Δ 1h | `-0.112805451822907651` |
| Price Δ 1d | `-0.50620832771694665` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `124` |
| Owner SS58 (API) | `5HKYqfJrUFKYPMRFZZ7kfhUNEyHUbY2ZyEjQqKJf2RKVpeXM` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5813454` |
| Registration wall time | `2025-06-19T06:48:12Z` |
| Registration cost snapshot | `79312501676` |
| Active keys | `256` |
| Active validators | `13` |
| Active miners | `2` |
| Active dual-role | `1` |
| Emission | `3883802` |
| Max neurons | `256` |
| Validator slots (metadata) | `13` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<a id="readme-top"></a>

<p align="center">
  <img src="https://raw.githubusercontent.com/swarm-subnet/swarm/main/swarm/assets/Swarm_2.png" alt="Swarm" width="60%" />
</p>

<h1 align="center">Swarm — Autonomous Drone Navigation</h1>

<p align="center">
  <b>The open benchmark where AI learns to fly.</b><br/>
  <i>Train a neural network to navigate drones through 3D worlds it has never seen —<br/>
  using nothing but a depth camera and raw flight state. No maps. No rules. No shortcuts.</i>
</p>

<p align="center">
  <a href="https://github.com/swarm-subnet/swarm/releases"><img alt="Version" src="https://img.shields.io/badge/version-v4.0.0-green?style=flat-square" /></a>
  <a href="https://discord.gg/8dPqPDw7GC"><img alt="Discord" src="https://img.shields.io/badge/Discord-Join-5865F2?style=flat-square&logo=discord&logoColor=white" /></a>
  <a href="https://x.com/SwarmSubnet"><img alt="X" src="https://img.shields.io/badge/X-Follow-000000?style=flat-square&logo=x&logoColor=white" /></a>
  <a href="https://swarm124.com"><img alt="Website" src="https://img.shields.io/badge/swarm124.com-visit-orange?style=flat-square&logo=googlechrome&logoColor=white" /></a>
</p>

<p align="center">
  <a href="docs/miner.md">
    <img alt="Start Training" src="https://img.shields.io/badge/Start%20Training-Miner%20Guide-111111?style=for-the-badge" />
  </a>
  &nbsp;
  <a href="#cli">
    <img alt="Run Benchmark" src="https://img.shields.io/badge/Run%20Benchmark-CLI-111111?style=for-the-badge" />
  </a>
  &nbsp;
  <a href="docs/validator.md">
    <img alt="Run Validator" src="https://img.shields.io/badge/Run%20Validator-Guide-111111?style=for-the-badge" />
  </a>
</p>

---

<details>
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li><a href="#about-swarm">About Swarm</a></li>
    <li><a href="#see-it-fly">See It Fly</a></li>
    <li><a href="#environments">Environments</a></li>
    <li><a href="#cli">CLI</a></li>
    <li><a href="#how-it-works">How It Works</a></li>
    <li><a href="#scoring">Scoring</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#community">Community</a></li>
    <li><a href="#from-simulation-to-reality">From Simulation to Reality</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

---

<!-- ABOUT SWARM -->

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** A global arena for autonomous drone flight, backed by real-world impact and on-chain notarization.

**Fetched document title:** Swarm124

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
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5HKYqfJrUFKYPMRFZZ7kfhUNEyHUbY2ZyEjQqKJf2RKVpeXM` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
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

## Environments

Every benchmark run generates unique worlds. Six environment types test completely different navigation skills — tight urban corridors, open-air precision, mountain terrain, village streets, indoor obstacle courses, and dense forests.

<table>
<tr>
<td align="center" width="50%">
<img src="https://raw.githubusercontent.com/swarm-subnet/swarm/main/swarm/assets/map_images/Type1_sub2.png" alt="City" width="100%">
<br><b>City</b> — dense streets, buildings, intersections
</td>
<td align="center" width="50%">
<img src="https://raw.githubusercontent.com/swarm-subnet/swarm/main/swarm/assets/map_images/Type3_sub2.png" alt="Ski Village" width="100%">
<br><b>Ski Village</b> — snow-roofed buildings, mountain backdrop
</td>
</tr>
<tr>
<td align="center" width="50%">
<img src="https://raw.githubusercontent.com/swarm-subnet/swarm/main/swarm/assets/map_images/Type3.png" alt="Mountains" width="100%">
<br><b>Mountains</b> — procedural terrain, peaks and valleys
</td>
<td align="center" width="50%">
<img src="https://raw.githubusercontent.com/swarm-subnet/swarm/main/swarm/assets/map_images/Type4_2.png" alt="Warehouse" width="100%">
<br><b>Warehouse</b> — indoor, racks, cranes, 12m ceiling
</td>
</tr>
</table>

<br>

<h3 align="center">Forest — 4 Seasonal Modes</h3>

<table>
<tr>
<td align="center" width="50%">
<img src="https://raw.githubusercontent.com/swarm-subnet/swarm/main/swarm/assets/map_images/Type6_sub1.png" alt="Forest Normal" width="100%">
<br><b>Normal</b> — green canopy, full foliage
</td>
<td align="center" width="50%">
<img src="https://raw.githubusercontent.com/swarm-subnet/swarm/main/swarm/assets/map_images/Type6_sub2.png" alt="Forest Autumn" width="100%">
<br><b>Autumn</b> — orange and brown tones
</td>
</tr>
<tr>
<td align="center" width="50%">
<img src="https://raw.githubusercontent.com/swarm-subnet/swarm/main/swarm/assets/map_images/Type6_sub3.png" alt="Forest Snow" width="100%">
<br><b>Snow</b> — white terrain, bare branches
</td>
<td align="center" width="50%">
<img src="https://raw.githubusercontent.com/swarm-subnet/swarm/main/swarm/assets/map_images/Type6_sub4.png" alt="Forest Dead" width="100%">
<br><b>Dead</b> — no leaves, dark ground
</td>
</tr>
</table>

<p align="center">
  <sub>1,000 unique seeds per epoch — 6 environment types, each procedurally generated with unique layouts every run.</sub>
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- CLI -->

---

##### Extra scrape: `miner.md` (grep only)





#### CPU / GPU / RAM lines (automatic grep)

- Submissions must be ≤ **50 MiB** compressed.
- `| Screening threshold | >= champion score + 0.015 (or >= 0.01 bootstrap) |`
- `| Max submission size | 50 MiB (compressed) |`
- torch, torchvision, torchaudio, onnx, onnxruntime, onnxruntime-gpu,
- - **Submission exceeds 50 MiB** — compressed size limit is enforced.
- **"Agent too large"** — Submissions must be ≤ 50 MiB compressed.

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- `| CPU | 12 cores | |`
- `| RAM | 48 GB | |`
- `| Disk | 50 GB | Environment + model cache |`
- `| GPU | None | |`

---

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- Submissions must be ≤ **50 MiB** compressed.
- `| Screening threshold | >= champion score + 0.015 (or >= 0.01 bootstrap) |`
- `| Max submission size | 50 MiB (compressed) |`
- torch, torchvision, torchaudio, onnx, onnxruntime, onnxruntime-gpu,
- - **Submission exceeds 50 MiB** — compressed size limit is enforced.
- **"Agent too large"** — Submissions must be ≤ 50 MiB compressed.

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- `| CPU | 12 cores | |`
- `| RAM | 48 GB | |`
- `| Disk | 50 GB | Environment + model cache |`
- `| GPU | None | |`


*Primary README URL used: `https://raw.githubusercontent.com/swarm-subnet/swarm/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.swarm124.com](https://www.swarm124.com)
- **GitHub:** [https://github.com/swarm-subnet/swarm](https://github.com/swarm-subnet/swarm)
- **Logo URL:** [https://raw.githubusercontent.com/swarm-subnet/swarm/refs/heads/main/swarm/assets/Swarm.png](https://raw.githubusercontent.com/swarm-subnet/swarm/refs/heads/main/swarm/assets/Swarm.png)
- **Contact:** admin@swarm124.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.007934755 |
| 8104292 | 0.007934724 |
| 8104340 | 0.007934674 |
| 8104388 | 0.00793467 |
| 8104436 | 0.007934655 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.006622248 --> 0.008807861
    line [0.007325266, 0.007426409, 0.007318977, 0.007213149, 0.00691531, 0.00677298, 0.006856603, 0.006981994, 0.006846894, 0.006968007, 0.00687189855481, 0.006897139, 0.007092453, 0.007130817, 0.007305417, 0.00737107385648, 0.00721196, 0.00703599, 0.007089794, 0.006888923, 0.006863073, 0.007146856, 0.006953866, 0.007021415, 0.007041335, 0.007570873, 0.008435784, 0.007940308, 0.008107736, 0.008128422, 0.008328521, 0.007845681, 0.007738566, 0.007659707, 0.007725038, 0.0074741, 0.007239342, 0.007270236, 0.006949688, 0.006855539, 0.006923281, 0.00689414, 0.006858698, 0.006903822, 0.007109222, 0.007267011, 0.007186561, 0.007816332, 0.007825525, 0.008656012, 0.008321686, 0.008657129, 0.007975393, 0.008073327, 0.00807603, 0.007934804]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

