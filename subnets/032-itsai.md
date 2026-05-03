# NetUID 32 — ItsAI (`ח`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**ItsAI** (NetUID **32**) (`ח`).

ItsAI is a bittensor subnet focused on high-quality AI detection for texts. Recognised as the most accurate AI detector by MGTD benchmark.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `19`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,923.019020264. **Alpha liquidity in pool (`alpha_in`)** = ‎1,992,543.821329748ח‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,990,436.158667483ח‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003978148`** *(also **moving-average price** `0.004053440177813172` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎258,249.784877350ח‎`. **Owner hotkey / coldkey (chain):** `5DWgkCSvq4brWSNLDU9FBgTk1ZpAQ2y6t3ky97CvEVuS9Qad` / `5DWgkCSvq4brWSNLDU9FBgTk1ZpAQ2y6t3ky97CvEVuS9Qad`.
- **Subnet registered at block:** `2515294` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎14.340891742ח‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.001533757` · α-out `‎1.000000000ח‎` · α-in `‎0.385545485ח‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104416`
- **Liquidity constant `k`:** `15786962595105106664638013472`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `ItsAI`
- **Symbol (API):** `ח`
- **Rank:** `57`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003978302`
- **Market cap:** `19822256138088.055750688`
- **Market cap Δ 1d:** `-4.527965444128958737`
- **Liquidity:** `15849243914071`
- **Total τ:** `7922814170095`
- **Total α:** `4982656969168208`
- **α in pool:** `1992415292749676`
- **α staked:** `2990176812648068`
- **Price Δ 1h:** `-0.102551585908548292`
- **Price Δ 1d:** `-4.69866054050298902`
#### Subnet activity (TAOStats)

- **NetUID (API):** `32`
- **Owner SS58 (API):** `5DWgkCSvq4brWSNLDU9FBgTk1ZpAQ2y6t3ky97CvEVuS9Qad`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `2515294`
- **Registration wall time:** `2024-03-07T13:23:12Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `8`
- **Active miners:** `129`
- **Active dual-role:** `0`
- **Emission:** `1541220`
- **Max neurons:** `256`
- **Validator slots (metadata):** `8`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `701715`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Bittensor SN32** <!-- omit in toc -->
[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Free AI Detector (AI Checker) with 99% accuracy. Detect ChatGPT, Claude, Gemini, DeepSeek. Deep scan, plagiarism checker, batch upload, and API.

**Fetched document title:** Best Free AI Detector & AI Checker - 99% Accuracy | It's AI

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
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5DWgkCSvq4brWSNLDU9FBgTk1ZpAQ2y6t3ky97CvEVuS9Qad`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
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

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/It-s-AI/llm-detection/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://its-ai.org/en](https://its-ai.org/en)
- **GitHub:** [https://github.com/It-s-AI/llm-detection](https://github.com/It-s-AI/llm-detection)
- **Discord:** [https://discord.com/channels/799672011265015819/1215319932062011464](https://discord.com/channels/799672011265015819/1215319932062011464)
- **Logo URL:** [https://github.com/It-s-AI/llm-detection/blob/main/full_logo.png](https://github.com/It-s-AI/llm-detection/blob/main/full_logo.png)
- **Contact:** support@its-ai.org

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.003978303 |
| 8104244 | 0.003978291 |
| 8104292 | 0.003978284 |
| 8104340 | 0.003978152 |
| 8104388 | 0.003978151 |
| 8104436 | 0.003978148 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004619942 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004636156 |
| 2026-03-11T23:59:48Z | 7725455 | 0.004405335 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.004311694 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004229067 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004276672 |
| 2026-03-15T23:59:48Z | 7754226 | 0.003736885 |
| 2026-03-16T23:59:48Z | 7761426 | 0.003702673 |
| 2026-03-17T23:59:48Z | 7768619 | 0.003674436 |
| 2026-03-18T23:59:48Z | 7775819 | 0.003612519 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00335927633902305531 |
| 2026-03-20T23:59:48Z | 7790201 | 0.003271433 |
| 2026-03-21T23:59:48Z | 7797398 | 0.003461237 |
| 2026-03-22T23:59:48Z | 7804598 | 0.003388461 |
| 2026-03-23T23:59:48Z | 7811798 | 0.003471117 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00333942986342252816 |
| 2026-03-25T23:59:48Z | 7826196 | 0.003310325 |
| 2026-03-26T23:59:48Z | 7833396 | 0.0032215 |
| 2026-03-27T23:59:48Z | 7840596 | 0.003281763 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.00328041 |
| 2026-03-29T23:59:48Z | 7854902 | 0.003312173 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.003319325 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003354086 |
| 2026-04-01T23:59:48Z | 7876474 | 0.00332453 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003313469 |
| 2026-04-03T23:59:48Z | 7890794 | 0.003376846 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.003441113 |
| 2026-04-05T23:59:48Z | 7905188 | 0.003597903 |
| 2026-04-06T23:59:48Z | 7912388 | 0.003594921 |
| 2026-04-07T23:59:48Z | 7919588 | 0.00359791 |
| 2026-04-08T23:59:48Z | 7926788 | 0.003917765 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003908402 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004725721 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004375755 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004303976 |
| 2026-04-13T23:59:48Z | 7962784 | 0.003870763 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003851607 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.003740588 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003740163 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003841417 |
| 2026-04-18T23:59:48Z | 7998779 | 0.003869615 |
| 2026-04-19T23:59:48Z | 8005979 | 0.00384393 |
| 2026-04-20T23:59:48Z | 8013179 | 0.003657606 |
| 2026-04-21T23:59:48Z | 8020376 | 0.00368923 |
| 2026-04-22T23:59:48Z | 8027562 | 0.003741359 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003661242 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003698487 |
| 2026-04-25T23:59:48Z | 8049151 | 0.00360301 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003623097 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.00372965 |
| 2026-04-28T23:59:48Z | 8070646 | 0.003712668 |
| 2026-04-29T23:59:48Z | 8077790 | 0.003770893 |
| 2026-04-30T23:59:48Z | 8084984 | 0.003809269 |
| 2026-05-01T23:59:48Z | 8092168 | 0.003929319 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004175728 |
| 2026-05-03T16:10:00Z | 8104202 | 0.003978302 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

