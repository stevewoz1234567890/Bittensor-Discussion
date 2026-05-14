# NetUID 70 — NexisGen (`غ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**NexisGen** (NetUID **70**) (`غ`).

Enterprise dataset delivery

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `57`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ817.807506484. **Alpha liquidity in pool (`alpha_in`)** = ‎96,259.409387118غ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎303,034.803439843غ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008496098`** *(also **moving-average price** `0.007937224814668298` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎13,750.539873994غ‎`. **Owner hotkey / coldkey (chain):** `5EJGfSvRcEGVQtqDuU7YYwuZRHmaktf6JEZDeFPyeXksiHrm` / `5HisJVRY5s72aGFqcvemjk2AzdQnPhbTcMjWDecWZKtoCqj9`.
- **Subnet registered at block:** `7787562` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎30.323561950غ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004248045` · α-out `‎1.000000000غ‎` · α-in `‎0.500000000غ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104378`
- **Liquidity constant `k`:** `78721667566501514251073112`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `NexisGen` |
| Symbol (API) | `غ` |
| Rank | `124` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.00844147` |
| Market cap | `2525663692828.58086773` |
| Market cap Δ 1d | `11.256520528624254947` |
| Liquidity | `1628401613290` |
| Total τ | `814190330764` |
| Total α | `398955881354359` |
| α in pool | `96453731699141` |
| α staked | `202743409655218` |
| Price Δ 1h | `1.702803629097599015` |
| Price Δ 1d | `8.537899360200785863` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `70` |
| Owner SS58 (API) | `5HisJVRY5s72aGFqcvemjk2AzdQnPhbTcMjWDecWZKtoCqj9` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7787562` |
| Registration wall time | `2026-03-20T15:10:12Z` |
| Registration cost snapshot | `614193494016` |
| Active keys | `180` |
| Active validators | `8` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `4220771` |
| Max neurons | `256` |
| Validator slots (metadata) | `8` |
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
| `subnetwork_n` | 180 |
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
| Owner SS58 (`owner_ss58`) | `5HisJVRY5s72aGFqcvemjk2AzdQnPhbTcMjWDecWZKtoCqj9` |


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


- **Logo URL:** [https://www.nexisgen.ai/logo.png](https://www.nexisgen.ai/logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.008453246 |
| 8104292 | 0.00843107 |
| 8104340 | 0.008403075 |
| 8104388 | 0.008486099 |
| 8104436 | 0.008496106 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in -0.03650828 --> 0.5278924
    line [0.003570029, 0.002916013, 0.002511141, 0.002824293, 0.002669412, 0.002530196, 0.002418819, 0.002492086, 0.002551388, 0.002453529, 0.00241590731881, 0.488968253, 0.014534948, 0.012525753, 0.010003076, 0.0104088137492, 0.016167702, 0.013903957, 0.013023683, 0.010938868, 0.009975886, 0.007731538, 0.006633931, 0.008051228, 0.0136411, 0.013093456, 0.012017618, 0.012077557, 0.01149932, 0.011202116, 0.008839974, 0.007332451, 0.008232928, 0.008106826, 0.007843606, 0.007535342, 0.007100527, 0.006445171, 0.006006924, 0.006129577, 0.005718956, 0.006022358, 0.005920941, 0.0058676, 0.006106813, 0.006608174, 0.00684372, 0.006650183, 0.006568291, 0.007414657, 0.007498288, 0.007638701, 0.007666583, 0.007622925, 0.00770589, 0.00844147]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

