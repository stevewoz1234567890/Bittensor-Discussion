# NetUID 5 — Hone (`ε`)

## Overview

**Hone** (NetUID **5**) (`ε`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `133`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ37,442.300380725. **Alpha liquidity in pool (`alpha_in`)** = ‎2,111,568.895707194ε‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,696,677.403614391ε‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.017732283`** *(also **moving-average price** `0.01775798131711781` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎882,270.930489304ε‎`. **Owner hotkey / coldkey (chain):** `5GZ2KuT2TtLbYTtsMcgAtazo6KQ4bc57ykZgyQv9oit3y7iq` / `5GurNtB3yQFCh6CSmfH7LrYJDsvzup4diHZiaYtKe274nrMX`.
- **Subnet registered at block:** `2491604` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎100.122229732ε‎`; pending root emission `τ0.000000000`.
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
| 8103976 | 0.017732345 |
| 8104024 | 0.017732338 |
| 8104072 | 0.017732324 |
| 8104120 | 0.017732306 |
| 8104168 | 0.017732293 |
| 8104216 | 0.017732283 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.01576657 |
| 2026-03-10T23:59:48Z | 7718257 | 0.015534025 |
| 2026-03-11T23:59:48Z | 7725455 | 0.015384372 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.015408077 |
| 2026-03-13T23:59:48Z | 7739841 | 0.015376662 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.015418387 |
| 2026-03-15T23:59:48Z | 7754226 | 0.015344035 |
| 2026-03-16T23:59:48Z | 7761426 | 0.015380396 |
| 2026-03-17T23:59:48Z | 7768619 | 0.015361447 |
| 2026-03-18T23:59:48Z | 7775819 | 0.015294041 |
| 2026-03-19T23:59:48Z | 7783014 | 0.0152781330173752861 |
| 2026-03-20T23:59:48Z | 7790201 | 0.015294865 |
| 2026-03-21T23:59:48Z | 7797398 | 0.015277787 |
| 2026-03-22T23:59:48Z | 7804598 | 0.015263414 |
| 2026-03-23T23:59:48Z | 7811798 | 0.014227505 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.01412200280607210657 |
| 2026-03-25T23:59:48Z | 7826196 | 0.014114441 |
| 2026-03-26T23:59:48Z | 7833396 | 0.01404183 |
| 2026-03-27T23:59:48Z | 7840596 | 0.013871777 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.013823492 |
| 2026-03-29T23:59:48Z | 7854902 | 0.013821074 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.013817585 |
| 2026-03-31T23:59:48Z | 7869291 | 0.013886972 |
| 2026-04-01T23:59:48Z | 7876474 | 0.013846416 |
| 2026-04-02T23:59:48Z | 7883622 | 0.013847123 |
| 2026-04-03T23:59:48Z | 7890794 | 0.013851482 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.013952633 |
| 2026-04-05T23:59:48Z | 7905188 | 0.013964602 |
| 2026-04-06T23:59:48Z | 7912388 | 0.014213375 |
| 2026-04-07T23:59:48Z | 7919588 | 0.014024891 |
| 2026-04-08T23:59:48Z | 7926788 | 0.01404007 |
| 2026-04-09T23:59:48Z | 7933987 | 0.013975333 |
| 2026-04-10T23:59:48Z | 7941184 | 0.017303765 |
| 2026-04-11T23:59:48Z | 7948384 | 0.017423698 |
| 2026-04-12T23:59:48Z | 7955584 | 0.017404474 |
| 2026-04-13T23:59:48Z | 7962784 | 0.017974865 |
| 2026-04-14T23:59:48Z | 7969979 | 0.018422462 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.019363673 |
| 2026-04-16T23:59:48Z | 7984379 | 0.020361449 |
| 2026-04-17T23:59:48Z | 7991579 | 0.021083377 |
| 2026-04-18T23:59:48Z | 7998779 | 0.022857828 |
| 2026-04-19T23:59:48Z | 8005979 | 0.020432576 |
| 2026-04-20T23:59:48Z | 8013179 | 0.020251077 |
| 2026-04-21T23:59:48Z | 8020376 | 0.019120589 |
| 2026-04-22T23:59:48Z | 8027562 | 0.019303276 |
| 2026-04-23T23:59:48Z | 8034762 | 0.019258447 |
| 2026-04-24T23:59:48Z | 8041962 | 0.019448437 |
| 2026-04-25T23:59:48Z | 8049151 | 0.018968662 |
| 2026-04-26T23:59:48Z | 8056274 | 0.019047428 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.018965157 |
| 2026-04-28T23:59:48Z | 8070646 | 0.018846856 |
| 2026-04-29T23:59:48Z | 8077790 | 0.018435643 |
| 2026-04-30T23:59:48Z | 8084984 | 0.017996979 |
| 2026-05-01T23:59:48Z | 8092168 | 0.017772638 |
| 2026-05-02T23:59:48Z | 8099357 | 0.017772915 |
| 2026-05-03T16:09:24.001Z | 8104199 | 0.017732287 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

