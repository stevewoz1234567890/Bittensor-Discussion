# NetUID 30 — Pending (`ו`)

## Overview

**Pending** (NetUID **30**) (`ו`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `220`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ9,422.944978548. **Alpha liquidity in pool (`alpha_in`)** = ‎2,051,816.675160978ו‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,910,324.110571866ו‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004590212`** *(also **moving-average price** `0.004417230142280459` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎299,723.487301449ו‎`. **Owner hotkey / coldkey (chain):** `5HW12NvEZoGz8ZzcWMh4xyDUy6H1Af85m5LB8V1L11erK1S1` / `5HTogQKFuDaLq5ifWNhL2owMpLPHM3TAmujUUaTVj7FWzf6p`.
- **Subnet registered at block:** `3250216` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎166.000808432ו‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.001767798` · α-out `‎1.000000000ו‎` · α-in `‎0.385123301ו‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.00459023`
- **Market cap:** `21009172254448.43403954`
- **Liquidity:** `18840989574378`
- **Total τ:** `9422831135728`
- **Total α:** `4962036826270518`
- **α in pool:** `2051783557392743`
- **α staked:** `2525148808621255`
- **Price Δ 1h:** `1.204694427847314241`
- **Price Δ 1d:** `9.403068137535884911`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `1773469`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `500000`

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 21600
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5HTogQKFuDaLq5ifWNhL2owMpLPHM3TAmujUUaTVj7FWzf6p`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `21600` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `180`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `15`
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
| 8104037 | 0.004600368 |
| 8104085 | 0.00459024 |
| 8104133 | 0.004590235 |
| 8104181 | 0.004590232 |
| 8104229 | 0.00459022 |
| 8104277 | 0.004590212 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004646827 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004412441 |
| 2026-03-11T23:59:48Z | 7725455 | 0.004467771 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.004341438 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004346108 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004418583 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004200969 |
| 2026-03-16T23:59:48Z | 7761426 | 0.00383933 |
| 2026-03-17T23:59:48Z | 7768619 | 0.004009796 |
| 2026-03-18T23:59:48Z | 7775819 | 0.003963513 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00399753477996359204 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004167644 |
| 2026-03-21T23:59:48Z | 7797398 | 0.00436956 |
| 2026-03-22T23:59:48Z | 7804598 | 0.004401825 |
| 2026-03-23T23:59:48Z | 7811798 | 0.004767092 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00456350569841442759 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004445624 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004584049 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004416881 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004637952 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004599284 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004606507 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004418865 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004511129 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004421475 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004496279 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004739338 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004677642 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004779047 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004770414 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004820579 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004710913 |
| 2026-04-10T23:59:48Z | 7941184 | 0.003998939 |
| 2026-04-11T23:59:48Z | 7948384 | 0.003963946 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004074291 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004148516 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004189857 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004016353 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004009366 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004279231 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004195173 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004202364 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004411828 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004670629 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004569805 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004769514 |
| 2026-04-24T23:59:48Z | 8041962 | 0.00461581 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004836116 |
| 2026-04-26T23:59:48Z | 8056274 | 0.00494567 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004938518 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004579275 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004622765 |
| 2026-04-30T23:59:48Z | 8084984 | 0.00463251 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004442215 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004334697 |
| 2026-05-03T16:10:00Z | 8104202 | 0.00459023 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

