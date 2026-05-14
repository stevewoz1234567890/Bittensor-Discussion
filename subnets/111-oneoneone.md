# NetUID 111 — oneoneone (`Ё`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**oneoneone** (NetUID **111**) (`Ё`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `98`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,707.153307189. **Alpha liquidity in pool (`alpha_in`)** = ‎1,265,527.868492980Ё‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,482,408.753910602Ё‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003716870`** *(also **moving-average price** `0.0037243219558149576` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎88,270.218153630Ё‎`. **Owner hotkey / coldkey (chain):** `5CG4zutn1o8ZRQKUfMqKS2DfbYUwNtbM3XqL7ZPkTkntppwK` / `5HKeYGvjWXKfB6VVtG4SBpRa87TyKYzc6n8pJKacStFwWyfZ`.
- **Subnet registered at block:** `5615562` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎72.285608538Ё‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Ё‎` · α-in `‎0.000000000Ё‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104337`
- **Liquidity constant `k`:** `5957033691516576680430033220`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `oneoneone` |
| Symbol (API) | `Ё` |
| Rank | `90` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.003716935` |
| Market cap | `12190999567111.652039055` |
| Market cap Δ 1d | `-0.428329166035731678` |
| Liquidity | `9411038134554` |
| Total τ | `4707194862824` |
| Total α | `3747703622403582` |
| α in pool | `1265516688274170` |
| α staked | `2014336084806783` |
| Price Δ 1h | `-0.000914723797804071` |
| Price Δ 1d | `-0.623912010653773483` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `111` |
| Owner SS58 (API) | `5HKeYGvjWXKfB6VVtG4SBpRa87TyKYzc6n8pJKacStFwWyfZ` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5615562` |
| Registration wall time | `2025-05-22T18:46:12Z` |
| Registration cost snapshot | `249855564892` |
| Active keys | `256` |
| Active validators | `5` |
| Active miners | `249` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `5` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# oneoneone - Subnet 111

**A Decentralized Protocol for Accessing User-Generated Content**

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Node.js](https://img.shields.io/badge/node.js-18+-green.svg)
![Bittensor](https://img.shields.io/badge/bittensor-subnet%20111-orange.svg)

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** A decentralized AI ecosystem built on the Bittensor network that specializes in collecting, validating, and serving high-quality user-generated content from platforms across the web. - oneoneone-io...

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
| Owner SS58 (`owner_ss58`) | `5HKeYGvjWXKfB6VVtG4SBpRa87TyKYzc6n8pJKacStFwWyfZ` |


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
| `liquid_alpha_enabled` | `True` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Validators

**Minimum Requirements:**
- **CPU**: 2 cores
- **RAM**: 8 GB
- **Storage**: 32 GB SSD
- **Network**: Stable internet connection
- **Stake**: Minimum stake requirement for permit validation
- **Apify API Access**: Valid APIFY_TOKEN for data scraping
- **Chutes API Access**: Valid CHUTES_API_TOKEN for keyword generation
- **Desearch API Access**: Valid DESEARCH_API_TOKEN for data scraping

---

### Miners

**Minimum Requirements:**
- **CPU**: 2 cores
- **RAM**: 8 GB
- **Storage**: 32 GB SSD
- **Network**: Stable internet connection with good latency
- **Apify API Access**: Valid APIFY_TOKEN for data scraping
- **Gravity API Access**: Valid GRAVITY_API_TOKEN for data scraping

---

### Required Software

- **Python**: 3.12+
- **Node.js**: 18+ (for the node stack)
- **npm**: Latest version
- **Conda**: For environment management

---

### Prerequisites

Ensure you have the following installed on your system:
- Conda or Miniconda
- Node.js and npm
- Git

---

### Installing PM2

PM2 is required for running the subnet services. Here's how to install it:

```bash

---

# Install NVM (Node Version Manager)

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

---

# Install Node.js v21 and PM2. You might want to refresh your terminal shell

nvm i 21 && npm i pm2 -g

---

# Verify installations

node --version  # Should show v21.x.x
pm2 --version   # Should show PM2 version
```

---

### 1. Clone and Setup Environment

```bash

---

# Install Miniconda

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
~/miniconda3/bin/conda init
source ~/.bashrc

---

# Create and activate conda environment

conda create -n subnet-111 python=3.12
conda activate subnet-111

---

# Install Python dependencies

pip install -r requirements.txt
pip install -e .

---

# Install Node.js dependencies

