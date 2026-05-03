# NetUID 116 — TaoLend (`ⴵ`)

## Overview

**TaoLend** (NetUID **116**) (`ⴵ`).

TaoLend is a decentralized lending protocol for the Bittensor ($TAO) ecosystem.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `306`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,664.447166653. **Alpha liquidity in pool (`alpha_in`)** = ‎890,901.064213179ъ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,731,655.996991599ъ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004113042`** *(also **moving-average price** `0.0040591927245259285` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎43,884.492582489ъ‎`. **Owner hotkey / coldkey (chain):** `5FFFjWqpNcu2yweMNaYcya5bq6zRuAAWJsudCyN462nLKhtj` / `5GgjJXbcDyiGenKGfPrPhRxJ7p91EdC22fcAAF4ccbATgu6H`.
- **Subnet registered at block:** `5699219` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎217.747492660ъ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002056522` · α-out `‎1.000000000ъ‎` · α-in `‎0.500000000ъ‎`.

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
| 8104085 | 0.004112729 |
| 8104133 | 0.004112823 |
| 8104181 | 0.004112923 |
| 8104229 | 0.004112972 |
| 8104277 | 0.004113042 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.003891604 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004002175 |
| 2026-03-11T23:59:48Z | 7725455 | 0.004232136 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.004359964 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004072252 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004077209 |
| 2026-03-15T23:59:48Z | 7754226 | 0.00390888 |
| 2026-03-16T23:59:48Z | 7761426 | 0.003893888 |
| 2026-03-17T23:59:48Z | 7768619 | 0.003834026 |
| 2026-03-18T23:59:48Z | 7775819 | 0.003669153 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00366914828954794521 |
| 2026-03-20T23:59:48Z | 7790201 | 0.003688948 |
| 2026-03-21T23:59:48Z | 7797398 | 0.003767131 |
| 2026-03-22T23:59:48Z | 7804598 | 0.003800576 |
| 2026-03-23T23:59:48Z | 7811798 | 0.003844143 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00385020895647993514 |
| 2026-03-25T23:59:48Z | 7826196 | 0.003740848 |
| 2026-03-26T23:59:48Z | 7833396 | 0.003608283 |
| 2026-03-27T23:59:48Z | 7840596 | 0.003594411 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.003668794 |
| 2026-03-29T23:59:48Z | 7854902 | 0.003712866 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.00365265 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003667979 |
| 2026-04-01T23:59:48Z | 7876474 | 0.003687838 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003687826 |
| 2026-04-03T23:59:48Z | 7890794 | 0.003686951 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.003727075 |
| 2026-04-05T23:59:48Z | 7905188 | 0.003720969 |
| 2026-04-06T23:59:48Z | 7912388 | 0.003775407 |
| 2026-04-07T23:59:48Z | 7919588 | 0.003762101 |
| 2026-04-08T23:59:48Z | 7926788 | 0.003627645 |
| 2026-04-09T23:59:48Z | 7933987 | 0.00357732 |
| 2026-04-10T23:59:48Z | 7941184 | 0.003651722 |
| 2026-04-11T23:59:48Z | 7948384 | 0.003644198 |
| 2026-04-12T23:59:48Z | 7955584 | 0.003607883 |
| 2026-04-13T23:59:48Z | 7962784 | 0.00358766 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003634473 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.00359481 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003670028 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003658789 |
| 2026-04-18T23:59:48Z | 7998779 | 0.003693944 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003725337 |
| 2026-04-20T23:59:48Z | 8013179 | 0.003685564 |
| 2026-04-21T23:59:48Z | 8020376 | 0.003674143 |
| 2026-04-22T23:59:48Z | 8027562 | 0.003650747 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003644254 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003625527 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003605104 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003604287 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.003589571 |
| 2026-04-28T23:59:48Z | 8070646 | 0.003622355 |
| 2026-04-29T23:59:48Z | 8077790 | 0.003731774 |
| 2026-04-30T23:59:48Z | 8084984 | 0.003901594 |
| 2026-05-01T23:59:48Z | 8092168 | 0.003853916 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004144309 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004112943 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

