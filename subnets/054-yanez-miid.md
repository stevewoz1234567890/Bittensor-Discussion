# NetUID 54 — Yanez MIID (`ت`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Yanez MIID** (NetUID **54**) (`ت`).

Yanez MIID generates synthetic identities for testing financial crime prevention systems



#### SubnetIdentity `additional` *(chain)*



This subnet powers Yanez Compliance, an AI-powered platform for detecting and correcting exposure, weaknesses, and configuration flaws in financial crime prevention systems. Effective financial crime prevention depends on how well these systems can detect fraudulent identities, prevent money laundering, and reduce regulatory risks. To properly test these systems, a diverse and controlled dataset of inorganic identities is essential. By leveraging Bittensor’s decentralized AI infrastructure, the Yanez subnet enables the generation of high-quality inorganic identities, which serve as the foundation for testing, tuning, and validating fraud detection, sanctions screening, and broader financial crime prevention measures. With a direct business use case and existing clients, the Yanez subnet brings practical, real-world adoption to the Bittensor ecosystem — demonstrating how decentralized AI can support financial institutions in strengthening their compliance and security frameworks.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `41`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ10,302.881601243. **Alpha liquidity in pool (`alpha_in`)** = ‎1,440,677.378034572ت‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,388,541.016991834ت‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007115810`** *(also **moving-average price** `0.007169150281697512` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎697,149.216484676ت‎`. **Owner hotkey / coldkey (chain):** `5DUB7kNLvvx8Dj7D8tn54N1C7Xok6GodNPQE2WECCaL9Wgpr` / `5FUfruyVDoDsCty1Sh7tCmHVdpoC3XV1nUZYjhcpfe31Defk`.
- **Subnet registered at block:** `4742549` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎30.874876597ت‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002014963` · α-out `‎1.000000000ت‎` · α-in `‎0.283167163ت‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104394`
- **Liquidity constant `k`:** `14843128451479398003572172996`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Yanez MIID` |
| Symbol (API) | `ت` |
| Rank | `32` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.007107177` |
| Market cap | `31682054221106.834103174` |
| Market cap Δ 1d | `-0.127352808615535652` |
| Liquidity | `20541134754032` |
| Total τ | `10296129995584` |
| Total α | `4828922609100613` |
| α in pool | `1441501282217689` |
| α staked | `3016253775958973` |
| Price Δ 1h | `-2.297538445930313362` |
| Price Δ 1d | `-0.291626051983427526` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `54` |
| Owner SS58 (API) | `5FUfruyVDoDsCty1Sh7tCmHVdpoC3XV1nUZYjhcpfe31Defk` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4742549` |
| Registration wall time | `2025-01-20T01:04:48Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `7` |
| Active miners | `190` |
| Active dual-role | `1` |
| Emission | `1957813` |
| Max neurons | `256` |
| Validator slots (metadata) | `7` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">
<picture>
    <source srcset="YanezSubnetLogo.png" media="(prefers-color-scheme: dark)">
    <source srcset="YanezSubnetLogo.png" media="(prefers-color-scheme: light)">
    <img src="YanezSubnetLogo.png" width="300">
</picture>

# **MIID Subnet 54 - Identity Testing Network**
[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.com/channels/799672011265015819/1351934165964296232)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Helpful Hints](https://img.shields.io/badge/Helpful-Hints-blue)](docs/helpful_hints.md)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black)](https://github.com/yanez-compliance/MIID-subnet)

[⛏️ Mining Guide](docs/miner.md) • [🧑‍🏫 Validator Guide](docs/validator.md) • [📊 Dashboard & Leaderboard](https://tao-ui-dashboard.yanez.ai/) • [🚀 Quick Start](docs/README.md)
</div>

---

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
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5FUfruyVDoDsCty1Sh7tCmHVdpoC3XV1nUZYjhcpfe31Defk` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `5` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

- - **8GB+ RAM (16GB recommended)**

---

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.yanez.ai](https://www.yanez.ai)
- **GitHub:** [https://github.com/yanez-compliance/MIID-subnet](https://github.com/yanez-compliance/MIID-subnet)
- **Discord:** [https://discord.com/channels/799672011265015819/1351934165964296232](https://discord.com/channels/799672011265015819/1351934165964296232)
- **Logo URL:** [https://www.dropbox.com/scl/fi/qdp0wjseryfuul0uibh06/Yanez-AI-Logo-Icon-Outline-Glow.png?rlkey=kbtcpb5mhdpymcbjjbsd425kw&st=te8yxdou&raw=1](https://www.dropbox.com/scl/fi/qdp0wjseryfuul0uibh06/Yanez-AI-Logo-Icon-Outline-Glow.png?rlkey=kbtcpb5mhdpymcbjjbsd425kw&st=te8yxdou&raw=1)
- **Contact:** jose@yanezcompliance.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.007106962 |
| 8104292 | 0.007113343 |
| 8104340 | 0.007094666 |
| 8104388 | 0.007089335 |
| 8104436 | 0.00711581 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

