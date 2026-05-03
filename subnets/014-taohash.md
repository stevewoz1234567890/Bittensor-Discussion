# NetUID 14 — TAOHash (`テ`)

## Overview

TAOHash is a Subnet for decentralizing PoW mining hashrate- rental and financialization. Validators incentivize miners to pool hashrate with them, rewarding them with Alpha based on the value of that hashrate.

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CKhH8nKAhXLmqxwaXzFtVFgxqwwnyckXG8qLpmGtzVJH9Ri`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
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
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `1`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

# Reward System

TAOHash operates two distinct reward mechanisms:

---

## 1. TIDES Protocol (All Miners)

TIDES (Time-based Incentivized Distribution of Earnings System) is a reward protocol that distributes BTC to miners contributing hashpower:
- **No Registration Required**: Any miner can earn TIDES rewards without joining Bittensor. You just have to enter a valid BTC/Lightning address in your username
- **Direct BTC Earnings**: Rewards paid directly in Bitcoin to your configured address
- **Fair Distribution**: BTC distributed proportionally based on share value contributions in the TIDES window
- **Window size**: Uses `network difficulty × 8` for creating the TIDES window. 
- **Performance-Based**: Higher hashrate = high difficulty shares = larger BTC rewards

---

## Miner Requirements

To run a miner with TAOHash rewards, you will need:

- A Bittensor wallet with coldkey and hotkey
- Bitcoin mining hardware (ASICs, GPUs, etc.) OR access to remote hashrate (NiceHash, MiningRigRentals)
- Python 3.9 or higher
- The most recent release of [Bittensor SDK](https://pypi.org/project/bittensor/)
- (Optional, for miner proxy usage): Docker & Docker Compose

See: [TAOHash miner guide](/docs/running_miner.md)

**Related Bittensor Documentation**:

- [Wallets, Coldkeys and Hotkeys in Bittensor](https://docs.learnbittensor.org/getting-started/wallets)
- [Miner registration](./miners/index.md#miner-registration)

---

## Validator Requirements

To run a TAOHash validator, you will need:

- A Bittensor wallet with coldkey and hotkey
- Subnet proxy credentials (provided by subnet maintainers)
- Python 3.9 or higher environment
- The most recent release of [Bittensor SDK](https://pypi.org/project/bittensor/)

See: [TAOHash validator guide](/docs/running_validator.md)

**Related Bittensor Documentation**:
- [Wallets, Coldkeys and Hotkeys in Bittensor](https://docs.learnbittensor.org/getting-started/wallets)
- [Validator registration](./validators/index.md#validator-registration)

---

## Common Setup

These steps apply to both miners and validators:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/latent-to/taohash.git
    cd taohash
    ```

2.  **Set up and activate a Python virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Upgrade pip:**
    ```bash
    pip install --upgrade pip
    ```

4.  **Install the TAOHash package:**
    ```bash
    pip install -e .
    ```

---

## Miner Specific Setup

After completing the common setup, the easiest way to start mining is:

---

### Quick Start (Direct Mining)

1. **Get Mining Pool Credentials**: Run the [`miner.py`](taohash/miner/miner.py) script to fetch your pool information:
   ```bash
   python taohash/miner/miner.py --subtensor.network finney --wallet.name WALLET_NAME --wallet.hotkey WALLET_HOTKEY --btc_address YOUR_BTC_ADDRESS
   ```
   This script will display your unique worker credentials and pool connection details. The username format will be `YOUR_BTC_ADDRESS.WORKER_SUFFIX`.

2. **Configure Your Miners**: Point your mining hardware directly to the subnet pool using the credentials from step 1.

3. **Monitor Your Performance**: Check your statistics at [https://taohash.com/leaderboard](https://taohash.com/leaderboard)

For complete details, see the [TAOHash Miner Setup Guide](docs/running_miner.md).

---

## Validator Specific Setup

After completing the common setup, follow the detailed steps in the Validator Guide:

* [Get subnet proxy credentials from the subnet staff](docs/running_validator.md#1-get-subnet-proxy-credentials)
* [Configure your validator (`.env` file)](docs/running_validator.md#4-configuration)
* [Run the validator (using PM2 recommended)](docs/running_validator.md#5-running-the-validator)

For the complete, step-by-step instructions for setting up and running your validator, please refer to the [TAOHash Validator Setup](docs/running_validator.md).

---

#### CPU / GPU / RAM lines (automatic grep)

*Nothing in this README excerpt matched GPU/VRAM/CPU sizing patterns (`\d+ GB/TB`, `CUDA`, `H100/RTX/…`, `vCPU/cores`). Check **`docs/`**, miner/validator guides linked here, Discord, or the subnet’s homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/latent-to/taohash/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


TAOHash is a Subnet for decentralizing PoW mining hashrate- rental and financialization. Validators incentivize miners to pool hashrate with them, rewarding them with Alpha based on the value of that hashrate.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://taohash.ai/](https://taohash.ai/)
- **GitHub:** [https://github.com/latent-to/taohash](https://github.com/latent-to/taohash)
- **Discord:** [https://discord.gg/wCvqvKJR7P](https://discord.gg/wCvqvKJR7P)
- **Logo URL:** [https://v2-dev.taohash.ai/assets/taohash_logo-4f75d956.png](https://v2-dev.taohash.ai/assets/taohash_logo-4f75d956.png)
- **Contact:** taohash@latent.to

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.009188872 |
| 8103843 | 0.009188861 |
| 8103891 | 0.009188856 |
| 8103939 | 0.009188851 |
| 8103987 | 0.009188845 |
| 8104035 | 0.009188842 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

