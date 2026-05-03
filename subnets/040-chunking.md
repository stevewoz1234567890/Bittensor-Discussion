# NetUID 40 — Chunking (`ן`)

## Overview

**Chunking** (NetUID **40**) (`ן`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `230`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,040.818949588. **Alpha liquidity in pool (`alpha_in`)** = ‎2,076,462.714849980ן‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,980,934.282765013ן‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003391576`** *(also **moving-average price** `0.003408280899748206` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎162,206.205682620ן‎`. **Owner hotkey / coldkey (chain):** `5F9Qvcz22Fwq4cm58o2bShiL6n8BnJmhqXB1cispBpqRfN6w` / `5F9Qvcz22Fwq4cm58o2bShiL6n8BnJmhqXB1cispBpqRfN6w`.
- **Subnet registered at block:** `3372582` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎173.785424128ן‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ן‎` · α-in `‎0.000000000ן‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003386775`
- **Market cap:** `13613309119687.2711165`
- **Liquidity:** `14073327430862`
- **Total τ:** `7035835434783`
- **Total α:** `5057321997614993`
- **α in pool:** `2077933135823859`
- **α staked:** `1941616175744601`
- **Price Δ 1h:** `0.138020470671093493`
- **Price Δ 1d:** `-1.628052071176411471`
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

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/VectorChat/chunking_subnet](https://github.com/VectorChat/chunking_subnet)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.003422793 |
| 8104133 | 0.003406084 |
| 8104181 | 0.003406082 |
| 8104229 | 0.003391582 |
| 8104277 | 0.003391576 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.003955136 |
| 2026-03-10T23:59:48Z | 7718257 | 0.0039302 |
| 2026-03-11T23:59:48Z | 7725455 | 0.003895999 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.003857475 |
| 2026-03-13T23:59:48Z | 7739841 | 0.003761405 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.00377937 |
| 2026-03-15T23:59:48Z | 7754226 | 0.003766479 |
| 2026-03-16T23:59:48Z | 7761426 | 0.003699641 |
| 2026-03-17T23:59:48Z | 7768619 | 0.003592429 |
| 2026-03-18T23:59:48Z | 7775819 | 0.003843801 |
| 2026-03-19T23:59:48Z | 7783014 | 0.0038352274914685314 |
| 2026-03-20T23:59:48Z | 7790201 | 0.003701512 |
| 2026-03-21T23:59:48Z | 7797398 | 0.003702111 |
| 2026-03-22T23:59:48Z | 7804598 | 0.003688761 |
| 2026-03-23T23:59:48Z | 7811798 | 0.003707689 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00363887074203778705 |
| 2026-03-25T23:59:48Z | 7826196 | 0.003399819 |
| 2026-03-26T23:59:48Z | 7833396 | 0.00342735 |
| 2026-03-27T23:59:48Z | 7840596 | 0.003458964 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.003515845 |
| 2026-03-29T23:59:48Z | 7854902 | 0.00350715 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.003371717 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003412995 |
| 2026-04-01T23:59:48Z | 7876474 | 0.003411465 |
| 2026-04-02T23:59:48Z | 7883622 | 0.00346814 |
| 2026-04-03T23:59:48Z | 7890794 | 0.003432943 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.0034336 |
| 2026-04-05T23:59:48Z | 7905188 | 0.003418394 |
| 2026-04-06T23:59:48Z | 7912388 | 0.003489961 |
| 2026-04-07T23:59:48Z | 7919588 | 0.003435947 |
| 2026-04-08T23:59:48Z | 7926788 | 0.003561204 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003341014 |
| 2026-04-10T23:59:48Z | 7941184 | 0.003400655 |
| 2026-04-11T23:59:48Z | 7948384 | 0.00342087 |
| 2026-04-12T23:59:48Z | 7955584 | 0.003380693 |
| 2026-04-13T23:59:48Z | 7962784 | 0.003374325 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003365212 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.003303852 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003297964 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003292859 |
| 2026-04-18T23:59:48Z | 7998779 | 0.003384996 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003418285 |
| 2026-04-20T23:59:48Z | 8013179 | 0.00337442 |
| 2026-04-21T23:59:48Z | 8020376 | 0.003389393 |
| 2026-04-22T23:59:48Z | 8027562 | 0.003480532 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003434555 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003427478 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003402001 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003494519 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.003473467 |
| 2026-04-28T23:59:48Z | 8070646 | 0.003449435 |
| 2026-04-29T23:59:48Z | 8077790 | 0.003453254 |
| 2026-04-30T23:59:48Z | 8084984 | 0.003506802 |
| 2026-05-01T23:59:48Z | 8092168 | 0.003438176 |
| 2026-05-02T23:59:48Z | 8099357 | 0.00340159 |
| 2026-05-03T16:10:00Z | 8104202 | 0.003386775 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

