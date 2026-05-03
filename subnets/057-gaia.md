# NetUID 57 — gaia (`ح`)

## Overview

**gaia** (NetUID **57**) (`ح`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `185`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,158.707295155. **Alpha liquidity in pool (`alpha_in`)** = ‎98,318.887737893ح‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎200,731.197283384ح‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011785253`** *(also **moving-average price** `0.007898979587480426` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎5,240.478615016ح‎`. **Owner hotkey / coldkey (chain):** `5Ejcqsbx3MFhNqiDjPJVvBtYWNvXXcvSJ3ibMCrzfCU3g5MN` / `5HdpnCSYczg52ZaiBKmgwJPFnVpyyu27o1GHgLcj8217xxr7`.
- **Subnet registered at block:** `8057320` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎94.112670605ح‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003652066` · α-out `‎1.000000000ح‎` · α-in `‎0.309883209ح‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.011785357`
- **Market cap:** `3325355328383.205825111`
- **Liquidity:** `2317335494644`
- **Total τ:** `1158662834328`
- **Total α:** `299033054916723`
- **α in pool:** `98314600085225`
- **α staked:** `183845314831498`
- **Price Δ 1h:** `9.382700236903593463`
- **Price Δ 1d:** `12.388338630254138717`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `108`
- **Active validators:** `6`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `3650859`
- **Max neurons:** `256`
- **Validators (metadata):** `6`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

## Operational parameters — registration, limits, economics (chain)


### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 108
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5HdpnCSYczg52ZaiBKmgwJPFnVpyyu27o1GHgLcj8217xxr7`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `4611686018427387903`)
- **`target_regs_per_interval`:** `2`
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
- **`yuma_version`:** `3`
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
| 8104024 | 0.011649242 |
| 8104072 | 0.011740603 |
| 8104120 | 0.011739321 |
| 8104168 | 0.011786948 |
| 8104216 | 0.011785253 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

