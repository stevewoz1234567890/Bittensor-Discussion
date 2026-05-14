# NetUID 116 — TaoLend (`ⴵ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**TaoLend** (NetUID **116**) (`ⴵ`).

TaoLend is a decentralized lending protocol for the Bittensor ($TAO) ecosystem.It allows users to lend TAO with confidence while borrowers secure their loans using subnet ALPHA as collateral.By unlocking TAO liquidity and keeping ALPHA staked within the subnet, TaoLend strengthens both capital efficiency and network security.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `103`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,664.902458236. **Alpha liquidity in pool (`alpha_in`)** = ‎890,948.358103387ъ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,731,806.821508213ъ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004113335`** *(also **moving-average price** `0.004061349667608738` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎43,886.681458266ъ‎`. **Owner hotkey / coldkey (chain):** `5FFFjWqpNcu2yweMNaYcya5bq6zRuAAWJsudCyN462nLKhtj` / `5GgjJXbcDyiGenKGfPrPhRxJ7p91EdC22fcAAF4ccbATgu6H`.
- **Subnet registered at block:** `5699219` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎73.295247161ъ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002056666` · α-out `‎1.000000000ъ‎` · α-in `‎0.500000000ъ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104332`
- **Liquidity constant `k`:** `3265238827774431046937645332`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `TaoLend` |
| Symbol (API) | `ⴵ` |
| Rank | `97` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004112943` |
| Market cap | `10004530514074.753492035` |
| Market cap Δ 1d | `4.604642682738308506` |
| Liquidity | `7328363989135` |
| Total τ | `3664248759613` |
| Total α | `2622463225648214` |
| α in pool | `890874303271902` |
| α staked | `1541576259275343` |
| Price Δ 1h | `0.027043913040200339` |
| Price Δ 1d | `4.219147550055911193` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `116` |
| Owner SS58 (API) | `5GgjJXbcDyiGenKGfPrPhRxJ7p91EdC22fcAAF4ccbATgu6H` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5699219` |
| Registration wall time | `2025-06-03T09:58:48Z` |
| Registration cost snapshot | `89944262256` |
| Active keys | `256` |
| Active validators | `11` |
| Active miners | `4` |
| Active dual-role | `0` |
| Emission | `2056468` |
| Max neurons | `256` |
| Validator slots (metadata) | `11` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `1000` |

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
| `immunity_period` (blocks) | 360 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5GgjJXbcDyiGenKGfPrPhRxJ7p91EdC22fcAAF4ccbATgu6H` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `360` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `1000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `500000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


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
| 8104244 | 0.004112998 |
| 8104292 | 0.004110829 |
| 8104340 | 0.004110892 |
| 8104388 | 0.004113241 |
| 8104436 | 0.004113337 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

