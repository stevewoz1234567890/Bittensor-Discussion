# NetUID 113 — TensorUSD (`Ѓ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**TensorUSD** (NetUID **113**) (`Ѓ`).

A reserve-backed stablecoin designed to support 1:1 redeemability for US Dollar within the Bittensor ecosystem.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `100`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,125.152958686. **Alpha liquidity in pool (`alpha_in`)** = ‎370,312.469690011Ѓ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎939,095.845139515Ѓ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005739207`** *(also **moving-average price** `0.005714956670999527` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎23,864.128767137Ѓ‎`. **Owner hotkey / coldkey (chain):** `5FRumLA6zhL7G72xfojizAeZaTGhAYqw3WQYrq1iusC3M8uB` / `5C85m1bfiEXNW3fP3B5xY5Q9Fhmz5eAxwTk2qezLHenBNezY`.
- **Subnet registered at block:** `7119664` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎64.838541003Ѓ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002869601` · α-out `‎1.000000000Ѓ‎` · α-in `‎0.500000000Ѓ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104335`
- **Liquidity constant `k`:** `786970640600046573909885546`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `TensorUSD` |
| Symbol (API) | `Ѓ` |
| Rank | `108` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.005749285` |
| Market cap | `5326956313179.981519365` |
| Market cap Δ 1d | `3.370211780766819089` |
| Liquidity | `4252844293915` |
| Total τ | `2126349966299` |
| Total α | `1309089044433889` |
| α in pool | `369871093121322` |
| α staked | `556671305312567` |
| Price Δ 1h | `0.38146207457192458` |
| Price Δ 1d | `2.625486416050837171` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `113` |
| Owner SS58 (API) | `5C85m1bfiEXNW3fP3B5xY5Q9Fhmz5eAxwTk2qezLHenBNezY` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7119664` |
| Registration wall time | `2025-12-17T17:51:00.001Z` |
| Registration cost snapshot | `248370924615` |
| Active keys | `129` |
| Active validators | `13` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `2874640` |
| Max neurons | `256` |
| Validator slots (metadata) | `13` |
| Max validators (API) | `64` |
| Neuron reg. cost | `1000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

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


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 129 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.001000000 |
| Owner SS58 (`owner_ss58`) | `5C85m1bfiEXNW3fP3B5xY5Q9Fhmz5eAxwTk2qezLHenBNezY` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.001000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


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
| 8104244 | 0.00574779 |
| 8104292 | 0.005747809 |
| 8104340 | 0.005738887 |
| 8104388 | 0.005739059 |
| 8104436 | 0.005739211 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.004310654 --> 0.00585585
    line [0.004671563, 0.005058133, 0.005502115, 0.005289348, 0.005069708, 0.005196894, 0.004962031, 0.005319586, 0.0056549, 0.005397708, 0.00522774022174, 0.004913076, 0.005106958, 0.005316128, 0.005293694, 0.0056383068728, 0.005045051, 0.00477721, 0.004834083, 0.004986553, 0.004995912, 0.004647421, 0.004560082, 0.004450251, 0.004540028, 0.004417219, 0.004555894, 0.004646383, 0.004765561, 0.004803644, 0.004746172, 0.004835978, 0.004771732, 0.004666572, 0.004574725, 0.004890157, 0.005180245, 0.004968939, 0.005206279, 0.005247536, 0.004812343, 0.004853094, 0.004763958, 0.004820879, 0.005059361, 0.005329179, 0.004982994, 0.004985304, 0.005097709, 0.005371839, 0.005353844, 0.005390697, 0.005335215, 0.005464734, 0.005672004, 0.005749285]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

