# NetUID 95 — nion (`ᚅ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**nion** (NetUID **95**) (`ᚅ`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `82`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ19,289.619819149. **Alpha liquidity in pool (`alpha_in`)** = ‎578,681.120252589ᚅ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,979,135.576010057ᚅ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.033261938`** *(also **moving-average price** `0.03184230602346361` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎234,361.845939427ᚅ‎`. **Owner hotkey / coldkey (chain):** `5ExqqyEBXLpGwqy6sSVrauozhcyAKBaMz1y5x9wAYSk7n7HP` / `5D5UhUuc6cC47CXUBHyBkpDBrdeyeL6bpWGAreZgNm5WTyrg`.
- **Subnet registered at block:** `5403674` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎58.186728712ᚅ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.016630946` · α-out `‎1.000000000ᚅ‎` · α-in `‎0.500000000ᚅ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104353`
- **Liquidity constant `k`:** `11162538806191686547379026761`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Unknown` |
| Symbol (API) | `ᚅ` |
| Rank | `16` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.033070699` |
| Market cap | `62357915376175.105099292` |
| Market cap Δ 1d | `4.089318204557094313` |
| Liquidity | `38419139519935` |
| Total τ | `19230169410162` |
| Total α | `2557559513876308` |
| α in pool | `580240838265124` |
| α staked | `1305353275611184` |
| Price Δ 1h | `-1.605524683920751605` |
| Price Δ 1d | `3.792537446046361549` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `95` |
| Owner SS58 (API) | `5D5UhUuc6cC47CXUBHyBkpDBrdeyeL6bpWGAreZgNm5WTyrg` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5403674` |
| Registration wall time | `2025-04-22T00:48:24Z` |
| Registration cost snapshot | `210595055304` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `16589065` |
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
| Owner SS58 (`owner_ss58`) | `5D5UhUuc6cC47CXUBHyBkpDBrdeyeL6bpWGAreZgNm5WTyrg` |


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
| 8104244 | 0.033056767 |
| 8104292 | 0.033062222 |
| 8104340 | 0.033050062 |
| 8104388 | 0.033259923 |
| 8104436 | 0.033261984 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.01468494 --> 0.0358668
    line [0.017872951, 0.017831613, 0.017760197, 0.017900948, 0.017034536, 0.017118488, 0.016882914, 0.017799714, 0.017586371, 0.017758622, 0.0178443376471, 0.017655968, 0.017854263, 0.017027395, 0.016145757, 0.0181215798424, 0.018727463, 0.018060446, 0.018124622, 0.017971766, 0.018033653, 0.017507412, 0.019590436, 0.0195934, 0.018737141, 0.019551757, 0.020220669, 0.019554215, 0.019842228, 0.019431854, 0.019311588, 0.019304494, 0.018379555, 0.019107884, 0.020461855, 0.021286594, 0.021256639, 0.021860872, 0.023322873, 0.023612315, 0.023863345, 0.024241365, 0.023833673, 0.024332534, 0.024681278, 0.026751438, 0.027618483, 0.028582565, 0.028874479, 0.029209497, 0.02931868, 0.030169578, 0.034405982, 0.032454904, 0.031496428, 0.033070699]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

