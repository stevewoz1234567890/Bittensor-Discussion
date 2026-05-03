# NetUID 73 — Parked (`ك`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Parked** (NetUID **73**) (`ك`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `60`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,785.011420575. **Alpha liquidity in pool (`alpha_in`)** = ‎1,940,825.347337970ك‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,763,052.000203688ك‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004023830`** *(also **moving-average price** `0.004000430228188634` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎556,994.560192363ك‎`. **Owner hotkey / coldkey (chain):** `5Dnkprjf9fUrvWq3ZfFP8WrUNSjQws6UoHkbDfR1bQK8pFhW` / `5CUjS24TsKfKBc8kvHnjubAiAkkxwHF4u6vDLBE9jg4CGBJm`.
- **Subnet registered at block:** `5160047` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎45.093535814ك‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ك‎` · α-in `‎0.000000000ك‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104375`
- **Liquidity constant `k`:** `15109347494367537624336732750`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Parked`
- **Symbol (API):** `ك`
- **Rank:** `79`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004023948`
- **Market cap:** `14409055608278.433288816`
- **Market cap Δ 1d:** `0.884538536606234421`
- **Liquidity:** `15594791693496`
- **Total τ:** `7785126984973`
- **Total α:** `4703644347541658`
- **α in pool:** `1940796627720774`
- **α staked:** `1640028872081518`
- **Price Δ 1h:** `-0.000497021845104136`
- **Price Δ 1d:** `0.765088352141473608`
#### Subnet activity (TAOStats)

- **NetUID (API):** `73`
- **Owner SS58 (API):** `5CUjS24TsKfKBc8kvHnjubAiAkkxwHF4u6vDLBE9jg4CGBJm`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `5160047`
- **Registration wall time:** `2025-03-19T04:43:00.001Z`
- **Registration cost snapshot:** `246711333592`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `1`
- **Active dual-role:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `11`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

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
- **Owner SS58 (`owner_ss58`):** `5CUjS24TsKfKBc8kvHnjubAiAkkxwHF4u6vDLBE9jg4CGBJm`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `120`
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


*No links or contacts in chain identity.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004023937 |
| 8104292 | 0.004023929 |
| 8104340 | 0.004023834 |
| 8104388 | 0.004023833 |
| 8104436 | 0.00402383 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

