# NetUID 41 — Almanac (`נ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Almanac** (NetUID **41**) (`נ`).

Incentivized market intelligence.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `28`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ12,685.429849010. **Alpha liquidity in pool (`alpha_in`)** = ‎2,325,671.953555261נ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,357,977.653810075נ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005542733`** *(also **moving-average price** `0.005522059742361307` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,508,370.197734035נ‎`. **Owner hotkey / coldkey (chain):** `5FCSevLkofmKZRixMawp6jyyjBty1AeSCLa7N5Fv892DYkXX` / `5FCSevLkofmKZRixMawp6jyyjBty1AeSCLa7N5Fv892DYkXX`.
- **Subnet registered at block:** `3394182` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎21.036785564נ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000נ‎` · α-in `‎0.000000000נ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104407`
- **Liquidity constant `k`:** `29502148418635306279921141610`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Almanac` |
| Symbol (API) | `נ` |
| Rank | `49` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.005544678` |
| Market cap | `22241404773787.113967236` |
| Market cap Δ 1d | `1.439895262616574006` |
| Liquidity | `25580531565354` |
| Total τ | `12687708552604` |
| Total α | `4683416607365336` |
| α in pool | `2325260910146761` |
| α staked | `1686045927470701` |
| Price Δ 1h | `0.700641107135722199` |
| Price Δ 1d | `1.330883462899412155` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `41` |
| Owner SS58 (API) | `5FCSevLkofmKZRixMawp6jyyjBty1AeSCLa7N5Fv892DYkXX` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3394182` |
| Registration wall time | `2024-07-15T23:41:12Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `10` |
| Active miners | `33` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `10` |
| Max validators (API) | `64` |
| Neuron reg. cost | `100000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">


</div>

- [Introduction](#introduction)
- [How it Works](#how-it-works)
- [Miner and Validator Functionality](#miner-and-validator-functionality)
  - [Miner](#miner)
  - [Validator](#validator)
- [Miner setup and running Validators](#miner-setup-and-running-validators)
  - [Setting up a Miner](#setting-up-a-miner)
  - [Running a Validator](#running-a-validator)
- [Community](#community)
- [License](#license)

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Prediction markets have earned a reputation for accurate forecasting—but that accuracy mostly shows up in the final hours before resolution. Almanac rewards traders for being right early, when the signal matters most.

**Fetched document title:** Almanac — Accurate Before It's Obvious

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
| `immunity_period` (blocks) | 14400 |
| Registration recycle cost snapshot (`burn`) | τ0.100000000 |
| Owner SS58 (`owner_ss58`) | `5FCSevLkofmKZRixMawp6jyyjBty1AeSCLa7N5Fv892DYkXX` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.100000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `14400` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `950000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Miner

- Miners generate **information signals** by trading on Almanac, which routes Polymarket CLOB orders through the miner’s proxy wallet.  
- Every trade becomes a scored prediction within the **incentive mechanism**, which evaluates accuracy, ROI, timing, and informational value.  
- Miners may use **manual strategies, models, or automated systems**—the scoring is model-agnostic and purely performance-based.  
- High-signal miners earn the largest share of **daily Alpha Token emissions**.

---

### Validator

- **Metadata Syncing**: Validators continuously sync miner metadata from chain (wallets, proxy addresses, UIDs).  
- **Data Ingestion**: At each epoch, the validator pulls miner trading history from Almanac’s backend (rolling window).  
- **Scoring**: The validator runs the **two-phase scoring mechanism**.
- **Weight Setting**: After generating scores, validators set miner weights on-chain, determining Alpha Token emissions for the next epoch.

---

#### Requirements

- Almanac account linked to Polymarket  
- Almanac account connected to a registered Bittensor coldkey  
- Python 3.10+  
- Pip  
- CPU

---

#### Almanac and Polymarket Setup

1. Go to **https://beta.almanac.market**  
2. Create an account
    - Deploy safe wallet
    - Sign all approvals
    - Fund your safe wallet
3. Connect your Bittensor coldkey:  
   - Install the Bittensor wallet extension  
   - Import the coldkey tied to your miner UID  
   - Link wallet in Almanac settings

---

#### Miner Metadata Registration

1. Clone the repository:
```bash
git clone https://github.com/sportstensor/sn41/
cd sn41
```
2. Install dependencies:
```bash 
pip install -r requirements.txt
```

3. Register miner metadata:
```bash 
python miner.py
```

---

## Miner Trading with Almanac dApp

Once linked, miners can trade directly on **https://beta.almanac.market**.  
Validators automatically detect trades, compute scores, and distribute emissions.

*Note: Miners trading directly on the app don't need to connect their Bittensor wallet after initially linking account.

---

---

## Miner Trading with API

For programmatic trading:

1. Complete all onboarding steps above.
2. Use the **Almanac API Trading Client** (`api_trading.py`) to:
   - Generate Polymarket API credentials  
   - Create Almanac trading sessions  
   - Search markets  
   - Place signed CLOB orders  
   - Submit proxy-signed EIP-712 orders  

---

---

### Requirements

- Python 3.10+  
- Pip  
- CPU

---

### Setup

Clone and enter the repo:
```bash 
git clone https://github.com/sportstensor/sn41/
cd sn41
```
Install pm2 (if not already installed).

Install Python dependencies:
```bash 
pip install -r requirements.txt
```

---

### Run Auto-Updating Validator with PM2 (recommended)

```bash 
pm2 start validator_auto_update.sh --name sn41-validator -- \
    --netuid 41 \
    --wallet.name {wallet} \
    --wallet.hotkey {hotkey} \
    --logging.debug
```

---

### Run Basic Validator with PM2

```bash 
pm2 start validator.py --name sn41-validator -- \
    --netuid 41 \
    --wallet.name {wallet} \
    --wallet.hotkey {hotkey} \
    --logging.debug
```

---

## Environments

| Network | Netuid |
| ----------- | -----: |
| Mainnet     |     41 |
| Testnet     |    172 |

---









#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/sportstensor/sn41/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://almanac.market](https://almanac.market)
- **GitHub:** [https://github.com/sportstensor/sn41](https://github.com/sportstensor/sn41)
- **Logo URL:** [https://beta.almanac.market/assets/favicons/favicon-32x32.png](https://beta.almanac.market/assets/favicons/favicon-32x32.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.00554212 |
| 8104244 | 0.005544664 |
| 8104292 | 0.005544655 |
| 8104340 | 0.005542312 |
| 8104388 | 0.005542737 |
| 8104436 | 0.005542733 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

