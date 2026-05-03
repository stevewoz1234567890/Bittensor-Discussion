# NetUID 76 — Byzantium (`ن`)

## Overview

**Byzantium** (NetUID **76**) (`ن`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `266`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,119.007092825. **Alpha liquidity in pool (`alpha_in`)** = ‎144,507.229750031ن‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎518,495.945519483ن‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007742879`** *(also **moving-average price** `0.00749357626773417` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎17,911.498743839ن‎`. **Owner hotkey / coldkey (chain):** `5Cw4E2tJjsx1mxGaxpJHEAS9fEgjZQt7r7DeHhZ1Ce6yu5cs` / `5FFNhWd881QTWuuiDgkqW4vgiWFDW1QYqPwRB9MZUkH7cMUP`.
- **Subnet registered at block:** `7574784` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎154.086088940ن‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003871504` · α-out `‎1.000000000ن‎` · α-in `‎0.500000000ن‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.007744613`
- **Market cap:** `3482081698906.170903463`
- **Liquidity:** `2237578834915`
- **Total τ:** `1118842070374`
- **Total α:** `662895799191451`
- **α in pool:** `144453540098264`
- **α staked:** `305159849093187`
- **Price Δ 1h:** `0.073886517390402635`
- **Price Δ 1d:** `7.386300373035249009`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `43`
- **Active validators:** `9`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `3872324`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `500000000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 43
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 100
- **Registration recycle cost snapshot (`burn`):** τ0.500000000
- **Owner SS58 (`owner_ss58`):** `5FFNhWd881QTWuuiDgkqW4vgiWFDW1QYqPwRB9MZUkH7cMUP`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.500000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `100` blocks
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


*No links or contacts in chain identity.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.007746057 |
| 8104133 | 0.007745843 |
| 8104181 | 0.007744642 |
| 8104229 | 0.0077436 |
| 8104277 | 0.007742879 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

