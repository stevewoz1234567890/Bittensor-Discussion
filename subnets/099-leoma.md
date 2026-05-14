# NetUID 99 — Leoma (`გ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Leoma** (NetUID **99**) (`გ`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `86`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,334.247939260. **Alpha liquidity in pool (`alpha_in`)** = ‎155,530.771312124გ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎653,162.224728828გ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008577727`** *(also **moving-average price** `0.008259400492534041` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎39,928.633686934გ‎`. **Owner hotkey / coldkey (chain):** `5C7LM2i42XgL2oB4x3rcmB7KDiof4B92KZzUpg5miZ6DogjU` / `5FxogcQr2XDRNCKSaaHh3AujzJKqksCzKLQWvPzToxG64tfm`.
- **Subnet registered at block:** `7415113` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎51.541320135გ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004289961` · α-out `‎1.000000000გ‎` · α-in `‎0.500000000გ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104349`
- **Liquidity constant `k`:** `207516611114719773253588240`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Leoma` |
| Symbol (API) | `გ` |
| Rank | `105` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.008578907` |
| Market cap | `5736633730150.622033994` |
| Market cap Δ 1d | `6.80421270564967844` |
| Liquidity | `2666534910199` |
| Total τ | `1333341301837` |
| Total α | `808361280164273` |
| α in pool | `155403667199369` |
| α staked | `513286846656373` |
| Price Δ 1h | `2.459973712921454663` |
| Price Δ 1d | `5.186837709013441231` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `99` |
| Owner SS58 (API) | `5FxogcQr2XDRNCKSaaHh3AujzJKqksCzKLQWvPzToxG64tfm` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7415113` |
| Registration wall time | `2026-01-27T19:06:00.001Z` |
| Registration cost snapshot | `395166236844` |
| Active keys | `256` |
| Active validators | `10` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `4289462` |
| Max neurons | `256` |
| Validator slots (metadata) | `10` |
| Max validators (API) | `64` |
| Neuron reg. cost | `50000000` |
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
| Registration recycle cost snapshot (`burn`) | τ0.050000000 |
| Owner SS58 (`owner_ss58`) | `5FxogcQr2XDRNCKSaaHh3AujzJKqksCzKLQWvPzToxG64tfm` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.050000000 / τ100.000000000 |
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


- **Logo URL:** [https://www.leoma.ai/logo-leoma.png](https://www.leoma.ai/logo-leoma.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.008554144 |
| 8104292 | 0.00854631 |
| 8104340 | 0.008584018 |
| 8104388 | 0.00857993 |
| 8104436 | 0.008577735 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

