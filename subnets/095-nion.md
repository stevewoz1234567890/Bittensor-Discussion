# NetUID 95 — nion (`ᚅ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**nion** (NetUID **95**) (`ᚅ`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `82`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ19,289.619819149. **Alpha liquidity in pool (`alpha_in`)** = ‎578,681.120252589ᚅ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,979,135.576010057ᚅ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.033261938`** *(also **moving-average price** `0.03184230602346361` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎234,361.845939427ᚅ‎`. **Owner hotkey / coldkey (chain):** `5ExqqyEBXLpGwqy6sSVrauozhcyAKBaMz1y5x9wAYSk7n7HP` / `5D5UhUuc6cC47CXUBHyBkpDBrdeyeL6bpWGAreZgNm5WTyrg`.
- **Subnet registered at block:** `5403674` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎58.186728712ᚅ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.016630946` · α-out `‎1.000000000ᚅ‎` · α-in `‎0.500000000ᚅ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104353`
- **Liquidity constant `k`:** `11162538806191686547379026761`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Unknown`
- **Symbol (API):** `ᚅ`
- **Rank:** `16`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.033070699`
- **Market cap:** `62357915376175.105099292`
- **Market cap Δ 1d:** `4.089318204557094313`
- **Liquidity:** `38419139519935`
- **Total τ:** `19230169410162`
- **Total α:** `2557559513876308`
- **α in pool:** `580240838265124`
- **α staked:** `1305353275611184`
- **Price Δ 1h:** `-1.605524683920751605`
- **Price Δ 1d:** `3.792537446046361549`
#### Subnet activity (TAOStats)

- **NetUID (API):** `95`
- **Owner SS58 (API):** `5D5UhUuc6cC47CXUBHyBkpDBrdeyeL6bpWGAreZgNm5WTyrg`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `5403674`
- **Registration wall time:** `2025-04-22T00:48:24Z`
- **Registration cost snapshot:** `210595055304`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `16589065`
- **Max neurons:** `256`
- **Validator slots (metadata):** `12`
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
- **Owner SS58 (`owner_ss58`):** `5D5UhUuc6cC47CXUBHyBkpDBrdeyeL6bpWGAreZgNm5WTyrg`

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
| 8104244 | 0.033056767 |
| 8104292 | 0.033062222 |
| 8104340 | 0.033050062 |
| 8104388 | 0.033259923 |
| 8104436 | 0.033261984 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.017872951 |
| 2026-03-10T23:59:48Z | 7718257 | 0.017831613 |
| 2026-03-11T23:59:48Z | 7725455 | 0.017760197 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.017900948 |
| 2026-03-13T23:59:48Z | 7739841 | 0.017034536 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.017118488 |
| 2026-03-15T23:59:48Z | 7754226 | 0.016882914 |
| 2026-03-16T23:59:48Z | 7761426 | 0.017799714 |
| 2026-03-17T23:59:48Z | 7768619 | 0.017586371 |
| 2026-03-18T23:59:48Z | 7775819 | 0.017758622 |
| 2026-03-19T23:59:48Z | 7783014 | 0.01784433764711791233 |
| 2026-03-20T23:59:48Z | 7790201 | 0.017655968 |
| 2026-03-21T23:59:48Z | 7797398 | 0.017854263 |
| 2026-03-22T23:59:48Z | 7804598 | 0.017027395 |
| 2026-03-23T23:59:48Z | 7811798 | 0.016145757 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.01812157984235999321 |
| 2026-03-25T23:59:48Z | 7826196 | 0.018727463 |
| 2026-03-26T23:59:48Z | 7833396 | 0.018060446 |
| 2026-03-27T23:59:48Z | 7840596 | 0.018124622 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.017971766 |
| 2026-03-29T23:59:48Z | 7854902 | 0.018033653 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.017507412 |
| 2026-03-31T23:59:48Z | 7869291 | 0.019590436 |
| 2026-04-01T23:59:48Z | 7876474 | 0.0195934 |
| 2026-04-02T23:59:48Z | 7883622 | 0.018737141 |
| 2026-04-03T23:59:48Z | 7890794 | 0.019551757 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.020220669 |
| 2026-04-05T23:59:48Z | 7905188 | 0.019554215 |
| 2026-04-06T23:59:48Z | 7912388 | 0.019842228 |
| 2026-04-07T23:59:48Z | 7919588 | 0.019431854 |
| 2026-04-08T23:59:48Z | 7926788 | 0.019311588 |
| 2026-04-09T23:59:48Z | 7933987 | 0.019304494 |
| 2026-04-10T23:59:48Z | 7941184 | 0.018379555 |
| 2026-04-11T23:59:48Z | 7948384 | 0.019107884 |
| 2026-04-12T23:59:48Z | 7955584 | 0.020461855 |
| 2026-04-13T23:59:48Z | 7962784 | 0.021286594 |
| 2026-04-14T23:59:48Z | 7969979 | 0.021256639 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.021860872 |
| 2026-04-16T23:59:48Z | 7984379 | 0.023322873 |
| 2026-04-17T23:59:48Z | 7991579 | 0.023612315 |
| 2026-04-18T23:59:48Z | 7998779 | 0.023863345 |
| 2026-04-19T23:59:48Z | 8005979 | 0.024241365 |
| 2026-04-20T23:59:48Z | 8013179 | 0.023833673 |
| 2026-04-21T23:59:48Z | 8020376 | 0.024332534 |
| 2026-04-22T23:59:48Z | 8027562 | 0.024681278 |
| 2026-04-23T23:59:48Z | 8034762 | 0.026751438 |
| 2026-04-24T23:59:48Z | 8041962 | 0.027618483 |
| 2026-04-25T23:59:48Z | 8049151 | 0.028582565 |
| 2026-04-26T23:59:48Z | 8056274 | 0.028874479 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.029209497 |
| 2026-04-28T23:59:48Z | 8070646 | 0.02931868 |
| 2026-04-29T23:59:48Z | 8077790 | 0.030169578 |
| 2026-04-30T23:59:48Z | 8084984 | 0.034405982 |
| 2026-05-01T23:59:48Z | 8092168 | 0.032454904 |
| 2026-05-02T23:59:48Z | 8099357 | 0.031496428 |
| 2026-05-03T16:10:00Z | 8104202 | 0.033070699 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

