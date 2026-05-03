# NetUID 78 — Vocence (`و`)

## Overview

The voice layer for decentralized intelligence

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 142
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5FnQCJW2Rm1BijNBUJzPetcpZx43RWutYiyaxA8j88fy9i9L`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
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

## Validator quick start

**To run a validator you must contact the Vocence team.** They will:

- Grant **Chutes permission** so your validator can access miners' chutes.
- Provide the **owner API endpoint** (`API_URL`) for miner list, blocklist, and evaluation submission (dashboard integration).
- Provide the **Hippius sub-bucket keys**

Then:

1. **Clone, env, and run with Docker (recommended)**

   ```bash
   git clone https://github.com/Vocence-bt/vocence
   cd vocence
   cp env.example .env
   # Edit .env: NETWORK, NETUID (78), WALLET_NAME, HOTKEY_NAME,
   # CHUTES_API_KEY, API_URL, Hippius keys, VALIDATOR_NAME, etc.
   # Edit VALIDATOR_BUCKETS_JSON with readonly access for active validator sample buckets.
   docker-compose up -d
   ```

   The stack runs the published validator image and **Watchtower**; when the team pushes a new image, your validator auto-updates. See **[docs/validator-setup.md](docs/validator-setup.md)** for details and **[docs/cicd-pipeline.md](docs/cicd-pipeline.md)** for how the image is built and published.

2. **Optional: run from source**

   ```bash
   uv sync
   uv run vocence serve
   ```

   For all validator CLI options (e.g. split generator vs weight setter), see [docs/CLI.md](docs/CLI.md#validator-commands).

---

---

## Validator scoring

Sample generation is still local to each validator: each validator downloads source audio, queries miners, evaluates results, uploads artifacts to its own Hippius bucket, and submits evaluation metadata to the owner API.

Weight setting is now **global and deterministic**:

- Validators fetch the current **valid miner list** from the owner API.
- Validators fetch the current **active validator list** from the owner API. A validator is considered active when it submitted evaluation data recently (default window: 24 hours).
- Validators load local readonly bucket credentials from `VALIDATOR_BUCKETS_JSON` in `.env`.
- For each active validator that also exists in `VALIDATOR_BUCKETS_JSON`, validators read the most recent scoring window from that validator's bucket (default: 50 evaluations).
- Miner win rates are aggregated across active validators using **stake-weighted scoring**, where each validator's influence is weighted by `sqrt(stake)` from the current metagraph.
- A miner is globally eligible only if it has more than **40 evaluations** in at least **3 active validator buckets**.
- The winner must still beat earlier eligible miners, including the owner base model when present, by `THRESHOLD_MARGIN`.
- If there are too few active validators, too few readable validator buckets, or no miner satisfies the consensus + margin rules, validators burn by setting weight `1.0` on UID `0`.

This makes honest validators converge on the same leader from the same cross-validator evidence instead of relying on a single validator's local bucket.

---

---

## Miner quick start

See the **miner_sample/** directory for the full flow (HF repo + Chutes wrapper). You can also use the [CLI](docs/CLI.md#miner-commands) to deploy and commit:

- **vocence miner push** — Deploy your model to Chutes (`--model-name`, `--model-revision`).
- **vocence miner commit** — Commit model + Chute ID to chain (`--chute-id`, wallet).

miner_sample contains:

- **MINER_GUIDE.md** — Repo layout, engine contract, approved variables, render/build/deploy, and owner-side wrapper integrity.
- **chute_template/** — Canonical Jinja2 template; render with your four variables.
- **example_repo/** — Example HF repo layout (mock miner.py, chute_config.yml, vocence_config.yaml).

Use **uv** for local tooling (e.g. `uv run vocence`); Chutes builds run in their own environment.

---

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- `| **Miners** | Train PromptTTS models, publish them on Hugging Face, and deploy on [Chutes](https://chutes.ai) using the canonical Vocence wrapper. They expose a single `/speak` API (text + instruction → WAV). You can run miner workflows via the [CLI](docs/CLI.md#miner-commands) (`vocence miner push`, `vocence miner commit`) or follow [miner_sample](miner_sample/MINER_GUIDE.md) for the Chutes deploy. Rewards come from validator scores. |`


*Primary README URL used: `https://raw.githubusercontent.com/vocence-78/vocence/master/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


The voice layer for decentralized intelligence

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://www.vocence.ai](https://www.vocence.ai)
- **GitHub:** [https://github.com/vocence-78/vocence](https://github.com/vocence-78/vocence)
- **Discord:** [https://discord.gg/TWmfwJAtXG](https://discord.gg/TWmfwJAtXG)
- **Logo URL:** [https://www.vocence.ai/tab_logo.png](https://www.vocence.ai/tab_logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.011765339 |
| 8103891 | 0.011772546 |
| 8103939 | 0.011810428 |
| 8103987 | 0.011465059 |
| 8104035 | 0.01155241 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

