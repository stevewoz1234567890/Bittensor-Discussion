# NetUID 39 — deprecated (`מ`)

## Overview

**deprecated** (NetUID **39**) (`מ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `229`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ16,728.160594136. **Alpha liquidity in pool (`alpha_in`)** = ‎2,624,700.218515800מ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,433,028.747021801מ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006405913`** *(also **moving-average price** `0.006594568956643343` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎973,638.535796555מ‎`. **Owner hotkey / coldkey (chain):** `5G3qVaXzKMPDm5AJ3dpzbpUC27kpccBvDwzSWXrq8M6qMmbC` / `5CQKh1G5MKRyBEPCY7cHRW1okvj2LxjK94cgjsD9c24wrpCN`.
- **Subnet registered at block:** `3280104` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎173.030651148מ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000מ‎` · α-in `‎0.000000000מ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.006405934`
- **Market cap:** `24753746723624.498523894`
- **Liquidity:** `33541816963646`
- **Total τ:** `16728188427448`
- **Total α:** `5057653965537601`
- **α in pool:** `2624695873575744`
- **α staked:** `1239494223235197`
- **Price Δ 1h:** `0.005932351830926724`
- **Price Δ 1d:** `-2.896932960600850744`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

deprecated

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
- **`immunity_period` (blocks):** 15000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CQKh1G5MKRyBEPCY7cHRW1okvj2LxjK94cgjsD9c24wrpCN`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `15000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `20`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `500000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No miner/validator sections auto-matched.* Open [https://github.com/deprecated/deprecated](https://github.com/deprecated/deprecated) for requirements.

## On-chain identity — description


deprecated

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/deprecated/deprecated](https://github.com/deprecated/deprecated)
- **Discord (handle / invite hint):** `deprecated`
- **Logo URL:** [https://deprecated.png](https://deprecated.png)
- **Contact:** deprecated@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.006405417 |
| 8104133 | 0.006405411 |
| 8104181 | 0.006405936 |
| 8104229 | 0.006405923 |
| 8104277 | 0.006405913 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.022144797 |
| 2026-03-10T23:59:48Z | 7718257 | 0.022337119 |
| 2026-03-11T23:59:48Z | 7725455 | 0.021972859 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.022813966 |
| 2026-03-13T23:59:48Z | 7739841 | 0.023907394 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.023769113 |
| 2026-03-15T23:59:48Z | 7754226 | 0.021242789 |
| 2026-03-16T23:59:48Z | 7761426 | 0.020893498 |
| 2026-03-17T23:59:48Z | 7768619 | 0.020605316 |
| 2026-03-18T23:59:48Z | 7775819 | 0.02093089 |
| 2026-03-19T23:59:48Z | 7783014 | 0.02006974594473303583 |
| 2026-03-20T23:59:48Z | 7790201 | 0.021730929 |
| 2026-03-21T23:59:48Z | 7797398 | 0.021095938 |
| 2026-03-22T23:59:48Z | 7804598 | 0.020664932 |
| 2026-03-23T23:59:48Z | 7811798 | 0.020149861 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.02367460378265777028 |
| 2026-03-25T23:59:48Z | 7826196 | 0.022818681 |
| 2026-03-26T23:59:48Z | 7833396 | 0.02173551 |
| 2026-03-27T23:59:48Z | 7840596 | 0.022499658 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.02204379 |
| 2026-03-29T23:59:48Z | 7854902 | 0.020850685 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.022788293 |
| 2026-03-31T23:59:48Z | 7869291 | 0.021670794 |
| 2026-04-01T23:59:48Z | 7876474 | 0.022081553 |
| 2026-04-02T23:59:48Z | 7883622 | 0.022943713 |
| 2026-04-03T23:59:48Z | 7890794 | 0.023147851 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.024453452 |
| 2026-04-05T23:59:48Z | 7905188 | 0.023842532 |
| 2026-04-06T23:59:48Z | 7912388 | 0.022724114 |
| 2026-04-07T23:59:48Z | 7919588 | 0.020605824 |
| 2026-04-08T23:59:48Z | 7926788 | 0.019302547 |
| 2026-04-09T23:59:48Z | 7933987 | 0.008489859 |
| 2026-04-10T23:59:48Z | 7941184 | 0.008134231 |
| 2026-04-11T23:59:48Z | 7948384 | 0.009305395 |
| 2026-04-12T23:59:48Z | 7955584 | 0.007815933 |
| 2026-04-13T23:59:48Z | 7962784 | 0.007087332 |
| 2026-04-14T23:59:48Z | 7969979 | 0.007168463 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.007070701 |
| 2026-04-16T23:59:48Z | 7984379 | 0.007557167 |
| 2026-04-17T23:59:48Z | 7991579 | 0.007425308 |
| 2026-04-18T23:59:48Z | 7998779 | 0.006562013 |
| 2026-04-19T23:59:48Z | 8005979 | 0.006676172 |
| 2026-04-20T23:59:48Z | 8013179 | 0.006368211 |
| 2026-04-21T23:59:48Z | 8020376 | 0.006391833 |
| 2026-04-22T23:59:48Z | 8027562 | 0.006448219 |
| 2026-04-23T23:59:48Z | 8034762 | 0.006513325 |
| 2026-04-24T23:59:48Z | 8041962 | 0.006537187 |
| 2026-04-25T23:59:48Z | 8049151 | 0.00663684 |
| 2026-04-26T23:59:48Z | 8056274 | 0.00645901 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.00654374 |
| 2026-04-28T23:59:48Z | 8070646 | 0.006777955 |
| 2026-04-29T23:59:48Z | 8077790 | 0.006826372 |
| 2026-04-30T23:59:48Z | 8084984 | 0.006939707 |
| 2026-05-01T23:59:48Z | 8092168 | 0.006720133 |
| 2026-05-02T23:59:48Z | 8099357 | 0.006652725 |
| 2026-05-03T16:10:00Z | 8104202 | 0.006405934 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

