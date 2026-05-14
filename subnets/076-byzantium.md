# NetUID 76 — Byzantium (`ن`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Byzantium** (NetUID **76**) (`ن`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `63`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,119.261523035. **Alpha liquidity in pool (`alpha_in`)** = ‎144,632.356641176ن‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎518,597.250281199ن‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007737942`** *(also **moving-average price** `0.007501866202801466` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎17,912.019385751ن‎`. **Owner hotkey / coldkey (chain):** `5Cw4E2tJjsx1mxGaxpJHEAS9fEgjZQt7r7DeHhZ1Ce6yu5cs` / `5FFNhWd881QTWuuiDgkqW4vgiWFDW1QYqPwRB9MZUkH7cMUP`.
- **Subnet registered at block:** `7574784` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎36.497786336ن‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003868967` · α-out `‎1.000000000ن‎` · α-in `‎0.500000000ن‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104372`
- **Liquidity constant `k`:** `161881431774343946753489160`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Byzantium` |
| Symbol (API) | `ن` |
| Rank | `119` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.007744613` |
| Market cap | `3482081698906.170903463` |
| Market cap Δ 1d | `9.140257534564697121` |
| Liquidity | `2237578834915` |
| Total τ | `1118842070374` |
| Total α | `662895799191451` |
| α in pool | `144453540098264` |
| α staked | `305159849093187` |
| Price Δ 1h | `0.073886517390402635` |
| Price Δ 1d | `7.386300373035249009` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `76` |
| Owner SS58 (API) | `5FFNhWd881QTWuuiDgkqW4vgiWFDW1QYqPwRB9MZUkH7cMUP` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7574784` |
| Registration wall time | `2026-02-19T01:16:12Z` |
| Registration cost snapshot | `467942376295` |
| Active keys | `43` |
| Active validators | `9` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `3872324` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 43 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 100 |
| Registration recycle cost snapshot (`burn`) | τ0.500000000 |
| Owner SS58 (`owner_ss58`) | `5FFNhWd881QTWuuiDgkqW4vgiWFDW1QYqPwRB9MZUkH7cMUP` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.500000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `100` blocks |
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

*No GitHub URL on-chain; hardware notes not fetched automatically.*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


*No links or contacts in chain identity.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.007743427 |
| 8104292 | 0.007742814 |
| 8104340 | 0.007741643 |
| 8104388 | 0.007738072 |
| 8104436 | 0.007737949 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

