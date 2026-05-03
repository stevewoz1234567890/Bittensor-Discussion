# NetUID 111 — oneoneone (`Ё`)

## Overview

**From crawled page (site or GitHub):** A decentralized AI ecosystem built on the Bittensor network that specializes in collecting, validating, and serving high-quality user-generated content from platforms across the web. - oneoneone-io...

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

## Miner / validator compute notes (README excerpts)

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

# Start miner with auto-updater (recommended)

pm2 start ./auto-updater.sh --name "autoupdater-miner-prod" -- miner 111 miner default 9001

---

# Start validator with auto-updater on testnet

pm2 start ./auto-updater.sh --name "autoupdater-validator-test" -- validator 427 validator default 9000 test

---

# Start miner with auto-updater on testnet

pm2 start ./auto-updater.sh --name "autoupdater-miner-test" -- miner 427 miner default 9001 test

---

#### Option B: Manual Setup

If you prefer manual control over the processes:

##### For Miners

```bash

---

# Setup PM2 to start on system boot

pm2 startup
```


*README source used for excerpts: `https://raw.githubusercontent.com/oneoneone-io/subnet-111/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


*Empty — no description bytes set in `SubnetIdentity`.*

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/oneoneone-io/subnet-111](https://github.com/oneoneone-io/subnet-111)
- **Contact:** support@oneoneone.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.003717069 |
| 8103738 | 0.003717061 |
| 8103786 | 0.003716991 |
| 8103834 | 0.003716986 |
| 8103882 | 0.003716972 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Meta / og:description:** A decentralized AI ecosystem built on the Bittensor network that specializes in collecting, validating, and serving high-quality user-generated content from platforms across the web. - oneoneone-io...
- **Fetched from:** [https://github.com/oneoneone-io/subnet-111](https://github.com/oneoneone-io/subnet-111)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

