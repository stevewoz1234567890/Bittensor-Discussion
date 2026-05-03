# NetUID 80 — dogelayer (`ى`)

## Overview

Dogelayer is the world's first mining pool enabling Scrypt miners to join Bittensor subnet. Our merged mining technology allows traditional miners to earn Alpha tokens through subnet validation while mining LTC/DOGE

more information on website: dogelayer.ai

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 226
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
- **Owner SS58 (`owner_ss58`):** `5ERJCUPWkgEmVDFCcdwMgaBbtEqGmzZnhdqNRcf3W29JsJJs`

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

# Reward System

DogeLayer operates a dual reward mechanism:

---

## 1. Mining Rewards (LTC/DOGE)

Direct cryptocurrency earnings from actual mining with **secondary distribution**:
- **Mining Revenue**: Earn LTC/DOGE from contributing hashpower
- **Platform Collection**: All mining rewards are first collected by the platform
- **Secondary Distribution**: Platform redistributes rewards to miners and validators based on contributions
- **Manual Withdrawal Required**: Both miners and validators must login to DogeLayer website to set withdrawal addresses and submit withdrawal requests
- **Processing Time**: 1-3 business days for withdrawal processing

---

## Miner Requirements

To run a miner with DogeLayer rewards, you will need:

- A Bittensor wallet with coldkey and hotkey
- Scrypt mining hardware (ASICs for LTC/DOGE) OR access to remote hashrate
- Python 3.9 or higher
- The most recent release of [Bittensor SDK](https://pypi.org/project/bittensor/)

**Related Bittensor Documentation**:
- [Wallets, Coldkeys and Hotkeys in Bittensor](https://docs.learnbittensor.org/getting-started/wallets)
- [Miner registration](https://docs.learnbittensor.org/miners/index.md#miner-registration)

---

## Validator Requirements

To run a DogeLayer validator, you will need:

- A Bittensor wallet with coldkey and hotkey
- Subnet proxy configuration (pre-configured, no setup needed)
- Sufficient TAO stake (minimum ~0.5 TAO, recommended 5-10 TAO)
- Python 3.9 or higher environment
- The most recent release of [Bittensor SDK](https://pypi.org/project/bittensor/)
- Docker & Docker Compose (for containerized deployment)

**Related Bittensor Documentation**:
- [Wallets, Coldkeys and Hotkeys in Bittensor](https://docs.learnbittensor.org/getting-started/wallets)
- [Validator registration](https://docs.learnbittensor.org/validators/index.md#validator-registration)

---

---

## Common Setup

These steps apply to both miners and validators:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dogelayer-ai/dogelayer.git
   cd dogelayer
   ```

2. **Set up and activate a Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Upgrade pip:**
   ```bash
   pip install --upgrade pip
   ```

4. **Install the DogeLayer package:**
   ```bash
   pip install -e .
   ```

---

---

## Miner Specific Setup

After completing the common setup:

---

# Create hotkey (used for mining operations)

btcli wallet new_hotkey --wallet.name my_miner --wallet.hotkey default
```

---

### 3. Connect Your Mining Hardware

Use your **48-character hotkey** as the miner username to connect to the mining pool.

**Miner Username Format:**

DogeLayer supports two formats for miner usernames:

1. **Single rig**: Use your full hotkey
   ```
   5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY
   ```

2. **Multiple rigs**: Add a suffix with dot (`.`) separator
   ```
   5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY.worker01
   5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY.rig1
   ```

**Production Environment (Mainnet)**:
- Pool (Primary): `stratum+tcp://sn80-stratum.dogelayer.ai:3331`
- Pool (Backup): `stratum+tcp://stratum.dogelayer.ai:3331`
- Username: Your hotkey or `hotkey.suffix` for multiple rigs
- Password: `x`

**Important:** All rigs with the same hotkey share the same rewards. The suffix is only used to identify individual rigs.

---

### 4. Start Mining

Once connected, your mining hardware will:
- Automatically contribute hashrate to the pool
- Have contributions recorded by validators
- Earn TAO rewards sent to your hotkey
- Accumulate LTC/DOGE rewards for withdrawal

---

## Validator Specific Setup

After completing the common setup:

---

# Create hotkey (used for validator operations)

btcli wallet new_hotkey --wallet.name my_validator --wallet.hotkey default
```

---

### 3. Stake TAO (Required)

Validators need sufficient stake to set weights:

```bash

---

# Stake TAO to your validator

btcli stake add \
  --wallet.name my_validator \
  --wallet.hotkey default \
  --amount 10.0 \
  --subtensor.network finney

---

### 5. Configure Environment

Navigate to the validator directory and create a `.env` file:

```bash
cd dogelayer/validator
cp env.example .env
nano .env
```

Update the `.env` file with your wallet information:

```env

---

# Note: This is a shared API token for all validators

SUBNET_PROXY_API_URL="http://dogelayer-205dd0511d5781e4.elb.ap-southeast-1.amazonaws.com:8889"
SUBNET_PROXY_API_TOKEN="2z1gLMqF6yZuf9G56iCLi5H6lKPMWJ_kgiYp-61…

---

#### CPU / GPU / RAM lines (automatic grep)

*Nothing in this README excerpt matched GPU/VRAM/CPU sizing patterns (`\d+ GB/TB`, `CUDA`, `H100/RTX/…`, `vCPU/cores`). Check **`docs/`**, miner/validator guides linked here, Discord, or the subnet’s homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/dogelayer-ai/dogelayer/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Dogelayer is the world's first mining pool enabling Scrypt miners to join Bittensor subnet. Our merged mining technology allows traditional miners to earn Alpha tokens through subnet validation while mining LTC/DOGE

## On-chain identity — additional field


more information on website: dogelayer.ai

## Registered contact & links


- **Website:** [https://dogelayer.ai](https://dogelayer.ai)
- **GitHub:** [https://github.com/dogelayer-ai/dogelayer](https://github.com/dogelayer-ai/dogelayer)
- **Discord (handle / invite hint):** `dogelayer`
- **Logo URL:** [https://dogelayer.ai/images/design/dogemine-logo.svg](https://dogelayer.ai/images/design/dogemine-logo.svg)
- **Contact:** dev@dogelayer.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.004207927 |
| 8103891 | 0.004207973 |
| 8103939 | 0.00421922 |
| 8103987 | 0.004217976 |
| 8104035 | 0.004232995 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

