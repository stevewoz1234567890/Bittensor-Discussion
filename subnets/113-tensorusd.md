# NetUID 113 — TensorUSD (`Ѓ`)

## Overview

**TensorUSD** (NetUID **113**) (`Ѓ`).

A reserve-backed stablecoin designed to support 1:1 redeemability for US Dollar within the Bittensor ecosystem.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `303`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,126.287209557. **Alpha liquidity in pool (`alpha_in`)** = ‎369,957.006065116Ѓ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎939,234.655591772Ѓ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005747781`** *(also **moving-average price** `0.005713914288207889` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎23,862.307237560Ѓ‎`. **Owner hotkey / coldkey (chain):** `5FRumLA6zhL7G72xfojizAeZaTGhAYqw3WQYrq1iusC3M8uB` / `5C85m1bfiEXNW3fP3B5xY5Q9Fhmz5eAxwTk2qezLHenBNezY`.
- **Subnet registered at block:** `7119664` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎196.452041995Ѓ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002873901` · α-out `‎1.000000000Ѓ‎` · α-in `‎0.500000000Ѓ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005749285`
- **Market cap:** `5326956313179.981519365`
- **Liquidity:** `4252844293915`
- **Total τ:** `2126349966299`
- **Total α:** `1309089044433889`
- **α in pool:** `369871093121322`
- **α staked:** `556671305312567`
- **Price Δ 1h:** `0.38146207457192458`
- **Price Δ 1d:** `2.625486416050837171`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `129`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `2874640`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `1000000`

### On-chain declared purpose *(SubnetIdentity)*

A reserve-backed stablecoin designed to support 1:1 redeemability for US Dollar within the Bittensor ecosystem.

### Repository README excerpt *(everything before first `##` heading)*

# TensorUSD Subnet (SN113)

> **Decentralized liquidation auctions and price oracle for TensorUSD stablecoin on Bittensor**

Miners earn TAO by participating in liquidation auctions and contributing to the price oracle. Validators track on-chain activity and distribute rewards.

📚 **[Documentation](https://docs.tensorusd.com/components/subnet)**

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** A decentralized, 1.5× overcollateralized stablecoin backed by TAO for the Bittensor ecosystem.

**Fetched document title:** TensorUSD (TUSDT) – TAO-Backed Stablecoin for Bittensor

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 129
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.001000000
- **Owner SS58 (`owner_ss58`):** `5C85m1bfiEXNW3fP3B5xY5Q9Fhmz5eAxwTk2qezLHenBNezY`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.001000000 / τ100.000000000
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

### Prerequisites

1. **Python 3.10+** installed
2. **Bittensor wallet** registered on netuid 113
3. **[uv](https://docs.astral.sh/uv/)**
4. **For Miners**: TUSDT tokens + CoinMarketCap API key

---

### Installation

```bash

---

# Install dependencies

uv sync

---

# Install as package

uv pip install -e .

---

# Run database migrations (validators only)

uv run alembic upgrade head
```

---

---

## ⚡ Running a Miner

Miners can participate in **two mechanisms** to earn rewards:

- **Mechanism 0**: Liquidation auctions (bid on undercollateralized vaults)
- **Mechanism 1**: Price oracle (submit TAO/USD prices)

---

### Option 1: Run Both Mechanisms (Recommended)

```bash
uv run neurons/miner.py \
  --netuid 113 \
  --subtensor.network finney \
  --wallet.name my_wallet \
  --wallet.hotkey my_hotkey \
  --mech.ids 0,1 \
  --auction_contract.address 5FHneW46xGXgs5mUiveU4sbTyGBzmstUspZC92UhjJM694ty \
  --vault_contract.address 5CiPPseXPECbkjWca6MnjNokrgYjMqmKndv2rSnekmSK2DjL \
  --tusdt.address 5DAAnrj7VKbSBAiC3R9YJY4g8eZN8DLqr3gZJvJT8qYgL3Nq \
  --oracle_contract.address 5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY \
  --cmc.api_key YOUR_COINMARKETCAP_API_KEY \
  --price.submission_interval_seconds 300 \
  --coldkey.password YOUR_COLDKEY_PASSWORD
```

---

### Using Environment Variables

Create a `.env` file to avoid passing secrets via CLI:

```bash

---

# Required for all miners

WALLET_NAME=my_wallet
WALLET_HOTKEY=my_hotkey

---

## 🔍 Running a Validator

Validators monitor on-chain events and distribute rewards for both mechanisms.

---

### Basic Validator

```bash
uv run neurons/validator.py \
  --netuid 113 \
  --subtensor.network finney \
  --wallet.name validator_wallet \
  --wallet.hotkey validator_hotkey \
  --logging.info \
  --auction_contract.address 5FHneW46xGXgs5mUiveU4sbTyGBzmstUspZC92UhjJM694ty \
  --oracle_contract.address 5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY \
```

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/TensorUSD/subnet/main/README.md`*

## On-chain identity — description


A reserve-backed stablecoin designed to support 1:1 redeemability for US Dollar within the Bittensor ecosystem.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://tensorusd.com](https://tensorusd.com)
- **GitHub:** [https://github.com/TensorUSD/subnet](https://github.com/TensorUSD/subnet)
- **Discord:** [https://discord.com/invite/fAHB6N92Qd](https://discord.com/invite/fAHB6N92Qd)
- **Logo URL:** [https://avatars.githubusercontent.com/u/228006888?s=200&v=4](https://avatars.githubusercontent.com/u/228006888?s=200&v=4)
- **Contact:** admin@tensorusd.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.005728368 |
| 8104133 | 0.005750044 |
| 8104181 | 0.005749232 |
| 8104229 | 0.00574778 |
| 8104277 | 0.005747781 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004671563 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005058133 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005502115 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005289348 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005069708 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005196894 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004962031 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005319586 |
| 2026-03-17T23:59:48Z | 7768619 | 0.0056549 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005397708 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00522774022173944855 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004913076 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005106958 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005316128 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005293694 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00563830687279712201 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005045051 |
| 2026-03-26T23:59:48Z | 7833396 | 0.00477721 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004834083 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004986553 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004995912 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004647421 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004560082 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004450251 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004540028 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004417219 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004555894 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004646383 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004765561 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004803644 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004746172 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004835978 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004771732 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004666572 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004574725 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004890157 |
| 2026-04-14T23:59:48Z | 7969979 | 0.005180245 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004968939 |
| 2026-04-16T23:59:48Z | 7984379 | 0.005206279 |
| 2026-04-17T23:59:48Z | 7991579 | 0.005247536 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004812343 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004853094 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004763958 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004820879 |
| 2026-04-22T23:59:48Z | 8027562 | 0.005059361 |
| 2026-04-23T23:59:48Z | 8034762 | 0.005329179 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004982994 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004985304 |
| 2026-04-26T23:59:48Z | 8056274 | 0.005097709 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.005371839 |
| 2026-04-28T23:59:48Z | 8070646 | 0.005353844 |
| 2026-04-29T23:59:48Z | 8077790 | 0.005390697 |
| 2026-04-30T23:59:48Z | 8084984 | 0.005335215 |
| 2026-05-01T23:59:48Z | 8092168 | 0.005464734 |
| 2026-05-02T23:59:48Z | 8099357 | 0.005672004 |
| 2026-05-03T16:10:00Z | 8104202 | 0.005749285 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

