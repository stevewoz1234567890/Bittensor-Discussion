# NetUID 30 — Pending (`ו`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Pending** (NetUID **30**) (`ו`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `17`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ9,423.403811407. **Alpha liquidity in pool (`alpha_in`)** = ‎2,051,848.144293042ו‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,910,516.254769294ו‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004590364`** *(also **moving-average price** `0.004425274441018701` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎299,783.847101032ו‎`. **Owner hotkey / coldkey (chain):** `5HW12NvEZoGz8ZzcWMh4xyDUy6H1Af85m5LB8V1L11erK1S1` / `5HTogQKFuDaLq5ifWNhL2owMpLPHM3TAmujUUaTVj7FWzf6p`.
- **Subnet registered at block:** `3250216` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎12.827452885ו‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.001768017` · α-out `‎1.000000000ו‎` · α-in `‎0.385158300ו‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104418`
- **Liquidity constant `k`:** `19335393623359432078310330094`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Pending` |
| Symbol (API) | `ו` |
| Rank | `54` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.00459023` |
| Market cap | `21009172254448.43403954` |
| Market cap Δ 1d | `9.512124678332776661` |
| Liquidity | `18840989574378` |
| Total τ | `9422831135728` |
| Total α | `4962036826270518` |
| α in pool | `2051783557392743` |
| α staked | `2525148808621255` |
| Price Δ 1h | `1.204694427847314241` |
| Price Δ 1d | `9.403068137535884911` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `30` |
| Owner SS58 (API) | `5HTogQKFuDaLq5ifWNhL2owMpLPHM3TAmujUUaTVj7FWzf6p` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3250216` |
| Registration wall time | `2024-06-24T18:19:36.006Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `1773469` |
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
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 21600 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5HTogQKFuDaLq5ifWNhL2owMpLPHM3TAmujUUaTVj7FWzf6p` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `21600` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `180` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `15` |
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


*No links or contacts in chain identity.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.004590231 |
| 8104244 | 0.004590218 |
| 8104292 | 0.004619651 |
| 8104340 | 0.004600034 |
| 8104388 | 0.004600033 |
| 8104436 | 0.004590364 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.004646827 |
| 2026-03-10T23:59:48Z | — | 0.004412441 |
| 2026-03-11T23:59:48Z | — | 0.004467771 |
| 2026-03-12T23:59:48Z | — | 0.004341438 |
| 2026-03-13T23:59:48Z | — | 0.004346108 |
| 2026-03-14T23:59:48Z | — | 0.004418583 |
| 2026-03-15T23:59:48Z | — | 0.004200969 |
| 2026-03-16T23:59:48Z | — | 0.00383933 |
| 2026-03-17T23:59:48Z | — | 0.004009796 |
| 2026-03-18T23:59:48Z | — | 0.003963513 |
| 2026-03-19T23:59:48Z | — | 0.00399753477996 |
| 2026-03-20T23:59:48Z | — | 0.004167644 |
| 2026-03-21T23:59:48Z | — | 0.00436956 |
| 2026-03-22T23:59:48Z | — | 0.004401825 |
| 2026-03-23T23:59:48Z | — | 0.004767092 |
| 2026-03-24T23:59:48Z | — | 0.00456350569841 |
| 2026-03-25T23:59:48Z | — | 0.004445624 |
| 2026-03-26T23:59:48Z | — | 0.004584049 |
| 2026-03-27T23:59:48Z | — | 0.004416881 |
| 2026-03-28T23:59:48Z | — | 0.004637952 |
| 2026-03-29T23:59:48Z | — | 0.004599284 |
| 2026-03-30T23:59:48Z | — | 0.004606507 |
| 2026-03-31T23:59:48Z | — | 0.004418865 |
| 2026-04-01T23:59:48Z | — | 0.004511129 |
| 2026-04-02T23:59:48Z | — | 0.004421475 |
| 2026-04-03T23:59:48Z | — | 0.004496279 |
| 2026-04-04T23:59:48Z | — | 0.004739338 |
| 2026-04-05T23:59:48Z | — | 0.004677642 |
| 2026-04-06T23:59:48Z | — | 0.004779047 |
| 2026-04-07T23:59:48Z | — | 0.004770414 |
| 2026-04-08T23:59:48Z | — | 0.004820579 |
| 2026-04-09T23:59:48Z | — | 0.004710913 |
| 2026-04-10T23:59:48Z | — | 0.003998939 |
| 2026-04-11T23:59:48Z | — | 0.003963946 |
| 2026-04-12T23:59:48Z | — | 0.004074291 |
| 2026-04-13T23:59:48Z | — | 0.004148516 |
| 2026-04-14T23:59:48Z | — | 0.004189857 |
| 2026-04-15T23:59:48Z | — | 0.004016353 |
| 2026-04-16T23:59:48Z | — | 0.004009366 |
| 2026-04-17T23:59:48Z | — | 0.004279231 |
| 2026-04-18T23:59:48Z | — | 0.004195173 |
| 2026-04-19T23:59:48Z | — | 0.004202364 |
| 2026-04-20T23:59:48Z | — | 0.004411828 |
| 2026-04-21T23:59:48Z | — | 0.004670629 |
| 2026-04-22T23:59:48Z | — | 0.004569805 |
| 2026-04-23T23:59:48Z | — | 0.004769514 |
| 2026-04-24T23:59:48Z | — | 0.00461581 |
| 2026-04-25T23:59:48Z | — | 0.004836116 |
| 2026-04-26T23:59:48Z | — | 0.00494567 |
| 2026-04-27T23:59:48Z | — | 0.004938518 |
| 2026-04-28T23:59:48Z | — | 0.004579275 |
| 2026-04-29T23:59:48Z | — | 0.004622765 |
| 2026-04-30T23:59:48Z | — | 0.00463251 |
| 2026-05-01T23:59:48Z | — | 0.004442215 |
| 2026-05-02T23:59:48Z | — | 0.004334697 |
| 2026-05-03T23:59:48Z | — | 0.00459023 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

