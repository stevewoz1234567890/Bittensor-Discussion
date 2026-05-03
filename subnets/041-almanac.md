# NetUID 41 — Almanac (`נ`)

## Overview

Incentivized market intelligence.

**From crawled page (site or GitHub):** Prediction markets have earned a reputation for accurate forecasting—but that accuracy mostly shows up in the final hours before resolution. Almanac rewards traders for being right early, when the signal matters most.

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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/sportstensor/sn41/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

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
| 8103642 | 0.005504287 |
| 8103690 | 0.005504278 |
| 8103738 | 0.005504273 |
| 8103786 | 0.005504244 |
| 8103834 | 0.005504241 |
| 8103882 | 0.005506102 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Almanac — Accurate Before It's Obvious
- **Meta / og:description:** Prediction markets have earned a reputation for accurate forecasting—but that accuracy mostly shows up in the final hours before resolution. Almanac rewards traders for being right early, when the signal matters most.
- **Fetched from:** [https://almanac.market](https://almanac.market)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

