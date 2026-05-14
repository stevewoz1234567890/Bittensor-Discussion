# NetUID 19 — blockmachine (`t`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**blockmachine** (NetUID **19**) (`t`).

Harnessing Bittensor's incentive layer to forge self-optimizing infrastructure.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `6`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ37,544.011082627. **Alpha liquidity in pool (`alpha_in`)** = ‎2,671,934.301813635t‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,280,738.750902264t‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.014053925`** *(also **moving-average price** `0.014193728566169739` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,594,234.623190782t‎`. **Owner hotkey / coldkey (chain):** `5CK49hDJcseEk1V7iB1dmmztdw4igafhxLsVN82VtUVAQRfC` / `5FWh37LfVV5LE9dZA91STzbtebh6vxYa3MH71c621sYafo1L`.
- **Subnet registered at block:** `1956072` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎4.526691405t‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000t‎` · α-in `‎0.000000000t‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104429`
- **Liquidity constant `k`:** `100315131039342347945940219145`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `blockmachine` |
| Symbol (API) | `t` |
| Rank | `18` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.014128891` |
| Market cap | `59894670470417.628066886` |
| Market cap Δ 1d | `-1.236055593733386287` |
| Liquidity | `75295213163090` |
| Total τ | `37644040965839` |
| Total α | `4952440052715899` |
| α in pool | `2664835633401922` |
| α staked | `1574327261295024` |
| Price Δ 1h | `-0.010148386537464637` |
| Price Δ 1d | `-1.335345514707494647` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `19` |
| Owner SS58 (API) | `5FWh37LfVV5LE9dZA91STzbtebh6vxYa3MH71c621sYafo1L` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `1956072` |
| Registration wall time | `2023-12-18T13:01:48Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `10` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `12` |
| Max validators (API) | `64` |
| Neuron reg. cost | `100000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `360` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to taostat/blockmachine development by creating an account on GitHub.

**Fetched document title:** GitHub - taostat/blockmachine · GitHub

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
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 3600 |
| Registration recycle cost snapshot (`burn`) | τ0.100000000 |
| Owner SS58 (`owner_ss58`) | `5FWh37LfVV5LE9dZA91STzbtebh6vxYa3MH71c621sYafo1L` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.100000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `3600` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `360` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `True` / `0` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Miners

https://github.com/taostat/blockmachine-miner

---

## Validators

https://github.com/taostat/blockmachine-validator

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/taostat/blockmachine/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/taostat/blockmachine/](https://github.com/taostat/blockmachine/)
- **Logo URL:** [https://blockmachine.io/logo.svg](https://blockmachine.io/logo.svg)
- **Contact:** team@blockmachine.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.014128893 |
| 8104244 | 0.014128861 |
| 8104292 | 0.01412876 |
| 8104340 | 0.014128729 |
| 8104388 | 0.014053932 |
| 8104436 | 0.014053925 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

