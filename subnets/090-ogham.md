# NetUID 90 — ogham (` `)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**ogham** (NetUID **90**) (` `).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `77`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,919.942259930. **Alpha liquidity in pool (`alpha_in`)** = ‎411,327.760710107 ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎969,649.978766082 ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004668601`** *(also **moving-average price** `0.004547039745375514` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎26,485.330519982 ‎`. **Owner hotkey / coldkey (chain):** `5E7rCzjycq3GgALTXqoSFHn9ZHRtJ96Nd4YaT2RBNdH5k6AK` / `5CqrdkU4FuH8LdUjkq4YQFJbQiK1Bmf9q4fVpFuhrxGcGwbW`.
- **Subnet registered at block:** `7063126` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎50.332819479 ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002334300` · α-out `‎1.000000000 ‎` · α-in `‎0.500000000 ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104358`
- **Liquidity constant `k`:** `789725550469709095172112510`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Unknown` |
| Symbol (API) | ` ` |
| Rank | `114` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.00466886` |
| Market cap | `4562940208863.68138124` |
| Market cap Δ 1d | `6.642535745014148565` |
| Liquidity | `3839286166118` |
| Total τ | `1919451670189` |
| Total α | `1380640814524034` |
| α in pool | `411199842344717` |
| α staked | `566113722179317` |
| Price Δ 1h | `-1.014835075254514412` |
| Price Δ 1d | `5.80889918278361216` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `90` |
| Owner SS58 (API) | `5CqrdkU4FuH8LdUjkq4YQFJbQiK1Bmf9q4fVpFuhrxGcGwbW` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7063126` |
| Registration wall time | `2025-12-09T21:20:12.001Z` |
| Registration cost snapshot | `308402715168` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `2334431` |
| Max neurons | `256` |
| Validator slots (metadata) | `12` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

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
| Owner SS58 (`owner_ss58`) | `5CqrdkU4FuH8LdUjkq4YQFJbQiK1Bmf9q4fVpFuhrxGcGwbW` |


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


*No `SubnetIdentity` registered on-chain.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004668739 |
| 8104292 | 0.004668683 |
| 8104340 | 0.004668554 |
| 8104388 | 0.004668599 |
| 8104436 | 0.004668602 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

