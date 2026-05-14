# NetUID 102 — ConnitoAI (`ვ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**ConnitoAI** (NetUID **102**) (`ვ`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `89`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ958.062016641. **Alpha liquidity in pool (`alpha_in`)** = ‎48,290.081200254ვ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎223,721.119735624ვ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.019840325`** *(also **moving-average price** `0.016374852042645216` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎7,930.140750443ვ‎`. **Owner hotkey / coldkey (chain):** `5EEinUEy3cfBCUyhbvCcYfWU713QCsDoVXqbbRLKFtEqKkC9` / `5HidKLutq4YQgmBPWtLRYzh2cGYgWJRaC4owcz756W87puTL`.
- **Subnet registered at block:** `7840965` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎44.660491723ვ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.008208951` · α-out `‎1.000000000ვ‎` · α-in `‎0.413750738ვ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104346`
- **Liquidity constant `k`:** `46264892578472989001426814`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `ConnitoAI` |
| Symbol (API) | `ვ` |
| Rank | `113` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.019976853` |
| Market cap | `4590584934844.152957687` |
| Market cap Δ 1d | `54.502173689020363128` |
| Liquidity | `1918890274404` |
| Total τ | `959430411495` |
| Total α | `271682030217179` |
| α in pool | `48028579021391` |
| α staked | `181766621195788` |
| Price Δ 1h | `1.053034289286458247` |
| Price Δ 1d | `47.479911002007017252` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `102` |
| Owner SS58 (API) | `5HidKLutq4YQgmBPWtLRYzh2cGYgWJRaC4owcz756W87puTL` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7840965` |
| Registration wall time | `2026-03-28T01:14:48Z` |
| Registration cost snapshot | `658946473389` |
| Active keys | `256` |
| Active validators | `4` |
| Active miners | `3` |
| Active dual-role | `0` |
| Emission | `8266953` |
| Max neurons | `256` |
| Validator slots (metadata) | `4` |
| Max validators (API) | `64` |
| Neuron reg. cost | `2224407` |
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
| Registration recycle cost snapshot (`burn`) | τ0.002237463 |
| Owner SS58 (`owner_ss58`) | `5HidKLutq4YQgmBPWtLRYzh2cGYgWJRaC4owcz756W87puTL` |


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


*No links or contacts in chain identity.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.019972116 |
| 8104292 | 0.019962777 |
| 8104340 | 0.019841161 |
| 8104388 | 0.019842306 |
| 8104436 | 0.019840325 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

