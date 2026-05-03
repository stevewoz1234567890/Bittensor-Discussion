# NetUID 34 — BitMind (`י`)

## Overview

**BitMind** (NetUID 34) does not currently expose a long on-chain description. Use the registered links and any website excerpt below; confirm the subnet’s purpose on official channels and explorers.

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
- **`difficulty` (PoW field on info view):** 943295763109
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5DthmKBR83sUdudSfgFnsxBkTYtYTFLJUgovNfb1TSKVLiTH`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `943295763109` (min `10000000`, max `18446744073709551615`)
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
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `500000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Installation

```bash
git clone https://github.com/BitMind-AI/bitmind-subnet.git
cd bitmind-subnet
./install.sh
```

**Options:**
- `./install.sh --no-system-deps` - Skip system dependency installation (intended for discriminative miners)

---

# Activate virtual environment to use gascli

source .venv/bin/activate

---

# Validators: Start or restart validator services

gascli validator start

---

# Miners: Start or restart generative miner

gascli generator start

---

# Miners: Push discriminator models (all three modalities at once)

gascli d push \
  --image-model image_detector.zip \
  --video-model video_detector.zip \
  --audio-model audio_detector.zip \
  --wallet-name default --wallet-hotkey default

---

# Miners: Check your benchmark performance (epistula-authenticated)

gascli d perf --wallet-name default --wallet-hotkey default
gascli d perf --modality image              # filter by modality
gascli d perf --modality image --vertical human  # filter by vertical
```

**Available Aliases:**
- `validator` → `vali`, `v`
- `discriminator` → `d`
- `generator` → `gen`, `g`

---

# (Does not require virtualenv activation)

pm2 start validator.config.js

---

# Miners: Start or restart generative miner

pm2 start gen_miner.config.js

---

# Miners: Push discriminator models

source .venv/bin/activate
python neurons/discriminator/push_model.py \
  --image-model image_detector.zip \
  --video-model video_detector.zip \
  --audio-model audio_detector.zip \
  --wallet-name default --wallet-hotkey default
```
For detailed installation and usage instructions, see [Installation Guide](docs/Installation.md).

---

#### Discriminative Miners [[docs](docs/Discriminative-Mining.md)]

Discriminative miners submit detection models for evaluation against a wide variety of real and synthetic media across **image, video, and audio** modalities. Models are evaluated on cloud infrastructure and rewarded based on their accuracy and calibration. This significantly reduces the capital required to mine compared to previous versions that required GPU hosting, and allows the subnet to more reliably identify unique models and reward novel contributions proportionally to their accuracy.

---

#### Generative Miners [[docs](docs/Generative-Mining.md)]

Generative miners generate synthetic images and videos according to prompts from validators, and are rewarded based on their ability to pass validation checks and fool discriminative miners.

---

#### Validators [[docs](docs/Validating.md)]

Validators are responsible for challenging and scoring both miner types. Generative miners are sent prompts, and their returned synthetic media are validated to mitigate gaming and incentivize high quality results. Discriminative miners are continually evaluated against a mix of data from generative miners, real world data, and data generated locally on the validator.

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- `| Track | What You Do | How You're Scored |`
- `| **Discriminative Mining** | Submit AI-generated content detection models (image, video, audio) | `sn34_score` -- geometric mean of MCC and Brier score, measuring both accuracy and calibration |`
- - **Cloud-evaluated**: Discriminator models are benchmarked on cloud infrastructure -- no GPU hosting required
- Discriminative miners submit detection models for evaluation against a wide variety of real and synthetic media across **image, video, and audio** modalities. Models are evaluated on cloud infrastructure and rewarded based on their accuracy and calibration. This significantly reduces the capital required to mine compared to previous versions that required GPU hosting, and allows the subnet to more reliably identify unique models and reward novel contributions proportionally to their accuracy.


*Primary README URL used: `https://raw.githubusercontent.com/BitMind-AI/bitmind-subnet/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


*Empty — no description bytes set in `SubnetIdentity`.*

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/BitMind-AI/bitmind-subnet](https://github.com/BitMind-AI/bitmind-subnet)
- **Contact:** intern@bitmind.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.013708205 |
| 8103843 | 0.013706698 |
| 8103891 | 0.013706691 |
| 8103939 | 0.013706493 |
| 8103987 | 0.013706487 |
| 8104035 | 0.013706482 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

