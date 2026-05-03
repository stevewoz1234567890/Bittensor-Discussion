# NetUID 96 — Verathos (`᚛`)

## Overview

**Verathos** (NetUID **96**) (`᚛`).

Verified AI inference and training subnet.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `224`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ63.754288588. **Alpha liquidity in pool (`alpha_in`)** = ‎2,879.932801789᚛‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎60,772.453572421᚛‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.022133219`** *(also **moving-average price** `0.014719460159540176` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,308.394185054᚛‎`. **Owner hotkey / coldkey (chain):** `5GpKXttD7h1spLMvFADW6pnpftakhiWy8iUAipq1najWMz8c` / `5CGq1JQhmZmR8w3pXFqycUgX9mcLt8bPwMZ8YDJbEmELpw7X`.
- **Subnet registered at block:** `7692872` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎97.639351691᚛‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002159834` · α-out `‎1.000000000᚛‎` · α-in `‎0.097562644᚛‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.021728965`
- **Market cap:** `860706158532.765960555`
- **Liquidity:** `126271042378`
- **Total τ:** `63135290338`
- **Total α:** `63638113780249`
- **α in pool:** `2905603283014`
- **α staked:** `36705402511913`
- **Price Δ 1h:** `-9.004551999235484572`
- **Price Δ 1d:** `43.737797333282177086`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `6`
- **Active miners:** `6`
- **Active dual:** `1`
- **Emission:** `2152974`
- **Max neurons:** `256`
- **Validators (metadata):** `6`
- **Neuron reg. cost:** `10000000`

### On-chain declared purpose *(SubnetIdentity)*

Verified AI inference and training subnet.

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <strong>Verathos</strong><br>
  Cryptographically verified AI compute on <a href="https://bittensor.com">Bittensor</a>
</p>

<p align="center">
  <a href="https://verathos.ai">Website</a> &middot;
  <a href="https://verathos.ai/docs">Docs</a> &middot;
  <a href="https://verathos.ai/chat">Try It</a> &middot;
  <a href="https://verathos.ai/docs?page=setup">Setup Guide</a>
</p>

---

Verathos is a decentralized compute network on Bittensor (Subnet 96) where any tensor operation – in inference or training – can be cryptographically proven via ZK-inspired **sumcheck-based verification** over Merkle-committed weights, anchored on-chain. Validators verify proofs on CPU in milliseconds and set weights accordingly. The result is a permissionless network where compute is verifiable, not trusted.

### Verified Inference – Live

A proof plugin integrates directly into production [vLLM](https://github.com/vllm-project/vllm) serving. It generates sumcheck proofs for GEMM operations in parallel during CUDA graph execution – no challenge-response round trip, single-digit percent overhead. The network exposes an OpenAI-compatible API with score-weighted routing across all miners.

### Verified Training – In Development

The same proof system extends to training. The training prover verifies forward pass, backward pass (gradient GEMM), and optimizer step for full fine-tuning and LoRA (AdamW, SGD, Muon). A training job produces proofs that the correct base model was fine-tuned with the claimed data and optimizer. The protocol is implemented and tested but not yet active on the network.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Cryptographically verified AI inference and training on Bittensor. Trust the math, not the server.

**Fetched document title:** Verathos — Verified Intelligence for Everyone

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

## On-chain identity — description


Verified AI inference and training subnet.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://verathos.ai](https://verathos.ai)
- **GitHub:** [https://github.com/verathos-ai/verathos](https://github.com/verathos-ai/verathos)
- **Logo URL:** [https://raw.githubusercontent.com/verathos-ai/verathos/main/assets/logo.png](https://raw.githubusercontent.com/verathos-ai/verathos/main/assets/logo.png)
- **Contact:** info@verathos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.023869921 |
| 8104072 | 0.023394761 |
| 8104120 | 0.022928382 |
| 8104168 | 0.021779155 |
| 8104216 | 0.022133219 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

