# NetUID 41 — Almanac (`נ`)

## Overview

**Almanac** (NetUID **41**) (`נ`).

Incentivized market intelligence.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `231`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ12,687.684412025. **Alpha liquidity in pool (`alpha_in`)** = ‎2,325,265.263994060נ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,358,226.343371276נ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005544657`** *(also **moving-average price** `0.005521135870367289` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,508,366.943422793נ‎`. **Owner hotkey / coldkey (chain):** `5FCSevLkofmKZRixMawp6jyyjBty1AeSCLa7N5Fv892DYkXX` / `5FCSevLkofmKZRixMawp6jyyjBty1AeSCLa7N5Fv892DYkXX`.
- **Subnet registered at block:** `3394182` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎173.552087200נ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000נ‎` · α-in `‎0.000000000נ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005544678`
- **Market cap:** `22241404773787.113967236`
- **Liquidity:** `25580531565354`
- **Total τ:** `12687708552604`
- **Total α:** `4683416607365336`
- **α in pool:** `2325260910146761`
- **α staked:** `1686045927470701`
- **Price Δ 1h:** `0.700641107135722199`
- **Price Δ 1d:** `1.330883462899412155`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `33`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `10`
- **Neuron reg. cost:** `100000000`

### On-chain declared purpose *(SubnetIdentity)*

Incentivized market intelligence.

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">


</div>

- [Introduction](#introduction)
- [How it Works](#how-it-works)
- [Miner and Validator Functionality](#miner-and-validator-functionality)
  - [Miner](#miner)
  - [Validator](#validator)
- [Miner setup and running Validators](#miner-setup-and-running-validators)
  - [Setting up a Miner](#setting-up-a-miner)
  - [Running a Validator](#running-a-validator)
- [Community](#community)
- [License](#license)

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Prediction markets have earned a reputation for accurate forecasting—but that accuracy mostly shows up in the final hours before resolution. Almanac rewards traders for being right early, when the signal matters most.

**Fetched document title:** Almanac — Accurate Before It's Obvious

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

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/sportstensor/sn41/main/README.md`*

## On-chain identity — description


Incentivized market intelligence.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://almanac.market](https://almanac.market)
- **GitHub:** [https://github.com/sportstensor/sn41](https://github.com/sportstensor/sn41)
- **Logo URL:** [https://beta.almanac.market/assets/favicons/favicon-32x32.png](https://beta.almanac.market/assets/favicons/favicon-32x32.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.005505946 |
| 8104133 | 0.005548522 |
| 8104181 | 0.005542121 |
| 8104229 | 0.005544667 |
| 8104277 | 0.005544657 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.006921663 |
| 2026-03-10T23:59:48Z | 7718257 | 0.006837564 |
| 2026-03-11T23:59:48Z | 7725455 | 0.006657613 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.006529178 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005842807 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.006061421 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005759046 |
| 2026-03-16T23:59:48Z | 7761426 | 0.006120611 |
| 2026-03-17T23:59:48Z | 7768619 | 0.006086136 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005596983 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00555405685249725572 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005569424 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005530618 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005462552 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005478163 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00519559048540589115 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005022574 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004991898 |
| 2026-03-27T23:59:48Z | 7840596 | 0.005265351 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005323737 |
| 2026-03-29T23:59:48Z | 7854902 | 0.005338547 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.005321139 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005568169 |
| 2026-04-01T23:59:48Z | 7876474 | 0.00554238 |
| 2026-04-02T23:59:48Z | 7883622 | 0.005656892 |
| 2026-04-03T23:59:48Z | 7890794 | 0.00558049 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.005595502 |
| 2026-04-05T23:59:48Z | 7905188 | 0.005674793 |
| 2026-04-06T23:59:48Z | 7912388 | 0.005707194 |
| 2026-04-07T23:59:48Z | 7919588 | 0.005661819 |
| 2026-04-08T23:59:48Z | 7926788 | 0.005761597 |
| 2026-04-09T23:59:48Z | 7933987 | 0.005709483 |
| 2026-04-10T23:59:48Z | 7941184 | 0.005501231 |
| 2026-04-11T23:59:48Z | 7948384 | 0.005462665 |
| 2026-04-12T23:59:48Z | 7955584 | 0.005475551 |
| 2026-04-13T23:59:48Z | 7962784 | 0.005518838 |
| 2026-04-14T23:59:48Z | 7969979 | 0.005475905 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.005345915 |
| 2026-04-16T23:59:48Z | 7984379 | 0.005437412 |
| 2026-04-17T23:59:48Z | 7991579 | 0.005380248 |
| 2026-04-18T23:59:48Z | 7998779 | 0.005414431 |
| 2026-04-19T23:59:48Z | 8005979 | 0.005419482 |
| 2026-04-20T23:59:48Z | 8013179 | 0.005421029 |
| 2026-04-21T23:59:48Z | 8020376 | 0.005449146 |
| 2026-04-22T23:59:48Z | 8027562 | 0.00531954 |
| 2026-04-23T23:59:48Z | 8034762 | 0.005427847 |
| 2026-04-24T23:59:48Z | 8041962 | 0.00541606 |
| 2026-04-25T23:59:48Z | 8049151 | 0.005402304 |
| 2026-04-26T23:59:48Z | 8056274 | 0.005444767 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.005443698 |
| 2026-04-28T23:59:48Z | 8070646 | 0.005521808 |
| 2026-04-29T23:59:48Z | 8077790 | 0.005588016 |
| 2026-04-30T23:59:48Z | 8084984 | 0.005721859 |
| 2026-05-01T23:59:48Z | 8092168 | 0.005690019 |
| 2026-05-02T23:59:48Z | 8099357 | 0.005499917 |
| 2026-05-03T16:10:00Z | 8104202 | 0.005544678 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

