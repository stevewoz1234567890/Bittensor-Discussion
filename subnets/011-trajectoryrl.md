# NetUID 11 — TrajectoryRL (`λ`)

## Overview

Agentic RL as a Service, Optimize agent trajectories to make agents cheaper, safer, and more reliable.

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.223643578
- **Owner SS58 (`owner_ss58`):** `5D2Jhtbnm7iAdKfjRk6DisXBnr1MEsYat8kXqaPNrVqJP3uE`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.200000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `10`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `100000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### For Validators

Validators run in Docker, auto-updated by Watchtower. The validator pulls the latest TrajRL-Bench image before each eval cycle — new scenarios are picked up automatically.

```bash

---

### For Miners

Mining means writing a **SKILL.md** — instructions and strategies that teach an AI agent how to handle operational scenarios. The testee agent SSHes into an isolated sandbox (shell + mock services + scenario files), reads your SKILL.md, solves the task. A judge agent then SSHes in, grounds its evaluation in the sandbox state, and scores the work. No GPU, no server, no uptime required.

---

#### 1. Prerequisites (one-time)

```bash
pip install bittensor-cli

btcli wallet create --wallet-name my-miner
btcli subnets register --wallet-name my-miner --hotkey default --netuid 11
```

---

# Upload to S3-compatible storage (configure S3_BUCKET, AWS_* in .env.miner)

trajectoryrl-miner upload pack.json

---

# Get the two Docker images (pull from GHCR is fastest):

docker pull ghcr.io/trajectoryrl/trajrl-bench:latest
docker pull ghcr.io/trajectoryrl/hermes-agent:latest

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - **No server required** — Miners upload packs to any HTTP endpoint and commit on-chain. No GPU, no uptime needed.
- Mining means writing a **SKILL.md** — instructions and strategies that teach an AI agent how to handle operational scenarios. The testee agent SSHes into an isolated sandbox (shell + mock services + scenario files), reads your SKILL.md, solves the task. A judge agent then SSHes in, grounds its evaluation in the sandbox state, and scores the work. No GPU, no server, no uptime required.
- Prereqs: Docker, [uv](https://docs.astral.sh/uv/), an LLM API key, ~6 GB free disk.


*Primary README URL used: `https://raw.githubusercontent.com/trajectoryRL/trajectoryRL/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Agentic RL as a Service, Optimize agent trajectories to make agents cheaper, safer, and more reliable.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://trajrl.com](https://trajrl.com)
- **GitHub:** [https://github.com/trajectoryRL/trajectoryRL](https://github.com/trajectoryRL/trajectoryRL)
- **Logo URL:** [https://pbs.twimg.com/profile_images/2018928039716089856/2PZ-Bhm2_400x400.jpg](https://pbs.twimg.com/profile_images/2018928039716089856/2PZ-Bhm2_400x400.jpg)
- **Contact:** trajectoryrl@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.011316362 |
| 8103843 | 0.011310867 |
| 8103891 | 0.011310858 |
| 8103939 | 0.011310849 |
| 8103987 | 0.011298589 |
| 8104035 | 0.011326588 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

