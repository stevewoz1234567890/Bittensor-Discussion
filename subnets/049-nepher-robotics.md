# NetUID 49 — Nepher Robotics (`ר`)

## Overview

**Nepher Robotics** (NetUID **49**) (`ר`).

Pioneering Simulation-First Robotics Development

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `239`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,946.731084766. **Alpha liquidity in pool (`alpha_in`)** = ‎370,146.099014103ר‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,232,663.907983817ר‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005125984`** *(also **moving-average price** `0.005032846005633473` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎55,197.682271757ר‎`. **Owner hotkey / coldkey (chain):** `5DLYBBCdYwBgjJi76dHJuAU7tUb7rNHJmNtpYRmBesBnrAgn` / `5FL781vfkLNnYBUi58JnhZ3r2waHDMiehxRhzcMaMWvKDfXf`.
- **Subnet registered at block:** `6783158` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎159.690400002ר‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.001381153` · α-out `‎1.000000000ר‎` · α-in `‎0.269440680ר‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.00512629`
- **Market cap:** `5642650528510.62499911`
- **Liquidity:** `3843999612654`
- **Total τ:** `1946683997538`
- **Total α:** `1602714746784517`
- **α in pool:** `370114764306499`
- **α staked:** `730613155594760`
- **Price Δ 1h:** `-0.172516902625415543`
- **Price Δ 1d:** `3.81798088083135555`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `2`
- **Active dual:** `1`
- **Emission:** `1385586`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Pioneering Simulation-First Robotics Development



**Additional commentary (on-chain)**


https://x.com/nepher_robotics

### Repository README excerpt *(everything before first `##` heading)*

# Nepher Robotics Subnet

**Bittensor Subnet 49 — Decentralized Robotics Tournament Platform**

Miners submit trained policies; validators evaluate them in standardized Isaac Lab environments. The tournament winner receives all weights.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Pioneering simulation-first robotics development platform powered by NVIDIA Isaac Sim and Isaac Lab.

**Fetched document title:** Pioneering Simulation-First Robotics Development | Nepher AI

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
- **Owner SS58 (`owner_ss58`):** `5FL781vfkLNnYBUi58JnhZ3r2waHDMiehxRhzcMaMWvKDfXf`

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

### Miners

```bash
git clone https://github.com/nepher-ai/nepher-subnet.git && cd nepher-subnet
pip install -e .

cp config/miner_config.example.yaml config/miner_config.yaml

---

### Validators (GPU)

Requires NVIDIA GPU (A100+ recommended), Isaac Sim 5.1, Isaac Lab 2.3.0, Docker + NVIDIA Container Toolkit.

```bash
git clone https://github.com/nepher-ai/nepher-subnet.git && cd nepher-subnet

cp config/docker.env.example .env
cp config/validator_config.example.yaml config/validator_config.yaml

---

### Validators (CPU — No GPU Required)

A lightweight alternative (`~200 MB` image, no Isaac Sim, no NVIDIA drivers) that handles **weight-setting and burning only**. Use this on a cheap VPS to keep your validator online 24/7 while reserving the GPU machine solely for evaluation windows.

```bash
git clone https://github.com/nepher-ai/nepher-subnet.git && cd nepher-subnet

cp config/docker.env.example .env
cp config/validator_config.example.yaml config/validator_config.yaml

---

# Miner

nepher-miner submit   --path ./agent --config config/miner_config.yaml
nepher-miner validate --path ./agent

---

# Validator — GPU (default, full evaluation + weight-setting)

nepher-validator run --config config/validator_config.yaml [--verbose] [--json-logs]

---

# Validator — CPU (weight-setting & burn only, no GPU needed)

nepher-validator run --config config/validator_config.yaml --mode cpu

---

# Validator — CPU via Docker (recommended for 24/7 VPS deployment)

docker compose build validator-cpu && docker compose up -d validator-cpu
```

---

#### CPU / GPU / RAM lines (automatic grep)

