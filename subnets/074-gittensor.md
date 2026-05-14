# NetUID 74 — Gittensor (`ل`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Gittensor** (NetUID **74**) (`ل`).

autonomous software development

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `61`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,239.142530464. **Alpha liquidity in pool (`alpha_in`)** = ‎1,225,139.092527116ل‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,173,579.073915766ل‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006706744`** *(also **moving-average price** `0.006674321135506034` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎248,376.206607237ل‎`. **Owner hotkey / coldkey (chain):** `5Dnffftud49iScqvvymjuvS4D1MP4ApenAQG2R5wg4bXGH7L` / `5D1VXeeSdrfyrBdMe4SNwKnRsmzrjXES9dhx6kQkCHhJUPvS`.
- **Subnet registered at block:** `5086205` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎45.606554405ل‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000316123` · α-out `‎1.000000000ل‎` · α-in `‎0.047135098ل‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104374`
- **Liquidity constant `k`:** `10094095602974231152776061824`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Gittensor` |
| Symbol (API) | `ل` |
| Rank | `43` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.006781809` |
| Market cap | `26267912065855.596393663` |
| Market cap Δ 1d | `4.438222994064533688` |
| Liquidity | `16547394865392` |
| Total τ | `8285179558492` |
| Total α | `4398563426873983` |
| α in pool | `1218290769748994` |
| α staked | `2654999095220013` |
| Price Δ 1h | `-0.107216168062632271` |
| Price Δ 1d | `4.26992927064804925` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `74` |
| Owner SS58 (API) | `5D1VXeeSdrfyrBdMe4SNwKnRsmzrjXES9dhx6kQkCHhJUPvS` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5086205` |
| Registration wall time | `2025-03-08T22:34:36Z` |
| Registration cost snapshot | `291874466228` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `16` |
| Active dual-role | `0` |
| Emission | `789353` |
| Max neurons | `256` |
| Validator slots (metadata) | `12` |
| Max validators (API) | `64` |
| Neuron reg. cost | `150000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** The workforce for open source. Compete for rewards by contributing quality code to open source repositories.

**Fetched document title:** Gittensor | Autonomous Software Development

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
| Registration recycle cost snapshot (`burn`) | τ0.150000000 |
| Owner SS58 (`owner_ss58`) | `5D1VXeeSdrfyrBdMe4SNwKnRsmzrjXES9dhx6kQkCHhJUPvS` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.150000000 / τ100.000000000 |
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

*No miner/validator sections auto-matched.* Open [https://github.com/entrius/gittensor/tree/main](https://github.com/entrius/gittensor/tree/main) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://gittensor.io](https://gittensor.io)
- **GitHub:** [https://github.com/entrius/gittensor/tree/main](https://github.com/entrius/gittensor/tree/main)
- **Logo URL:** [https://gittensor.s3.us-east-2.amazonaws.com/gt-logo-white.png](https://gittensor.s3.us-east-2.amazonaws.com/gt-logo-white.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.006706921 |
| 8104292 | 0.006706895 |
| 8104340 | 0.006706759 |
| 8104388 | 0.006706756 |
| 8104436 | 0.006706744 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

