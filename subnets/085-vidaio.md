# NetUID 85 — Vidaio (`ᚱ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Vidaio** (NetUID **85**) (`ᚱ`).

Next-Generation Video Processing Powered By AI

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `72`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ19,535.704294431. **Alpha liquidity in pool (`alpha_in`)** = ‎1,478,721.906699189ᚱ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,671,751.206489515ᚱ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.013159658`** *(also **moving-average price** `0.013117627007886767` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,161,650.739993697ᚱ‎`. **Owner hotkey / coldkey (chain):** `5FR392L6eKrTGwUjQurpxw89YUe7LzKANktDwRKLYYSgwxhb` / `5GTPBjA4uXhuQ51SJB7Jd55JwY6dKEnbnjCrsSSEXy3MN63z`.
- **Subnet registered at block:** `5258781` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎53.576706865ᚱ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.006579828` · α-out `‎1.000000000ᚱ‎` · α-in `‎0.500000000ᚱ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104363`
- **Liquidity constant `k`:** `28887873902972543055404916459`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Vidaio`
- **Symbol (API):** `ᚱ`
- **Rank:** `21`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.01311447`
- **Market cap:** `50468446167862.12922148`
- **Market cap Δ 1d:** `-1.37330051845558366`
- **Liquidity:** `38925239761036`
- **Total τ:** `19500297233783`
- **Total α:** `4150139911302876`
- **α in pool:** `1481183953850458`
- **α staked:** `2367118430299426`
- **Price Δ 1h:** `0.079647235320607022`
- **Price Δ 1d:** `-1.573580455798409743`
#### Subnet activity (TAOStats)

- **NetUID (API):** `85`
- **Owner SS58 (API):** `5GTPBjA4uXhuQ51SJB7Jd55JwY6dKEnbnjCrsSSEXy3MN63z`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `5258781`
- **Registration wall time:** `2025-04-01T21:49:48Z`
- **Registration cost snapshot:** `264805234604`
- **Active keys:** `256`
- **Active validators:** `4`
- **Active miners:** `101`
- **Active dual-role:** `1`
- **Emission:** `6557234`
- **Max neurons:** `256`
- **Validator slots (metadata):** `4`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Vidaio Subnet**: Revolutionizing Video Processing with AI-Driven Decentralization <!-- omit in toc -->


Please check our [Tweet](https://x.com/vidaio_τ) to follow us.
[Website](https://vidaio.io)
[![vidAio](./docs/images/banner.png)](https://vidaio.io)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

</div>

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
- **`immunity_period` (blocks):** 7000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GTPBjA4uXhuQ51SJB7Jd55JwY6dKEnbnjCrsSSEXy3MN63z`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7000` blocks
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

### 2.2 Miners

Miners enhance video quality and optimize file sizes using AI-driven processing techniques. They can:
- Optimise open-source models or develop proprietary ones for superior upscaling and compression results.
- Handle video upscaling and compression requests from validators and end-users.
- Process both upscaling tasks (enhancing video quality) and compression tasks (reducing file size while maintaining quality).

---

### 2.3 Validators

Validators ensure miners deliver consistent, high-quality results by evaluating performance through synthetic and organic queries for both upscaling and compression workflows.

---

## 3. Setup

- [Validator Setup Guide](docs/validator_setup.md)
- [Miner Setup Guide](docs/miner_setup.md)

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/vidaio-subnet/vidaio-subnet/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://vidaio.io/](https://vidaio.io/)
- **GitHub:** [https://github.com/vidaio-subnet/vidaio-subnet](https://github.com/vidaio-subnet/vidaio-subnet)
- **Discord:** [https://discord.gg/xhn4jxJMEX](https://discord.gg/xhn4jxJMEX)
- **Logo URL:** [https://raw.githubusercontent.com/vidAio-subnet/brand-assets/main/logos/320x320.png](https://raw.githubusercontent.com/vidAio-subnet/brand-assets/main/logos/320x320.png)
- **Contact:** Vidaio@vidaio.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.013159974 |
| 8104292 | 0.013161113 |
| 8104340 | 0.013161085 |
| 8104388 | 0.013161111 |
| 8104436 | 0.013159659 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

