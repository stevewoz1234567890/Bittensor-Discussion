# NetUID 36 — automata (`כ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**automata** (NetUID **36**) (`כ`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `23`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ480.992311192. **Alpha liquidity in pool (`alpha_in`)** = ‎59,434.700861570כ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎211,734.977677967כ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008092882`** *(also **moving-average price** `0.00784396706148982` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎2,307.390601984כ‎`. **Owner hotkey / coldkey (chain):** `5Eh5G8BD8NVHfqeWdKhNbrssDKKV8B74a2VghHzr2YYWrwmK` / `5GLGTwG6n4dFPMwcN5BWJ1tw7fwcgQsjxCV4xb5ft3vKLUxc`.
- **Subnet registered at block:** `7894898` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎11.536723236כ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003891585` · α-out `‎1.000000000כ‎` · α-in `‎0.480865214כ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104412`
- **Liquidity constant `k`:** `28587634132411707953691440`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Unknown`
- **Symbol (API):** `כ`
- **Rank:** `125`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.008005058`
- **Market cap:** `1483132921929.118503972`
- **Market cap Δ 1d:** `12.056948831911725426`
- **Liquidity:** `954951736103`
- **Total τ:** `477473267626`
- **Total α:** `270824255454034`
- **α in pool:** `59647096682774`
- **α staked:** `125627378771260`
- **Price Δ 1h:** `-2.076776877711600399`
- **Price Δ 1d:** `7.371967736332304779`
#### Subnet activity (TAOStats)

- **NetUID (API):** `36`
- **Owner SS58 (API):** `5GLGTwG6n4dFPMwcN5BWJ1tw7fwcgQsjxCV4xb5ft3vKLUxc`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `7894898`
- **Registration wall time:** `2026-04-04T13:41:12Z`
- **Registration cost snapshot:** `700897161592`
- **Active keys:** `154`
- **Active validators:** `10`
- **Active miners:** `1`
- **Active dual-role:** `1`
- **Emission:** `3876669`
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
- **`subnetwork_n`:** 154
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
- **Owner SS58 (`owner_ss58`):** `5GLGTwG6n4dFPMwcN5BWJ1tw7fwcgQsjxCV4xb5ft3vKLUxc`

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
| 8104196 | 0.008005342 |
| 8104244 | 0.008000738 |
| 8104292 | 0.007998125 |
| 8104340 | 0.008094449 |
| 8104388 | 0.008094155 |
| 8104436 | 0.008092882 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

