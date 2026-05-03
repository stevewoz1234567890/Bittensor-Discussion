# NetUID 92 — TensorClaw (`ᚂ`)

## Overview

**TensorClaw** (NetUID **92**) (`ᚂ`).

This project is a decentralized Large Language Model (LLM) inference subnet built on the Bittensor network.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `282`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,819.744418699. **Alpha liquidity in pool (`alpha_in`)** = ‎341,705.795383375ᚂ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎951,847.796890014ᚂ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005325097`** *(also **moving-average price** `0.005050938343629241` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎22,594.017740560ᚂ‎`. **Owner hotkey / coldkey (chain):** `5GCR7hqR4JjBNrApho6NJkeD6wy5zHvvWU3RpxkGamjzPTDf` / `5Ck9Wu6bQ923pPgb7KWfszAWo6uraNryxw88JLfmRx7xUBTT`.
- **Subnet registered at block:** `7013758` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎182.498646244ᚂ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002662555` · α-out `‎1.000000000ᚂ‎` · α-in `‎0.500000000ᚂ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005324887`
- **Market cap:** `5200352768346.997071223`
- **Liquidity:** `3638889795171`
- **Total τ:** `1819508728353`
- **Total α:** `1293459405193871`
- **α in pool:** `341675056544550`
- **α staked:** `634937736993979`
- **Price Δ 1h:** `0.839361098549321625`
- **Price Δ 1d:** `9.972338014020583128`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `2662433`
- **Max neurons:** `256`
- **Validators (metadata):** `11`
- **Neuron reg. cost:** `50000000`

### On-chain declared purpose *(SubnetIdentity)*

This project is a decentralized Large Language Model (LLM) inference subnet built on the Bittensor network. Its core purpose is to aggregate high-quality LLM API nodes (e.g., OpenAI, DeepSeek, Claude, Llama) globally through Bittensor's incentive mechanism, providing a unified, highly available, and load-balanced compatible API service to the public.

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** Tensorclaw Network | Subnet 92

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
- **Owner SS58 (`owner_ss58`):** `5Ck9Wu6bQ923pPgb7KWfszAWo6uraNryxw88JLfmRx7xUBTT`

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

#### Sections matched by heading (miner / validator / hardware / requirements)

### 1. Start Miner

```bash

---

### 2. Start Validator

```bash

---

## 📝 Log Management System

All core components feature an enterprise-grade rolling log system. In addition to console output, logs are automatically persisted to the `logs/` directory:
- **Daily Rotation**: Generates a new file every midnight formatted as `module-YYYYMMDD.

**In the next phase, we will launch the user UI, integrate Tao wallet connectivity, and enable Tao/Alpha deposits and spending.**

<img width="3002" height="1488" alt="image" src="https://github.com/user-attachments/assets/401eb4b2-fa60-4767-b593-8675d00bc8f4" />

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/tensorclaw/tensorclaw/main/README.md`*

## On-chain identity — description


This project is a decentralized Large Language Model (LLM) inference subnet built on the Bittensor network. Its core purpose is to aggregate high-quality LLM API nodes (e.g., OpenAI, DeepSeek, Claude, Llama) globally through Bittensor's incentive mechanism, providing a unified, highly available, and load-balanced compatible API service to the public.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.tensorclaw.ai](https://www.tensorclaw.ai)
- **GitHub:** [https://github.com/tensorclaw/tensorclaw](https://github.com/tensorclaw/tensorclaw)
- **Discord:** [https://discord.gg/5Qsqcttq](https://discord.gg/5Qsqcttq)
- **Contact:** support@tensorclaw.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.00531249 |
| 8104133 | 0.005324448 |
| 8104181 | 0.005324757 |
| 8104229 | 0.005324905 |
| 8104277 | 0.005325097 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004614349 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004943689 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005341724 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005150604 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004547308 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004882827 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004682439 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005039367 |
| 2026-03-17T23:59:48Z | 7768619 | 0.004894895 |
| 2026-03-18T23:59:48Z | 7775819 | 0.004997334 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00488812771087015797 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004523306 |
| 2026-03-21T23:59:48Z | 7797398 | 0.004730177 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005531101 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005217936 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00489770924847888309 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004809799 |
| 2026-03-26T23:59:48Z | 7833396 | 0.00455602 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004673188 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004664969 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004539578 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.00444439 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004290293 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004198052 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003946581 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004044572 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004240006 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004092411 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004026728 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004188909 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004230526 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003900864 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004113435 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004143651 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004082821 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004084932 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004016146 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.003910765 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003940145 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003798342 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004154147 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003725454 |
| 2026-04-20T23:59:48Z | 8013179 | 0.003772871 |
| 2026-04-21T23:59:48Z | 8020376 | 0.003850715 |
| 2026-04-22T23:59:48Z | 8027562 | 0.003851321 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003818719 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003928303 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003926955 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003967744 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004045251 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004271237 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004497644 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004862746 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004772042 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004877096 |
| 2026-05-03T16:10:00Z | 8104202 | 0.005324887 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