cd node
npm install
cd ..
```

---

# Copy the root environment file (no editing needed)

cp .env.example .env

---

# For validators:

cp node/.env.validator.example node/.env

---

# For miners:

cp node/.env.miner.example node/.env

---

# Edit the node .env file to add your required fields (only for validators)

nano node/.env
```

**Required Configuration:**
- Root `.env`: Contains general project settings. No editing required
- Node `.env`: Contains Node.js application settings.
- Required for miners: `APIFY_TOKEN`, `GRAVITY_API_TOKEN`,
- Required for validators: `DESEARCH_API_TOKEN`, `CHUTES_API_TOKEN` and `PLATFORM_TOKEN` (ask from subnet owner team)

---

#### APIFY Token Setup

1. Sign up at [Apify.com](https://apify.com)
2. Subscribe to the Starter plan
3. Navigate to Settings → API & Integrations
4. Create a new token with appropriate permissions
5. Add the token to your `node/.env` file:
   ```bash
   APIFY_TOKEN=your_apify_token_here
   ```

---

#### Chutes API Token Setup (Validators Only)

1. Go to [chutes.ai](https://chutes.ai)
2. Press "Get Started" and login
3. Navigate to API at [chutes.ai/app/api](https://chutes.ai/app/api)
4. Create a new API Key
5. Add the token to your `node/.env` file:
   ```bash
   CHUTES_API_TOKEN=your_chutes_token_here
   ```

---

#### Desearch API Token Setup (Validators Only)

1. Go to [desearch.ai](https://desearch.ai)
2. Press "API Dashboard" and login
3. Navigate to API Keys at [console.desearch.ai/api-keys](https://console.desearch.ai/api-keys)
4. Create a new API key
5. Add the token to your `node/.env` file:
   ```bash
   DESEARCH_API_TOKEN=your_desearch_token_here
   ```

---

#### Macrocosmos Gravity API Token Setup (Miners Only)

1. Go to [macrocosmos.ai](https://macrocosmos.ai) and login
2. Navigate to Account Settings → API Keys at [app.macrocosmos.ai/account?tab=api-keys](https://app.macrocosmos.ai/account?tab=api-keys)
3. Create a new API Key
4. Add the token to your `node/.env` file:
   ```bash
   GRAVITY_API_TOKEN=your_gravity_token_here
   GRAVITY_TWEET_LIMIT=100
   ```

---

#### Platform Token Setup

If you are a validator, please contact the subnet team and get your `PLATFORM_TOKEN`. This token will be used in the future features including the platform integration.

---

# Install btcli

pip install bittensor-cli

---

#### Option A: Automatic Setup (Recommended)

The auto-updater script checks for updates every 20 minutes and only restarts processes when actual code changes are detected:

```bash

---

# Start validator with auto-updater (recommended)

pm2 start ./auto-updater.sh --name "autoupdater-validator-prod" -- validator 111 validator default 9000

---

# Start mine…

---





#### CPU / GPU / RAM lines (automatic grep)

- - **CPU**: 2 cores
- - **RAM**: 8 GB
- - **Storage**: 32 GB SSD
- `| **Phase 1** (Kickoff)             | Implementation of 3 core job types<br/>95%+ API success rate<br/>Network benchmarking        | 🚧 In Progress |`


*Primary README URL used: `https://raw.githubusercontent.com/oneoneone-io/subnet-111/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/oneoneone-io/subnet-111](https://github.com/oneoneone-io/subnet-111)
- **Contact:** support@oneoneone.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.003716915 |
| 8104292 | 0.003716901 |
| 8104340 | 0.003716878 |
| 8104388 | 0.003716876 |
| 8104436 | 0.003716869 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.003590855 --> 0.005419014
    line [0.004070932, 0.004064977, 0.004197898, 0.004238863, 0.004228772, 0.004612118, 0.004588574, 0.004364591, 0.004545699, 0.004871337, 0.00529293409596, 0.004608592, 0.004772889, 0.004736557, 0.004656168, 0.00455925549602, 0.004426207, 0.004356802, 0.004549135, 0.004464586, 0.004522341, 0.004583875, 0.004904851, 0.004656579, 0.004829733, 0.004672197, 0.005177334, 0.004962099, 0.005140297, 0.004819238, 0.004631541, 0.003780036, 0.003949886, 0.004122554, 0.004265918, 0.004233429, 0.004348145, 0.004186789, 0.00420172, 0.004167457, 0.004140669, 0.004134888, 0.004125978, 0.004080836, 0.004132409, 0.004296368, 0.004251592, 0.00418076, 0.004162664, 0.00375631, 0.003819359, 0.003784306, 0.003814553, 0.003749581, 0.003738452, 0.003716935]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

