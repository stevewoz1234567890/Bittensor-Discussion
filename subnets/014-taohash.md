# NetUID 14 — TAOHash (`テ`)

## Overview

**TAOHash** (NetUID **14**) (`テ`).

TAOHash is a Subnet for decentralizing PoW mining hashrate- rental and financialization.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `204`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ23,727.847231408. **Alpha liquidity in pool (`alpha_in`)** = ‎2,583,025.806685823ξ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,447,901.875615303ξ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.009188699`** *(also **moving-average price** `0.009189520729705691` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎2,463,284.385767459ξ‎`. **Owner hotkey / coldkey (chain):** `5Cf4LPRv6tiyuFsfLRQaFYEEn3zJRGi4bAE9DwbbKmbCSHpV` / `5CKhH8nKAhXLmqxwaXzFtVFgxqwwnyckXG8qLpmGtzVJH9Ri`.
- **Subnet registered at block:** `4848444` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎154.081860110ξ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000426193` · α-out `‎1.000000000ξ‎` · α-in `‎0.046382344ξ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.009188821`
- **Market cap:** `38232414557608.015025147`
- **Liquidity:** `47462744710244`
- **Total τ:** `23727972420031`
- **Total α:** `5030849183695434`
- **α in pool:** `2583005185345731`
- **α staked:** `1577747816329676`
- **Price Δ 1h:** `-0.000348248034874429`
- **Price Δ 1d:** `0.068118214451167571`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `4`
- **Active dual:** `1`
- **Emission:** `428786`
- **Max neurons:** `256`
- **Validators (metadata):** `11`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

TAOHash is a Subnet for decentralizing PoW mining hashrate- rental and financialization. Validators incentivize miners to pool hashrate with them, rewarding them with Alpha based on the value of that hashrate.

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **TAOHash** ![Subnet 14](https://img.shields.io/badge/Subnet-14_%CE%BE-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/latent-to/taohash)

</div>

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Incentivizing Hashrate - Powered by Subnet 14 on Bittensor

**Fetched document title:** TAOHash - Bitcoin Mining

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

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/latent-to/taohash/main/README.md`*

## On-chain identity — description


TAOHash is a Subnet for decentralizing PoW mining hashrate- rental and financialization. Validators incentivize miners to pool hashrate with them, rewarding them with Alpha based on the value of that hashrate.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://taohash.ai/](https://taohash.ai/)
- **GitHub:** [https://github.com/latent-to/taohash](https://github.com/latent-to/taohash)
- **Discord:** [https://discord.gg/wCvqvKJR7P](https://discord.gg/wCvqvKJR7P)
- **Logo URL:** [https://v2-dev.taohash.ai/assets/taohash_logo-4f75d956.png](https://v2-dev.taohash.ai/assets/taohash_logo-4f75d956.png)
- **Contact:** taohash@latent.to

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104037 | 0.00918884 |
| 8104085 | 0.009188836 |
| 8104133 | 0.009188828 |
| 8104181 | 0.009188823 |
| 8104229 | 0.009188806 |
| 8104277 | 0.009188699 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

