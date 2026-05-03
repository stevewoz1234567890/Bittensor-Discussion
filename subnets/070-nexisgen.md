# NetUID 70 — NexisGen (`غ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**NexisGen** (NetUID **70**) (`غ`).

Enterprise dataset delivery

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `57`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ817.807506484. **Alpha liquidity in pool (`alpha_in`)** = ‎96,259.409387118غ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎303,034.803439843غ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008496098`** *(also **moving-average price** `0.007937224814668298` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎13,750.539873994غ‎`. **Owner hotkey / coldkey (chain):** `5EJGfSvRcEGVQtqDuU7YYwuZRHmaktf6JEZDeFPyeXksiHrm` / `5HisJVRY5s72aGFqcvemjk2AzdQnPhbTcMjWDecWZKtoCqj9`.
- **Subnet registered at block:** `7787562` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎30.323561950غ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004248045` · α-out `‎1.000000000غ‎` · α-in `‎0.500000000غ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104378`
- **Liquidity constant `k`:** `78721667566501514251073112`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `NexisGen`
- **Symbol (API):** `غ`
- **Rank:** `124`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.00844147`
- **Market cap:** `2525663692828.58086773`
- **Market cap Δ 1d:** `11.256520528624254947`
- **Liquidity:** `1628401613290`
- **Total τ:** `814190330764`
- **Total α:** `398955881354359`
- **α in pool:** `96453731699141`
- **α staked:** `202743409655218`
- **Price Δ 1h:** `1.702803629097599015`
- **Price Δ 1d:** `8.537899360200785863`
#### Subnet activity (TAOStats)

- **NetUID (API):** `70`
- **Owner SS58 (API):** `5HisJVRY5s72aGFqcvemjk2AzdQnPhbTcMjWDecWZKtoCqj9`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `7787562`
- **Registration wall time:** `2026-03-20T15:10:12Z`
- **Registration cost snapshot:** `614193494016`
- **Active keys:** `180`
- **Active validators:** `8`
- **Active miners:** `1`
- **Active dual-role:** `1`
- **Emission:** `4220771`
- **Max neurons:** `256`
- **Validator slots (metadata):** `8`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `50000000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 180
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
- **Owner SS58 (`owner_ss58`):** `5HisJVRY5s72aGFqcvemjk2AzdQnPhbTcMjWDecWZKtoCqj9`

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Logo URL:** [https://www.nexisgen.ai/logo.png](https://www.nexisgen.ai/logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.008453246 |
| 8104292 | 0.00843107 |
| 8104340 | 0.008403075 |
| 8104388 | 0.008486099 |
| 8104436 | 0.008496106 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.003570029 |
| 2026-03-10T23:59:48Z | 7718257 | 0.002916013 |
| 2026-03-11T23:59:48Z | 7725455 | 0.002511141 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.002824293 |
| 2026-03-13T23:59:48Z | 7739841 | 0.002669412 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.002530196 |
| 2026-03-15T23:59:48Z | 7754226 | 0.002418819 |
| 2026-03-16T23:59:48Z | 7761426 | 0.002492086 |
| 2026-03-17T23:59:48Z | 7768619 | 0.002551388 |
| 2026-03-18T23:59:48Z | 7775819 | 0.002453529 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00241590731880543645 |
| 2026-03-20T23:59:48Z | 7790201 | 0.488968253 |
| 2026-03-21T23:59:48Z | 7797398 | 0.014534948 |
| 2026-03-22T23:59:48Z | 7804598 | 0.012525753 |
| 2026-03-23T23:59:48Z | 7811798 | 0.010003076 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.01040881374918079521 |
| 2026-03-25T23:59:48Z | 7826196 | 0.016167702 |
| 2026-03-26T23:59:48Z | 7833396 | 0.013903957 |
| 2026-03-27T23:59:48Z | 7840596 | 0.013023683 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.010938868 |
| 2026-03-29T23:59:48Z | 7854902 | 0.009975886 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.007731538 |
| 2026-03-31T23:59:48Z | 7869291 | 0.006633931 |
| 2026-04-01T23:59:48Z | 7876474 | 0.008051228 |
| 2026-04-02T23:59:48Z | 7883622 | 0.0136411 |
| 2026-04-03T23:59:48Z | 7890794 | 0.013093456 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.012017618 |
| 2026-04-05T23:59:48Z | 7905188 | 0.012077557 |
| 2026-04-06T23:59:48Z | 7912388 | 0.01149932 |
| 2026-04-07T23:59:48Z | 7919588 | 0.011202116 |
| 2026-04-08T23:59:48Z | 7926788 | 0.008839974 |
| 2026-04-09T23:59:48Z | 7933987 | 0.007332451 |
| 2026-04-10T23:59:48Z | 7941184 | 0.008232928 |
| 2026-04-11T23:59:48Z | 7948384 | 0.008106826 |
| 2026-04-12T23:59:48Z | 7955584 | 0.007843606 |
| 2026-04-13T23:59:48Z | 7962784 | 0.007535342 |
| 2026-04-14T23:59:48Z | 7969979 | 0.007100527 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.006445171 |
| 2026-04-16T23:59:48Z | 7984379 | 0.006006924 |
| 2026-04-17T23:59:48Z | 7991579 | 0.006129577 |
| 2026-04-18T23:59:48Z | 7998779 | 0.005718956 |
| 2026-04-19T23:59:48Z | 8005979 | 0.006022358 |
| 2026-04-20T23:59:48Z | 8013179 | 0.005920941 |
| 2026-04-21T23:59:48Z | 8020376 | 0.0058676 |
| 2026-04-22T23:59:48Z | 8027562 | 0.006106813 |
| 2026-04-23T23:59:48Z | 8034762 | 0.006608174 |
| 2026-04-24T23:59:48Z | 8041962 | 0.00684372 |
| 2026-04-25T23:59:48Z | 8049151 | 0.006650183 |
| 2026-04-26T23:59:48Z | 8056274 | 0.006568291 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.007414657 |
| 2026-04-28T23:59:48Z | 8070646 | 0.007498288 |
| 2026-04-29T23:59:48Z | 8077790 | 0.007638701 |
| 2026-04-30T23:59:48Z | 8084984 | 0.007666583 |
| 2026-05-01T23:59:48Z | 8092168 | 0.007622925 |
| 2026-05-02T23:59:48Z | 8099357 | 0.00770589 |
| 2026-05-03T16:10:00Z | 8104202 | 0.00844147 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

