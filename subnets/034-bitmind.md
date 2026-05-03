# NetUID 34 — BitMind (`י`)

## Overview

**From crawled page (site or GitHub):** Contribute to BitMind-AI/bitmind-subnet development by creating an account on GitHub.

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

## Miner / validator compute notes (README excerpts)

### Installation

```bash
git clone https://github.com/BitMind-AI/bitmind-subnet.git
cd bitmind-subnet
./install.sh
```

**Options:**
- `./install.sh --no-system-deps` - Skip system dependency installation (intended for discriminative miners)

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


*README source used for excerpts: `https://raw.githubusercontent.com/BitMind-AI/bitmind-subnet/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

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
| 8103642 | 0.01370834 |
| 8103690 | 0.013708319 |
| 8103738 | 0.013708307 |
| 8103786 | 0.013708207 |
| 8103834 | 0.01370671 |
| 8103882 | 0.013706691 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** GitHub - BitMind-AI/bitmind-subnet · GitHub
- **Meta / og:description:** Contribute to BitMind-AI/bitmind-subnet development by creating an account on GitHub.
- **Fetched from:** [https://github.com/BitMind-AI/bitmind-subnet](https://github.com/BitMind-AI/bitmind-subnet)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

