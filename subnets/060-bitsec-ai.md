# NetUID 60 — Bitsec.ai (`ذ`)

## Overview

**Bitsec.ai** (NetUID **60**) (`ذ`).

find and fix exploits in codebases

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `188`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,738.788728514. **Alpha liquidity in pool (`alpha_in`)** = ‎1,688,385.572719824ذ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,944,725.174131458ذ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004007578`** *(also **moving-average price** `0.0040238534566015005` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎680,910.014485875ذ‎`. **Owner hotkey / coldkey (chain):** `5CXLwkK1Scd1uiMUrXYjJUTTPxqqyH2FTJQNLp9uXQhA9rhR` / `5CXLwkK1Scd1uiMUrXYjJUTTPxqqyH2FTJQNLp9uXQhA9rhR`.
- **Subnet registered at block:** `4796992` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎141.129324368ذ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ذ‎` · α-in `‎0.000000000ذ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004007786`
- **Market cap:** `16922013791442.014263534`
- **Liquidity:** `13505476784856`
- **Total τ:** `6738966823538`
- **Total α:** `4633097746851282`
- **α in pool:** `1688341134311656`
- **α staked:** `2533943636242963`
- **Price Δ 1h:** `-0.000848341492382392`
- **Price Δ 1d:** `2.059506823556734543`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `2`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

find and fix exploits in codebases

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Bitsec Subnet v2** <!-- omit in toc -->

[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** bitsec

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CXLwkK1Scd1uiMUrXYjJUTTPxqqyH2FTJQNLp9uXQhA9rhR`

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

## In order to simplify the building of subnets, this template abstracts away the complexity of the underlying blockchain and other boilerplate code. While the default behavior of the template is sufficient for a simple subnet, you should customize the template in order to meet your specific requirements.

```python
python -m venv env; source env/bin/activate;
pip install -U pip
pip install -r requirements.txt
```

---

#### CPU / GPU / RAM lines (automatic grep)

- - Limit resources (CPU/time) to prevent hangs.


*Primary README URL used: `https://raw.githubusercontent.com/Bitsec-AI/sandbox/main/README.md`*

## On-chain identity — description


find and fix exploits in codebases

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://bitsec.ai](https://bitsec.ai)
- **GitHub:** [https://github.com/Bitsec-AI/sandbox](https://github.com/Bitsec-AI/sandbox)
- **Discord (handle / invite hint):** `yubo`
- **Contact:** john@bitsec.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.004007802 |
| 8104072 | 0.004007797 |
| 8104120 | 0.004007792 |
| 8104168 | 0.004007788 |
| 8104216 | 0.004007578 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

