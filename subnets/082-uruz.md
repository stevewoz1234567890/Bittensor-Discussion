# NetUID 82 — uruz (`ᚢ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**uruz** (NetUID **82**) (`ᚢ`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `69`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ86.092960935. **Alpha liquidity in pool (`alpha_in`)** = ‎5,831.658060766ᚢ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎79,949.847369144ᚢ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.014763299`** *(also **moving-average price** `0.009586853440850973` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,007.293059046ᚢ‎`. **Owner hotkey / coldkey (chain):** `5CyG6MKWToCKKZhPhojKAj5QqyRr7BDYc7GPmdC5bPZ4GA3D` / `5FFPqmc9jeuRTrmcphtyLN727fHe2BYdr77KkAYw2CLd1KCb`.
- **Subnet registered at block:** `8026517` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎30.648929651ᚢ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.001913197` · α-out `‎1.000000000ᚢ‎` · α-in `‎0.129591360ᚢ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104366`
- **Liquidity constant `k`:** `502064709611805094176210`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Unknown`
- **Symbol (API):** `ᚢ`
- **Rank:** `128`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.015272676`
- **Market cap:** `824609922182.658639216`
- **Market cap Δ 1d:** `95.936369050434585605`
- **Liquidity:** `174229549345`
- **Total τ:** `87113937674`
- **Total α:** `85518627593916`
- **α in pool:** `5704017532426`
- **α staked:** `48288480061490`
- **Price Δ 1h:** `4.319084786719877609`
- **Price Δ 1d:** `76.557625502153116962`
#### Subnet activity (TAOStats)

- **NetUID (API):** `82`
- **Owner SS58 (API):** `5FFPqmc9jeuRTrmcphtyLN727fHe2BYdr77KkAYw2CLd1KCb`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `8026517`
- **Registration wall time:** `2026-04-22T20:29:12Z`
- **Registration cost snapshot:** `509096747134`
- **Active keys:** `47`
- **Active validators:** `8`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `1927716`
- **Max neurons:** `256`
- **Validator slots (metadata):** `8`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 47
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5FFPqmc9jeuRTrmcphtyLN727fHe2BYdr77KkAYw2CLd1KCb`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

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
| 8104244 | 0.015132415 |
| 8104292 | 0.015023382 |
| 8104340 | 0.014834741 |
| 8104388 | 0.014824931 |
| 8104436 | 0.014763299 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

