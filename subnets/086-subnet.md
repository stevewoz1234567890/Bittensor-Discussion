# NetUID 86 — ⚒ (`ᚳ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**⚒** (NetUID **86**) (`ᚳ`).

Methodical. Strong foundation. And...Sr Data Scientist, 4th team member, onboard.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `73`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,172.422281783. **Alpha liquidity in pool (`alpha_in`)** = ‎449,847.531685000ᚳ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,149,315.198436793ᚳ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004829025`** *(also **moving-average price** `0.004743494791910052` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎24,019.296684307ᚳ‎`. **Owner hotkey / coldkey (chain):** `5G3xU5vFLHWP7f8wGA755QkiwUXDktKHwW3dFvU9GH4MTRby` / `5ERnAHRQjTrLwtTcBgKqDu7j5YSL23eetTtnFgqb5jaKLqrq`.
- **Subnet registered at block:** `6914378` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎48.760472341ᚳ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002414510` · α-out `‎1.000000000ᚳ‎` · α-in `‎0.500000000ᚳ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104362`
- **Liquidity constant `k`:** `977258801237578090794355000`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `⚒`
- **Symbol (API):** `ᚳ`
- **Rank:** `107`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004826925`
- **Market cap:** `5468528506028.11167195`
- **Market cap Δ 1d:** `5.339298186837610579`
- **Liquidity:** `4342677777564`
- **Total τ:** `2171387276256`
- **Total α:** `1598857268929414`
- **α in pool:** `449828928626029`
- **α staked:** `683092860303385`
- **Price Δ 1h:** `-0.058160552941424931`
- **Price Δ 1d:** `4.738884312835410495`
#### Subnet activity (TAOStats)

- **NetUID (API):** `86`
- **Owner SS58 (API):** `5ERnAHRQjTrLwtTcBgKqDu7j5YSL23eetTtnFgqb5jaKLqrq`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `6914378`
- **Registration wall time:** `2025-11-19T04:51:12.001Z`
- **Registration cost snapshot:** `208695298504`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `2413457`
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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Logo URL:** [https://www.publicdomainpictures.net/pictures/390000/velka/image-1614231152FSV.jpg](https://www.publicdomainpictures.net/pictures/390000/velka/image-1614231152FSV.jpg)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004826956 |
| 8104292 | 0.00482706 |
| 8104340 | 0.004827102 |
| 8104388 | 0.004827286 |
| 8104436 | 0.004829029 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

