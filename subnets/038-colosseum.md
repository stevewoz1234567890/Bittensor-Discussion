# NetUID 38 — colosseum (`ם`)

## Overview

Strategic games on bittensor

**From crawled page (site or GitHub):** P2P betting game on Bittensor EVM. Choose your side - Red or Blue. Classic or Underdog mode.

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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/TAO-Colosseum/tao-colosseum-subnet/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Strategic games on bittensor

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://www.taocolosseum.com/](https://www.taocolosseum.com/)
- **GitHub:** [https://github.com/TAO-Colosseum/tao-colosseum-subnet](https://github.com/TAO-Colosseum/tao-colosseum-subnet)
- **Discord (handle / invite hint):** `Yousefmbtc`
- **Logo URL:** [https://www.taocolosseum.com/colosseum-logo.png](https://www.taocolosseum.com/colosseum-logo.png)
- **Contact:** support@taocolosseum.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.010771138 |
| 8103690 | 0.010839304 |
| 8103738 | 0.010677315 |
| 8103786 | 0.010688282 |
| 8103834 | 0.010740467 |
| 8103882 | 0.010751737 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** TAO Colosseum | Red vs Blue Betting
- **Meta / og:description:** P2P betting game on Bittensor EVM. Choose your side - Red or Blue. Classic or Underdog mode.
- **Fetched from:** [https://www.taocolosseum.com/](https://www.taocolosseum.com/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