- Requires NVIDIA GPU (A100+ recommended), Isaac Sim 5.1, Isaac Lab 2.3.0, Docker + NVIDIA Container Toolkit.
- A lightweight alternative (`~200 MB` image, no Isaac Sim, no NVIDIA drivers) that handles **weight-setting and burning only**. Use this on a cheap VPS to keep your validator online 24/7 while reserving the GPU machine solely for evaluation windows.
- docker compose build validator-cpu
- docker compose up -d validator-cpu
- nepher-validator run --config config/validator_config.yaml --mode cpu
- > **CPU/GPU split deployment:** run `validator-cpu` on a cheap VPS for 24/7 weight-setting and burn, and only spin up the full GPU validator during evaluation. See the [validator guide](docs/validator-guide.md#8-cpugpu-split-deployment).
- docker compose build validator-cpu && docker compose up -d validator-cpu


*Primary README URL used: `https://raw.githubusercontent.com/nepher-ai/nepher-subnet/main/README.md`*

## On-chain identity — description


Pioneering Simulation-First Robotics Development

## On-chain identity — additional field


https://x.com/nepher_robotics

## Registered contact & links


- **Website:** [https://www.nepher.ai/](https://www.nepher.ai/)
- **GitHub:** [https://github.com/nepher-ai/nepher-subnet](https://github.com/nepher-ai/nepher-subnet)
- **Discord:** [https://discord.gg/nepher](https://discord.gg/nepher)
- **Logo URL:** [https://tournaments.nepher.ai/logo.png](https://tournaments.nepher.ai/logo.png)
- **Contact:** contact@nepher.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.005134992 |
| 8104133 | 0.005126142 |
| 8104181 | 0.005126314 |
| 8104229 | 0.005126118 |
| 8104277 | 0.005125984 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.006649677 |
| 2026-03-10T23:59:48Z | 7718257 | 0.006804386 |
| 2026-03-11T23:59:48Z | 7725455 | 0.006705946 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.00674056 |
| 2026-03-13T23:59:48Z | 7739841 | 0.006009744 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.00666544 |
| 2026-03-15T23:59:48Z | 7754226 | 0.006132957 |
| 2026-03-16T23:59:48Z | 7761426 | 0.006394853 |
| 2026-03-17T23:59:48Z | 7768619 | 0.007064316 |
| 2026-03-18T23:59:48Z | 7775819 | 0.007953305 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00808139518973251688 |
| 2026-03-20T23:59:48Z | 7790201 | 0.007720637 |
| 2026-03-21T23:59:48Z | 7797398 | 0.008118174 |
| 2026-03-22T23:59:48Z | 7804598 | 0.009068692 |
| 2026-03-23T23:59:48Z | 7811798 | 0.008593681 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00864902875822486084 |
| 2026-03-25T23:59:48Z | 7826196 | 0.007937027 |
| 2026-03-26T23:59:48Z | 7833396 | 0.007341924 |
| 2026-03-27T23:59:48Z | 7840596 | 0.007449625 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.007423155 |
| 2026-03-29T23:59:48Z | 7854902 | 0.007251579 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.00703117 |
| 2026-03-31T23:59:48Z | 7869291 | 0.00698329 |
| 2026-04-01T23:59:48Z | 7876474 | 0.006980485 |
| 2026-04-02T23:59:48Z | 7883622 | 0.007144104 |
| 2026-04-03T23:59:48Z | 7890794 | 0.00722975 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.007834563 |
| 2026-04-05T23:59:48Z | 7905188 | 0.007543082 |
| 2026-04-06T23:59:48Z | 7912388 | 0.007811073 |
| 2026-04-07T23:59:48Z | 7919588 | 0.00788892 |
| 2026-04-08T23:59:48Z | 7926788 | 0.007347017 |
| 2026-04-09T23:59:48Z | 7933987 | 0.005352051 |
| 2026-04-10T23:59:48Z | 7941184 | 0.006452729 |
| 2026-04-11T23:59:48Z | 7948384 | 0.006532012 |
| 2026-04-12T23:59:48Z | 7955584 | 0.005487467 |
| 2026-04-13T23:59:48Z | 7962784 | 0.006056551 |
| 2026-04-14T23:59:48Z | 7969979 | 0.006079529 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.005711595 |
| 2026-04-16T23:59:48Z | 7984379 | 0.005399943 |
| 2026-04-17T23:59:48Z | 7991579 | 0.005487815 |
| 2026-04-18T23:59:48Z | 7998779 | 0.005589162 |
| 2026-04-19T23:59:48Z | 8005979 | 0.005557395 |
| 2026-04-20T23:59:48Z | 8013179 | 0.00558377 |
| 2026-04-21T23:59:48Z | 8020376 | 0.005466351 |
| 2026-04-22T23:59:48Z | 8027562 | 0.005261983 |
| 2026-04-23T23:59:48Z | 8034762 | 0.005353044 |
| 2026-04-24T23:59:48Z | 8041962 | 0.005263372 |
| 2026-04-25T23:59:48Z | 8049151 | 0.005235379 |
| 2026-04-26T23:59:48Z | 8056274 | 0.005115987 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.005262459 |
| 2026-04-28T23:59:48Z | 8070646 | 0.005032117 |
| 2026-04-29T23:59:48Z | 8077790 | 0.005213479 |
| 2026-04-30T23:59:48Z | 8084984 | 0.005122855 |
| 2026-05-01T23:59:48Z | 8092168 | 0.005021505 |
| 2026-05-02T23:59:48Z | 8099357 | 0.00495507 |
| 2026-05-03T16:10:00Z | 8104202 | 0.00512629 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

