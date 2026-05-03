# NetUID 40 — Chunking (`ן`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Chunking** (NetUID **40**) (`ן`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `27`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,035.952032945. **Alpha liquidity in pool (`alpha_in`)** = ‎2,077,898.708964397ן‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,979,656.288650596ן‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003386888`** *(also **moving-average price** `0.003407485317438841` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎162,211.272548909ן‎`. **Owner hotkey / coldkey (chain):** `5F9Qvcz22Fwq4cm58o2bShiL6n8BnJmhqXB1cispBpqRfN6w` / `5F9Qvcz22Fwq4cm58o2bShiL6n8BnJmhqXB1cispBpqRfN6w`.
- **Subnet registered at block:** `3372582` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎20.401047567ן‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ן‎` · α-in `‎0.000000000ן‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104408`
- **Liquidity constant `k`:** `14619995645591839967776059165`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Chunking`
- **Symbol (API):** `ן`
- **Rank:** `81`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003386775`
- **Market cap:** `13613309119687.2711165`
- **Market cap Δ 1d:** `-1.524180026470269632`
- **Liquidity:** `14073327430862`
- **Total τ:** `7035835434783`
- **Total α:** `5057321997614993`
- **α in pool:** `2077933135823859`
- **α staked:** `1941616175744601`
- **Price Δ 1h:** `0.138020470671093493`
- **Price Δ 1d:** `-1.628052071176411471`
#### Subnet activity (TAOStats)

- **NetUID (API):** `40`
- **Owner SS58 (API):** `5F9Qvcz22Fwq4cm58o2bShiL6n8BnJmhqXB1cispBpqRfN6w`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `3372582`
- **Registration wall time:** `2024-07-12T21:11:48.002Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `13`
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
- **`immunity_period` (blocks):** 14400
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5F9Qvcz22Fwq4cm58o2bShiL6n8BnJmhqXB1cispBpqRfN6w`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `14400` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `3`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No miner/validator sections auto-matched.* Open [https://github.com/VectorChat/chunking_subnet](https://github.com/VectorChat/chunking_subnet) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/VectorChat/chunking_subnet](https://github.com/VectorChat/chunking_subnet)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.003406082 |
| 8104244 | 0.003391581 |
| 8104292 | 0.003391575 |
| 8104340 | 0.003391566 |
| 8104388 | 0.003391661 |
| 8104436 | 0.003386888 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

