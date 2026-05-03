# NetUID 49 — Nepher Robotics (`ר`)

## Overview

Pioneering Simulation-First Robotics Development

https://x.com/nepher_robotics

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

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

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- Requires NVIDIA GPU (A100+ recommended), Isaac Sim 5.1, Isaac Lab 2.3.0, Docker + NVIDIA Container Toolkit.
- A lightweight alternative (`~200 MB` image, no Isaac Sim, no NVIDIA drivers) that handles **weight-setting and burning only**. Use this on a cheap VPS to keep your validator online 24/7 while reserving the GPU machine solely for evaluation windows.
- docker compose build validator-cpu
- docker compose up -d validator-cpu
- nepher-validator run --config config/validator_config.yaml --mode cpu
- > **CPU/GPU split deployment:** run `validator-cpu` on a cheap VPS for 24/7 weight-setting and burn, and only spin up the full GPU validator during evaluation. See the [validator guide](docs/validator-guide.md#8-cpugpu-split-deployment).
- docker compose build validator-cpu && docker compose up -d validator-cpu


*Primary README URL used: `https://raw.githubusercontent.com/nepher-ai/nepher-subnet/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

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

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.005135332 |
| 8103843 | 0.005135223 |
| 8103891 | 0.005135176 |
| 8103939 | 0.005135125 |
| 8103987 | 0.005135078 |
| 8104035 | 0.005135043 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

