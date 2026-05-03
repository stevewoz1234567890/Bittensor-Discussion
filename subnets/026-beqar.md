# NetUID 26 — beqar (`ב`)

## Overview

**beqar** (NetUID **26**) (`ב`).

A decentralized, incentive-driven web scraping engine

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `216`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,024.874437569. **Alpha liquidity in pool (`alpha_in`)** = ‎2,163,841.961640078ב‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,781,329.913780176ב‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003248864`** *(also **moving-average price** `0.003241161582991481` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎389,410.663820188ב‎`. **Owner hotkey / coldkey (chain):** `5FnLxqpzUFgrzW8aLjR5oYB8BUUS7XN9efw3N3diPpaxmTgt` / `5GsfAD4a3KXYKx2TF9UcajcW6C85Bw5vZsCTmrFep7RgMjcm`.
- **Subnet registered at block:** `4893280` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎162.941963307ב‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ב‎` · α-in `‎0.000000000ב‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003251032`
- **Market cap:** `13496662516600.84824784`
- **Liquidity:** `14059593111882`
- **Total τ:** `7027232001909`
- **Total α:** `4945096875420254`
- **α in pool:** `2163116545753417`
- **α staked:** `1988384428891203`
- **Price Δ 1h:** `0.319191480327634132`
- **Price Δ 1d:** `0.800380005320570578`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

A decentralized, incentive-driven web scraping engine



**Additional commentary (on-chain)**


בְּקַר

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GsfAD4a3KXYKx2TF9UcajcW6C85Bw5vZsCTmrFep7RgMjcm`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No miner/validator sections auto-matched.* Open [https://github.com/threetau/beqar/](https://github.com/threetau/beqar/) for requirements.

## On-chain identity — description


A decentralized, incentive-driven web scraping engine

## On-chain identity — additional field


בְּקַר

## Registered contact & links


- **GitHub:** [https://github.com/threetau/beqar/](https://github.com/threetau/beqar/)
- **Discord:** [https://discord.gg/6sFrH9B4Pa](https://discord.gg/6sFrH9B4Pa)
- **Logo URL:** [https://beqar.dev/beqar-tiny.png](https://beqar.dev/beqar-tiny.png)
- **Contact:** contact@kinitro.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104037 | 0.003250413 |
| 8104085 | 0.003251312 |
| 8104133 | 0.003251571 |
| 8104181 | 0.003251742 |
| 8104229 | 0.003251365 |
| 8104277 | 0.003248864 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.006845508 |
| 2026-03-10T23:59:48Z | 7718257 | 0.006827531 |
| 2026-03-11T23:59:48Z | 7725455 | 0.006901954 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.006739121 |
| 2026-03-13T23:59:48Z | 7739841 | 0.006647676 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.006569038 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005903055 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005900202 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005234375 |
| 2026-03-18T23:59:48Z | 7775819 | 0.004992132 |
| 2026-03-19T23:59:48Z | 7783014 | 0.0047931903600911131 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004965274 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005150411 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005294813 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005203839 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00517827480244748551 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005012035 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004992303 |
| 2026-03-27T23:59:48Z | 7840596 | 0.00495747 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005003108 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004957137 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004984533 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005042919 |
| 2026-04-01T23:59:48Z | 7876474 | 0.005084271 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004990111 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004998514 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.005187997 |
| 2026-04-05T23:59:48Z | 7905188 | 0.005168126 |
| 2026-04-06T23:59:48Z | 7912388 | 0.005120887 |
| 2026-04-07T23:59:48Z | 7919588 | 0.005081034 |
| 2026-04-08T23:59:48Z | 7926788 | 0.005058443 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004907791 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004328942 |
| 2026-04-11T23:59:48Z | 7948384 | 0.003849861 |
| 2026-04-12T23:59:48Z | 7955584 | 0.003884425 |
| 2026-04-13T23:59:48Z | 7962784 | 0.003813918 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003842781 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.003899199 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003951943 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003932551 |
| 2026-04-18T23:59:48Z | 7998779 | 0.003942117 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003896704 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004757025 |
| 2026-04-21T23:59:48Z | 8020376 | 0.005044501 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004971792 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003378559 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003366642 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003363563 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003368141 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.003212719 |
| 2026-04-28T23:59:48Z | 8070646 | 0.003272514 |
| 2026-04-29T23:59:48Z | 8077790 | 0.003279038 |
| 2026-04-30T23:59:48Z | 8084984 | 0.003245709 |
| 2026-05-01T23:59:48Z | 8092168 | 0.00321547 |
| 2026-05-02T23:59:48Z | 8099357 | 0.003223235 |
| 2026-05-03T16:10:00Z | 8104202 | 0.003251032 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

