# NetUID 81 — deprecated (`ᚠ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**deprecated** (NetUID **81**) (`ᚠ`).

deprecated

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `68`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ20,595.033131994. **Alpha liquidity in pool (`alpha_in`)** = ‎2,369,574.670548612ᚠ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,002,621.094894877ᚠ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008696573`** *(also **moving-average price** `0.008871127851307392` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎767,235.931957219ᚠ‎`. **Owner hotkey / coldkey (chain):** `5F9uEDDovurwEJihzZSpKypipVy84EEAPHTt3EfepTjcQfij` / `5DUELqJMeY6tA7652ooUUvU9TgUCi5hnv9o66nC8Zjw7BtW5`.
- **Subnet registered at block:** `5203057` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎50.815518897ᚠ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ᚠ‎` · α-in `‎0.000000000ᚠ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104367`
- **Liquidity constant `k`:** `48801468848682431308589492328`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `deprecated` |
| Symbol (API) | `ᚠ` |
| Rank | `33` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.008696842` |
| Market cap | `31035372958706.372534278` |
| Market cap Δ 1d | `-2.34295392909481236` |
| Liquidity | `41202849643913` |
| Total τ | `20595351666002` |
| Total α | `4371962765443489` |
| α in pool | `2369538043569365` |
| α staked | `1199041557934994` |
| Price Δ 1h | `-0.000747392147576144` |
| Price Δ 1d | `-2.458971346844344032` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `81` |
| Owner SS58 (API) | `5DUELqJMeY6tA7652ooUUvU9TgUCi5hnv9o66nC8Zjw7BtW5` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5203057` |
| Registration wall time | `2025-03-25T04:05:00Z` |
| Registration cost snapshot | `249790431509` |
| Active keys | `256` |
| Active validators | `7` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `7` |
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
| `immunity_period` (blocks) | 10799 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5DUELqJMeY6tA7652ooUUvU9TgUCi5hnv9o66nC8Zjw7BtW5` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `10799` blocks |
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
| 8104244 | 0.008696815 |
| 8104292 | 0.008696801 |
| 8104340 | 0.008696773 |
| 8104388 | 0.008696771 |
| 8104436 | 0.008696573 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.017824381 |
| 2026-03-10T23:59:48Z | — | 0.018371296 |
| 2026-03-11T23:59:48Z | — | 0.018785396 |
| 2026-03-12T23:59:48Z | — | 0.019447446 |
| 2026-03-13T23:59:48Z | — | 0.019706913 |
| 2026-03-14T23:59:48Z | — | 0.021665234 |
| 2026-03-15T23:59:48Z | — | 0.021575644 |
| 2026-03-16T23:59:48Z | — | 0.021818948 |
| 2026-03-17T23:59:48Z | — | 0.020903484 |
| 2026-03-18T23:59:48Z | — | 0.020991702 |
| 2026-03-19T23:59:48Z | — | 0.0209954435543 |
| 2026-03-20T23:59:48Z | — | 0.022395353 |
| 2026-03-21T23:59:48Z | — | 0.022067114 |
| 2026-03-22T23:59:48Z | — | 0.021721191 |
| 2026-03-23T23:59:48Z | — | 0.02211838 |
| 2026-03-24T23:59:48Z | — | 0.0242105329578 |
| 2026-03-25T23:59:48Z | — | 0.025033038 |
| 2026-03-26T23:59:48Z | — | 0.02484797 |
| 2026-03-27T23:59:48Z | — | 0.026924156 |
| 2026-03-28T23:59:48Z | — | 0.027599665 |
| 2026-03-29T23:59:48Z | — | 0.025541794 |
| 2026-03-30T23:59:48Z | — | 0.026647877 |
| 2026-03-31T23:59:48Z | — | 0.026266756 |
| 2026-04-01T23:59:48Z | — | 0.02668877 |
| 2026-04-02T23:59:48Z | — | 0.02712235 |
| 2026-04-03T23:59:48Z | — | 0.028194727 |
| 2026-04-04T23:59:48Z | — | 0.028584727 |
| 2026-04-05T23:59:48Z | — | 0.028359383 |
| 2026-04-06T23:59:48Z | — | 0.026910187 |
| 2026-04-07T23:59:48Z | — | 0.026308626 |
| 2026-04-08T23:59:48Z | — | 0.026279863 |
| 2026-04-09T23:59:48Z | — | 0.010884211 |
| 2026-04-10T23:59:48Z | — | 0.009919478 |
| 2026-04-11T23:59:48Z | — | 0.011350163 |
| 2026-04-12T23:59:48Z | — | 0.009851988 |
| 2026-04-13T23:59:48Z | — | 0.009388601 |
| 2026-04-14T23:59:48Z | — | 0.01045839 |
| 2026-04-15T23:59:48Z | — | 0.01006907 |
| 2026-04-16T23:59:48Z | — | 0.009460965 |
| 2026-04-17T23:59:48Z | — | 0.009388139 |
| 2026-04-18T23:59:48Z | — | 0.009012628 |
| 2026-04-19T23:59:48Z | — | 0.008375197 |
| 2026-04-20T23:59:48Z | — | 0.008350713 |
| 2026-04-21T23:59:48Z | — | 0.008427285 |
| 2026-04-22T23:59:48Z | — | 0.008424522 |
| 2026-04-23T23:59:48Z | — | 0.008428491 |
| 2026-04-24T23:59:48Z | — | 0.008568128 |
| 2026-04-25T23:59:48Z | — | 0.008598414 |
| 2026-04-26T23:59:48Z | — | 0.008567519 |
| 2026-04-27T23:59:48Z | — | 0.008489817 |
| 2026-04-28T23:59:48Z | — | 0.008445111 |
| 2026-04-29T23:59:48Z | — | 0.008741439 |
| 2026-04-30T23:59:48Z | — | 0.00884432 |
| 2026-05-01T23:59:48Z | — | 0.008917582 |
| 2026-05-02T23:59:48Z | — | 0.008914613 |
| 2026-05-03T23:59:48Z | — | 0.008696842 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

