# NetUID 57 — gaia (`ح`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**gaia** (NetUID **57**) (`ح`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `44`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,157.403131863. **Alpha liquidity in pool (`alpha_in`)** = ‎98,565.951040206ح‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎200,772.169564389ح‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011742520`** *(also **moving-average price** `0.007946990430355072` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎5,272.973332479ح‎`. **Owner hotkey / coldkey (chain):** `5Ejcqsbx3MFhNqiDjPJVvBtYWNvXXcvSJ3ibMCrzfCU3g5MN` / `5HdpnCSYczg52ZaiBKmgwJPFnVpyyu27o1GHgLcj8217xxr7`.
- **Subnet registered at block:** `8057320` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎22.387864984ح‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003619330` · α-out `‎1.000000000ح‎` · α-in `‎0.308224326ح‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104391`
- **Liquidity constant `k`:** `114080540428989547032683778`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Unknown` |
| Symbol (API) | `ح` |
| Rank | `121` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.011785357` |
| Market cap | `3325355328383.205825111` |
| Market cap Δ 1d | `14.969737767560495714` |
| Liquidity | `2317335494644` |
| Total τ | `1158662834328` |
| Total α | `299033054916723` |
| α in pool | `98314600085225` |
| α staked | `183845314831498` |
| Price Δ 1h | `9.382700236903593463` |
| Price Δ 1d | `12.388338630254138717` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `57` |
| Owner SS58 (API) | `5HdpnCSYczg52ZaiBKmgwJPFnVpyyu27o1GHgLcj8217xxr7` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `8057320` |
| Registration wall time | `2026-04-27T03:31:36Z` |
| Registration cost snapshot | `745941640813` |
| Active keys | `108` |
| Active validators | `6` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `3650859` |
| Max neurons | `256` |
| Validator slots (metadata) | `6` |
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
| `subnetwork_n` | 108 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5HdpnCSYczg52ZaiBKmgwJPFnVpyyu27o1GHgLcj8217xxr7` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `4611686018427387903`) |
| `target_regs_per_interval` | `2` |
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
| `yuma_version` | `3` |
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
| 8104244 | 0.011795009 |
| 8104292 | 0.011788101 |
| 8104340 | 0.011784203 |
| 8104388 | 0.011783954 |
| 8104436 | 0.01174252 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.002358011 --> 0.01248368
    line [0.003617567, 0.003638074, 0.003606288, 0.003577791, 0.003538728, 0.003510379, 0.003372257, 0.003288212, 0.00327464, 0.003342454, 0.00334448118477, 0.003357555, 0.00341123, 0.003333031, 0.003413555, 0.00334548311752, 0.003316934, 0.003291617, 0.003269373, 0.003280568, 0.003293988, 0.003314296, 0.003284038, 0.003342939, 0.003324207, 0.00334414, 0.003310436, 0.003274179, 0.003300781, 0.00328271, 0.003268959, 0.003056333, 0.003165757, 0.003196208, 0.003180073, 0.003163258, 0.003176723, 0.003138554, 0.003088016, 0.003107566, 0.003082941, 0.003103585, 0.003100733, 0.003164527, 0.003147627, 0.003159362, 0.003166889, 0.003176184, 0.003205325, 0.009896108, 0.008608011, 0.009889923, 0.010527932, 0.010840914, 0.010515553, 0.011785357]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

