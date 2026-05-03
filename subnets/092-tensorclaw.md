# NetUID 92 — TensorClaw (`ᚂ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**TensorClaw** (NetUID **92**) (`ᚂ`).

This project is a decentralized Large Language Model (LLM) inference subnet built on the Bittensor network. Its core purpose is to aggregate high-quality LLM API nodes (e.g., OpenAI, DeepSeek, Claude, Llama) globally through Bittensor's incentive mechanism, providing a unified, highly available, and load-balanced compatible API service to the public.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `79`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,825.558589732. **Alpha liquidity in pool (`alpha_in`)** = ‎340,775.245832894ᚂ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎952,976.494691202ᚂ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005356678`** *(also **moving-average price** `0.005062198033556342` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎22,618.606004621ᚂ‎`. **Owner hotkey / coldkey (chain):** `5GCR7hqR4JjBNrApho6NJkeD6wy5zHvvWU3RpxkGamjzPTDf` / `5Ck9Wu6bQ923pPgb7KWfszAWo6uraNryxw88JLfmRx7xUBTT`.
- **Subnet registered at block:** `7013758` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎51.127676451ᚂ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002678335` · α-out `‎1.000000000ᚂ‎` · α-in `‎0.500000000ᚂ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104356`
- **Liquidity constant `k`:** `622105177198273580376244408`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `TensorClaw`
- **Symbol (API):** `ᚂ`
- **Rank:** `109`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005324887`
- **Market cap:** `5200352768346.997071223`
- **Market cap Δ 1d:** `10.684542770668502562`
- **Liquidity:** `3638889795171`
- **Total τ:** `1819508728353`
- **Total α:** `1293459405193871`
- **α in pool:** `341675056544550`
- **α staked:** `634937736993979`
- **Price Δ 1h:** `0.839361098549321625`
- **Price Δ 1d:** `9.972338014020583128`
#### Subnet activity (TAOStats)

- **NetUID (API):** `92`
- **Owner SS58 (API):** `5Ck9Wu6bQ923pPgb7KWfszAWo6uraNryxw88JLfmRx7xUBTT`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `7013758`
- **Registration wall time:** `2025-12-03T00:19:48Z`
- **Registration cost snapshot:** `269838319596`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `2662433`
- **Max neurons:** `256`
- **Validator slots (metadata):** `11`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `50000000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.tensorclaw.ai](https://www.tensorclaw.ai)
- **GitHub:** [https://github.com/tensorclaw/tensorclaw](https://github.com/tensorclaw/tensorclaw)
- **Discord:** [https://discord.gg/5Qsqcttq](https://discord.gg/5Qsqcttq)
- **Contact:** support@tensorclaw.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.005324971 |
| 8104292 | 0.005325183 |
| 8104340 | 0.005347242 |
| 8104388 | 0.005356387 |
| 8104436 | 0.005356686 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

