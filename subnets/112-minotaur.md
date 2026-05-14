# NetUID 112 — minotaur (`Ђ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**minotaur** (NetUID **112**) (`Ђ`).

Distributed DEX aggregator and swap intent solver engine

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `99`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,983.489203591. **Alpha liquidity in pool (`alpha_in`)** = ‎905,127.307195438Ђ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,610,927.064964749Ђ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005505966`** *(also **moving-average price** `0.005538266850635409` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎71,923.804972323Ђ‎`. **Owner hotkey / coldkey (chain):** `5E1ohAszHfhyQUEtz6mvCCkW4pYHsinPjxXS938fAZ2jFvCt` / `5D7Rf7HbeE7ti49fyLg3TM3F96uWFUwzYBo9SkzBpAUTQMhM`.
- **Subnet registered at block:** `5633022` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎70.117806207Ђ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Ђ‎` · α-in `‎0.000000000Ђ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104336`
- **Liquidity constant `k`:** `4510692163283859722408417858`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `minotaur` |
| Symbol (API) | `Ђ` |
| Rank | `96` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.005506142` |
| Market cap | `10188391229668.516368554` |
| Market cap Δ 1d | `-1.776751551440048737` |
| Liquidity | `9967248683616` |
| Total τ | `4983568629566` |
| Total α | `2515821372160187` |
| α in pool | `905112881950766` |
| α staked | `945255530209421` |
| Price Δ 1h | `-0.001707155305366497` |
| Price Δ 1d | `-2.011628389129443999` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `112` |
| Owner SS58 (API) | `5D7Rf7HbeE7ti49fyLg3TM3F96uWFUwzYBo9SkzBpAUTQMhM` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5633022` |
| Registration wall time | `2025-05-25T05:08:00Z` |
| Registration cost snapshot | `196761272984` |
| Active keys | `256` |
| Active validators | `13` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `13` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Minotaur — Distributed DEX Aggregator & Swap Intent Solver Engine

Minotaur is a Bittensor subnet (Subnet 112) focused on swap-intent processing and execution optimization. It leverages a subnet-native incentive mechanism to deliver better, cheaper, and faster trades for users.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Verifiable financial coordination layer. DEX aggregation & swap intent routing.

**Fetched document title:** minotaur - Powering DEX aggregation & swap intent routing

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
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5D7Rf7HbeE7ti49fyLg3TM3F96uWFUwzYBo9SkzBpAUTQMhM` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://minotaursubnet.com](https://minotaursubnet.com)
- **GitHub:** [https://github.com/subnet112/minotaur_subnet](https://github.com/subnet112/minotaur_subnet)
- **Logo URL:** [https://minotaursubnet.com/logos/logo.png](https://minotaursubnet.com/logos/logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.005506085 |
| 8104292 | 0.005506049 |
| 8104340 | 0.005505988 |
| 8104388 | 0.005505984 |
| 8104436 | 0.005505966 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.005188689 --> 0.007788616
    line [0.006443669, 0.006358129, 0.006386669, 0.006393804, 0.006375526, 0.006827123, 0.006974526, 0.007566885, 0.007127039, 0.007046898, 0.00701454507186, 0.006986265, 0.006978819, 0.007014404, 0.007046514, 0.00680626398409, 0.006547311, 0.00652896, 0.006563819, 0.006646781, 0.006860497, 0.006931337, 0.007150799, 0.007442251, 0.007609311, 0.007340315, 0.007186735, 0.007180668, 0.007177399, 0.007255145, 0.006868377, 0.006103721, 0.005584974, 0.005605355, 0.005622928, 0.005541004, 0.005771063, 0.005454377, 0.005619798, 0.005591657, 0.005442334, 0.005437751, 0.00547057, 0.005415097, 0.005390517, 0.005367994, 0.005381234, 0.005381658, 0.005378627, 0.005455428, 0.005472246, 0.005553697, 0.005514049, 0.005660919, 0.005508402, 0.005506142]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

