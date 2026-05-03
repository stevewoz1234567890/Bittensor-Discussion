# NetUID 54 — Yanez MIID (`ت`)

## Overview

Yanez MIID generates synthetic identities for testing financial crime prevention systems

This subnet powers Yanez Compliance, an AI-powered platform for detecting and correcting exposure, weaknesses, and configuration flaws in financial crime prevention systems. Effective financial crime prevention depends on how well these systems can detect fraudulent identities, prevent money laundering, and reduce regulatory risks. To properly test these systems, a diverse and controlled dataset of inorganic identities is essential. By leveraging Bittensor’s decentralized AI infrastructure, the Yanez subnet enables the generation of high-quality inorganic identities, which serve as the foundation for testing, tuning, and validating fraud detection, sanctions screening, and broader financial crime prevention measures. With a direct business use case and existing clients, the Yanez subnet brings practical, real-world adoption to the Bittensor ecosystem — demonstrating how decentralized AI can support financial institutions in strengthening their compliance and security frameworks.

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5FUfruyVDoDsCty1Sh7tCmHVdpoC3XV1nUZYjhcpfe31Defk`

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
- **`commit_reveal_period`:** `5`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### 🛠️ **Miners: Generate KAV and Image Variations**

Miners process requests from validators and return **identity data variations** to enhance detection models.

- Receive mixed identity challenges from validators (KAV and image-variation requests; UAV address not in scope this cycle)
- Generate **KAV** variations: Name / DOB / Address
- Generate **face image variations** from validator-provided seed images (Phase 4; Cycle 2 includes screen_replay)
- Earn rewards based on accuracy, novelty, constraint adherence, and real-world adversarial value

---

### 🧑‍🏫 **Validators: Evaluate & Score Miners**

Validators ensure the dataset maintains **high-quality** and **real-world relevance**.

- Issue challenge queries across KAV and image variations (UAV address not in scope this cycle)
- Run online validation for immediate weight setting (where applicable)
- Perform post-validation to assess novelty/quality and update miner reputation for the next cycle
- Allocate rewards and continuously evolve the dataset for KYC/IDV resilience

---

---

### Prerequisites

- **Python 3.10+**
- **Ollama (default LLM: llama3.1)**
- **Bittensor wallet with TAO**
- **8GB+ RAM (16GB recommended)**
- **Open port 8091 for miner-to-validator communication** ([Network Setup Guide](docs/network_setup.md))

---

### 1️⃣ **Setup for Miners**

```bash

---

# Install dependencies

bash scripts/miner/setup.sh

---

# Activate the miner environment

source miner_env/bin/activate

---

# Start mining

pm2 start python --name neuron-miner -- neurons/miner.py --netuid 54 --wallet.name your-wallet --wallet.hotkey your-hotkey --subtensor.network finney

```

---

### 2️⃣ **Setup for Validators**

```bash

---

# Install dependencies

bash scripts/validator/setup.sh

---

# Activate the validator environment

source validator_env/bin/activate

---

### Phase 2: Miner-Contributed Threat Scenarios (Q4 2025)

- Expand Threat Scenario Query System to allow miners to propose unknown threat scenarios.
- Introduce a **Post-Evaluation System** to systematically validate and assess new miner-submitted threat scenarios.
- Support new evasion tactics, including nickname-based threats, transliteration-based alterations, and middle name manipulations.
- Improve validator scoring and introduce penalties for repetitive or low-value submissions.

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - **8GB+ RAM (16GB recommended)**

