# NetUID 49 — Nepher Robotics (`ר`)

## Overview

**Nepher Robotics** (NetUID **49**) (`ר`).

Pioneering Simulation-First Robotics Development

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `177`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,946.701368120. **Alpha liquidity in pool (`alpha_in`)** = ‎370,118.408501866ר‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,232,612.854644534ר‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005126284`** *(also **moving-average price** `0.00503135472536087` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎55,197.626157745ר‎`. **Owner hotkey / coldkey (chain):** `5DLYBBCdYwBgjJi76dHJuAU7tUb7rNHJmNtpYRmBesBnrAgn` / `5FL781vfkLNnYBUi58JnhZ3r2waHDMiehxRhzcMaMWvKDfXf`.
- **Subnet registered at block:** `6783158` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎118.264173349ר‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.001386044` · α-out `‎1.000000000ר‎` · α-in `‎0.270379836ר‎`.

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
| 8104024 | 0.005135053 |
| 8104072 | 0.005134999 |
| 8104120 | 0.005134458 |
| 8104168 | 0.005126105 |
| 8104216 | 0.005126284 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

