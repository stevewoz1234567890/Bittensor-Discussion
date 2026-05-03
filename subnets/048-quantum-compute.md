# NetUID 48 — Quantum Compute (`ק`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Quantum Compute** (NetUID **48**) (`ק`).

Quantum Computing

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `35`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ11,708.761699636. **Alpha liquidity in pool (`alpha_in`)** = ‎2,183,406.438908645ק‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,590,150.801254397ק‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005391867`** *(also **moving-average price** `0.005309318192303181` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎644,708.427506295ק‎`. **Owner hotkey / coldkey (chain):** `5D2Qc9ud7vTJrPzk8mT1ruY8oV8UaDP3ttepD7zVNNi943ch` / `5GNH5YMkcX8jEF1PukvxKafifcqz13jp18BT73jRL3AZc4Rc`.
- **Subnet registered at block:** `3856677` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎26.333787822ק‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ק‎` · α-in `‎0.000000000ק‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104400`
- **Liquidity constant `k`:** `25564985686632172431133753220`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Quantum Compute`
- **Symbol (API):** `ק`
- **Rank:** `50`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.00539191`
- **Market cap:** `22143025960247.3328735`
- **Market cap Δ 1d:** `-1.085875718832325782`
- **Liquidity:** `23481492711293`
- **Total τ:** `11708809619283`
- **Total α:** `4773324240163042`
- **α in pool:** `2183397551519015`
- **α staked:** `1923315275706835`
- **Price Δ 1h:** `1.236753760767850035`
- **Price Δ 1d:** `-1.259294636781233679`
#### Subnet activity (TAOStats)

- **NetUID (API):** `48`
- **Owner SS58 (API):** `5GNH5YMkcX8jEF1PukvxKafifcqz13jp18BT73jRL3AZc4Rc`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `3856677`
- **Registration wall time:** `2024-09-18T20:44:12Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `6`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `12`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Decentralized deep tech. Innovation from everywhere. Quantum computing, AI, and decentralized networks powered by Bittensor.

**Fetched document title:** qBitTensor Labs — Decentralized Deep Tech

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
- **`immunity_period` (blocks):** 2000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GNH5YMkcX8jEF1PukvxKafifcqz13jp18BT73jRL3AZc4Rc`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `2000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `3`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Validators

To set up a Validator please see [validator.md](qbittensor/validator/validator.md).

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/qbittensor-labs/quantum-compute/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.qbittensorlabs.com/](https://www.qbittensorlabs.com/)
- **GitHub:** [https://github.com/qbittensor-labs/quantum-compute](https://github.com/qbittensor-labs/quantum-compute)
- **Discord (handle / invite hint):** `qbittensorlabs`
- **Logo URL:** [https://qbittensorlabs.com/48.png](https://qbittensorlabs.com/48.png)
- **Contact:** qbittensorlabs@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.005391896 |
| 8104292 | 0.005391887 |
| 8104340 | 0.005391872 |
| 8104388 | 0.005391871 |
| 8104436 | 0.005391867 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.005946852 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005886146 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005802041 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005797698 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005650947 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.00570952 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005554154 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005460995 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005378215 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005274149 |
| 2026-03-19T23:59:48Z | 7783014 | 0.005214054824234724 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005219287 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005598617 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005640908 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005444556 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00604659470692959714 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005446305 |
| 2026-03-26T23:59:48Z | 7833396 | 0.005333612 |
| 2026-03-27T23:59:48Z | 7840596 | 0.00591835 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005492412 |
| 2026-03-29T23:59:48Z | 7854902 | 0.005733475 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.005980614 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005664542 |
| 2026-04-01T23:59:48Z | 7876474 | 0.005739697 |
| 2026-04-02T23:59:48Z | 7883622 | 0.005566388 |
| 2026-04-03T23:59:48Z | 7890794 | 0.005313196 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.005496048 |
| 2026-04-05T23:59:48Z | 7905188 | 0.00544761 |
| 2026-04-06T23:59:48Z | 7912388 | 0.005480475 |
| 2026-04-07T23:59:48Z | 7919588 | 0.005356887 |
| 2026-04-08T23:59:48Z | 7926788 | 0.005307427 |
| 2026-04-09T23:59:48Z | 7933987 | 0.005310094 |
| 2026-04-10T23:59:48Z | 7941184 | 0.00526893 |
| 2026-04-11T23:59:48Z | 7948384 | 0.005266132 |
| 2026-04-12T23:59:48Z | 7955584 | 0.005139672 |
| 2026-04-13T23:59:48Z | 7962784 | 0.005191656 |
| 2026-04-14T23:59:48Z | 7969979 | 0.005156601 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.005160929 |
| 2026-04-16T23:59:48Z | 7984379 | 0.005198343 |
| 2026-04-17T23:59:48Z | 7991579 | 0.005169509 |
| 2026-04-18T23:59:48Z | 7998779 | 0.005175443 |
| 2026-04-19T23:59:48Z | 8005979 | 0.00515798 |
| 2026-04-20T23:59:48Z | 8013179 | 0.005223027 |
| 2026-04-21T23:59:48Z | 8020376 | 0.005348639 |
| 2026-04-22T23:59:48Z | 8027562 | 0.00533972 |
| 2026-04-23T23:59:48Z | 8034762 | 0.005330535 |
| 2026-04-24T23:59:48Z | 8041962 | 0.005367844 |
| 2026-04-25T23:59:48Z | 8049151 | 0.005566972 |
| 2026-04-26T23:59:48Z | 8056274 | 0.006056865 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.005456548 |
| 2026-04-28T23:59:48Z | 8070646 | 0.005732627 |
| 2026-04-29T23:59:48Z | 8077790 | 0.005703574 |
| 2026-04-30T23:59:48Z | 8084984 | 0.00560805 |
| 2026-05-01T23:59:48Z | 8092168 | 0.005354062 |
| 2026-05-02T23:59:48Z | 8099357 | 0.005307291 |
| 2026-05-03T16:10:00Z | 8104202 | 0.00539191 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

