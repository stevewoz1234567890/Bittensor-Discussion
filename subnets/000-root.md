# NetUID 0 — root (`Τ`)

## Overview

The **root network** (NetUID 0) is Bittensor’s top-level coordination layer. TAO holders delegate stake to root validators, who set **weights** on other subnets. Those weights help determine how network **emissions** are allocated across subnets. Root is not an application or “task” subnet like higher netuids; it is the mechanism through which the protocol routes incentive and security across the rest of the network.

### Root snapshot *(block 8104436)*

- **Root tempo:** `100` blocks between epoch strides (see [`SubnetHyperparameters`](https://learnbittensor.org/explore/concept/subnet-hyperparameters)). Validators allocate weight across subnets rather than miners competing inside a commodity task.
- **`tao_in` (pool-facing TAO):** τ5,236,700.393785132
- **Root alpha bookkeeping (`alpha_in` / `alpha_out`):** τ1,370,564.147064066 / τ4,680,049.210763495
- **Reported subnet volume rolling figure:** τ48,487,284.777831234

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `4919910`
- **Liquidity constant `k`:** `7177233808638177988290642266712`

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Root`
- **Symbol (API):** `Τ`
- **Rank:** `0`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `1`
- **Market cap:** `6050613357827561`
- **Market cap Δ 1d:** `0`
- **Liquidity:** `6607264540849198`
- **Total τ:** `5237049972112335`
- **Total α:** `6050613357827561`
- **α in pool:** `1370214568736863`
- **α staked:** `4680398789090698`
- **Price Δ 1h:** `0`
- **Price Δ 1d:** `0`
#### Subnet activity (TAOStats)

- **NetUID (API):** `0`
- **Owner SS58 (API):** `5C4hrfjw9DjXZTzV3MwzrrAr9P1MJhSrvWGWqi1eSuyUpnhM`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration wall time:** `2023-03-20T18:47:48Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `64`
- **Active validators:** `8`
- **Active miners:** `28`
- **Active dual-role:** `4`
- **Emission:** `0`
- **Max neurons:** `64`
- **Validator slots (metadata):** `8`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `100`
- **Min allowed weights (API):** `0`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`


### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 64
- **`subnetwork_n`:** 64
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 0
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 100
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 4611686018427387903
- **`immunity_period` (blocks):** 4096
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5C4hrfjw9DjXZTzV3MwzrrAr9P1MJhSrvWGWqi1eSuyUpnhM`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `4611686018427387903` (min `4611686018427387903`, max `4611686018427387903`)
- **`target_regs_per_interval`:** `64`
- **`immunity_period`:** `4096` blocks
- **`max_regs_per_block`:** `64`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `18446744073709551615`
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

Root: protocol uses **1 τ per root weight unit** in pricing helpers.

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8103860 | 1 |
| 8103908 | 1 |
| 8103956 | 1 |
| 8104004 | 1 |
| 8104052 | 1 |
| 8104100 | 1 |
| 8104148 | 1 |
| 8104196 | 1 |
| 8104244 | 1 |
| 8104292 | 1 |
| 8104340 | 1 |
| 8104388 | 1 |
| 8104436 | 1 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

