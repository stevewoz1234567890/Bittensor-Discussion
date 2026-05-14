# NetUID 39 — deprecated (`מ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**deprecated** (NetUID **39**) (`מ`).

deprecated

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `26`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ16,729.131873172. **Alpha liquidity in pool (`alpha_in`)** = ‎2,624,548.605027360מ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,433,338.360510241מ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006406652`** *(also **moving-average price** `0.006586378440260887` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎973,639.564013972מ‎`. **Owner hotkey / coldkey (chain):** `5G3qVaXzKMPDm5AJ3dpzbpUC27kpccBvDwzSWXrq8M6qMmbC` / `5CQKh1G5MKRyBEPCY7cHRW1okvj2LxjK94cgjsD9c24wrpCN`.
- **Subnet registered at block:** `3280104` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎19.645546948מ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000מ‎` · α-in `‎0.000000000מ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104409`
- **Liquidity constant `k`:** `43906419721052318573109985920`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `deprecated` |
| Symbol (API) | `מ` |
| Rank | `45` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.006405934` |
| Market cap | `24753746723624.498523894` |
| Market cap Δ 1d | `-2.790281113112085055` |
| Liquidity | `33541816963646` |
| Total τ | `16728188427448` |
| Total α | `5057653965537601` |
| α in pool | `2624695873575744` |
| α staked | `1239494223235197` |
| Price Δ 1h | `0.005932351830926724` |
| Price Δ 1d | `-2.896932960600850744` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `39` |
| Owner SS58 (API) | `5CQKh1G5MKRyBEPCY7cHRW1okvj2LxjK94cgjsD9c24wrpCN` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3280104` |
| Registration wall time | `2024-06-28T22:23:24.003Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `13` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `13` |
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
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 15000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5CQKh1G5MKRyBEPCY7cHRW1okvj2LxjK94cgjsD9c24wrpCN` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `15000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `20` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `500000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No miner/validator sections auto-matched.* Open [https://github.com/deprecated/deprecated](https://github.com/deprecated/deprecated) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/deprecated/deprecated](https://github.com/deprecated/deprecated)
- **Discord (handle / invite hint):** `deprecated`
- **Logo URL:** [https://deprecated.png](https://deprecated.png)
- **Contact:** deprecated@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.006405935 |
| 8104244 | 0.006405921 |
| 8104292 | 0.006405912 |
| 8104340 | 0.006405897 |
| 8104388 | 0.006406656 |
| 8104436 | 0.006406652 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

