# NetUID 77 — Liquidity (`ه`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Liquidity** (NetUID **77**) (`ه`).

Supply liquidity on external chains via uniswap, incentivize any project

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `64`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ9,693.411367439. **Alpha liquidity in pool (`alpha_in`)** = ‎2,326,618.175078917ه‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,157,112.798524279ه‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004167815`** *(also **moving-average price** `0.0041701027657836676` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎299,117.800399751ه‎`. **Owner hotkey / coldkey (chain):** `5DqALXRZumwGDyaJWRJ2fMzBqPxEuoqWypnexcwuYMDdohsE` / `5GxxsUeYRyJSJKCuPeG1jZZiCummHJttmTNsfgDRSfxVnhGi`.
- **Subnet registered at block:** `5128460` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎47.922041604ه‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ه‎` · α-in `‎0.000000000ه‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104371`
- **Liquidity constant `k`:** `22552867066000155548709183563`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Liquidity` |
| Symbol (API) | `ه` |
| Rank | `62` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004168789` |
| Market cap | `18122678977943.710781607` |
| Market cap Δ 1d | `0.030517157017155543` |
| Liquidity | `19392591490248` |
| Total τ | `9694545725067` |
| Total α | `4483497973603196` |
| α in pool | `2326346036026755` |
| α staked | `2020882614294408` |
| Price Δ 1h | `-0.000431778204172081` |
| Price Δ 1d | `-0.135156144633843511` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `77` |
| Owner SS58 (API) | `5GxxsUeYRyJSJKCuPeG1jZZiCummHJttmTNsfgDRSfxVnhGi` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5128460` |
| Registration wall time | `2025-03-14T19:25:36.001Z` |
| Registration cost snapshot | `303154601714` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `12` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `12` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Subnet77 Liquidity Auction & Voting

This project manages a liquidity mining system for the Bittensor ecosystem, where token holders vote on liquidity pools and validators process these votes to set miner weights on subnet 77.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Incentivizing $299,973.26 worth of liquidity on chain via Bittensor

**Fetched document title:** SN77 - Liquidity

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
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5GxxsUeYRyJSJKCuPeG1jZZiCummHJttmTNsfgDRSfxVnhGi` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
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

### Validator (`validator/index.ts`)

- **Weight Fetching**: Retrieves calculated weights from the server
- **On-chain Updates**: Sets miner weights on the Bittensor network
- **Version Management**: Includes automatic version checking and update capabilities

---

# Fill in the required variables (see Environment section below)

```

3. **Query current pool weights**

```bash
bun run pools
```

---

### ⚡ Validators

Validators read weights from the server and periodically push them to subnet 77.

**What you can do:**
- **Run weight calculation**: Process votes and compute final miner weights
- **Submit weights to subnet**: Push calculated weights to the Bittensor network
- **Monitor system health**: Track voting patterns and pool performance

**Key commands:**
```bash

---

# Start the validator (processes votes and submits weights)

just validate

---

# Run in test mode (compute weights but skip submission)

TEST_MODE=true just validate

---

### ⛏️ Miners

Miners provide liquidity to pools and can register their addresses to participate in the system.

**What you can do:**
- **Register your address**: Link your Bittensor public key to an EVM address
- **Provide liquidity**: Add liquidity to pools to earn rewards
- **Monitor earnings**: Track your pool performance and rewards

**Key commands:**
```bash

---

## Environment Variables

Create a `.env` file in the project root. The most important keys are:

```dotenv

---

# VALIDATOR ONLY: used to fetch uniswap v3 LP positions for miners

THEGRAPH_API_KEY=

---

# VALIDATOR ONLY: set to 'true' to run in test mode (weights saved to files, not submitted to network)

TEST_MODE=false

---

# VALIDATOR ONLY: OPT-IN: will automatically git pull when a new minor version is live

AUTO_UPDATE_ENABLED=false
```

*Everything else has sensible defaults or is only required for specific tasks.*

---

### Obtaining required API keys

• **The Graph**: Log in to [Subgraph Studio](https://thegraph.com/studio/apikeys/) → **API Keys** in the sidebar → *Create API Key* → copy the generated token. See the official guide for details ([docs](https://thegraph.com/docs/en/subgraphs/querying/managing-api-keys/)).

---

#### Environment Variables

- `AUTO_UPDATE_ENABLED`: Set to `true` to enable automatic updates (default: `false`)
- `TEST_MODE`: Set to `true` to run in test mode (default: `false`)
- `LOG`: Set to `true` to enable console logging (default: `false`)

---









#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/creativebuilds/sn77/master/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://sn77.xyz](https://sn77.xyz)
- **GitHub:** [https://github.com/creativebuilds/sn77](https://github.com/creativebuilds/sn77)
- **Discord (handle / invite hint):** `CreativeBuilds`
- **Logo URL:** [https://sn77.xyz/assets/Logo.svg](https://sn77.xyz/assets/Logo.svg)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004168778 |
| 8104292 | 0.004168771 |
| 8104340 | 0.004168759 |
| 8104388 | 0.004168692 |
| 8104436 | 0.004167814 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.004110972 --> 0.004949323
    line [0.004891506, 0.004881439, 0.004769115, 0.004757074, 0.004681333, 0.004692115, 0.004622024, 0.004579019, 0.004359043, 0.004328089, 0.0043903688474, 0.004373559, 0.00431876, 0.004329169, 0.004360941, 0.00427561141196, 0.004240442, 0.004186035, 0.004207486, 0.004211843, 0.00421221, 0.004240367, 0.004247088, 0.004204158, 0.004194928, 0.004186496, 0.004202917, 0.004184046, 0.004200497, 0.004217143, 0.004317871, 0.00428924, 0.004345761, 0.004326029, 0.004313416, 0.004306162, 0.004301507, 0.004288034, 0.004287825, 0.004259705, 0.004267121, 0.004251532, 0.004240254, 0.004217726, 0.004235789, 0.004194311, 0.004271752, 0.004275477, 0.004232926, 0.004228973, 0.004211435, 0.004193414, 0.004230735, 0.004175804, 0.004173601, 0.004168789]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

