# NetUID 124 — Swarm (`𑀁`)

## Overview

**Swarm** (NetUID **124**) (`𑀁`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `252`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ9,281.787107902. **Alpha liquidity in pool (`alpha_in`)** = ‎1,165,961.357176709𑀁‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,450,629.739233198𑀁‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007934802`** *(also **moving-average price** `0.008029140997678041` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎178,647.247212534𑀁‎`. **Owner hotkey / coldkey (chain):** `5GZPtUjyp5d4j7aWWV9774caQAxxbsxNNM3nuaJYDPAEDjmt` / `5HKYqfJrUFKYPMRFZZ7kfhUNEyHUbY2ZyEjQqKJf2RKVpeXM`.
- **Subnet registered at block:** `5813454` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎185.278258761𑀁‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003885085` · α-out `‎1.000000000𑀁‎` · α-in `‎0.489625995𑀁‎`.

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
| 8104024 | 0.007943742 |
| 8104072 | 0.007943728 |
| 8104120 | 0.007943711 |
| 8104168 | 0.007943697 |
| 8104216 | 0.007934802 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

