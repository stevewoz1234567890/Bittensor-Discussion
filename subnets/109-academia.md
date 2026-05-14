# NetUID 109 — Academia (`՞`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Academia** (NetUID **109**) (`՞`).

Academia: where builders become subnet owners.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `96`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,278.331672393. **Alpha liquidity in pool (`alpha_in`)** = ‎201,814.588058757՞‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎813,288.052667563՞‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006333144`** *(also **moving-average price** `0.00617447099648416` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎22,448.494223272՞‎`. **Owner hotkey / coldkey (chain):** `5DyQkk4x6CwDtjtxe1NG2aMgQVXe9ZpZdT14SdYYwEVd3XUk` / `5EZcsP7SqGLNfXujcX6ZRJ3epRQ2yCDXURjr8XcaEY45eZdm`.
- **Subnet registered at block:** `7257480` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎59.768200905՞‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003166568` · α-out `‎1.000000000՞‎` · α-in `‎0.500000000՞‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104339`
- **Liquidity constant `k`:** `257985979866455203158795501`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Academia` |
| Symbol (API) | `՞` |
| Rank | `115` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.006293581` |
| Market cap | `4331695648721.370937791` |
| Market cap Δ 1d | `6.261685629322546882` |
| Liquidity | `2546986598515` |
| Total τ | `1273595072902` |
| Total α | `1014782070596411` |
| α in pool | `202331792601679` |
| α staked | `485940217994732` |
| Price Δ 1h | `-0.12723754716858372` |
| Price Δ 1d | `5.213743227271131499` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `109` |
| Owner SS58 (API) | `5EZcsP7SqGLNfXujcX6ZRJ3epRQ2yCDXURjr8XcaEY45eZdm` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7257480` |
| Registration wall time | `2026-01-05T21:25:12Z` |
| Registration cost snapshot | `279657398124` |
| Active keys | `256` |
| Active validators | `14` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `3146787` |
| Max neurons | `256` |
| Validator slots (metadata) | `14` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Academia

We're building a Bittensor subnet incubation academy - modeled after La Masia, where promising subnet ideas are developed in-house on mainnet and graduated into dedicated subnets. **Where builders become subnet owners.**

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Academia: where builders become subnet owners. Contribute to fx-integral/academia development by creating an account on GitHub.

**Fetched document title:** GitHub - fx-integral/academia: Academia: where builders become subnet owners · GitHub

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
| Owner SS58 (`owner_ss58`) | `5EZcsP7SqGLNfXujcX6ZRJ3epRQ2yCDXURjr8XcaEY45eZdm` |


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

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/fx-integral/academia/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/fx-integral/academia](https://github.com/fx-integral/academia)
- **Discord:** [https://discord.gg/invite/m9J8QTf5JT](https://discord.gg/invite/m9J8QTf5JT)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.006293337 |
| 8104292 | 0.006293329 |
| 8104340 | 0.006332608 |
| 8104388 | 0.006332945 |
| 8104436 | 0.006333151 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