---

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - CPU: 4 physical cores minimum (8+ recommended for better throughput)
- - Sufficient storage for LLM model weights (~10GB or more depending on model)
- - Storage recommendation (Basic path): 30GB minimum free disk, 50GB+ recommended (OS + repo + venv + Ollama models + logs)
- - At least 8GB RAM (16GB+ recommended)
- - GPU with at least 8GB VRAM recommended (NVIDIA CUDA or Apple Silicon MPS)
- - CPU: 8 physical cores recommended (12+ preferred when handling image jobs continuously)
- - Additional storage for diffusion model weights (typically ~10GB for FLUX.2-klein; more if you also use Kontext/Qwen)
- - Storage recommendation (Full path): 80GB minimum free disk, 150GB+ recommended (base stack + multiple image models + cache + outputs)
- > **Machine sizing quick guide:** For **Basic** mining, target at least **4 cores / 8GB RAM / 30GB free disk** (better: 8 cores / 16GB / 50GB+). For **Full** mining, target at least **8 cores / 16GB RAM / 80GB free disk + 8GB VRAM GPU** (better: 12+ cores / 32GB RAM / 150GB+ disk + higher-VRAM GPU).
- `| Path | What it does | Extra packages | GPU needed? |`
- `| **Full (recommended)** | Name variations **+ face image variations** (Phase 4) | `requirements-miner.txt` (`diffusers`, `transformers`, `accelerate`, `opencv-python`, AdaFace setup) | Yes (8+ GB VRAM) |`
- > **Which should I pick?** If you have a GPU and want to earn the maximum possible rewards (including face-variation reputation), choose **Full**. If you just want to get started quickly or do not have a GPU, choose **Basic** -- you can upgrade to Full later without losing anything.
- 4. **If you chose Full**, set your Hugging Face token and GPU device **before** the first miner run (create a token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and accept model licenses—see [Path B](#path-b-full-setup-name--image-variations) for details):
- export FLUX_DEVICE="cuda"   # or mps (Apple) or cpu (slow)
- - **Production**: After either path, consider a process manager (systemd, supervisor, tmux, pm2—see [Background Mining Guide](background_mining.md)), monitoring, logging, and a GPU for LLM and image workloads.
- export FLUX_DEVICE="cuda"    # NVIDIA
- export FLUX_DEVICE="cuda"
- - `FLUX_DEVICE`: Device for image generation (`cuda`, `mps`, or `cpu`)
- `| `FLUX_DEVICE` | `cuda`, `mps`, or `cpu` | `cpu` | Full |`
- `| Model | Description | VRAM needed |`
- `| **FLUX.2-klein** (`flux_klein`) | Fast baseline model; lowest overhead and most stable default path | ~8 GB |`
- `| **PuLID** (`pulid`) | Identity-focused path: tries Nunchaku PuLID on CUDA, otherwise falls back to FLUX.1-Kontext | ~12 GB+ (Nunchaku path); fallback depends on Kontext |`
- `| **PuLID-FLUX2** (`pulid_flux2`) | FLUX.2-klein backbone for PuLID-FLUX2-style identity experiments | ~8 GB |`
- - Best on higher-memory GPUs (commonly ~24 GB class).
- `| **KAV (Known Attack Vectors)** | 15% | All miners, based on quality score |`
- `| Tier | Score Range | Multiplier |`
- 4. Use a powerful GPU if available to speed up LLM inference
- 1. **Use a GPU** -- image generation on CPU is too slow for production.


*Primary README URL used: `https://raw.githubusercontent.com/yanez-compliance/MIID-subnet/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Yanez MIID generates synthetic identities for testing financial crime prevention systems

## On-chain identity — additional field


This subnet powers Yanez Compliance, an AI-powered platform for detecting and correcting exposure, weaknesses, and configuration flaws in financial crime prevention systems. Effective financial crime prevention depends on how well these systems can detect fraudulent identities, prevent money laundering, and reduce regulatory risks. To properly test these systems, a diverse and controlled dataset of inorganic identities is essential. By leveraging Bittensor’s decentralized AI infrastructure, the Yanez subnet enables the generation of high-quality inorganic identities, which serve as the foundation for testing, tuning, and validating fraud detection, sanctions screening, and broader financial crime prevention measures. With a direct business use case and existing clients, the Yanez subnet brings practical, real-world adoption to the Bittensor ecosystem — demonstrating how decentralized AI can support financial institutions in strengthening their compliance and security frameworks.

## Registered contact & links


- **Website:** [https://www.yanez.ai](https://www.yanez.ai)
- **GitHub:** [https://github.com/yanez-compliance/MIID-subnet](https://github.com/yanez-compliance/MIID-subnet)
- **Discord:** [https://discord.com/channels/799672011265015819/1351934165964296232](https://discord.com/channels/799672011265015819/1351934165964296232)
- **Logo URL:** [https://www.dropbox.com/scl/fi/qdp0wjseryfuul0uibh06/Yanez-AI-Logo-Icon-Outline-Glow.png?rlkey=kbtcpb5mhdpymcbjjbsd425kw&st=te8yxdou&raw=1](https://www.dropbox.com/scl/fi/qdp0wjseryfuul0uibh06/Yanez-AI-Logo-Icon-Outline-Glow.png?rlkey=kbtcpb5mhdpymcbjjbsd425kw&st=te8yxdou&raw=1)
- **Contact:** jose@yanezcompliance.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.007274335 |
| 8103843 | 0.007274318 |
| 8103891 | 0.007274311 |
| 8103939 | 0.007274303 |
| 8103987 | 0.007276638 |
| 8104035 | 0.007275944 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

