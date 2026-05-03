# NetUID 5 — Hone (`ε`)

## Overview

Hone training

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GurNtB3yQFCh6CSmfH7LrYJDsvzup4diHZiaYtKe274nrMX`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
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

### Prerequisites

- **Python 3.10+**
- **Docker & Docker Compose**
- **Bittensor CLI** (`btcli`)
- **NVIDIA GPU + drivers** (for sandbox runner / local testing)
- TAO for registration and staking

---

### Requirements

- 4+ CPU cores
- 8GB+ RAM
- 20GB disk
- Reliable network connection

---

### 2. Configure Environment

Create `validator/.env`:

```ini

---

# register validator on subnet

btcli subnet register --netuid 5 --wallet.name default --wallet.hotkey validator

---

### 4. Start Validator

```bash
cd validator
make up
```

This starts:
- PostgreSQL database
- Adminer (DB UI on port 8080)
- Validator service

---

### Requirements

- Public IP address
- Open port (default: 8091)
- Minimal compute (the heavy lifting happens in sandbox)

---

### 2. Configure Environment

Create `miner/.env`:

```ini
WALLET_NAME=default
WALLET_HOTKEY=miner
MINER_PORT=8091

---

### 3. Register Miner

```bash

---

# set your public IP on-chain so validators can discover you

python tools/post_ip_chain.py \
  --wallet-name default \
  --hotkey miner \
  --ip YOUR_PUBLIC_IP \
  --port 8091
```

---

### 4. Start Miner

```bash

---

# check info endpoint (what validators see)

curl http://localhost:8091/info
```

Expected `/info` response:
```json
{
  "repo_url": "https://github.com/your-username/your-arc-solver",
  "repo_branch": "main",
  "weight_class": "1xH200",
  "use_vllm": true,
  "vllm_config": {
    "model": "unsloth/Meta-Llama-3.1-8B-Instruct",
    "dtype": "half",
    "gpu_memory_utilization": 0.8,
    "max_model_len": 12000
  },
  "version": "1.0.0",
  "hotkey": "5Abc...xyz"
}
```

---

---

### Required Files

```
your-solver-repo/
├── Dockerfile           # builds your execution environment
├── requirements.txt     # python dependencies
├── arc_main.py          # entry point (CLI wrapper)
├── arc_prep_phase.py    # downloads models, data (internet ON)
├── arc_inference_phase.py  # solves problems (internet OFF)
├── arc_solver_llm.py    # your solver implementation (or any name)
└── arc_utils.py         # I/O utilities
```

---

### Validator Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `NETUID` | `5` | Subnet UID |
| `CHAIN_ENDPOINT` | mainnet | Bittensor chain endpoint |
| `WALLET_NAME` | `default` | Wallet name |
| `WALLET_HOTKEY` | `validator` | Hotkey name |
| `DB_URL` | - | PostgreSQL connection string |
| `SANDBOX_RUNNER_ENDPOINT` | - | Sandbox runner API URL |
| `SANDBOX_RUNNER_API_KEY` | - | API key for sandbox |
| `SANDBOX_RUNNER_TIMEOUT_HOURS` | `3` | Max job execution time |
| `SANDBOX_POLL_INTERVAL` | `30` | Seconds between status polls |
| `SANDBOX_MAX_POLL_ATTEMPTS` | `360` | Max polling attempts (360 × 30s = 3h) |
| `MAX_SUBMISSIONS_PER_DAY` | `1` | Submissions per miner per day |
| `MIN_ACCURACY_FLOOR` | `0.20` | Minimum exact_match_rate to qualify |
| `TOP_MINERS_COUNT` | `5` | Number of miners to reward |
| `BURN_UID` | `251` | UID to receive burn weight |
| `BURN_PERCENTAGE` | `0.95` | Percentage of emissions to burn |
| `CYCLE_DURATION` | `30` | Blocks per query cycle |
| `MINER_INFO_TIMEOUT` | `5` | Timeout for /info endpoint (seconds) |
| `RETENTION_DAYS` | `30` | Days to keep query results in DB |
| `CLEANUP_INTERVAL_HOURS` | `24` | Hours between DB cleanup runs |

---

### Miner Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `WALLET_NAME` | `default` | Wallet name |
| `WALLET_HOTKEY` | `miner` | Hotkey name |
| `MINER_PORT` | `8091` | HTTP server port |
| `MINER_REPO_URL` | - | Your solver repository URL |
| `MINER_REPO_BRANCH` | `main` | Git branch |
| `MINER_REPO_COMMIT` | - | Specific commit (optional) |
| `MINER_REPO_PATH` | - | Subdirectory in repo |
| `MINER_WEIGHT_CLASS` | `1xH200` | GPU requirement |
| `MINER_USE_VLLM` | `false` | Enable vLLM sidecar |

---

### Validator Issues

**Cannot connect to database**
```bash

---

### Miner Issues

**Not discovered by validators**
```bash

---

# check GPU status

curl http://localhost:8000/v1/status -H "X-API-Key: ..."

---

# remove specific network

docker network rm sandbox-job-xyz
```

**vLLM not starting**
- Check GPU memory is sufficient
- Verify model exists in /app/models after prep phase
- Check vLLM logs: `curl .../v1/logs/{job_id}/tail?lines=100`

---

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- A Bittensor subnet where **validators** evaluate **miners** on their ability to solve novel ARC-AGI-2 reasoning problems. Miners don't run solvers directly—they point to a git repository containing their solution, which is executed in a secure GPU sandbox.
- 2. **Validators** fetch miner info, submit jobs to a **Sandbox Runner** (secure GPU execution service)
- - **GPU isolation**: Inference runs without network access
- │ │ M1    │ │    │  │ H200 #0 │  │ H200 #1 │  │ H200 #2 │  │ H200 #3 │ │
- │ ┌───────┐ │    │  │ H200 #4 │  │ H200 #5 │  │ H200 #6 │  │ H200 #7 │ │
- - **NVIDIA GPU + drivers** (for sandbox runner / local testing)
- - 4+ CPU cores
- - 8GB+ RAM
- - 20GB disk
- `| `MINER_WEIGHT_CLASS` | `1xH200` | GPU requirement |`
- `| Class | GPUs | Use Case |`
- **GPU allocation failures**
- nvidia-smi
- - Check GPU memory is sufficient
- ├── sandbox_runner/         # GPU execution service
- │   ├── core/               # job queue, GPU pool, scheduler, executor


*Primary README URL used: `https://raw.githubusercontent.com/manifold-inc/hone/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Hone training

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://www.hone.training/](https://www.hone.training/)
- **GitHub:** [https://github.com/manifold-inc/hone](https://github.com/manifold-inc/hone)
- **Logo URL:** [https://www.hone.training/logo.svg](https://www.hone.training/logo.svg)
- **Contact:** devs@manifold.inc

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.017733389 |
| 8103843 | 0.017732382 |
| 8103891 | 0.017732369 |
| 8103939 | 0.017732356 |
| 8103987 | 0.017732343 |
| 8104035 | 0.017732336 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

