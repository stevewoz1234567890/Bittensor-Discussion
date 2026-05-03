# NetUID 96 — Verathos (`᚛`)

## Overview

Verified AI inference and training subnet.

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
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.010000000
- **Owner SS58 (`owner_ss58`):** `5CGq1JQhmZmR8w3pXFqycUgX9mcLt8bPwMZ8YDJbEmELpw7X`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.010000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `True`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### As a Miner

Requires NVIDIA GPU with 24 GB+ VRAM (RTX 4090, A100, H100, etc.).

**Quick start** (guided wizard handles wallet, registration, funding, HTTPS, PM2):
```bash
curl -fsSL https://verathos.ai/install.sh | bash   # or: git clone ... && cd verathos && bash scripts/setup_miner.sh
verathos setup                                       # interactive setup wizard
verathos start                                       # start mining
```

**Manual step-by-step:**
```bash
git clone https://github.com/verathos-ai/verathos && cd verathos
bash scripts/setup_miner.sh          # creates venv, installs deps, builds CUDA ext
```

Then create a wallet, register on subnet, fund your EVM address, and start:

```bash
python -m neurons.miner \
    --wallet miner --hotkey default \
    --model-id auto \
    --netuid 96 \
    --subtensor-network finney \
    --endpoint https://YOUR-PUBLIC-IP-OR-DOMAIN
```

`--model-id auto` detects your GPU and picks the optimal model. See the [Setup Guide](docs/setup.md) for wallet creation, EVM funding, model selection, and production deployment with PM2.

---

### As a Validator

No GPU required.

**Quick start:**
```bash
curl -fsSL https://verathos.ai/install.sh | bash -s – --validator   # or: git clone ... && bash scripts/setup_validator.sh
verathos setup validator                                              # interactive setup wizard
verathos start validator                                              # start validating
```

**Manual step-by-step:**
```bash
git clone https://github.com/verathos-ai/verathos && cd verathos
bash scripts/setup_validator.sh

python -m neurons.validator \
    --wallet validator --hotkey default \
    --netuid 96 \
    --subtensor-network finney
```

See the [Setup Guide](docs/setup.md) for wallet creation, EVM funding, auto-update, and running the gateway proxy.

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- Verathos is a decentralized compute network on Bittensor (Subnet 96) where any tensor operation – in inference or training – can be cryptographically proven via ZK-inspired **sumcheck-based verification** over Merkle-committed weights, anchored on-chain. Validators verify proofs on CPU in milliseconds and set weights accordingly. The result is a permissionless network where compute is verifiable, not trusted.
- A proof plugin integrates directly into production [vLLM](https://github.com/vllm-project/vllm) serving. It generates sumcheck proofs for GEMM operations in parallel during CUDA graph execution – no challenge-response round trip, single-digit percent overhead. The network exposes an OpenAI-compatible API with score-weighted routing across all miners.
- │  (GPU)   │  ── receipt ──►   │  (CPU)     │──shared_state──►│  (API)     │
- Requires NVIDIA GPU with 24 GB+ VRAM (RTX 4090, A100, H100, etc.).
- bash scripts/setup_miner.sh          # creates venv, installs deps, builds CUDA ext
- `--model-id auto` detects your GPU and picks the optimal model. See the [Setup Guide](docs/setup.md) for wallet creation, EVM funding, model selection, and production deployment with PM2.
- No GPU required.
- dist/           Pre-built wheels – zkllm (CUDA kernels)
- `zkllm` (cryptographic primitives, field arithmetic, Merkle trees, sumcheck, CUDA kernels) is distributed as a pre-built wheel in `dist/`. The setup scripts install it automatically.


*Primary README URL used: `https://raw.githubusercontent.com/verathos-ai/verathos/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Verified AI inference and training subnet.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://verathos.ai](https://verathos.ai)
- **GitHub:** [https://github.com/verathos-ai/verathos](https://github.com/verathos-ai/verathos)
- **Logo URL:** [https://raw.githubusercontent.com/verathos-ai/verathos/main/assets/logo.png](https://raw.githubusercontent.com/verathos-ai/verathos/main/assets/logo.png)
- **Contact:** info@verathos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.024033101 |
| 8103891 | 0.023934527 |
| 8103939 | 0.023831652 |
| 8103987 | 0.023830149 |
| 8104035 | 0.023151936 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

