# NetUID 82 — uruz (`ᚢ`)

## Overview

**uruz** (NetUID **82**) (`ᚢ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `272`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ86.733128608. **Alpha liquidity in pool (`alpha_in`)** = ‎5,748.133750020ᚢ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎79,855.020468127ᚢ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.015089203`** *(also **moving-average price** `0.009516611928120255` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,004.350686290ᚢ‎`. **Owner hotkey / coldkey (chain):** `5CyG6MKWToCKKZhPhojKAj5QqyRr7BDYc7GPmdC5bPZ4GA3D` / `5FFPqmc9jeuRTrmcphtyLN727fHe2BYdr77KkAYw2CLd1KCb`.
- **Subnet registered at block:** `8026517` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎120.789621192ᚢ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.001918443` · α-out `‎1.000000000ᚢ‎` · α-in `‎0.127140116ᚢ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.015272676`
- **Market cap:** `824609922182.658639216`
- **Liquidity:** `174229549345`
- **Total τ:** `87113937674`
- **Total α:** `85518627593916`
- **α in pool:** `5704017532426`
- **α staked:** `48288480061490`
- **Price Δ 1h:** `4.319084786719877609`
- **Price Δ 1d:** `76.557625502153116962`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `47`
- **Active validators:** `8`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `1927716`
- **Max neurons:** `256`
- **Validators (metadata):** `8`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

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

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


*No `SubnetIdentity` registered on-chain.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.01482108 |
| 8104133 | 0.014862638 |
| 8104181 | 0.015115203 |
| 8104229 | 0.01515335 |
| 8104277 | 0.015089203 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

