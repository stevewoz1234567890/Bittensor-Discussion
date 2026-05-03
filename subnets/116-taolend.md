# NetUID 116 — TaoLend (`ⴵ`)

## Overview

**TaoLend** (NetUID **116**) (`ⴵ`).

TaoLend is a decentralized lending protocol for the Bittensor ($TAO) ecosystem.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `244`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,664.288496816. **Alpha liquidity in pool (`alpha_in`)** = ‎890,877.641805981ъ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,731,601.835544499ъ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004112974`** *(also **moving-average price** `0.004058305872604251` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎43,884.396935877ъ‎`. **Owner hotkey / coldkey (chain):** `5FFFjWqpNcu2yweMNaYcya5bq6zRuAAWJsudCyN462nLKhtj` / `5GgjJXbcDyiGenKGfPrPhRxJ7p91EdC22fcAAF4ccbATgu6H`.
- **Subnet registered at block:** `5699219` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎173.628578016ъ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002056485` · α-out `‎1.000000000ъ‎` · α-in `‎0.500000000ъ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004112943`
- **Market cap:** `10004530514074.753492035`
- **Liquidity:** `7328363989135`
- **Total τ:** `3664248759613`
- **Total α:** `2622463225648214`
- **α in pool:** `890874303271902`
- **α staked:** `1541576259275343`
- **Price Δ 1h:** `0.027043913040200339`
- **Price Δ 1d:** `4.219147550055911193`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `4`
- **Active dual:** `0`
- **Emission:** `2056468`
- **Max neurons:** `256`
- **Validators (metadata):** `11`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

TaoLend is a decentralized lending protocol for the Bittensor ($TAO) ecosystem.It allows users to lend TAO with confidence while borrowers secure their loans using subnet ALPHA as collateral.By unlocking TAO liquidity and keeping ALPHA staked within the subnet, TaoLend strengthens both capital efficiency and network security.

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# TaoLend

**A Decentralized TAO Lending Protocol on Bittensor**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Solidity](https://img.shields.io/badge/Solidity-^0.8.24-orange.svg)](https://soliditylang.org/)
[![Subnet](https://img.shields.io/badge/Bittensor-SN116-purple.svg)](https://taostats.io/subnets/netuid-116/)

</div>

---

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** Taolend

## Operational parameters — registration, limits, economics (chain)


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
- **`immunity_period` (blocks):** 360
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GgjJXbcDyiGenKGfPrPhRxJ7p91EdC22fcAAF4ccbATgu6H`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `360` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `1000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `500000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## ⛏️ Mining Rewards

TaoLend incentivizes actual trading activity by distributing ALPHA rewards to market participants:

---

### Prerequisites

Install NodeJS (latest LTS version) and PM2:

```bash

---

# Install build essentials

sudo apt install build-essential libssl-dev git

---

# Install NVM (Node Version Manager)

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
source ~/.bashrc

---

# Install NodeJS (latest LTS version)

nvm install --lts
nvm use --lts

---

# Install TypeScript and PM2

npm install -g typescript ts-node pm2
```

---

### Installation

Download code and install dependencies:

```bash

---

# Install Python dependencies

pip install -r requirement.txt
```

---

### Running Validator

Start validator with auto-upgrade:

```bash
pm2 start --name sn116-auto-upgrade python3 -- start_validator.py \
  --wallet.name <your_wallet_name> \
  --wallet.hotkey <your_hotkey>
```

**Parameters**:
- `--wallet.name`: Your Bittensor wallet name
- `--wallet.hotkey`: Your validator hotkey

**Monitoring**:
```bash

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/xpenlab/taolend/main/README.md`*

## On-chain identity — description


TaoLend is a decentralized lending protocol for the Bittensor ($TAO) ecosystem.It allows users to lend TAO with confidence while borrowers secure their loans using subnet ALPHA as collateral.By unlocking TAO liquidity and keeping ALPHA staked within the subnet, TaoLend strengthens both capital efficiency and network security.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://taolend.io](https://taolend.io)
- **GitHub:** [https://github.com/xpenlab/taolend](https://github.com/xpenlab/taolend)
- **Discord:** [https://discord.gg/DNeq2fWCQW](https://discord.gg/DNeq2fWCQW)
- **Logo URL:** [https://raw.githubusercontent.com/xpenlab/taolend/logo/TaoLend.png](https://raw.githubusercontent.com/xpenlab/taolend/logo/TaoLend.png)
- **Contact:** elsieyy@taolend.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.004112604 |
| 8104072 | 0.004112701 |
| 8104120 | 0.004112797 |
| 8104168 | 0.004112895 |
| 8104216 | 0.004112974 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

