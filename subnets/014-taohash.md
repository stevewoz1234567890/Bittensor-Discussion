# NetUID 14 — TAOHash (`テ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**TAOHash** (NetUID **14**) (`テ`).

TAOHash is a Subnet for decentralizing PoW mining hashrate- rental and financialization. Validators incentivize miners to pool hashrate with them, rewarding them with Alpha based on the value of that hashrate.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `1`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ23,727.876877229. **Alpha liquidity in pool (`alpha_in`)** = ‎2,583,037.236218111ξ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,448,055.774019437ξ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.009188670`** *(also **moving-average price** `0.009189447155222297` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎2,463,284.423455618ξ‎`. **Owner hotkey / coldkey (chain):** `5Cf4LPRv6tiyuFsfLRQaFYEEn3zJRGi4bAE9DwbbKmbCSHpV` / `5CKhH8nKAhXLmqxwaXzFtVFgxqwwnyckXG8qLpmGtzVJH9Ri`.
- **Subnet registered at block:** `4848444` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎0.755309211ξ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000425828` · α-out `‎1.000000000ξ‎` · α-in `‎0.046342824ξ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104434`
- **Liquidity constant `k`:** `61289989510281218452613294419`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `TAOHash`
- **Symbol (API):** `テ`
- **Rank:** `27`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.009188821`
- **Market cap:** `38232414557608.015025147`
- **Market cap Δ 1d:** `0.178742380458604884`
- **Liquidity:** `47462744710244`
- **Total τ:** `23727972420031`
- **Total α:** `5030849183695434`
- **α in pool:** `2583005185345731`
- **α staked:** `1577747816329676`
- **Price Δ 1h:** `-0.000348248034874429`
- **Price Δ 1d:** `0.068118214451167571`
#### Subnet activity (TAOStats)

- **NetUID (API):** `14`
- **Owner SS58 (API):** `5CKhH8nKAhXLmqxwaXzFtVFgxqwwnyckXG8qLpmGtzVJH9Ri`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `4848444`
- **Registration wall time:** `2025-02-03T18:04:24Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `4`
- **Active dual-role:** `1`
- **Emission:** `428786`
- **Max neurons:** `256`
- **Validator slots (metadata):** `11`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


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
| 8104196 | 0.009188822 |
| 8104244 | 0.009188709 |
| 8104292 | 0.009188697 |
| 8104340 | 0.009188676 |
| 8104388 | 0.009188674 |
| 8104436 | 0.00918867 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.009710381 |
| 2026-03-10T23:59:48Z | 7718257 | 0.009703478 |
| 2026-03-11T23:59:48Z | 7725455 | 0.009651389 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.009680399 |
| 2026-03-13T23:59:48Z | 7739841 | 0.009648028 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.009664371 |
| 2026-03-15T23:59:48Z | 7754226 | 0.009650859 |
| 2026-03-16T23:59:48Z | 7761426 | 0.009611244 |
| 2026-03-17T23:59:48Z | 7768619 | 0.009487282 |
| 2026-03-18T23:59:48Z | 7775819 | 0.009339408 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00929754035330721634 |
| 2026-03-20T23:59:48Z | 7790201 | 0.009304435 |
| 2026-03-21T23:59:48Z | 7797398 | 0.009299899 |
| 2026-03-22T23:59:48Z | 7804598 | 0.009311546 |
| 2026-03-23T23:59:48Z | 7811798 | 0.009280997 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00907421544092514243 |
| 2026-03-25T23:59:48Z | 7826196 | 0.00897961 |
| 2026-03-26T23:59:48Z | 7833396 | 0.008999656 |
| 2026-03-27T23:59:48Z | 7840596 | 0.008956859 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.008932274 |
| 2026-03-29T23:59:48Z | 7854902 | 0.008915633 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.008861131 |
| 2026-03-31T23:59:48Z | 7869291 | 0.008920251 |
| 2026-04-01T23:59:48Z | 7876474 | 0.008947474 |
| 2026-04-02T23:59:48Z | 7883622 | 0.008941556 |
| 2026-04-03T23:59:48Z | 7890794 | 0.009276772 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.009275079 |
| 2026-04-05T23:59:48Z | 7905188 | 0.009148631 |
| 2026-04-06T23:59:48Z | 7912388 | 0.009067013 |
| 2026-04-07T23:59:48Z | 7919588 | 0.009142309 |
| 2026-04-08T23:59:48Z | 7926788 | 0.009194422 |
| 2026-04-09T23:59:48Z | 7933987 | 0.009173303 |
| 2026-04-10T23:59:48Z | 7941184 | 0.008894033 |
| 2026-04-11T23:59:48Z | 7948384 | 0.008963757 |
| 2026-04-12T23:59:48Z | 7955584 | 0.008979181 |
| 2026-04-13T23:59:48Z | 7962784 | 0.008877182 |
| 2026-04-14T23:59:48Z | 7969979 | 0.008926893 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.008932053 |
| 2026-04-16T23:59:48Z | 7984379 | 0.009050969 |
| 2026-04-17T23:59:48Z | 7991579 | 0.009078352 |
| 2026-04-18T23:59:48Z | 7998779 | 0.009208104 |
| 2026-04-19T23:59:48Z | 8005979 | 0.00926294 |
| 2026-04-20T23:59:48Z | 8013179 | 0.009208533 |
| 2026-04-21T23:59:48Z | 8020376 | 0.009227806 |
| 2026-04-22T23:59:48Z | 8027562 | 0.009239989 |
| 2026-04-23T23:59:48Z | 8034762 | 0.00924206 |
| 2026-04-24T23:59:48Z | 8041962 | 0.009261723 |
| 2026-04-25T23:59:48Z | 8049151 | 0.009228921 |
| 2026-04-26T23:59:48Z | 8056274 | 0.009261955 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.009222401 |
| 2026-04-28T23:59:48Z | 8070646 | 0.009192881 |
| 2026-04-29T23:59:48Z | 8077790 | 0.009230229 |
| 2026-04-30T23:59:48Z | 8084984 | 0.009230667 |
| 2026-05-01T23:59:48Z | 8092168 | 0.009183431 |
| 2026-05-02T23:59:48Z | 8099357 | 0.009195424 |
| 2026-05-03T16:10:00Z | 8104202 | 0.009188821 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

