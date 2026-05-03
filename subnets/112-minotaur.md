# NetUID 112 — minotaur (`Ђ`)

## Overview

**minotaur** (NetUID **112**) (`Ђ`).

Distributed DEX aggregator and swap intent solver engine

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `240`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,983.568134611. **Alpha liquidity in pool (`alpha_in`)** = ‎905,112.971844370Ђ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,610,721.400315817Ђ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005506140`** *(also **moving-average price** `0.005540274083614349` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎71,923.726041303Ђ‎`. **Owner hotkey / coldkey (chain):** `5E1ohAszHfhyQUEtz6mvCCkW4pYHsinPjxXS938fAZ2jFvCt` / `5D7Rf7HbeE7ti49fyLg3TM3F96uWFUwzYBo9SkzBpAUTQMhM`.
- **Subnet registered at block:** `5633022` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎169.980110418Ђ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Ђ‎` · α-in `‎0.000000000Ђ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005506142`
- **Market cap:** `10188391229668.516368554`
- **Liquidity:** `9967248683616`
- **Total τ:** `4983568629566`
- **Total α:** `2515821372160187`
- **α in pool:** `905112881950766`
- **α staked:** `945255530209421`
- **Price Δ 1h:** `-0.001707155305366497`
- **Price Δ 1d:** `-2.011628389129443999`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Distributed DEX aggregator and swap intent solver engine

### Repository README excerpt *(everything before first `##` heading)*

# Minotaur — Distributed DEX Aggregator & Swap Intent Solver Engine

Minotaur is a Bittensor subnet (Subnet 112) focused on swap-intent processing and execution optimization. It leverages a subnet-native incentive mechanism to deliver better, cheaper, and faster trades for users.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Verifiable financial coordination layer. DEX aggregation & swap intent routing.

**Fetched document title:** minotaur - Powering DEX aggregation & swap intent routing

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
- **Owner SS58 (`owner_ss58`):** `5D7Rf7HbeE7ti49fyLg3TM3F96uWFUwzYBo9SkzBpAUTQMhM`

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

### Miners (Ingress and Availability)

- Execute quotes
- Compute candidate settlements that maximize user surplus
- Compete for best optimization (tokens/gas usage/speed)
- Use direct matches, AMMs, RFQ/MMs, and aggregators when helpful
- Earn solver fees on target chains (paid in buy tokens)
- Earn emissions based on performance (winner-takes-most model)

---

### Validators (Canonical State and Attestation)

- Fetch pending orders from the aggregator
- Validate order execution through Docker-based simulation
- Run epochs (time windows, default: 5 minutes) to collect validation results
- Compute miner scores based on validation success rates
- Compute and emit weights on the Bittensor chain
- Submit weights to the aggregator for transparency

---

### Prerequisites

- Python 3.12+
- Docker (for order simulation)
- **Bittensor Mode:** A registered wallet/hotkey on the target subnet (Subnet 112)
- **Simulation Mode:** Access to the Aggregator API and Docker + RPC for simulation
- **Both Modes:** API keys (VALIDATOR_API_KEY for validators, MINER_API_KEY for miners)

---

### Easy Setup (Recommended for Beginners)

We provide several tools to make setup and monitoring easier:

---

#### 1. Interactive Setup Wizard

The setup wizard guides you through configuration step-by-step:
```bash
python scripts/setup_wizard.py
```

This will:
- Check system requirements (Docker, Python, etc.)
- Guide you through choosing validator/miner mode
- Validate your RPC endpoints
- Generate .env configuration files
- Optionally pull Docker images

---

#### 2. Docker Compose (Simplest Deployment)

After running the setup wizard, start everything with:
```bash

---

# Or start only validator

docker compose --profile validator up -d

---

# Or start only miners

docker compose --profile miner up -d

---

#### 4. Configuration Validator

Validate your .env files before starting:
```bash
python scripts/validate_config.py
python scripts/validate_config.py --env-file /path/to/.env
```

---

---

#### Validator - Simulation Mode (Testing)

```bash
git clone <repo>
cd minotaur
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

