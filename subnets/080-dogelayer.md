# NetUID 80 — dogelayer (`ى`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**dogelayer** (NetUID **80**) (`ى`).

Dogelayer is the world's first mining pool enabling Scrypt miners to join Bittensor subnet. Our merged mining technology allows traditional miners to earn Alpha tokens through subnet validation while mining LTC/DOGE



#### SubnetIdentity `additional` *(chain)*



more information on website: dogelayer.ai

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `67`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,128.983569658. **Alpha liquidity in pool (`alpha_in`)** = ‎267,035.943740684ى‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎895,982.733194709ى‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004228445`** *(also **moving-average price** `0.004045746987685561` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎19,287.133454401ى‎`. **Owner hotkey / coldkey (chain):** `5HTwtytUfeUhK4p8NRCGppjUZrhJ5ckoRHeVWEQafg2N1Zo6` / `5ERJCUPWkgEmVDFCcdwMgaBbtEqGmzZnhdqNRcf3W29JsJJs`.
- **Subnet registered at block:** `7151800` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎42.642587839ى‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002114221` · α-out `‎1.000000000ى‎` · α-in `‎0.500000000ى‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104368`
- **Liquidity constant `k`:** `301479192991350283802566072`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `dogelayer`
- **Symbol (API):** `ى`
- **Rank:** `112`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004233121`
- **Market cap:** `4744404005505.835053295`
- **Market cap Δ 1d:** `8.135438562701952393`
- **Liquidity:** `2258392716621`
- **Total τ:** `1129115695064`
- **Total α:** `1162686394583431`
- **α in pool:** `266771732146962`
- **α staked:** `854009839063933`
- **Price Δ 1h:** `0.597914286753132931`
- **Price Δ 1d:** `7.129568915142292497`
#### Subnet activity (TAOStats)

- **NetUID (API):** `80`
- **Owner SS58 (API):** `5ERJCUPWkgEmVDFCcdwMgaBbtEqGmzZnhdqNRcf3W29JsJJs`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `7151800`
- **Registration wall time:** `2025-12-22T05:00:24Z`
- **Registration cost snapshot:** `219601306590`
- **Active keys:** `226`
- **Active validators:** `15`
- **Active miners:** `9`
- **Active dual-role:** `0`
- **Emission:** `2116561`
- **Max neurons:** `256`
- **Validator slots (metadata):** `15`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **DogeLayer** ![Subnet 80](https://img.shields.io/badge/Subnet-80-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Bittensor](https://img.shields.io/badge/bittensor-9.10.1-blue.svg)](https://github.com/opentensor/bittensor)

</div>

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** The world's first mining pool enabling Scrypt miners to join Bittensor subnet.

**Fetched document title:** DogeLayer - Triple Mining, Triple Rewards

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

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/dogelayer-ai/dogelayer/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://dogelayer.ai](https://dogelayer.ai)
- **GitHub:** [https://github.com/dogelayer-ai/dogelayer](https://github.com/dogelayer-ai/dogelayer)
- **Discord (handle / invite hint):** `dogelayer`
- **Logo URL:** [https://dogelayer.ai/images/design/dogemine-logo.svg](https://dogelayer.ai/images/design/dogemine-logo.svg)
- **Contact:** dev@dogelayer.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004232945 |
| 8104292 | 0.004232877 |
| 8104340 | 0.00422143 |
| 8104388 | 0.004228997 |
| 8104436 | 0.004228447 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.00572947 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005637162 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005843639 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005915901 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005140843 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005711558 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005222098 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005971515 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005760234 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005250571 |
| 2026-03-19T23:59:48Z | 7783014 | 0.0052905346307125625 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005222645 |
| 2026-03-21T23:59:48Z | 7797398 | 0.00546566 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005442759 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005311762 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00559862306861555322 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005236313 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004996679 |
| 2026-03-27T23:59:48Z | 7840596 | 0.005229987 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005245412 |
| 2026-03-29T23:59:48Z | 7854902 | 0.005106814 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004903511 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004475897 |
| 2026-04-01T23:59:48Z | 7876474 | 0.00404258 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003769896 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004114455 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004402595 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004377959 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004209221 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004427954 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004453176 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003894437 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004210731 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004218726 |
| 2026-04-12T23:59:48Z | 7955584 | 0.00405437 |
| 2026-04-13T23:59:48Z | 7962784 | 0.003858155 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003998488 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.003790649 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003698045 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003779927 |
| 2026-04-18T23:59:48Z | 7998779 | 0.003715389 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003617488 |
| 2026-04-20T23:59:48Z | 8013179 | 0.003667557 |
| 2026-04-21T23:59:48Z | 8020376 | 0.003632892 |
| 2026-04-22T23:59:48Z | 8027562 | 0.003934187 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003911904 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003705195 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003730627 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003764611 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.003805854 |
| 2026-04-28T23:59:48Z | 8070646 | 0.003721812 |
| 2026-04-29T23:59:48Z | 8077790 | 0.003853635 |
| 2026-04-30T23:59:48Z | 8084984 | 0.003819666 |
| 2026-05-01T23:59:48Z | 8092168 | 0.003980316 |
| 2026-05-02T23:59:48Z | 8099357 | 0.003991107 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004233121 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

