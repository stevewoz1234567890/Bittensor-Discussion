# NetUID 5 — Hone (`ε`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Hone** (NetUID **5**) (`ε`).

Hone training

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `353`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ37,442.056202045. **Alpha liquidity in pool (`alpha_in`)** = ‎2,111,582.666094981ε‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,696,883.633226604ε‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.017732053`** *(also **moving-average price** `0.01775636849924922` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎882,271.174667984ε‎`. **Owner hotkey / coldkey (chain):** `5GZ2KuT2TtLbYTtsMcgAtazo6KQ4bc57ykZgyQv9oit3y7iq` / `5GurNtB3yQFCh6CSmfH7LrYJDsvzup4diHZiaYtKe274nrMX`.
- **Subnet registered at block:** `2491604` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎265.738387714ε‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ε‎` · α-in `‎0.000000000ε‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104082`
- **Liquidity constant `k`:** `79061996859192299692096436145`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Hone` |
| Symbol (API) | `ε` |
| Rank | `15` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.017732285` |
| Market cap | `64194848244719.22881606` |
| Market cap Δ 1d | `-0.147141355390603752` |
| Liquidity | `74885241836530` |
| Total τ | `37442301413892` |
| Total α | `4808233299321585` |
| α in pool | `2111568837441920` |
| α staked | `1508655417058796` |
| Price Δ 1h | `-0.00043423431125532` |
| Price Δ 1d | `-0.264083323710685672` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `5` |
| Owner SS58 (API) | `5GurNtB3yQFCh6CSmfH7LrYJDsvzup4diHZiaYtKe274nrMX` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `2491604` |
| Registration wall time | `2024-03-04T03:19:48.001Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `14` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `14` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Hone Subnet — ARC-AGI-2 Benchmarking on Bittensor

A Bittensor subnet where **validators** evaluate **miners** on their ability to solve novel ARC-AGI-2 reasoning problems. Miners don't run solvers directly—they point to a git repository containing their solution, which is executed in a secure GPU sandbox.

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Incentivized distributed training of large language models. Train together, build what's next.

**Fetched document title:** Hone

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
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5GurNtB3yQFCh6CSmfH7LrYJDsvzup4diHZiaYtKe274nrMX` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.hone.training/](https://www.hone.training/)
- **GitHub:** [https://github.com/manifold-inc/hone](https://github.com/manifold-inc/hone)
- **Logo URL:** [https://www.hone.training/logo.svg](https://www.hone.training/logo.svg)
- **Contact:** devs@manifold.inc

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.017732288 |
| 8104244 | 0.017732149 |
| 8104292 | 0.017732119 |
| 8104340 | 0.017732068 |
| 8104388 | 0.017732064 |
| 8104436 | 0.017732053 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.01309437 --> 0.02358105
    line [0.01576657, 0.015534025, 0.015384372, 0.015408077, 0.015376662, 0.015418387, 0.015344035, 0.015380396, 0.015361447, 0.015294041, 0.0152781330174, 0.015294865, 0.015277787, 0.015263414, 0.014227505, 0.0141220028061, 0.014114441, 0.01404183, 0.013871777, 0.013823492, 0.013821074, 0.013817585, 0.013886972, 0.013846416, 0.013847123, 0.013851482, 0.013952633, 0.013964602, 0.014213375, 0.014024891, 0.01404007, 0.013975333, 0.017303765, 0.017423698, 0.017404474, 0.017974865, 0.018422462, 0.019363673, 0.020361449, 0.021083377, 0.022857828, 0.020432576, 0.020251077, 0.019120589, 0.019303276, 0.019258447, 0.019448437, 0.018968662, 0.019047428, 0.018965157, 0.018846856, 0.018435643, 0.017996979, 0.017772638, 0.017772915, 0.017732285]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

