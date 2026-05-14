# NetUID 104 — for sale (burn to uid1) (`Բ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**for sale (burn to uid1)** (NetUID **104**) (`Բ`).

subnet for sale. in the meantime, burning to uid1 and experimentation stops to park subnet until sold.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `91`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ5,188.940875562. **Alpha liquidity in pool (`alpha_in`)** = ‎1,394,876.372050718Բ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,496,390.358401025Բ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003561420`** *(also **moving-average price** `0.0035634504165500402` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎53,573.042262360Բ‎`. **Owner hotkey / coldkey (chain):** `5CoeuhimLNpjegk9zDBLmp9EBEy6X44Ad6naf2dCupkWYG6y` / `5HBb3F1bmDzdwQ5WTweXUvnKETTzu6aWNAH811vrLkvSdQAn`.
- **Subnet registered at block:** `5528520` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎67.344690799Բ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Բ‎` · α-in `‎0.000000000Բ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104344`
- **Liquidity constant `k`:** `7237931023289598724390753516`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `for sale (burn to uid1)` |
| Symbol (API) | `Բ` |
| Rank | `87` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.003561423` |
| Market cap | `12848388899070.360102669` |
| Market cap Δ 1d | `-0.043326969887119485` |
| Liquidity | `10156685669123` |
| Total τ | `5188943307200` |
| Total α | `3891033730451743` |
| α in pool | `1394875689274680` |
| α staked | `2212780267086123` |
| Price Δ 1h | `-0.000028078656177978` |
| Price Δ 1d | `-0.238715162278410452` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `104` |
| Owner SS58 (API) | `5HBb3F1bmDzdwQ5WTweXUvnKETTzu6aWNAH811vrLkvSdQAn` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5528520` |
| Registration wall time | `2025-05-09T08:57:36Z` |
| Registration cost snapshot | `147970415680` |
| Active keys | `64` |
| Active validators | `1` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `64` |
| Validator slots (metadata) | `1` |
| Max validators (API) | `64` |
| Neuron reg. cost | `999999999` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `720` |

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 64 |
| `subnetwork_n` | 64 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 720 |
| Registration recycle cost snapshot (`burn`) | τ0.999999999 |
| Owner SS58 (`owner_ss58`) | `5HBb3F1bmDzdwQ5WTweXUvnKETTzu6aWNAH811vrLkvSdQAn` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.999999999 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `720` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `1024` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `720` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `0` |
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
| 8104244 | 0.003561423 |
| 8104292 | 0.003561422 |
| 8104340 | 0.00356142 |
| 8104388 | 0.003561419 |
| 8104436 | 0.003561419 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

