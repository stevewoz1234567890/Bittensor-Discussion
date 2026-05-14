# NetUID 44 — Score (`ף`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Score** (NetUID **44**) (`ף`).

Making every camera intelligent

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `31`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ57,648.007168888. **Alpha liquidity in pool (`alpha_in`)** = ‎1,645,451.556043042ף‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,255,362.044677652ף‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.034999699`** *(also **moving-average price** `0.03514493256807327` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,667,406.770660980ף‎`. **Owner hotkey / coldkey (chain):** `5FsREvyUXSZWYRqVyQLDdpYmZZPnkhZyW6HjooozKP1nQkwu` / `5CaCekuxb9pKQyLoxh3jbkEXig8fxjkeS4AQ6UmZa12xfQ9H`.
- **Subnet registered at block:** `3550319` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎23.369857832ף‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.015778888` · α-out `‎1.000000000ף‎` · α-in `‎0.450829249ף‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104404`
- **Liquidity constant `k`:** `94857003098827199914291277296`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Score` |
| Symbol (API) | `ף` |
| Rank | `5` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.034981927` |
| Market cap | `159126896741954.483867871` |
| Market cap Δ 1d | `-1.421349414600304979` |
| Liquidity | `115201730535565` |
| Total τ | `57629660343592` |
| Total α | `4900475719433509` |
| α in pool | `1645766117800595` |
| α staked | `2903065532953078` |
| Price Δ 1h | `-0.091854453217389149` |
| Price Δ 1d | `-1.605311760375272082` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `44` |
| Owner SS58 (API) | `5CaCekuxb9pKQyLoxh3jbkEXig8fxjkeS4AQ6UmZa12xfQ9H` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3550319` |
| Registration wall time | `2024-08-06T19:54:12.002Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `9` |
| Active miners | `6` |
| Active dual-role | `0` |
| Emission | `15689458` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Score Vision (SN44)

Score Vision is a decentralised computer vision framework built on Bittensor that drastically reduces the cost and time required for complex video analysis. By leveraging innovative lightweight validation techniques and aligned incentives, we're making advanced computer vision accessible and scalable.

Our initial focus is Game State Recognition (GSR) in football - a strategic entry point into the $600 billion football industry, with $50 billion in betting and $30 billion in data services. Current solutions are prohibitively expensive: a single football match requires hundreds of hours of manual annotation, costing thousands of dollars. Score Vision aims to reduce these costs by 10x to 100x while dramatically improving speed and accuracy, unlocking new possibilities in sports analytics and beyond.

**Get Started:**

- [Miner Setup](miner/README.md)
- [Validator Setup](validator/README.md)

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Democratising visual intelligence by building an open, permissionless computer vision layer for sports and beyond.

**Fetched document title:** We Are Score | Making Every Camera Intelligent

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
| `immunity_period` (blocks) | 7500 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5CaCekuxb9pKQyLoxh3jbkEXig8fxjkeS4AQ6UmZa12xfQ9H` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `7500` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `2` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

##### Extra scrape: `README.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- - Manages GPU memory for optimal performance
- - Monitors system resources (GPU/CPU usage)
- DEVICE=cuda                                   # Computing device (cuda/cpu/mps)
- - Check CUDA/GPU availability
- - Monitor GPU memory usage

---

##### Extra scrape: `README.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- - Manages GPU memory for optimal performance
- - Monitors system resources (GPU/CPU usage)
- DEVICE=cuda                                   # Computing device (cuda/cpu/mps)
- - Check CUDA/GPU availability
- - Monitor GPU memory usage


