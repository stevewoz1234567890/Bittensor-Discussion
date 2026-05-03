# NetUID 41 — Almanac (`נ`)

## Overview

Incentivized market intelligence.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

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
- **`immunity_period` (blocks):** 14400
- **Registration recycle cost snapshot (`burn`):** τ0.100000000
- **Owner SS58 (`owner_ss58`):** `5FCSevLkofmKZRixMawp6jyyjBty1AeSCLa7N5Fv892DYkXX`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.100000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `14400` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `950000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

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

*Nothing in this README excerpt matched GPU/VRAM/CPU sizing patterns (`\d+ GB/TB`, `CUDA`, `H100/RTX/…`, `vCPU/cores`). Check **`docs/`**, miner/validator guides linked here, Discord, or the subnet’s homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/sportstensor/sn41/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Incentivized market intelligence.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://almanac.market](https://almanac.market)
- **GitHub:** [https://github.com/sportstensor/sn41](https://github.com/sportstensor/sn41)
- **Logo URL:** [https://beta.almanac.market/assets/favicons/favicon-32x32.png](https://beta.almanac.market/assets/favicons/favicon-32x32.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.005504244 |
| 8103843 | 0.005505935 |
| 8103891 | 0.005506102 |
| 8103939 | 0.005506098 |
| 8103987 | 0.005506095 |
| 8104035 | 0.00550595 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

