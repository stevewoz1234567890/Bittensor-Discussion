# NetUID 35 — OxMarkets (`ך`)

## Overview

Liquidity-as-a-Service subnet powering 0xMarkets - a permissionless perp DEX for FX, crypto, and commodities. Deposit USDC. Earn Spread + Fees + Alpha.

https://x.com/0x_Markets

**From crawled page (site or GitHub):** Decentralized exchange for commodities and crypto

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.100000000
- **Owner SS58 (`owner_ss58`):** `5EqZVDbW5sKXE5qB5zVaH6SQT2sud3LkmFBo2dn79NdY9RTr`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.100000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `True`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

# Cartha Validator

**The official validator implementation for Cartha subnet (SN35).** Score miners based on their USDC liquidity positions, compute weights, and publish them to the Bittensor network—all with built-in on-chain event replay and robust scoring algorithms.

---

## Why Cartha Validator?

Cartha Validator provides a complete, production-ready solution for running a validator on the Cartha subnet:

- **📊 Intelligent Scoring** - Score miners based on locked USDC amounts, lock duration, pool weights, and expired pool filtering
- **🔄 Weekly Epoch Management** - Automatic weekly epoch detection (Friday 00:00 UTC) with daily expiry checks
- **🔒 Validator Whitelist** - Only whitelisted validators can query verified miners (contact subnet owner to be added)

---

# Install dependencies

uv sync

---

# Run a dry-run to see computed weights

uv run python -m cartha_validator.main \
  --wallet-name cold \
  --wallet-hotkey hot \
  --netuid 35 \
  --dry-run

---

### Software Requirements

- Python 3.11
- [`uv`](https://github.com/astral-sh/uv) for dependency management
- Bittensor wallet (coldkey and hotkey)
- Access to Cartha verifier instance
- **Validator Whitelist**: Your validator hotkey must be whitelisted by the subnet owner

---

### Minimum Compute Requirements

- **CPU**: 2 cores
- **RAM**: 4 GB
- **Disk**: 20 GB SSD
- **Network**: Stable internet connection with minimal downtime

---

### Miner Score (Sum of All Positions)

A miner's total score is the **sum of all their active position scores**. Positions are evaluated individually — not collapsed by pool — so every position with a distinct lock duration contributes its own unique boost:

```
miner_score = Σ position_score_i   (for all non-expired, non-deregistered positions)
```

A principal miner below 100,000 USDC total across their entire vault receives `score = 0.0` regardless of lock duration. This also means all federated miners in that vault earn no ALPHA rewards for that epoch.

---

### Federated Miner Impact

Every federated miner who locks USDC into a principal miner's vault contributes an independent position that adds directly to the principal's aggregate score. A federated miner locking for 365 days contributes **twice** the score of one locking for 182 days at the same amount. This design makes the system robust and fair — every individual position matters, and longer commitments are proportionally rewarded.

---

#### Initial Setup

```bash

---

# One-time installation

cd cartha-validator
chmod +x scripts/run.sh
./scripts/run.sh
```

This will:
- Install PM2 globally
- Install Python dependencies
- Create PM2 ecosystem configuration
- Set up PM2 to start on system boot
- Start both validator manager and validator processes

---

#### Managing Validator

```bash

---

# View validator logs locally

pm2 logs cartha-validator


*README source used for excerpts: `https://raw.githubusercontent.com/General-Tao-Ventures/cartha-validator/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Liquidity-as-a-Service subnet powering 0xMarkets - a permissionless perp DEX for FX, crypto, and commodities. Deposit USDC. Earn Spread + Fees + Alpha.

## On-chain identity — additional field


https://x.com/0x_Markets

## Registered contact & links


- **Website:** [https://www.0xmarkets.io/](https://www.0xmarkets.io/)
- **GitHub:** [https://github.com/General-Tao-Ventures/cartha-validator](https://github.com/General-Tao-Ventures/cartha-validator)
- **Discord:** [https://0xmarkets.io/discord](https://0xmarkets.io/discord)
- **Logo URL:** [https://storage.googleapis.com/cartha-assets/cartha_logo.png](https://storage.googleapis.com/cartha-assets/cartha_logo.png)
- **Contact:** contact@0xmarkets.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.005373057 |
| 8103690 | 0.005373029 |
| 8103738 | 0.005272892 |
| 8103786 | 0.005273543 |
| 8103834 | 0.005274056 |
| 8103882 | 0.005274047 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** 0xMarkets
- **Meta / og:description:** Decentralized exchange for commodities and crypto
- **Fetched from:** [https://www.0xmarkets.io/](https://www.0xmarkets.io/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

