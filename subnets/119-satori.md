# NetUID 119 — Satori (`Ⲃ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Satori** (NetUID **119**) (`Ⲃ`).

Satori constructs a persistent 'Second Life' in Japan. We merge deep AI companionship with authentic Digital Residency, creating a seamless bridge where virtual emotional connections unlock real-world value and physical experiences.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `106`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ5,203.588973256. **Alpha liquidity in pool (`alpha_in`)** = ‎764,273.444918314Ⲃ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,146,640.119379115Ⲃ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006811294`** *(also **moving-average price** `0.006941622123122215` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎56,041.261059518Ⲃ‎`. **Owner hotkey / coldkey (chain):** `5HMwvi1dHWCBHTNTtizL5peRBwqvd8HtGrTVouN51p75JNd4` / `5GbLENPLG8Takn1puaz5HorPmrFtDT7i2PojiJsqutbaGwWu`.
- **Subnet registered at block:** `5740660` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎72.563604351Ⲃ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.001577555` · α-out `‎1.000000000Ⲃ‎` · α-in `‎0.231608785Ⲃ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104329`
- **Liquidity constant `k`:** `3976964870529315618050610384`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Satori` |
| Symbol (API) | `Ⲃ` |
| Rank | `99` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.006811621` |
| Market cap | `9150078971176.966736048` |
| Market cap Δ 1d | `-6.931029260814775027` |
| Liquidity | `10408793652218` |
| Total τ | `5203345901979` |
| Total α | `1910626511365488` |
| α in pool | `764201025018833` |
| α staked | `579103156346655` |
| Price Δ 1h | `-0.108051208177634544` |
| Price Δ 1d | `-7.389081990103458895` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `119` |
| Owner SS58 (API) | `5GbLENPLG8Takn1puaz5HorPmrFtDT7i2PojiJsqutbaGwWu` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5740660` |
| Registration wall time | `2025-06-09T04:08:48Z` |
| Registration cost snapshot | `99380483902` |
| Active keys | `256` |
| Active validators | `8` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `1583970` |
| Max neurons | `256` |
| Validator slots (metadata) | `8` |
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
| `immunity_period` (blocks) | 3600 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5GbLENPLG8Takn1puaz5HorPmrFtDT7i2PojiJsqutbaGwWu` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `3600` blocks |
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

*No miner/validator sections auto-matched.* Open [https://github.com/Satori119/Satori](https://github.com/Satori119/Satori) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/Satori119/Satori](https://github.com/Satori119/Satori)
- **Logo URL:** [https://raw.githubusercontent.com/Satori119/Satori/refs/heads/main/assets/logo.png](https://raw.githubusercontent.com/Satori119/Satori/refs/heads/main/assets/logo.png)
- **Contact:** Akihabara119@outlook.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.006811513 |
| 8104292 | 0.006811448 |
| 8104340 | 0.006811336 |
| 8104388 | 0.006811328 |
| 8104436 | 0.006811294 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

