# NetUID 32 — ItsAI (`ח`)

## Overview

ItsAI is a bittensor subnet focused on high-quality AI detection for texts. Recognised as the most accurate AI detector by MGTD benchmark.

**From crawled page (site or GitHub):** Free AI Detector (AI Checker) with 99% accuracy. Detect ChatGPT, Claude, Gemini, DeepSeek. Deep scan, plagiarism checker, batch upload, and API.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

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
- **Registration recycle cost snapshot (`burn`):** τ0.000813921
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

## Miner / validator compute notes (README excerpts)

No matching README sections were auto-detected for [https://github.com/It-s-AI/llm-detection](https://github.com/It-s-AI/llm-detection). Open the repository for miner/validator machine requirements, dependencies, and cloud sizing.

## On-chain identity — description


ItsAI is a bittensor subnet focused on high-quality AI detection for texts. Recognised as the most accurate AI detector by MGTD benchmark.

## On-chain identity — additional field


ItsAI is a bittensor subnet focused on high-quality AI detection for texts. Recognised as the most accurate AI detector by MGTD benchmark.

## Registered contact & links


- **Website:** [https://its-ai.org/en](https://its-ai.org/en)
- **GitHub:** [https://github.com/It-s-AI/llm-detection](https://github.com/It-s-AI/llm-detection)
- **Discord:** [https://discord.com/channels/799672011265015819/1215319932062011464](https://discord.com/channels/799672011265015819/1215319932062011464)
- **Logo URL:** [https://github.com/It-s-AI/llm-detection/blob/main/full_logo.png](https://github.com/It-s-AI/llm-detection/blob/main/full_logo.png)
- **Contact:** support@its-ai.org

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.003955875 |
| 8103690 | 0.004026103 |
| 8103738 | 0.004024085 |
| 8103786 | 0.004024069 |
| 8103834 | 0.003977377 |
| 8103882 | 0.003982388 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Best Free AI Detector & AI Checker - 99% Accuracy | It's AI
- **Meta / og:description:** Free AI Detector (AI Checker) with 99% accuracy. Detect ChatGPT, Claude, Gemini, DeepSeek. Deep scan, plagiarism checker, batch upload, and API.
- **Fetched from:** [https://its-ai.org/en](https://its-ai.org/en)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

