# NetUID 111 — oneoneone (`Ё`)

## Overview

**oneoneone** (NetUID **111**) (`Ё`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `301`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,707.174822712. **Alpha liquidity in pool (`alpha_in`)** = ‎1,265,522.079879018Ё‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,482,256.542524564Ё‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003716904`** *(also **moving-average price** `0.0037246758583933115` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎88,270.196638107Ё‎`. **Owner hotkey / coldkey (chain):** `5CG4zutn1o8ZRQKUfMqKS2DfbYUwNtbM3XqL7ZPkTkntppwK` / `5HKeYGvjWXKfB6VVtG4SBpRa87TyKYzc6n8pJKacStFwWyfZ`.
- **Subnet registered at block:** `5615562` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎222.018354582Ё‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Ё‎` · α-in `‎0.000000000Ё‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003716935`
- **Market cap:** `12190999567111.652039055`
- **Liquidity:** `9411038134554`
- **Total τ:** `4707194862824`
- **Total α:** `3747703622403582`
- **α in pool:** `1265516688274170`
- **α staked:** `2014336084806783`
- **Price Δ 1h:** `-0.000914723797804071`
- **Price Δ 1d:** `-0.623912010653773483`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `5`
- **Active miners:** `249`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `5`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

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
- **Owner SS58 (`owner_ss58`):** `5HKeYGvjWXKfB6VVtG4SBpRa87TyKYzc6n8pJKacStFwWyfZ`

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
- **`liquid_alpha_enabled`:** `True`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

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

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/oneoneone-io/subnet-111](https://github.com/oneoneone-io/subnet-111)
- **Contact:** support@oneoneone.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.003716951 |
| 8104133 | 0.003716942 |
| 8104181 | 0.003716938 |
| 8104229 | 0.003716919 |
| 8104277 | 0.003716903 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

