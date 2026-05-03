# NetUID 5 — Hone (`ε`)

## Overview

**Hone** (NetUID **5**) (`ε`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `195`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ37,442.131100112. **Alpha liquidity in pool (`alpha_in`)** = ‎2,111,578.442217213ε‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,696,729.857104372ε‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.017732124`** *(also **moving-average price** `0.0177575193811208` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎882,271.099769917ε‎`. **Owner hotkey / coldkey (chain):** `5GZ2KuT2TtLbYTtsMcgAtazo6KQ4bc57ykZgyQv9oit3y7iq` / `5GurNtB3yQFCh6CSmfH7LrYJDsvzup4diHZiaYtKe274nrMX`.
- **Subnet registered at block:** `2491604` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎146.795727222ε‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ε‎` · α-in `‎0.000000000ε‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.017732285`
- **Market cap:** `64194848244719.22881606`
- **Liquidity:** `74885241836530`
- **Total τ:** `37442301413892`
- **Total α:** `4808233299321585`
- **α in pool:** `2111568837441920`
- **α staked:** `1508655417058796`
- **Price Δ 1h:** `-0.00043423431125532`
- **Price Δ 1d:** `-0.264083323710685672`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `14`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `14`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Hone training

### Repository README excerpt *(everything before first `##` heading)*

# Hone Subnet — ARC-AGI-2 Benchmarking on Bittensor

A Bittensor subnet where **validators** evaluate **miners** on their ability to solve novel ARC-AGI-2 reasoning problems. Miners don't run solvers directly—they point to a git repository containing their solution, which is executed in a secure GPU sandbox.

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Incentivized distributed training of large language models. Train together, build what's next.

**Fetched document title:** Hone

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

## On-chain identity — description


Hone training

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.hone.training/](https://www.hone.training/)
- **GitHub:** [https://github.com/manifold-inc/hone](https://github.com/manifold-inc/hone)
- **Logo URL:** [https://www.hone.training/logo.svg](https://www.hone.training/logo.svg)
- **Contact:** devs@manifold.inc

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104037 | 0.017732331 |
| 8104085 | 0.017732322 |
| 8104133 | 0.017732301 |
| 8104181 | 0.017732291 |
| 8104229 | 0.017732246 |
| 8104277 | 0.017732124 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

