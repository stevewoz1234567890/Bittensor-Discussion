# NetUID 106 — VoidAI (`Դ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**VoidAI** (NetUID **106**) (`Դ`).

Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `93`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,610.155464054. **Alpha liquidity in pool (`alpha_in`)** = ‎1,853,344.087452605Դ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,972,598.147252910Դ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004122369`** *(also **moving-average price** `0.0041194765362888575` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎294,788.599512976Դ‎`. **Owner hotkey / coldkey (chain):** `5D7FVSM1fJM56zHJuMBuQ5LH32mkLni52JonoeppFrezvyHy` / `5E5Ctr2D9SjvLwNn45UNhBpjuQ7QWuinMqpAXY1ueRfJr5PT`.
- **Subnet registered at block:** `5558480` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎68.722929363Դ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Դ‎` · α-in `‎0.000000000Դ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104342`
- **Liquidity constant `k`:** `14104236633899616362506160670`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `VoidAI` |
| Symbol (API) | `Դ` |
| Rank | `84` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004122417` |
| Market cap | `13284750341513.167188945` |
| Market cap Δ 1d | `0.221740204973191594` |
| Liquidity | `15250412636598` |
| Total τ | `7610200884574` |
| Total α | `3825709234705515` |
| α in pool | `1853333069416388` |
| α staked | `1369230378559197` |
| Price Δ 1h | `0.031957487078692582` |
| Price Δ 1d | `0.089882402642571773` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `106` |
| Owner SS58 (API) | `5E5Ctr2D9SjvLwNn45UNhBpjuQ7QWuinMqpAXY1ueRfJr5PT` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5558480` |
| Registration wall time | `2025-05-13T12:49:36Z` |
| Registration cost snapshot | `133585556570` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `1` |
| Active dual-role | `1` |
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

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP - v0idai/SN106

**Fetched document title:** GitHub - v0idai/SN106: Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP · GitHub

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
| Owner SS58 (`owner_ss58`) | `5E5Ctr2D9SjvLwNn45UNhBpjuQ7QWuinMqpAXY1ueRfJr5PT` |


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

#### Minimum Specifications

- **CPU**: 4 cores 
- **RAM**: 8GB RAM
- **Storage**: 50GB+ SSD storage
- **Network**: Stable internet connection (50+ Mbps)
- **OS**: Linux (Ubuntu 20.04+ recommended), macOS, or Windows

---

#### Recommended Specifications

- **CPU**: 8 cores 
- **RAM**: 16GB RAM
- **Storage**: 100GB+  SSD
- **Network**: High-speed internet (100+ Mbps)
- **OS**: Linux (Ubuntu 22.04 LTS)

---

#### Required Software

- **Node.js**: v18.0.0 or higher
- **npm**: v8.0.0 or higher
- **Git**: Latest version

---

#### 2. Install Dependencies

```bash
npm install
```

---

#### 3. Configure Environment

```bash

---

# Copy environment template

cp .env.example .env

---

# Edit environment variables

nano .env
```

---

#### 4. Required Environment Variables

```bash

---

#### 5. Run the Validator

```bash

---

# Start the validator

npm run validator

```

---

### What the Validator Does

1. **Data Collection**: Fetches NFT liquidity positions from enabled chains
2. **Performance Analysis**: Calculates current tick data and position quality (only in-range positions get rewards)
3. **Weight Calculation**: Determines miner weights based on position quality and subnet performance
4. **Weight Submission**: Submits calculated weights to the BitTensor network every 20 minutes
5. **Distribution Policy**: Burn disabled (0%). 100% of weight is allocated to miners; UID 0 receives 0 units.

---

#### CPU / GPU / RAM lines (automatic grep)

- - **CPU**: 4 cores
- - **RAM**: 8GB RAM
- - **Storage**: 50GB+ SSD storage
- - **CPU**: 8 cores
- - **RAM**: 16GB RAM
- - **Storage**: 100GB+  SSD


*Primary README URL used: `https://raw.githubusercontent.com/v0idai/SN106/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/v0idai/SN106](https://github.com/v0idai/SN106)
- **Discord:** [https://discord.gg/Qu8gGDJETB](https://discord.gg/Qu8gGDJETB)
- **Contact:** voidai7777@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004122401 |
| 8104292 | 0.004122391 |
| 8104340 | 0.004122375 |
| 8104388 | 0.004122374 |
| 8104436 | 0.004122368 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