---

#### Validator - Bittensor Mode (Production)

```bash

---

#### Miner - Simulation Mode (Testing)

```bash

---

# Run miner in simulation mode (generates hotkey from miner_id)

export MINER_MODE=simulation
export MINER_ID=my-test-miner
export AGGREGATOR_URL=http://localhost:4000
export MINER_API_KEY=your-miner-api-key  # Required for /v1/solvers/* endpoints
export MINER_BASE_PORT=8000
export ETHEREUM_RPC_URL=https://mainnet.infura.io/v3/YOUR_INFURA_KEY

python -m neurons.miner \
  --miner.mode simulation \
  --miner.id my-test-miner \
  --aggregator.url http://localhost:4000 \
  --miner.api_key your-miner-api-key \
  --miner.base_port 8000 \
  --miner.num_solvers 2  # Run 2 solvers (default: 1)
```

---

#### Miner - Bittensor Mode (Production)

```bash

---

# Run miner in bittensor mode (uses configured wallet)

export MINER_MODE=bittensor
export WALLET_NAME=my-miner
export WALLET_HOTKEY=my-hotkey
export AGGREGATOR_URL=http://your-aggregator:4000
export MINER_API_KEY=your-miner-api-key  # Required
export ETHEREUM_RPC_URL=https://mainnet.infura.io/v3/YOUR_INFURA_KEY

python -m neurons.miner \
  --miner.mode bittensor \
  --wallet.name my-miner \
  --wallet.hotkey my-hotkey \
  --aggregator.url http://your-aggregator:4000 \
  --miner.api_key your-miner-api-key
```

**Important:** The solver always queries Uniswap V2/V3 on-chain for price quotes, so you **must** configure an Ethereum RPC URL (`ETHEREUM_RPC_URL` or `ALCHEMY_API_KEY`) to avoid rate limiting errors.

---

### Validator Settings

| Variable | Description | Default |
|----------|-------------|---------|
| `VALIDATOR_MODE` | `bittensor` or `mock` | `bittensor` |
| `VALIDATOR_POLL_SECONDS` | Poll interval for new epochs | 12 |
| `VALIDATOR_EPOCH_MINUTES` | Epoch duration in minutes | 5 |
| `VALIDATOR_CONTINUOUS` | Enable continuous epoch mode | true |
| `SIMULATOR_RPC_URL` | Ethereum RPC URL for simulation | Required |
| `SIMULATOR_MAX_CONCURRENT` | Maximum concurrent simulations | 5 |
| `SIMULATOR_TIMEOUT_SECONDS` | Simulation timeout (seconds) | 300 |
| `BURN_PERCENTAGE` | Fraction of emissions to burn (0.0-1.0) | 0.0 |

---

### Miner Settings

| Variable | Description | Default |
|----------|-------------|---------|
| `MINER_MODE` | `simulation` or `bittensor` | `simulation` |
| `MINER_ID` | Miner identifier (required in simulation mode) | – |
| `MINER_BASE_PORT` | Base port for solver servers | 8000 |
| `MINER_NUM_SOLV…

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/subnet112/minotaur_subnet/main/README.md`*

## On-chain identity — description


Distributed DEX aggregator and swap intent solver engine

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://minotaursubnet.com](https://minotaursubnet.com)
- **GitHub:** [https://github.com/subnet112/minotaur_subnet](https://github.com/subnet112/minotaur_subnet)
- **Logo URL:** [https://minotaursubnet.com/logos/logo.png](https://minotaursubnet.com/logos/logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.005506205 |
| 8104072 | 0.005506189 |
| 8104120 | 0.005506168 |
| 8104168 | 0.005506151 |
| 8104216 | 0.00550614 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

