# NetUID 99 — Leoma (`გ`)

## Overview

**Leoma** (NetUID **99**) (`გ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `289`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,331.124811127. **Alpha liquidity in pool (`alpha_in`)** = ‎155,737.491151826გ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎652,730.507013085გ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008546320`** *(also **moving-average price** `0.008248117519542575` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎39,924.875884979გ‎`. **Owner hotkey / coldkey (chain):** `5C7LM2i42XgL2oB4x3rcmB7KDiof4B92KZzUpg5miZ6DogjU` / `5FxogcQr2XDRNCKSaaHh3AujzJKqksCzKLQWvPzToxG64tfm`.
- **Subnet registered at block:** `7415113` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎173.188731431გ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004273211` · α-out `‎1.000000000გ‎` · α-in `‎0.500000000გ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.008578907`
- **Market cap:** `5736633730150.622033994`
- **Liquidity:** `2666534910199`
- **Total τ:** `1333341301837`
- **Total α:** `808361280164273`
- **α in pool:** `155403667199369`
- **α staked:** `513286846656373`
- **Price Δ 1h:** `2.459973712921454663`
- **Price Δ 1d:** `5.186837709013441231`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `4289462`
- **Max neurons:** `256`
- **Validators (metadata):** `10`
- **Neuron reg. cost:** `50000000`

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
- **Registration recycle cost snapshot (`burn`):** τ0.050000000
- **Owner SS58 (`owner_ss58`):** `5FxogcQr2XDRNCKSaaHh3AujzJKqksCzKLQWvPzToxG64tfm`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.050000000 / τ100.000000000
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


- **Logo URL:** [https://www.leoma.ai/logo-leoma.png](https://www.leoma.ai/logo-leoma.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.008347845 |
| 8104133 | 0.008347779 |
| 8104181 | 0.008582837 |
| 8104229 | 0.008554241 |
| 8104277 | 0.00854632 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.007433164 |
| 2026-03-10T23:59:48Z | 7718257 | 0.007981515 |
| 2026-03-11T23:59:48Z | 7725455 | 0.009112262 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.00793552 |
| 2026-03-13T23:59:48Z | 7739841 | 0.007877019 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.008354134 |
| 2026-03-15T23:59:48Z | 7754226 | 0.00777541 |
| 2026-03-16T23:59:48Z | 7761426 | 0.007556566 |
| 2026-03-17T23:59:48Z | 7768619 | 0.007403846 |
| 2026-03-18T23:59:48Z | 7775819 | 0.006771343 |
| 2026-03-19T23:59:48Z | 7783014 | 0.0068969538503692768 |
| 2026-03-20T23:59:48Z | 7790201 | 0.007220576 |
| 2026-03-21T23:59:48Z | 7797398 | 0.007514434 |
| 2026-03-22T23:59:48Z | 7804598 | 0.007149703 |
| 2026-03-23T23:59:48Z | 7811798 | 0.007178482 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00730160773017562736 |
| 2026-03-25T23:59:48Z | 7826196 | 0.006795376 |
| 2026-03-26T23:59:48Z | 7833396 | 0.006672356 |
| 2026-03-27T23:59:48Z | 7840596 | 0.006836792 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.006898123 |
| 2026-03-29T23:59:48Z | 7854902 | 0.006617551 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.00579155 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005053657 |
| 2026-04-01T23:59:48Z | 7876474 | 0.005107954 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004449759 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004904677 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.005196715 |
| 2026-04-05T23:59:48Z | 7905188 | 0.005609266 |
| 2026-04-06T23:59:48Z | 7912388 | 0.005167437 |
| 2026-04-07T23:59:48Z | 7919588 | 0.005029485 |
| 2026-04-08T23:59:48Z | 7926788 | 0.00505829 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004388147 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004774658 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004937915 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004763934 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004770952 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004788216 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004525448 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004590658 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004719064 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004672775 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004673523 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004722977 |
| 2026-04-21T23:59:48Z | 8020376 | 0.006106538 |
| 2026-04-22T23:59:48Z | 8027562 | 0.006150099 |
| 2026-04-23T23:59:48Z | 8034762 | 0.006052974 |
| 2026-04-24T23:59:48Z | 8041962 | 0.005956278 |
| 2026-04-25T23:59:48Z | 8049151 | 0.006187922 |
| 2026-04-26T23:59:48Z | 8056274 | 0.005570113 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.008959957 |
| 2026-04-28T23:59:48Z | 8070646 | 0.00783179 |
| 2026-04-29T23:59:48Z | 8077790 | 0.007982407 |
| 2026-04-30T23:59:48Z | 8084984 | 0.007811099 |
| 2026-05-01T23:59:48Z | 8092168 | 0.008117222 |
| 2026-05-02T23:59:48Z | 8099357 | 0.008255147 |
| 2026-05-03T16:10:00Z | 8104202 | 0.008578907 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

