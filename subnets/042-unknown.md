# NetUID 42 — Unknown (`ס`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Unknown** (NetUID **42**) (`ס`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `29`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,884.527767849. **Alpha liquidity in pool (`alpha_in`)** = ‎2,443,445.357796891ס‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,231,566.294639945ס‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003636812`** *(also **moving-average price** `0.003670833772048354` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎342,971.566830110ס‎`. **Owner hotkey / coldkey (chain):** `5Gbdb5s2WrRaFXTgMUiVNBKACe3cgSLwZNyK2Vwvjfvf6jUJ` / `5EC5HHfLqgmr8cdt2MAW5nJMG9n3jKF1QhZb1gYTgiJGNMo5`.
- **Subnet registered at block:** `3613591` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎21.785034863ס‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ס‎` · α-in `‎0.000000000ס‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104406`
- **Liquidity constant `k`:** `21708858130568213144541957459`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Unknown`
- **Symbol (API):** `ס`
- **Rank:** `68`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003636841`
- **Market cap:** `16593582733605.061657564`
- **Market cap Δ 1d:** `-1.688433758662188466`
- **Liquidity:** `17770950026054`
- **Total τ:** `8884564206432`
- **Total α:** `4674778652436836`
- **α in pool:** `2443435338422164`
- **α staked:** `2119200953240040`
- **Price Δ 1h:** `-0.005911374474300093`
- **Price Δ 1d:** `-1.779789140048104891`
#### Subnet activity (TAOStats)

- **NetUID (API):** `42`
- **Owner SS58 (API):** `5EC5HHfLqgmr8cdt2MAW5nJMG9n3jKF1QhZb1gYTgiJGNMo5`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `3613591`
- **Registration wall time:** `2024-08-15T20:16:48.002Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `10`
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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5EC5HHfLqgmr8cdt2MAW5nJMG9n3jKF1QhZb1gYTgiJGNMo5`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
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
| 8104196 | 0.003636842 |
| 8104244 | 0.003636831 |
| 8104292 | 0.003636825 |
| 8104340 | 0.003636815 |
| 8104388 | 0.003636815 |
| 8104436 | 0.003636812 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

