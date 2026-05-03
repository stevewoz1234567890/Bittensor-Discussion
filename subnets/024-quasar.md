# NetUID 24 — Quasar (`ω`)

## Overview

Bittensor subnet built to crush the long-context barrier.

-

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

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
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
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

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

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

## Mining Guide

Requirements:

- Bittensor wallet registered on subnet 24.
- Hugging Face account for model hosting.
- Training infrastructure of your choice.

Install the miner dependencies:

```bash
python -m pip install -r requirements-miner.txt
```

Check your model before committing:

```bash
python miner/check_model.py --model-repo your-username/your-model
python miner/test_miner.py --model-repo your-username/your-model
```

Submit a dry run first:

```bash
python miner/miner.py \
  --network finney \
  --netuid 24 \
  --wallet-name my_wallet \
  --hotkey-name my_hotkey \
  --model-repo your-username/your-model \
  --dry-run
```

Remove `--dry-run` only after the checks pass and you are ready to commit that
repo revision on-chain.

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

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - Pre-checks run before GPU evaluation: architecture compliance, tokenizer
- - GPU capacity for the current evaluator.


*Primary README URL used: `https://raw.githubusercontent.com/SILX-LABS/QUASAR-SUBNET/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

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
| 8103795 | 0.014572736 |
| 8103843 | 0.014572113 |
| 8103891 | 0.014534075 |
| 8103939 | 0.014534549 |
| 8103987 | 0.01462203 |
| 8104035 | 0.014543955 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

