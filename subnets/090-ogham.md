# NetUID 90 — ogham (` `)

## Overview

**ogham** (NetUID **90**) (` `).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `280`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,919.590676531. **Alpha liquidity in pool (`alpha_in`)** = ‎411,245.068737457 ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎969,504.123696672 ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004668685`** *(also **moving-average price** `0.004542197333648801` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎26,485.234356539 ‎`. **Owner hotkey / coldkey (chain):** `5E7rCzjycq3GgALTXqoSFHn9ZHRtJ96Nd4YaT2RBNdH5k6AK` / `5CqrdkU4FuH8LdUjkq4YQFJbQiK1Bmf9q4fVpFuhrxGcGwbW`.
- **Subnet registered at block:** `7063126` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎183.020272260 ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002334350` · α-out `‎1.000000000 ‎` · α-in `‎0.500000000 ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.00466886`
- **Market cap:** `4562940208863.68138124`
- **Liquidity:** `3839286166118`
- **Total τ:** `1919451670189`
- **Total α:** `1380640814524034`
- **α in pool:** `411199842344717`
- **α staked:** `566113722179317`
- **Price Δ 1h:** `-1.014835075254514412`
- **Price Δ 1d:** `5.80889918278361216`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `2334431`
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
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CqrdkU4FuH8LdUjkq4YQFJbQiK1Bmf9q4fVpFuhrxGcGwbW`

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


*No `SubnetIdentity` registered on-chain.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.004693346 |
| 8104133 | 0.00469335 |
| 8104181 | 0.004668855 |
| 8104229 | 0.004668753 |
| 8104277 | 0.004668685 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.005263607 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005734379 |
| 2026-03-11T23:59:48Z | 7725455 | 0.006357651 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.006068266 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005437179 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005580961 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005238597 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005892164 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005637767 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005535862 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00559887021260101389 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005258727 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005752013 |
| 2026-03-22T23:59:48Z | 7804598 | 0.00590982 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005878428 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00535144926975929325 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004483545 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004616406 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004801398 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004739479 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004691223 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004531804 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004462666 |
| 2026-04-01T23:59:48Z | 7876474 | 0.00457594 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004631179 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004707709 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.00493515 |
| 2026-04-05T23:59:48Z | 7905188 | 0.005010948 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004757147 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004975292 |
| 2026-04-08T23:59:48Z | 7926788 | 0.005017316 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004536171 |
| 2026-04-10T23:59:48Z | 7941184 | 0.00472356 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004759907 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004775922 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004698318 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004302218 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004432011 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004532036 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004512983 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004494146 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004504567 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004417677 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004315096 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004352727 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004350764 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004490974 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004398384 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004335286 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004341854 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004461655 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004451838 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004399497 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004401538 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004551616 |
| 2026-05-03T16:10:00Z | 8104202 | 0.00466886 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

