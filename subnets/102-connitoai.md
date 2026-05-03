# NetUID 102 — ConnitoAI (`ვ`)

## Overview

**ConnitoAI** (NetUID **102**) (`ვ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `292`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ959.731906624. **Alpha liquidity in pool (`alpha_in`)** = ‎48,075.535630642ვ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎223,712.417677259ვ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.019963612`** *(also **moving-average price** `0.016288130544126034` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎7,926.844936389ვ‎`. **Owner hotkey / coldkey (chain):** `5EEinUEy3cfBCUyhbvCcYfWU713QCsDoVXqbbRLKFtEqKkC9` / `5HidKLutq4YQgmBPWtLRYzh2cGYgWJRaC4owcz756W87puTL`.
- **Subnet registered at block:** `7840965` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎146.498095108ვ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.008240521` · α-out `‎1.000000000ვ‎` · α-in `‎0.412741647ვ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.019976853`
- **Market cap:** `4590584934844.152957687`
- **Liquidity:** `1918890274404`
- **Total τ:** `959430411495`
- **Total α:** `271682030217179`
- **α in pool:** `48028579021391`
- **α staked:** `181766621195788`
- **Price Δ 1h:** `1.053034289286458247`
- **Price Δ 1d:** `47.479911002007017252`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `4`
- **Active miners:** `3`
- **Active dual:** `0`
- **Emission:** `8266953`
- **Max neurons:** `256`
- **Validators (metadata):** `4`
- **Neuron reg. cost:** `2224407`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

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
- **Registration recycle cost snapshot (`burn`):** τ0.002411871
- **Owner SS58 (`owner_ss58`):** `5HidKLutq4YQgmBPWtLRYzh2cGYgWJRaC4owcz756W87puTL`

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
| 8104085 | 0.020098022 |
| 8104133 | 0.020163652 |
| 8104181 | 0.020005912 |
| 8104229 | 0.019974937 |
| 8104277 | 0.019963612 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.003895559 |
| 2026-03-10T23:59:48Z | 7718257 | 0.003867532 |
| 2026-03-11T23:59:48Z | 7725455 | 0.003960268 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.003782082 |
| 2026-03-13T23:59:48Z | 7739841 | 0.003634709 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.003561758 |
| 2026-03-15T23:59:48Z | 7754226 | 0.003158587 |
| 2026-03-16T23:59:48Z | 7761426 | 0.002709126 |
| 2026-03-17T23:59:48Z | 7768619 | 0.002561703 |
| 2026-03-18T23:59:48Z | 7775819 | 0.003226148 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00355680799515171633 |
| 2026-03-20T23:59:48Z | 7790201 | 0.003309864 |
| 2026-03-21T23:59:48Z | 7797398 | 0.003197418 |
| 2026-03-22T23:59:48Z | 7804598 | 0.003146101 |
| 2026-03-23T23:59:48Z | 7811798 | 0.003393885 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.003264886593147123 |
| 2026-03-25T23:59:48Z | 7826196 | 0.002843409 |
| 2026-03-26T23:59:48Z | 7833396 | 0.002365034 |
| 2026-03-27T23:59:48Z | 7840596 | 0.002371671 |
| 2026-03-28T23:59:48.001Z | 7847743 | 2.763686089 |
| 2026-03-29T23:59:48Z | 7854902 | 2.992460765 |
| 2026-03-30T23:59:48.001Z | 7862095 | 3.523753302 |
| 2026-03-31T23:59:48Z | 7869291 | 3.67212112 |
| 2026-04-01T23:59:48Z | 7876474 | 4.006807525 |
| 2026-04-02T23:59:48Z | 7883622 | 4.006807525 |
| 2026-04-03T23:59:48Z | 7890794 | 0.019873635 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.012999394 |
| 2026-04-05T23:59:48Z | 7905188 | 0.011982206 |
| 2026-04-06T23:59:48Z | 7912388 | 0.01264796 |
| 2026-04-07T23:59:48Z | 7919588 | 0.013522478 |
| 2026-04-08T23:59:48Z | 7926788 | 0.013545537 |
| 2026-04-09T23:59:48Z | 7933987 | 0.014031838 |
| 2026-04-10T23:59:48Z | 7941184 | 0.013570092 |
| 2026-04-11T23:59:48Z | 7948384 | 0.01418983 |
| 2026-04-12T23:59:48Z | 7955584 | 0.013453901 |
| 2026-04-13T23:59:48Z | 7962784 | 0.013577183 |
| 2026-04-14T23:59:48Z | 7969979 | 0.01602227 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.014071681 |
| 2026-04-16T23:59:48Z | 7984379 | 0.014630989 |
| 2026-04-17T23:59:48Z | 7991579 | 0.014655196 |
| 2026-04-18T23:59:48Z | 7998779 | 0.014575491 |
| 2026-04-19T23:59:48Z | 8005979 | 0.014610763 |
| 2026-04-20T23:59:48Z | 8013179 | 0.015948439 |
| 2026-04-21T23:59:48Z | 8020376 | 0.015078088 |
| 2026-04-22T23:59:48Z | 8027562 | 0.016028749 |
| 2026-04-23T23:59:48Z | 8034762 | 0.015188132 |
| 2026-04-24T23:59:48Z | 8041962 | 0.013350209 |
| 2026-04-25T23:59:48Z | 8049151 | 0.010546056 |
| 2026-04-26T23:59:48Z | 8056274 | 0.010467549 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.010894228 |
| 2026-04-28T23:59:48Z | 8070646 | 0.010529778 |
| 2026-04-29T23:59:48Z | 8077790 | 0.011829503 |
| 2026-04-30T23:59:48Z | 8084984 | 0.012485071 |
| 2026-05-01T23:59:48Z | 8092168 | 0.013366323 |
| 2026-05-02T23:59:48Z | 8099357 | 0.016207921 |
| 2026-05-03T16:10:00Z | 8104202 | 0.019976853 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

