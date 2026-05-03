# NetUID 38 — colosseum (`ם`)

## Overview

**colosseum** (NetUID **38**) (`ם`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `166`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,003.771260575. **Alpha liquidity in pool (`alpha_in`)** = ‎186,158.730937802ם‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎797,912.241487815ם‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.010746849`** *(also **moving-average price** `0.010545383207499981` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎34,103.337105848ם‎`. **Owner hotkey / coldkey (chain):** `5DDDD2gnwrXoAM764HRn4i6nXF2wHY2JXCfs4k9LaE9voi3v` / `5CaHKFJZQQRhEBT9RkHWM7NBsAW58MkBBo3mKKfGykNPmBqp`.
- **Subnet registered at block:** `7284230` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎102.820090647ם‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.005373431` · α-out `‎1.000000000ם‎` · α-in `‎0.500000000ם‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.010746869`
- **Market cap:** `7686158023398.005562565`
- **Liquidity:** `4004255045886`
- **Total τ:** `2003702134921`
- **Total α:** `984051563353136`
- **α in pool:** `186152163105865`
- **α staked:** `529047587016520`
- **Price Δ 1h:** `-0.043816815761032332`
- **Price Δ 1d:** `0.881472821747483283`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `5373456`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Strategic games on bittensor

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <h1 align="center">🏛️ TAO Colosseum</h1>
  <h3 align="center">P2P Betting on Bittensor EVM with Validator Incentives</h3>
</p>

<p align="center">
  <a href="https://github.com/TAO-Colosseum/tao-colosseum-subnet/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT">
  </a>
  <a href="https://bittensor.com">
    <img src="https://img.shields.io/badge/Bittensor-Subnet-green.svg" alt="Bittensor Subnet">
  </a>
  <img src="https://img.shields.io/badge/Python-3.9+-yellow.svg" alt="Python 3.9+">
</p>

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** P2P betting game on Bittensor EVM. Choose your side - Red or Blue. Classic or Underdog mode.

**Fetched document title:** TAO Colosseum | Red vs Blue Betting

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
- **Owner SS58 (`owner_ss58`):** `5CaHKFJZQQRhEBT9RkHWM7NBsAW58MkBBo3mKKfGykNPmBqp`

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

### ⚡ Validator Features

- **Time-Decayed Rewards**: 7-day window with exponential decay (recent activity weighted higher)
- **REST API**: Query validator state, scores, volumes, and leaderboards
- **Snapshot Storage**: Historical weight data stored in SQLite
- **Automatic Weight Setting**: Every 360 blocks (~72 minutes)

---

### Prerequisites

- Python 3.9+
- Bittensor wallet
- TAO for betting (miners) or staking (validators)

---

### Installation

```bash

---

# Create virtual environment

python -m venv venv
source venv/bin/activate  # Linux/Mac

---

# Install dependencies

pip install -e .
```

---

### Running a Validator

```bash
python validator/validator.py \
    --netuid <NETUID> \
    --wallet.name <WALLET_NAME> \
    --wallet.hotkey <HOTKEY_NAME> \
    --subtensor.network finney
```

---

### Becoming a Miner

1. Register on the subnet with your Bittensor wallet
2. Link your coldkey to an EVM address via the TAO Colosseum frontend
3. Place bets on the TAO Colosseum smart contract
4. Earn rewards based on your betting volume!

See the [Miner Guide](docs/miner.md) for detailed instructions.

---

---

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `BITTENSOR_EVM_RPC` | Bittensor EVM RPC endpoint | `https://lite.chain.opentensor.ai` |
| `API_PORT` | Validator API port | `8000` |

---

## 📊 Validator API

The validator exposes a REST API for querying state:

| Endpoint | Description |
|----------|-------------|
| `GET /health` | Validator health status |
| `GET /scores` | Current miner scores |
| `GET /volumes` | Current betting volumes |
| `GET /leaderboard` | Top miners by score |
| `GET /snapshots` | Historical weight snapshots |
| `POST /api/wallet-mapping` | Register coldkey-to-EVM mapping |

API documentation available at `http://localhost:8000/docs`

---

---

#### CPU / GPU / RAM lines (automatic grep)

- `| `GET /scores` | Current miner scores |`
- `| `GET /leaderboard` | Top miners by score |`

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- `| CPU | 2 cores | 4+ cores |`
- `| RAM | 4 GB | 8+ GB |`
- `| Storage | 20 GB SSD | 50+ GB SSD |`
- `| `/scores` | GET | All miner scores |`
- `| `/scores/{uid}` | GET | Specific miner's score and details |`
- `| `/leaderboard` | GET | Top miners ranked by score |`

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- `| CPU | 2 cores | 4+ cores |`
- `| RAM | 4 GB | 8+ GB |`
- `| Storage | 20 GB SSD | 50+ GB SSD |`
- `| `/scores` | GET | All miner scores |`
- `| `/scores/{uid}` | GET | Specific miner's score and details |`
- `| `/leaderboard` | GET | Top miners ranked by score |`


*Primary README URL used: `https://raw.githubusercontent.com/TAO-Colosseum/tao-colosseum-subnet/main/README.md`*

## On-chain identity — description


Strategic games on bittensor

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.taocolosseum.com/](https://www.taocolosseum.com/)
- **GitHub:** [https://github.com/TAO-Colosseum/tao-colosseum-subnet](https://github.com/TAO-Colosseum/tao-colosseum-subnet)
- **Discord (handle / invite hint):** `Yousefmbtc`
- **Logo URL:** [https://www.taocolosseum.com/colosseum-logo.png](https://www.taocolosseum.com/colosseum-logo.png)
- **Contact:** support@taocolosseum.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.01074784 |
| 8104072 | 0.010747558 |
| 8104120 | 0.010747205 |
| 8104168 | 0.010746997 |
| 8104216 | 0.010746849 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

