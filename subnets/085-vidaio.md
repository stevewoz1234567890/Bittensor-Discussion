# NetUID 85 — Vidaio (`ᚱ`)

## Overview

**Vidaio** (NetUID **85**) (`ᚱ`).

Next-Generation Video Processing Powered By AI

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `275`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ19,535.746651269. **Alpha liquidity in pool (`alpha_in`)** = ‎1,478,560.684629681ᚱ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,671,686.902764039ᚱ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.013161102`** *(also **moving-average price** `0.01311569451354444` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,161,649.355896656ᚱ‎`. **Owner hotkey / coldkey (chain):** `5FR392L6eKrTGwUjQurpxw89YUe7LzKANktDwRKLYYSgwxhb` / `5GTPBjA4uXhuQ51SJB7Jd55JwY6dKEnbnjCrsSSEXy3MN63z`.
- **Subnet registered at block:** `5258781` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎204.631286709ᚱ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.006580553` · α-out `‎1.000000000ᚱ‎` · α-in `‎0.500000000ᚱ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.01311447`
- **Market cap:** `50468446167862.12922148`
- **Liquidity:** `38925239761036`
- **Total τ:** `19500297233783`
- **Total α:** `4150139911302876`
- **α in pool:** `1481183953850458`
- **α staked:** `2367118430299426`
- **Price Δ 1h:** `0.079647235320607022`
- **Price Δ 1d:** `-1.573580455798409743`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `4`
- **Active miners:** `101`
- **Active dual:** `1`
- **Emission:** `6557234`
- **Max neurons:** `256`
- **Validators (metadata):** `4`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Next-Generation Video Processing Powered By AI

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

## On-chain identity — description


Next-Generation Video Processing Powered By AI

## On-chain identity — additional field


*Unset.*

## Registered contact & links


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
| 8104085 | 0.013158692 |
| 8104133 | 0.013114226 |
| 8104181 | 0.013114459 |
| 8104229 | 0.013114447 |
| 8104277 | 0.013161102 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

