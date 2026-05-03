# NetUID 95 — nion (`ᚅ`)

## Overview

**nion** (NetUID **95**) (`ᚅ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `223`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ19,230.552292561. **Alpha liquidity in pool (`alpha_in`)** = ‎580,242.260669103ᚅ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,977,331.588322102ᚅ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.033071314`** *(also **moving-average price** `0.03176576318219304` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎234,248.557797175ᚅ‎`. **Owner hotkey / coldkey (chain):** `5ExqqyEBXLpGwqy6sSVrauozhcyAKBaMz1y5x9wAYSk7n7HP` / `5D5UhUuc6cC47CXUBHyBkpDBrdeyeL6bpWGAreZgNm5WTyrg`.
- **Subnet registered at block:** `5403674` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎158.237015953ᚅ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.016535615` · α-out `‎1.000000000ᚅ‎` · α-in `‎0.500000000ᚅ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.033070699`
- **Market cap:** `62357915376175.105099292`
- **Liquidity:** `38419139519935`
- **Total τ:** `19230169410162`
- **Total α:** `2557559513876308`
- **α in pool:** `580240838265124`
- **α staked:** `1305353275611184`
- **Price Δ 1h:** `-1.605524683920751605`
- **Price Δ 1d:** `3.792537446046361549`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `16589065`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

## Operational parameters — registration, limits, economics (chain)


### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 256
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
- **Owner SS58 (`owner_ss58`):** `5D5UhUuc6cC47CXUBHyBkpDBrdeyeL6bpWGAreZgNm5WTyrg`

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
| 8104024 | 0.033604416 |
| 8104072 | 0.033554843 |
| 8104120 | 0.033181004 |
| 8104168 | 0.033176817 |
| 8104216 | 0.033071314 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

