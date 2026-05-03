# NetUID 86 — ⚒ (`ᚳ`)

## Overview

**⚒** (NetUID **86**) (`ᚳ`).

Methodical. Strong foundation. And...Sr Data Scientist, 4th team member, onboard.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `276`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,171.588688255. **Alpha liquidity in pool (`alpha_in`)** = ‎449,862.202256752ᚳ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,149,093.296278205ᚳ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004827016`** *(also **moving-average price** `0.004740098956972361` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎24,018.467450433ᚳ‎`. **Owner hotkey / coldkey (chain):** `5G3xU5vFLHWP7f8wGA755QkiwUXDktKHwW3dFvU9GH4MTRby` / `5ERnAHRQjTrLwtTcBgKqDu7j5YSL23eetTtnFgqb5jaKLqrq`.
- **Subnet registered at block:** `6914378` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎184.348371055ᚳ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002413512` · α-out `‎1.000000000ᚳ‎` · α-in `‎0.500000000ᚳ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004826925`
- **Market cap:** `5468528506028.11167195`
- **Liquidity:** `4342677777564`
- **Total τ:** `2171387276256`
- **Total α:** `1598857268929414`
- **α in pool:** `449828928626029`
- **α staked:** `683092860303385`
- **Price Δ 1h:** `-0.058160552941424931`
- **Price Δ 1d:** `4.738884312835410495`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `2413457`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Methodical. Strong foundation. And...Sr Data Scientist, 4th team member, onboard.

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
- **Owner SS58 (`owner_ss58`):** `5ERnAHRQjTrLwtTcBgKqDu7j5YSL23eetTtnFgqb5jaKLqrq`

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


Methodical. Strong foundation. And...Sr Data Scientist, 4th team member, onboard.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Logo URL:** [https://www.publicdomainpictures.net/pictures/390000/velka/image-1614231152FSV.jpg](https://www.publicdomainpictures.net/pictures/390000/velka/image-1614231152FSV.jpg)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.004813256 |
| 8104133 | 0.004813391 |
| 8104181 | 0.004813548 |
| 8104229 | 0.004826924 |
| 8104277 | 0.004827016 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

