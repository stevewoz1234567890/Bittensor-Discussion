# NetUID 113 — TensorUSD (`Ѓ`)

## Overview

**TensorUSD** (NetUID **113**) (`Ѓ`).

A reserve-backed stablecoin designed to support 1:1 redeemability for US Dollar within the Bittensor ecosystem.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `241`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,126.137893771. **Alpha liquidity in pool (`alpha_in`)** = ‎369,920.983901755Ѓ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎939,185.835627897Ѓ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005747938`** *(also **moving-average price** `0.005713406018912792` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎23,862.184590892Ѓ‎`. **Owner hotkey / coldkey (chain):** `5FRumLA6zhL7G72xfojizAeZaTGhAYqw3WQYrq1iusC3M8uB` / `5C85m1bfiEXNW3fP3B5xY5Q9Fhmz5eAxwTk2qezLHenBNezY`.
- **Subnet registered at block:** `7119664` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎156.253337440Ѓ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002873966` · α-out `‎1.000000000Ѓ‎` · α-in `‎0.500000000Ѓ‎`.

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

## Operational parameters — registration, limits, economics (chain)


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
| 8104024 | 0.00572821 |
| 8104072 | 0.005728323 |
| 8104120 | 0.005728419 |
| 8104168 | 0.005748753 |
| 8104216 | 0.005747938 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

