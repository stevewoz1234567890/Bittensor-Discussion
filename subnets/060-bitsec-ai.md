# NetUID 60 — Bitsec.ai (`ذ`)

## Overview

**Bitsec.ai** (NetUID **60**) (`ذ`).

find and fix exploits in codebases

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `250`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,738.770591154. **Alpha liquidity in pool (`alpha_in`)** = ‎1,688,390.098509524ذ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,944,782.648341758ذ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004007557`** *(also **moving-average price** `0.004023564048111439` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎680,910.032623235ذ‎`. **Owner hotkey / coldkey (chain):** `5CXLwkK1Scd1uiMUrXYjJUTTPxqqyH2FTJQNLp9uXQhA9rhR` / `5CXLwkK1Scd1uiMUrXYjJUTTPxqqyH2FTJQNLp9uXQhA9rhR`.
- **Subnet registered at block:** `4796992` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎187.671943815ذ‎`; pending root emission `τ0.000000000`.
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
| 8104085 | 0.004007797 |
| 8104133 | 0.004007791 |
| 8104181 | 0.004007788 |
| 8104229 | 0.004007567 |
| 8104277 | 0.004007557 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.006394688 |
| 2026-03-10T23:59:48Z | 7718257 | 0.006716602 |
| 2026-03-11T23:59:48Z | 7725455 | 0.006451568 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.006310053 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005932015 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005942042 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005187023 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005290001 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005286301 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005458151 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00562918933527824808 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005376614 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005230109 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005072456 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005017827 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00488878158308374976 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004484147 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004533794 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004529827 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004576235 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004692067 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004580834 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004562022 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004641299 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004531971 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004474304 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004586781 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004804275 |
| 2026-04-06T23:59:48Z | 7912388 | 0.00527032 |
| 2026-04-07T23:59:48Z | 7919588 | 0.005846711 |
| 2026-04-08T23:59:48Z | 7926788 | 0.005938759 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004659872 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004895054 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004899274 |
| 2026-04-12T23:59:48Z | 7955584 | 0.005087512 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004934673 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004853116 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004979039 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004776763 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004820377 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004934581 |
| 2026-04-19T23:59:48Z | 8005979 | 0.005474128 |
| 2026-04-20T23:59:48Z | 8013179 | 0.005104784 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004983402 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004840347 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004840728 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004583533 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004603386 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004608686 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.00444885 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004389493 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004266986 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004166565 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004032505 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004079755 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004007786 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

