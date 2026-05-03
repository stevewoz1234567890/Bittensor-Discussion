# NetUID 119 — Satori (`Ⲃ`)

## Overview

**Satori** (NetUID **119**) (`Ⲃ`).

Satori constructs a persistent 'Second Life' in Japan.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `247`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ5,203.365728496. **Alpha liquidity in pool (`alpha_in`)** = ‎764,204.164805707Ⲃ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,146,438.371797916Ⲃ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006811619`** *(also **moving-average price** `0.006949411705136299` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎56,041.136734130Ⲃ‎`. **Owner hotkey / coldkey (chain):** `5HMwvi1dHWCBHTNTtizL5peRBwqvd8HtGrTVouN51p75JNd4` / `5GbLENPLG8Takn1puaz5HorPmrFtDT7i2PojiJsqutbaGwWu`.
- **Subnet registered at block:** `5740660` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎169.082484226Ⲃ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.001584494` · α-out `‎1.000000000Ⲃ‎` · α-in `‎0.232616339Ⲃ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.006811621`
- **Market cap:** `9150078971176.966736048`
- **Liquidity:** `10408793652218`
- **Total τ:** `5203345901979`
- **Total α:** `1910626511365488`
- **α in pool:** `764201025018833`
- **α staked:** `579103156346655`
- **Price Δ 1h:** `-0.108051208177634544`
- **Price Δ 1d:** `-7.389081990103458895`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `8`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `1583970`
- **Max neurons:** `256`
- **Validators (metadata):** `8`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Satori constructs a persistent 'Second Life' in Japan. We merge deep AI companionship with authentic Digital Residency, creating a seamless bridge where virtual emotional connections unlock real-world value and physical experiences.

## Operational parameters — registration, limits, economics (chain)


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
- **`immunity_period` (blocks):** 3600
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GbLENPLG8Takn1puaz5HorPmrFtDT7i2PojiJsqutbaGwWu`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `3600` blocks
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
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No miner/validator sections auto-matched.* Open [https://github.com/Satori119/Satori](https://github.com/Satori119/Satori) for requirements.

## On-chain identity — description


Satori constructs a persistent 'Second Life' in Japan. We merge deep AI companionship with authentic Digital Residency, creating a seamless bridge where virtual emotional connections unlock real-world value and physical experiences.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/Satori119/Satori](https://github.com/Satori119/Satori)
- **Logo URL:** [https://raw.githubusercontent.com/Satori119/Satori/refs/heads/main/assets/logo.png](https://raw.githubusercontent.com/Satori119/Satori/refs/heads/main/assets/logo.png)
- **Contact:** Akihabara119@outlook.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.00681894 |
| 8104072 | 0.006818908 |
| 8104120 | 0.006818867 |
| 8104168 | 0.006818837 |
| 8104216 | 0.006811619 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.008460254 |
| 2026-03-10T23:59:48Z | 7718257 | 0.008303009 |
| 2026-03-11T23:59:48Z | 7725455 | 0.008458324 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.00846541 |
| 2026-03-13T23:59:48Z | 7739841 | 0.008239374 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.008229195 |
| 2026-03-15T23:59:48Z | 7754226 | 0.007791865 |
| 2026-03-16T23:59:48Z | 7761426 | 0.007648909 |
| 2026-03-17T23:59:48Z | 7768619 | 0.007135936 |
| 2026-03-18T23:59:48Z | 7775819 | 0.007124287 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00717332362752389905 |
| 2026-03-20T23:59:48Z | 7790201 | 0.00710352 |
| 2026-03-21T23:59:48Z | 7797398 | 0.006928345 |
| 2026-03-22T23:59:48Z | 7804598 | 0.006815421 |
| 2026-03-23T23:59:48Z | 7811798 | 0.006920038 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00713142222628766816 |
| 2026-03-25T23:59:48Z | 7826196 | 0.00697647 |
| 2026-03-26T23:59:48Z | 7833396 | 0.00694823 |
| 2026-03-27T23:59:48Z | 7840596 | 0.006936116 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.006995853 |
| 2026-03-29T23:59:48Z | 7854902 | 0.006962294 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.007010649 |
| 2026-03-31T23:59:48Z | 7869291 | 0.007053536 |
| 2026-04-01T23:59:48Z | 7876474 | 0.006889868 |
| 2026-04-02T23:59:48Z | 7883622 | 0.006821147 |
| 2026-04-03T23:59:48Z | 7890794 | 0.006825717 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.006770149 |
| 2026-04-05T23:59:48Z | 7905188 | 0.006686691 |
| 2026-04-06T23:59:48Z | 7912388 | 0.006727335 |
| 2026-04-07T23:59:48Z | 7919588 | 0.006820858 |
| 2026-04-08T23:59:48Z | 7926788 | 0.006453119 |
| 2026-04-09T23:59:48Z | 7933987 | 0.006490826 |
| 2026-04-10T23:59:48Z | 7941184 | 0.006404363 |
| 2026-04-11T23:59:48Z | 7948384 | 0.006422572 |
| 2026-04-12T23:59:48Z | 7955584 | 0.006421028 |
| 2026-04-13T23:59:48Z | 7962784 | 0.006435404 |
| 2026-04-14T23:59:48Z | 7969979 | 0.006460991 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.00637737 |
| 2026-04-16T23:59:48Z | 7984379 | 0.006339874 |
| 2026-04-17T23:59:48Z | 7991579 | 0.006159529 |
| 2026-04-18T23:59:48Z | 7998779 | 0.006136099 |
| 2026-04-19T23:59:48Z | 8005979 | 0.006110076 |
| 2026-04-20T23:59:48Z | 8013179 | 0.006059326 |
| 2026-04-21T23:59:48Z | 8020376 | 0.006018822 |
| 2026-04-22T23:59:48Z | 8027562 | 0.006086868 |
| 2026-04-23T23:59:48Z | 8034762 | 0.006008762 |
| 2026-04-24T23:59:48Z | 8041962 | 0.006203704 |
| 2026-04-25T23:59:48Z | 8049151 | 0.006140822 |
| 2026-04-26T23:59:48Z | 8056274 | 0.006149221 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.006279254 |
| 2026-04-28T23:59:48Z | 8070646 | 0.006550932 |
| 2026-04-29T23:59:48Z | 8077790 | 0.006470663 |
| 2026-04-30T23:59:48Z | 8084984 | 0.006730855 |
| 2026-05-01T23:59:48Z | 8092168 | 0.006969994 |
| 2026-05-02T23:59:48Z | 8099357 | 0.006937906 |
| 2026-05-03T16:10:00Z | 8104202 | 0.006811621 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

