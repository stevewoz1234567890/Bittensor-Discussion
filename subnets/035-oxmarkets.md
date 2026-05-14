# NetUID 35 — OxMarkets (`ך`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**OxMarkets** (NetUID **35**) (`ך`).

Liquidity-as-a-Service subnet powering 0xMarkets - a permissionless perp DEX for FX, crypto, and commodities. Deposit USDC. Earn Spread + Fees + Alpha.



#### SubnetIdentity `additional` *(chain)*



https://x.com/0x_Markets

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `22`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ10,298.853502749. **Alpha liquidity in pool (`alpha_in`)** = ‎1,964,672.208053304ך‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,983,739.451538615ך‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005272969`** *(also **moving-average price** `0.005415210500359535` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎698,768.256067785ך‎`. **Owner hotkey / coldkey (chain):** `5EsmkLf4VnpgNM31syMjAWsUrQdW2Yu5xzWbv6oDQydP9vVx` / `5EqZVDbW5sKXE5qB5zVaH6SQT2sud3LkmFBo2dn79NdY9RTr`.
- **Subnet registered at block:** `3037158` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎16.596824027ך‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ך‎` · α-in `‎0.000000000ך‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104413`
- **Liquidity constant `k`:** `20233871251663381986902532696`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `OxMarkets` |
| Symbol (API) | `ך` |
| Rank | `44` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.005272048` |
| Market cap | `24867082299422.053253744` |
| Market cap Δ 1d | `-3.57321678367817825` |
| Liquidity | `20656699607986` |
| Total τ | `10297942474319` |
| Total α | `4948178659591919` |
| α in pool | `1964844996416499` |
| α staked | `2751933435688454` |
| Price Δ 1h | `-0.0375424628007284` |
| Price Δ 1d | `-3.72040895077933346` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `35` |
| Owner SS58 (API) | `5EqZVDbW5sKXE5qB5zVaH6SQT2sud3LkmFBo2dn79NdY9RTr` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3037158` |
| Registration wall time | `2024-05-26T01:20:24.001Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `11` |
| Active miners | `3` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `11` |
| Max validators (API) | `64` |
| Neuron reg. cost | `100000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Cartha Validator

**The official validator implementation for Cartha subnet (SN35).** Score miners based on their USDC liquidity positions, compute weights, and publish them to the Bittensor network—all with built-in on-chain event replay and robust scoring algorithms.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Decentralized exchange for commodities and crypto

**Fetched document title:** 0xMarkets

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
| `immunity_period` (blocks) | 7200 |
| Registration recycle cost snapshot (`burn`) | τ0.100000000 |
| Owner SS58 (`owner_ss58`) | `5EqZVDbW5sKXE5qB5zVaH6SQT2sud3LkmFBo2dn79NdY9RTr` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.100000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `7200` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `True` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `3` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

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

### Weekly Epoch System

- **Epoch Duration**: Friday 00:00 UTC → Thursday 23:59 UTC (7 days)
- **Weight Calculation**: Computed once per week at epoch start
- **Weight Publishing**: Cached weights are republished every Bittensor epoch (tempo blocks) throughout the week
- **Daily Expiry Checks**: Validator checks for expired pools daily and updates weights accordingly

---

### Auto-Updater System

The validator includes an automated update system that:

- **Checks GitHub Releases**: Automatically checks for new releases on GitHub
- **PM2 Process Management**: Manages validator process via PM2 (survives SSH disconnect)
- **Automatic Updates**: Pulls latest code, installs dependencies, and restarts validator
- **Environment Validation**: Validates `.env` file before restarting
- **Failure Handling**: Keeps validator running on current version if update fails

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

---








#### CPU / GPU / RAM lines (automatic grep)

- - **CPU**: 2 cores
- - **RAM**: 4 GB
- - **Disk**: 20 GB SSD


*Primary README URL used: `https://raw.githubusercontent.com/General-Tao-Ventures/cartha-validator/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.0xmarkets.io/](https://www.0xmarkets.io/)
- **GitHub:** [https://github.com/General-Tao-Ventures/cartha-validator](https://github.com/General-Tao-Ventures/cartha-validator)
- **Discord:** [https://0xmarkets.io/discord](https://0xmarkets.io/discord)
- **Logo URL:** [https://storage.googleapis.com/cartha-assets/cartha_logo.png](https://storage.googleapis.com/cartha-assets/cartha_logo.png)
- **Contact:** contact@0xmarkets.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.005272049 |
| 8104244 | 0.005272033 |
| 8104292 | 0.005272023 |
| 8104340 | 0.005272007 |
| 8104388 | 0.005271944 |
| 8104436 | 0.005272969 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

