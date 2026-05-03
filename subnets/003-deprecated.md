# NetUID 3 — deprecated (`γ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**deprecated** (NetUID **3**) (`γ`).

deprecated

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `351`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ74,660.732901473. **Alpha liquidity in pool (`alpha_in`)** = ‎2,798,350.073606372γ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,187,493.180710700γ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.026708824`** *(also **moving-average price** `0.026116409106180072` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎2,946,054.052978278γ‎`. **Owner hotkey / coldkey (chain):** `5HdTZQ6UXD7MWcRsMeExVwqAKKo4UwomUd662HvtXiZXkxmv` / `5FUJoAsY5TWfs1FGFtscC5QUuarJMCWYwYzEftyGAeH7pUqK`.
- **Subnet registered at block:** `4165565` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎264.938604259γ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000γ‎` · α-in `‎0.000000000γ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104084`
- **Liquidity constant `k`:** `208926867410342649288460985956`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `deprecated`
- **Symbol (API):** `γ`
- **Rank:** `7`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.026879948`
- **Market cap:** `118831461916541.272940744`
- **Market cap Δ 1d:** `4.415060751594848264`
- **Liquidity:** `149879472175390`
- **Total τ:** `74899975976697`
- **Total α:** `4985618799349183`
- **α in pool:** `2789421177403073`
- **α staked:** `1631400690129605`
- **Price Δ 1h:** `1.515698783606935288`
- **Price Δ 1d:** `4.256068292821420568`
#### Subnet activity (TAOStats)

- **NetUID (API):** `3`
- **Owner SS58 (API):** `5FUJoAsY5TWfs1FGFtscC5QUuarJMCWYwYzEftyGAeH7pUqK`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `4165565`
- **Registration wall time:** `2024-10-31T19:37:00.001Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `1`
- **Active miners:** `4`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `1`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `157432491`
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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 10000
- **Registration recycle cost snapshot (`burn`):** τ0.158364185
- **Owner SS58 (`owner_ss58`):** `5FUJoAsY5TWfs1FGFtscC5QUuarJMCWYwYzEftyGAeH7pUqK`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `1000000000`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `250`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `4`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No miner/validator sections auto-matched.* Open [https://github.com/username/repo](https://github.com/username/repo) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.deprecated.com](https://www.deprecated.com)
- **GitHub:** [https://github.com/username/repo](https://github.com/username/repo)
- **Discord (handle / invite hint):** `deprecated`
- **Logo URL:** [https://deprecated.png](https://deprecated.png)
- **Contact:** deprecated@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.026879952 |
| 8104244 | 0.026751084 |
| 8104292 | 0.026686072 |
| 8104340 | 0.026685232 |
| 8104388 | 0.02672 |
| 8104436 | 0.026708824 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.036749772 |
| 2026-03-10T23:59:48Z | 7718257 | 0.037919393 |
| 2026-03-11T23:59:48Z | 7725455 | 0.038931346 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.045114587 |
| 2026-03-13T23:59:48Z | 7739841 | 0.056383722 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.058482337 |
| 2026-03-15T23:59:48Z | 7754226 | 0.071247606 |
| 2026-03-16T23:59:48Z | 7761426 | 0.064903114 |
| 2026-03-17T23:59:48Z | 7768619 | 0.065859919 |
| 2026-03-18T23:59:48Z | 7775819 | 0.068780109 |
| 2026-03-19T23:59:48Z | 7783014 | 0.08202339610188012638 |
| 2026-03-20T23:59:48Z | 7790201 | 0.080331634 |
| 2026-03-21T23:59:48Z | 7797398 | 0.081724924 |
| 2026-03-22T23:59:48Z | 7804598 | 0.08642716 |
| 2026-03-23T23:59:48Z | 7811798 | 0.088418098 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.09555109257421302865 |
| 2026-03-25T23:59:48Z | 7826196 | 0.090761206 |
| 2026-03-26T23:59:48Z | 7833396 | 0.083371497 |
| 2026-03-27T23:59:48Z | 7840596 | 0.078577034 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.078354523 |
| 2026-03-29T23:59:48Z | 7854902 | 0.080971466 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.078362419 |
| 2026-03-31T23:59:48Z | 7869291 | 0.07357125 |
| 2026-04-01T23:59:48Z | 7876474 | 0.07512488 |
| 2026-04-02T23:59:48Z | 7883622 | 0.068543616 |
| 2026-04-03T23:59:48Z | 7890794 | 0.06947293 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.06935857 |
| 2026-04-05T23:59:48Z | 7905188 | 0.072578064 |
| 2026-04-06T23:59:48Z | 7912388 | 0.072158151 |
| 2026-04-07T23:59:48Z | 7919588 | 0.071545037 |
| 2026-04-08T23:59:48Z | 7926788 | 0.069103457 |
| 2026-04-09T23:59:48Z | 7933987 | 0.033039564 |
| 2026-04-10T23:59:48Z | 7941184 | 0.032848279 |
| 2026-04-11T23:59:48Z | 7948384 | 0.035232478 |
| 2026-04-12T23:59:48Z | 7955584 | 0.032389875 |
| 2026-04-13T23:59:48Z | 7962784 | 0.029945594 |
| 2026-04-14T23:59:48Z | 7969979 | 0.030045491 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.02924395 |
| 2026-04-16T23:59:48Z | 7984379 | 0.025898223 |
| 2026-04-17T23:59:48Z | 7991579 | 0.026113712 |
| 2026-04-18T23:59:48Z | 7998779 | 0.023831259 |
| 2026-04-19T23:59:48Z | 8005979 | 0.024289382 |
| 2026-04-20T23:59:48Z | 8013179 | 0.024453304 |
| 2026-04-21T23:59:48Z | 8020376 | 0.024507797 |
| 2026-04-22T23:59:48Z | 8027562 | 0.023769207 |
| 2026-04-23T23:59:48Z | 8034762 | 0.023983274 |
| 2026-04-24T23:59:48Z | 8041962 | 0.024082258 |
| 2026-04-25T23:59:48Z | 8049151 | 0.023917039 |
| 2026-04-26T23:59:48Z | 8056274 | 0.023814158 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.023978551 |
| 2026-04-28T23:59:48Z | 8070646 | 0.026352129 |
| 2026-04-29T23:59:48Z | 8077790 | 0.025904527 |
| 2026-04-30T23:59:48Z | 8084984 | 0.025596463 |
| 2026-05-01T23:59:48Z | 8092168 | 0.026107505 |
| 2026-05-02T23:59:48Z | 8099357 | 0.026010016 |
| 2026-05-03T16:10:00Z | 8104202 | 0.026879948 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