*Primary README URL used: `https://raw.githubusercontent.com/score-technologies/score-vision/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.wearescore.com/](https://www.wearescore.com/)
- **GitHub:** [https://github.com/score-technologies/score-vision](https://github.com/score-technologies/score-vision)
- **Logo URL:** [https://www.wearescore.com/android-chrome-512x512.png](https://www.wearescore.com/android-chrome-512x512.png)
- **Contact:** hello@wearescore.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.034981935 |
| 8104244 | 0.034981806 |
| 8104292 | 0.034999883 |
| 8104340 | 0.034999856 |
| 8104388 | 0.034999847 |
| 8104436 | 0.034999699 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.030358849 |
| 2026-03-10T23:59:48Z | — | 0.029903154 |
| 2026-03-11T23:59:48Z | — | 0.028435257 |
| 2026-03-12T23:59:48Z | — | 0.027498422 |
| 2026-03-13T23:59:48Z | — | 0.029225969 |
| 2026-03-14T23:59:48Z | — | 0.029557898 |
| 2026-03-15T23:59:48Z | — | 0.028063755 |
| 2026-03-16T23:59:48Z | — | 0.030943765 |
| 2026-03-17T23:59:48Z | — | 0.029703251 |
| 2026-03-18T23:59:48Z | — | 0.032287887 |
| 2026-03-19T23:59:48Z | — | 0.030422766396 |
| 2026-03-20T23:59:48Z | — | 0.031284104 |
| 2026-03-21T23:59:48Z | — | 0.029502348 |
| 2026-03-22T23:59:48Z | — | 0.030172707 |
| 2026-03-23T23:59:48Z | — | 0.028908879 |
| 2026-03-24T23:59:48Z | — | 0.0310816210157 |
| 2026-03-25T23:59:48Z | — | 0.030359735 |
| 2026-03-26T23:59:48Z | — | 0.031914092 |
| 2026-03-27T23:59:48Z | — | 0.029982715 |
| 2026-03-28T23:59:48Z | — | 0.02962583 |
| 2026-03-29T23:59:48Z | — | 0.029185775 |
| 2026-03-30T23:59:48Z | — | 0.030418192 |
| 2026-03-31T23:59:48Z | — | 0.030128411 |
| 2026-04-01T23:59:48Z | — | 0.030658798 |
| 2026-04-02T23:59:48Z | — | 0.029084897 |
| 2026-04-03T23:59:48Z | — | 0.029913742 |
| 2026-04-04T23:59:48Z | — | 0.030248639 |
| 2026-04-05T23:59:48Z | — | 0.029569831 |
| 2026-04-06T23:59:48Z | — | 0.029539415 |
| 2026-04-07T23:59:48Z | — | 0.029228075 |
| 2026-04-08T23:59:48Z | — | 0.030444136 |
| 2026-04-09T23:59:48Z | — | 0.029256262 |
| 2026-04-10T23:59:48Z | — | 0.029830419 |
| 2026-04-11T23:59:48Z | — | 0.031262626 |
| 2026-04-12T23:59:48Z | — | 0.031115615 |
| 2026-04-13T23:59:48Z | — | 0.03114932 |
| 2026-04-14T23:59:48Z | — | 0.031639618 |
| 2026-04-15T23:59:48Z | — | 0.035818598 |
| 2026-04-16T23:59:48Z | — | 0.035639021 |
| 2026-04-17T23:59:48Z | — | 0.036198966 |
| 2026-04-18T23:59:48Z | — | 0.03661732 |
| 2026-04-19T23:59:48Z | — | 0.036566889 |
| 2026-04-20T23:59:48Z | — | 0.037855267 |
| 2026-04-21T23:59:48Z | — | 0.037458089 |
| 2026-04-22T23:59:48Z | — | 0.037560169 |
| 2026-04-23T23:59:48Z | — | 0.036351341 |
| 2026-04-24T23:59:48Z | — | 0.034618369 |
| 2026-04-25T23:59:48Z | — | 0.033981624 |
| 2026-04-26T23:59:48Z | — | 0.035385104 |
| 2026-04-27T23:59:48Z | — | 0.035223109 |
| 2026-04-28T23:59:48Z | — | 0.033758028 |
| 2026-04-29T23:59:48Z | — | 0.033764557 |
| 2026-04-30T23:59:48Z | — | 0.035209021 |
| 2026-05-01T23:59:48Z | — | 0.036086238 |
| 2026-05-02T23:59:48Z | — | 0.035106966 |
| 2026-05-03T23:59:48Z | — | 0.034981927 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

