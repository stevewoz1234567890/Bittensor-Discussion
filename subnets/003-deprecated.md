# NetUID 3 — deprecated (`γ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**deprecated** (NetUID **3**) (`γ`).

deprecated

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `351`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ74,660.732901473. **Alpha liquidity in pool (`alpha_in`)** = ‎2,798,350.073606372γ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,187,493.180710700γ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.026708824`** *(also **moving-average price** `0.026116409106180072` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎2,946,054.052978278γ‎`. **Owner hotkey / coldkey (chain):** `5HdTZQ6UXD7MWcRsMeExVwqAKKo4UwomUd662HvtXiZXkxmv` / `5FUJoAsY5TWfs1FGFtscC5QUuarJMCWYwYzEftyGAeH7pUqK`.
- **Subnet registered at block:** `4165565` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎264.938604259γ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000γ‎` · α-in `‎0.000000000γ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104084`
- **Liquidity constant `k`:** `208926867410342649288460985956`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `deprecated` |
| Symbol (API) | `γ` |
| Rank | `7` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.026879948` |
| Market cap | `118831461916541.272940744` |
| Market cap Δ 1d | `4.415060751594848264` |
| Liquidity | `149879472175390` |
| Total τ | `74899975976697` |
| Total α | `4985618799349183` |
| α in pool | `2789421177403073` |
| α staked | `1631400690129605` |
| Price Δ 1h | `1.515698783606935288` |
| Price Δ 1d | `4.256068292821420568` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `3` |
| Owner SS58 (API) | `5FUJoAsY5TWfs1FGFtscC5QUuarJMCWYwYzEftyGAeH7pUqK` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4165565` |
| Registration wall time | `2024-10-31T19:37:00.001Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `1` |
| Active miners | `4` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `1` |
| Max validators (API) | `64` |
| Neuron reg. cost | `157432491` |
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
| `immunity_period` (blocks) | 10000 |
| Registration recycle cost snapshot (`burn`) | τ0.158364185 |
| Owner SS58 (`owner_ss58`) | `5FUJoAsY5TWfs1FGFtscC5QUuarJMCWYwYzEftyGAeH7pUqK` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `1000000000`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `10000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `250` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `4` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No miner/validator sections auto-matched.* Open [https://github.com/username/repo](https://github.com/username/repo) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.deprecated.com](https://www.deprecated.com)
- **GitHub:** [https://github.com/username/repo](https://github.com/username/repo)
- **Discord (handle / invite hint):** `deprecated`
- **Logo URL:** [https://deprecated.png](https://deprecated.png)
- **Contact:** deprecated@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.026879952 |
| 8104244 | 0.026751084 |
| 8104292 | 0.026686072 |
| 8104340 | 0.026685232 |
| 8104388 | 0.02672 |
| 8104436 | 0.026708824 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.01802666 --> 0.1012936
    line [0.036749772, 0.037919393, 0.038931346, 0.045114587, 0.056383722, 0.058482337, 0.071247606, 0.064903114, 0.065859919, 0.068780109, 0.0820233961019, 0.080331634, 0.081724924, 0.08642716, 0.088418098, 0.0955510925742, 0.090761206, 0.083371497, 0.078577034, 0.078354523, 0.080971466, 0.078362419, 0.07357125, 0.07512488, 0.068543616, 0.06947293, 0.06935857, 0.072578064, 0.072158151, 0.071545037, 0.069103457, 0.033039564, 0.032848279, 0.035232478, 0.032389875, 0.029945594, 0.030045491, 0.02924395, 0.025898223, 0.026113712, 0.023831259, 0.024289382, 0.024453304, 0.024507797, 0.023769207, 0.023983274, 0.024082258, 0.023917039, 0.023814158, 0.023978551, 0.026352129, 0.025904527, 0.025596463, 0.026107505, 0.026010016, 0.026879948]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

