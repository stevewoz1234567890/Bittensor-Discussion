# NetUID 112 — minotaur (`Ђ`)

## Overview

Distributed DEX aggregator and swap intent solver engine

**From crawled page (site or GitHub):** Verifiable financial coordination layer. DEX aggregation & swap intent routing.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

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

## Miner / validator compute notes (README excerpts)

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
| `MINER_NUM_SOLVERS` | Number of solvers to run | 1 |
| `MINER_SOLVER_TYPE` | Solver type (v2, v3, base, etc.) | v3 |
| `ETHEREUM_RPC_URL` | Ethereum RPC URL (required) | – |
| `ALCHEMY_API_KEY` | Alchemy API key (alternative to RPC URL) | – |

---

### Phase A - Training (Month 1–3): Miner Onboarding and Training

- Solver interface + scoring (user surplus, correctness, gas efficiency)
- Observability alpha: epoch metrics, basic dashboards between miners and competitor solvers
- Initial marketing

---

### Validator Documentation

- [Validator Overview](docs/validator/README.md) – Introduction to the validator
- [Validator Quickstart](docs/validator/quickstart.md) – Get started quickly
- [Validator Configuration](docs/validator/configuration.md) – Complete configuration reference
- [Validator Troubleshooting](docs/validator/troubleshooting.md) – Common issues and solutions

---

### Miner Documentation

- [Miner Overview](docs/miner/README.md) – Introduction to the miner
- [Miner Quickstart](docs/miner/quickstart.m…


*README source used for excerpts: `https://raw.githubusercontent.com/subnet112/minotaur_subnet/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Distributed DEX aggregator and swap intent solver engine

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://minotaursubnet.com](https://minotaursubnet.com)
- **GitHub:** [https://github.com/subnet112/minotaur_subnet](https://github.com/subnet112/minotaur_subnet)
- **Logo URL:** [https://minotaursubnet.com/logos/logo.png](https://minotaursubnet.com/logos/logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.00550649 |
| 8103738 | 0.005506468 |
| 8103786 | 0.005506296 |
| 8103834 | 0.005506281 |
| 8103882 | 0.005506246 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** minotaur - Powering DEX aggregation & swap intent routing
- **Meta / og:description:** Verifiable financial coordination layer. DEX aggregation & swap intent routing.
- **Fetched from:** [https://minotaursubnet.com](https://minotaursubnet.com)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

