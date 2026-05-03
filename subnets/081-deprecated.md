# NetUID 81 — deprecated (`ᚠ`)

## Overview

**deprecated** (NetUID **81**) (`ᚠ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `271`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ20,595.306864721. **Alpha liquidity in pool (`alpha_in`)** = ‎2,369,543.195028965ᚠ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,002,494.570414524ᚠ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008696804`** *(also **moving-average price** `0.008879065979272127` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎767,235.658224492ᚠ‎`. **Owner hotkey / coldkey (chain):** `5F9uEDDovurwEJihzZSpKypipVy84EEAPHTt3EfepTjcQfij` / `5DUELqJMeY6tA7652ooUUvU9TgUCi5hnv9o66nC8Zjw7BtW5`.
- **Subnet registered at block:** `5203057` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎202.513360156ᚠ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ᚠ‎` · α-in `‎0.000000000ᚠ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.008696842`
- **Market cap:** `31035372958706.372534278`
- **Liquidity:** `41202849643913`
- **Total τ:** `20595351666002`
- **Total α:** `4371962765443489`
- **α in pool:** `2369538043569365`
- **α staked:** `1199041557934994`
- **Price Δ 1h:** `-0.000747392147576144`
- **Price Δ 1d:** `-2.458971346844344032`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `7`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `7`
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
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 10799
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5DUELqJMeY6tA7652ooUUvU9TgUCi5hnv9o66nC8Zjw7BtW5`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10799` blocks
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
| 8104085 | 0.008696887 |
| 8104133 | 0.008696878 |
| 8104181 | 0.008696845 |
| 8104229 | 0.008696821 |
| 8104277 | 0.008696804 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.017824381 |
| 2026-03-10T23:59:48Z | 7718257 | 0.018371296 |
| 2026-03-11T23:59:48Z | 7725455 | 0.018785396 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.019447446 |
| 2026-03-13T23:59:48Z | 7739841 | 0.019706913 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.021665234 |
| 2026-03-15T23:59:48Z | 7754226 | 0.021575644 |
| 2026-03-16T23:59:48Z | 7761426 | 0.021818948 |
| 2026-03-17T23:59:48Z | 7768619 | 0.020903484 |
| 2026-03-18T23:59:48Z | 7775819 | 0.020991702 |
| 2026-03-19T23:59:48Z | 7783014 | 0.02099544355430684459 |
| 2026-03-20T23:59:48Z | 7790201 | 0.022395353 |
| 2026-03-21T23:59:48Z | 7797398 | 0.022067114 |
| 2026-03-22T23:59:48Z | 7804598 | 0.021721191 |
| 2026-03-23T23:59:48Z | 7811798 | 0.02211838 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.02421053295780671756 |
| 2026-03-25T23:59:48Z | 7826196 | 0.025033038 |
| 2026-03-26T23:59:48Z | 7833396 | 0.02484797 |
| 2026-03-27T23:59:48Z | 7840596 | 0.026924156 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.027599665 |
| 2026-03-29T23:59:48Z | 7854902 | 0.025541794 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.026647877 |
| 2026-03-31T23:59:48Z | 7869291 | 0.026266756 |
| 2026-04-01T23:59:48Z | 7876474 | 0.02668877 |
| 2026-04-02T23:59:48Z | 7883622 | 0.02712235 |
| 2026-04-03T23:59:48Z | 7890794 | 0.028194727 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.028584727 |
| 2026-04-05T23:59:48Z | 7905188 | 0.028359383 |
| 2026-04-06T23:59:48Z | 7912388 | 0.026910187 |
| 2026-04-07T23:59:48Z | 7919588 | 0.026308626 |
| 2026-04-08T23:59:48Z | 7926788 | 0.026279863 |
| 2026-04-09T23:59:48Z | 7933987 | 0.010884211 |
| 2026-04-10T23:59:48Z | 7941184 | 0.009919478 |
| 2026-04-11T23:59:48Z | 7948384 | 0.011350163 |
| 2026-04-12T23:59:48Z | 7955584 | 0.009851988 |
| 2026-04-13T23:59:48Z | 7962784 | 0.009388601 |
| 2026-04-14T23:59:48Z | 7969979 | 0.01045839 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.01006907 |
| 2026-04-16T23:59:48Z | 7984379 | 0.009460965 |
| 2026-04-17T23:59:48Z | 7991579 | 0.009388139 |
| 2026-04-18T23:59:48Z | 7998779 | 0.009012628 |
| 2026-04-19T23:59:48Z | 8005979 | 0.008375197 |
| 2026-04-20T23:59:48Z | 8013179 | 0.008350713 |
| 2026-04-21T23:59:48Z | 8020376 | 0.008427285 |
| 2026-04-22T23:59:48Z | 8027562 | 0.008424522 |
| 2026-04-23T23:59:48Z | 8034762 | 0.008428491 |
| 2026-04-24T23:59:48Z | 8041962 | 0.008568128 |
| 2026-04-25T23:59:48Z | 8049151 | 0.008598414 |
| 2026-04-26T23:59:48Z | 8056274 | 0.008567519 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.008489817 |
| 2026-04-28T23:59:48Z | 8070646 | 0.008445111 |
| 2026-04-29T23:59:48Z | 8077790 | 0.008741439 |
| 2026-04-30T23:59:48Z | 8084984 | 0.00884432 |
| 2026-05-01T23:59:48Z | 8092168 | 0.008917582 |
| 2026-05-02T23:59:48Z | 8099357 | 0.008914613 |
| 2026-05-03T16:10:00Z | 8104202 | 0.008696842 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

