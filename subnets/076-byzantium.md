# NetUID 76 — Byzantium (`ن`)

## Overview

**Byzantium** (NetUID **76**) (`ن`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `204`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,118.897524400. **Alpha liquidity in pool (`alpha_in`)** = ‎144,459.379795224ن‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎518,455.022221248ن‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007744674`** *(also **moving-average price** `0.007490203715860844` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎17,911.302801214ن‎`. **Owner hotkey / coldkey (chain):** `5Cw4E2tJjsx1mxGaxpJHEAS9fEgjZQt7r7DeHhZ1Ce6yu5cs` / `5FFNhWd881QTWuuiDgkqW4vgiWFDW1QYqPwRB9MZUkH7cMUP`.
- **Subnet registered at block:** `7574784` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎118.170099215ن‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003872339` · α-out `‎1.000000000ن‎` · α-in `‎0.500000000ن‎`.

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

## Operational parameters — registration, limits, economics (chain)


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
| 8104024 | 0.007746118 |
| 8104072 | 0.00774602 |
| 8104120 | 0.007745828 |
| 8104168 | 0.007744578 |
| 8104216 | 0.007744674 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.008757173 |
| 2026-03-10T23:59:48Z | 7718257 | 0.008869528 |
| 2026-03-11T23:59:48Z | 7725455 | 0.010379652 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.008779051 |
| 2026-03-13T23:59:48Z | 7739841 | 0.007386632 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.008007784 |
| 2026-03-15T23:59:48Z | 7754226 | 0.008444105 |
| 2026-03-16T23:59:48Z | 7761426 | 0.007842202 |
| 2026-03-17T23:59:48Z | 7768619 | 0.007355242 |
| 2026-03-18T23:59:48Z | 7775819 | 0.006726148 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00693567517036601926 |
| 2026-03-20T23:59:48Z | 7790201 | 0.00641958 |
| 2026-03-21T23:59:48Z | 7797398 | 0.006506612 |
| 2026-03-22T23:59:48Z | 7804598 | 0.006746431 |
| 2026-03-23T23:59:48Z | 7811798 | 0.007859181 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00813141366057121807 |
| 2026-03-25T23:59:48Z | 7826196 | 0.007210661 |
| 2026-03-26T23:59:48Z | 7833396 | 0.007403857 |
| 2026-03-27T23:59:48Z | 7840596 | 0.007832837 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.008068406 |
| 2026-03-29T23:59:48Z | 7854902 | 0.008480954 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.007021761 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005787871 |
| 2026-04-01T23:59:48Z | 7876474 | 0.00591136 |
| 2026-04-02T23:59:48Z | 7883622 | 0.006101607 |
| 2026-04-03T23:59:48Z | 7890794 | 0.007165631 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.007501472 |
| 2026-04-05T23:59:48Z | 7905188 | 0.0072953 |
| 2026-04-06T23:59:48Z | 7912388 | 0.007040293 |
| 2026-04-07T23:59:48Z | 7919588 | 0.006962335 |
| 2026-04-08T23:59:48Z | 7926788 | 0.006672664 |
| 2026-04-09T23:59:48Z | 7933987 | 0.005150483 |
| 2026-04-10T23:59:48Z | 7941184 | 0.005997307 |
| 2026-04-11T23:59:48Z | 7948384 | 0.006209962 |
| 2026-04-12T23:59:48Z | 7955584 | 0.005919351 |
| 2026-04-13T23:59:48Z | 7962784 | 0.006099637 |
| 2026-04-14T23:59:48Z | 7969979 | 0.00591395 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.005781934 |
| 2026-04-16T23:59:48Z | 7984379 | 0.006481242 |
| 2026-04-17T23:59:48Z | 7991579 | 0.006263048 |
| 2026-04-18T23:59:48Z | 7998779 | 0.006259088 |
| 2026-04-19T23:59:48Z | 8005979 | 0.006140653 |
| 2026-04-20T23:59:48Z | 8013179 | 0.006287538 |
| 2026-04-21T23:59:48Z | 8020376 | 0.00583127 |
| 2026-04-22T23:59:48Z | 8027562 | 0.005830066 |
| 2026-04-23T23:59:48Z | 8034762 | 0.006013503 |
| 2026-04-24T23:59:48Z | 8041962 | 0.006008128 |
| 2026-04-25T23:59:48Z | 8049151 | 0.006072702 |
| 2026-04-26T23:59:48Z | 8056274 | 0.005979049 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.006853612 |
| 2026-04-28T23:59:48Z | 8070646 | 0.006987169 |
| 2026-04-29T23:59:48Z | 8077790 | 0.007096961 |
| 2026-04-30T23:59:48Z | 8084984 | 0.007168468 |
| 2026-05-01T23:59:48Z | 8092168 | 0.007223356 |
| 2026-05-02T23:59:48Z | 8099357 | 0.007383722 |
| 2026-05-03T16:10:00Z | 8104202 | 0.007744613 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

