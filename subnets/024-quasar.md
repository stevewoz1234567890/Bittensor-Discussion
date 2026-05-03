# NetUID 24 — Quasar (`ω`)

## Overview

Bittensor subnet built to crush the long-context barrier.

-

**From crawled page (site or GitHub):** Building the next generation of long-context foundation models. Open weights, novel architectures, real benchmarks.

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
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.000564489
- **Owner SS58 (`owner_ss58`):** `5EjSHN7ZH4y21tgf8ACe5WtRQYvoWdLS6xsYvBktEycbmKYi`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
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

## Model Requirements

Submissions must match the official Quasar base interface. The canonical config
is the `config.json` in
[`silx-ai/Quasar-3B-A1B-Preview`](https://huggingface.co/silx-ai/Quasar-3B-A1B-Preview).

A valid model must:

- Use the Quasar architecture and tokenizer.
- Keep `vocab_size=248320`.
- Stay within the current subnet parameter cap.
- Provide public safetensors weights.
- Include the expected Quasar custom code files.
- Be loadable with `AutoModelForCausalLM.from_pretrained(..., trust_remote_code=True)`.
- Stay public and unchanged after the committed revision.
- Avoid quantized formats such as GPTQ, AWQ, GGUF, and FP8.
- Use unique weights that are not identical to an earlier committed model.

---

## Validator Guide

Requirements:

- Bittensor wallet registered as a validator on subnet 24.
- Python 3.10+.
- GPU capacity for the current evaluator.
- Local wallet keys kept on the validator host.

Quick start:

```bash
python -m pip install -r requirements-validator.txt
bash scripts/run_validator.sh
```

Common validator settings:

```bash
QUASAR_NETWORK=finney
QUASAR_NETUID=24
QUASAR_WALLET_NAME=validator
QUASAR_HOTKEY_NAME=validator
QUASAR_WALLET_PATH=/path/to/wallets
QUASAR_STATE_DIR=/path/to/state
```

Keep wallet files, provider keys, Hugging Face tokens, and state credentials out
of git. Use a private environment file or your process manager's secret store.


*README source used for excerpts: `https://raw.githubusercontent.com/SILX-LABS/QUASAR-SUBNET/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Bittensor subnet built to crush the long-context barrier.

## On-chain identity — additional field


-

## Registered contact & links


- **Website:** [https://silxinc.com/](https://silxinc.com/)
- **GitHub:** [https://github.com/SILX-LABS/QUASAR-SUBNET/](https://github.com/SILX-LABS/QUASAR-SUBNET/)
- **Discord:** [https://discordapp.com/channels/799672011265015819/1214246819886931988](https://discordapp.com/channels/799672011265015819/1214246819886931988)
- **Logo URL:** [https://silxinc.com/_next/image?url=%2Flogo-white.png&w=640&q=75](https://silxinc.com/_next/image?url=%2Flogo-white.png&w=640&q=75)
- **Contact:** -

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.014548731 |
| 8103690 | 0.014578242 |
| 8103738 | 0.014589056 |
| 8103786 | 0.01457274 |
| 8103834 | 0.014572145 |
| 8103882 | 0.014534076 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** SILX AI
- **Meta / og:description:** Building the next generation of long-context foundation models. Open weights, novel architectures, real benchmarks.
- **Fetched from:** [https://silxinc.com/](https://silxinc.com/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

