# NetUID 96 — Verathos (`᚛`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Verathos** (NetUID **96**) (`᚛`).

Verified AI inference and training subnet.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `83`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ63.990551392. **Alpha liquidity in pool (`alpha_in`)** = ‎2,912.646232639᚛‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎60,981.660736820᚛‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.021970066`** *(also **moving-average price** `0.014823513105511665` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,312.326599901᚛‎`. **Owner hotkey / coldkey (chain):** `5GpKXttD7h1spLMvFADW6pnpftakhiWy8iUAipq1najWMz8c` / `5CGq1JQhmZmR8w3pXFqycUgX9mcLt8bPwMZ8YDJbEmELpw7X`.
- **Subnet registered at block:** `7692872` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎36.189003245᚛‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002162836` · α-out `‎1.000000000᚛‎` · α-in `‎0.098444553᚛‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104352`
- **Liquidity constant `k`:** `186381838436401117283488`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Verathos` |
| Symbol (API) | `᚛` |
| Rank | `127` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.021728965` |
| Market cap | `860706158532.765960555` |
| Market cap Δ 1d | `65.09050163277971107` |
| Liquidity | `126271042378` |
| Total τ | `63135290338` |
| Total α | `63638113780249` |
| α in pool | `2905603283014` |
| α staked | `36705402511913` |
| Price Δ 1h | `-9.004551999235484572` |
| Price Δ 1d | `43.737797333282177086` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `96` |
| Owner SS58 (API) | `5CGq1JQhmZmR8w3pXFqycUgX9mcLt8bPwMZ8YDJbEmELpw7X` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7692872` |
| Registration wall time | `2026-03-07T11:19:36Z` |
| Registration cost snapshot | `444769705760` |
| Active keys | `256` |
| Active validators | `6` |
| Active miners | `6` |
| Active dual-role | `1` |
| Emission | `2152974` |
| Max neurons | `256` |
| Validator slots (metadata) | `6` |
| Max validators (API) | `64` |
| Neuron reg. cost | `10000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

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

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 256 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.010000000 |
| Owner SS58 (`owner_ss58`) | `5CGq1JQhmZmR8w3pXFqycUgX9mcLt8bPwMZ8YDJbEmELpw7X` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.010000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `True` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `3` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://verathos.ai](https://verathos.ai)
- **GitHub:** [https://github.com/verathos-ai/verathos](https://github.com/verathos-ai/verathos)
- **Logo URL:** [https://raw.githubusercontent.com/verathos-ai/verathos/main/assets/logo.png](https://raw.githubusercontent.com/verathos-ai/verathos/main/assets/logo.png)
- **Contact:** info@verathos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.021800902 |
| 8104292 | 0.021663449 |
| 8104340 | 0.021317046 |
| 8104388 | 0.021769773 |
| 8104436 | 0.021970066 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in -0.2290163 --> 3.202764
    line [2.201039035, 2.201039035, 2.293145388, 2.293145388, 2.293145388, 2.293145388, 2.319360266, 2.344552211, 2.470288298, 2.470288298, 2.47028828179, 2.491612824, 2.491612824, 2.491612824, 2.529893293, 2.55963223545, 2.559632301, 2.559632301, 2.559632301, 2.564431794, 2.564431794, 2.607308461, 2.690901156, 2.708984946, 2.708984946, 2.759127346, 2.759127346, 2.759127346, 2.765772255, 2.770761182, 2.770761182, 2.805138828, 2.805138828, 2.833547177, 2.872354896, 2.872354896, 2.907865891, 2.909616576, 2.909616576, 2.929025819, 2.929025819, 2.929025819, 2.929025819, 2.929025819, 2.964368665, 2.964368665, 2.966089785, 0.008805094, 0.007966327, 0.00765819, 0.012332225, 0.013177951, 0.013559801, 0.012766814, 0.022113699, 0.021728965]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

