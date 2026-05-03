# NetUID 124 — Swarm (`𑀁`)

## Overview

**Swarm** (NetUID **124**) (`𑀁`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `314`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ9,281.984746659. **Alpha liquidity in pool (`alpha_in`)** = ‎1,165,997.089697164𑀁‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,450,686.326958885𑀁‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007934729`** *(also **moving-average price** `0.00802752305753529` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎178,647.290157615𑀁‎`. **Owner hotkey / coldkey (chain):** `5GZPtUjyp5d4j7aWWV9774caQAxxbsxNNM3nuaJYDPAEDjmt` / `5HKYqfJrUFKYPMRFZZ7kfhUNEyHUbY2ZyEjQqKJf2RKVpeXM`.
- **Subnet registered at block:** `5813454` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎230.862709443𑀁‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003871384` · α-out `‎1.000000000𑀁‎` · α-in `‎0.487903527𑀁‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.007934804`
- **Market cap:** `22985566067442.71825302`
- **Liquidity:** `18533360895479`
- **Total τ:** `9281737127341`
- **Total α:** `3616571728691498`
- **α in pool:** `1165954920643047`
- **α staked:** `1730848335926708`
- **Price Δ 1h:** `-0.112805451822907651`
- **Price Δ 1d:** `-0.50620832771694665`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `2`
- **Active dual:** `1`
- **Emission:** `3883802`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

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

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 256
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5HKYqfJrUFKYPMRFZZ7kfhUNEyHUbY2ZyEjQqKJf2RKVpeXM`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
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

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.swarm124.com](https://www.swarm124.com)
- **GitHub:** [https://github.com/swarm-subnet/swarm](https://github.com/swarm-subnet/swarm)
- **Logo URL:** [https://raw.githubusercontent.com/swarm-subnet/swarm/refs/heads/main/swarm/assets/Swarm.png](https://raw.githubusercontent.com/swarm-subnet/swarm/refs/heads/main/swarm/assets/Swarm.png)
- **Contact:** admin@swarm124.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.007943726 |
| 8104133 | 0.007943707 |
| 8104181 | 0.007943678 |
| 8104229 | 0.007934765 |
| 8104277 | 0.007934729 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.007325266 |
| 2026-03-10T23:59:48Z | 7718257 | 0.007426409 |
| 2026-03-11T23:59:48Z | 7725455 | 0.007318977 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.007213149 |
| 2026-03-13T23:59:48Z | 7739841 | 0.00691531 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.00677298 |
| 2026-03-15T23:59:48Z | 7754226 | 0.006856603 |
| 2026-03-16T23:59:48Z | 7761426 | 0.006981994 |
| 2026-03-17T23:59:48Z | 7768619 | 0.006846894 |
| 2026-03-18T23:59:48Z | 7775819 | 0.006968007 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00687189855481453306 |
| 2026-03-20T23:59:48Z | 7790201 | 0.006897139 |
| 2026-03-21T23:59:48Z | 7797398 | 0.007092453 |
| 2026-03-22T23:59:48Z | 7804598 | 0.007130817 |
| 2026-03-23T23:59:48Z | 7811798 | 0.007305417 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00737107385648094852 |
| 2026-03-25T23:59:48Z | 7826196 | 0.00721196 |
| 2026-03-26T23:59:48Z | 7833396 | 0.00703599 |
| 2026-03-27T23:59:48Z | 7840596 | 0.007089794 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.006888923 |
| 2026-03-29T23:59:48Z | 7854902 | 0.006863073 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.007146856 |
| 2026-03-31T23:59:48Z | 7869291 | 0.006953866 |
| 2026-04-01T23:59:48Z | 7876474 | 0.007021415 |
| 2026-04-02T23:59:48Z | 7883622 | 0.007041335 |
| 2026-04-03T23:59:48Z | 7890794 | 0.007570873 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.008435784 |
| 2026-04-05T23:59:48Z | 7905188 | 0.007940308 |
| 2026-04-06T23:59:48Z | 7912388 | 0.008107736 |
| 2026-04-07T23:59:48Z | 7919588 | 0.008128422 |
| 2026-04-08T23:59:48Z | 7926788 | 0.008328521 |
| 2026-04-09T23:59:48Z | 7933987 | 0.007845681 |
| 2026-04-10T23:59:48Z | 7941184 | 0.007738566 |
| 2026-04-11T23:59:48Z | 7948384 | 0.007659707 |
| 2026-04-12T23:59:48Z | 7955584 | 0.007725038 |
| 2026-04-13T23:59:48Z | 7962784 | 0.0074741 |
| 2026-04-14T23:59:48Z | 7969979 | 0.007239342 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.007270236 |
| 2026-04-16T23:59:48Z | 7984379 | 0.006949688 |
| 2026-04-17T23:59:48Z | 7991579 | 0.006855539 |
| 2026-04-18T23:59:48Z | 7998779 | 0.006923281 |
| 2026-04-19T23:59:48Z | 8005979 | 0.00689414 |
| 2026-04-20T23:59:48Z | 8013179 | 0.006858698 |
| 2026-04-21T23:59:48Z | 8020376 | 0.006903822 |
| 2026-04-22T23:59:48Z | 8027562 | 0.007109222 |
| 2026-04-23T23:59:48Z | 8034762 | 0.007267011 |
| 2026-04-24T23:59:48Z | 8041962 | 0.007186561 |
| 2026-04-25T23:59:48Z | 8049151 | 0.007816332 |
| 2026-04-26T23:59:48Z | 8056274 | 0.007825525 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.008656012 |
| 2026-04-28T23:59:48Z | 8070646 | 0.008321686 |
| 2026-04-29T23:59:48Z | 8077790 | 0.008657129 |
| 2026-04-30T23:59:48Z | 8084984 | 0.007975393 |
| 2026-05-01T23:59:48Z | 8092168 | 0.008073327 |
| 2026-05-02T23:59:48Z | 8099357 | 0.00807603 |
| 2026-05-03T16:10:00Z | 8104202 | 0.007934804 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

