# NetUID 34 — BitMind (`י`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**BitMind** (NetUID **34**) (`י`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `21`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ36,243.409210717. **Alpha liquidity in pool (`alpha_in`)** = ‎2,646,069.351119866י‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,051,819.386828391י‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.013695969`** *(also **moving-average price** `0.01371437986381352` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎596,388.888183253י‎`. **Owner hotkey / coldkey (chain):** `5HjBSeeoz52CLfvDWDkzupqrYLHz1oToDPHjdmJjc4TF68LQ` / `5DthmKBR83sUdudSfgFnsxBkTYtYTFLJUgovNfb1TSKVLiTH`.
- **Subnet registered at block:** `3493948` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎15.781233636י‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000י‎` · α-in `‎0.000000000י‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104414`
- **Liquidity constant `k`:** `95902574292573706923118803922`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `BitMind` |
| Symbol (API) | `י` |
| Rank | `19` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.013696065` |
| Market cap | `59571419474742.254532945` |
| Market cap Δ 1d | `-0.075078309588777188` |
| Liquidity | `72484147037559` |
| Total τ | `36243536103830` |
| Total α | `4697795060174259` |
| α in pool | `2646060086143657` |
| α staked | `1703468006395496` |
| Price Δ 1h | `-0.077495021225771042` |
| Price Δ 1d | `-0.182048829520552518` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `34` |
| Owner SS58 (API) | `5DthmKBR83sUdudSfgFnsxBkTYtYTFLJUgovNfb1TSKVLiTH` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3493948` |
| Registration wall time | `2024-07-29T23:10:36.006Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `9` |
| Active miners | `68` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">
  <img src="docs/static/bm-logo-black.png" alt="BitMind Logo" width="120"/>

  <h1>GAS<br><small>Generative Adversarial Subnet</small></h1>
  <h3><code>Bittensor SN34</code></h3>
  <p>
    <a href="docs/Mining.md">⛏️ Mining</a> ·
    <a href="docs/Validating.md">🛡️ Validating</a> ·
    <a href="docs/Incentive.md">💰 Incentives</a> ·
    <a href="https://app.bitmind.ai/">🏆 Leaderboard</a>
  </p>
  <p>
    🤗 <a href="https://huggingface.co/gasstation">GAS-Station</a> ·
    <a href="https://www.bitmind.ai/apps">🌐 Apps</a>
  </p>
</div>

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to BitMind-AI/bitmind-subnet development by creating an account on GitHub.

**Fetched document title:** GitHub - BitMind-AI/bitmind-subnet · GitHub

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
| `difficulty` (PoW field on info view) | 943295763109 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5DthmKBR83sUdudSfgFnsxBkTYtYTFLJUgovNfb1TSKVLiTH` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `943295763109` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `500000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

- `| Track | What You Do | How You're Scored |`
- `| **Discriminative Mining** | Submit AI-generated content detection models (image, video, audio) | `sn34_score` -- geometric mean of MCC and Brier score, measuring both accuracy and calibration |`
- - **Cloud-evaluated**: Discriminator models are benchmarked on cloud infrastructure -- no GPU hosting required
- Discriminative miners submit detection models for evaluation against a wide variety of real and synthetic media across **image, video, and audio** modalities. Models are evaluated on cloud infrastructure and rewarded based on their accuracy and calibration. This significantly reduces the capital required to mine compared to previous versions that required GPU hosting, and allows the subnet to more reliably identify unique models and reward novel contributions proportionally to their accuracy.


*Primary README URL used: `https://raw.githubusercontent.com/BitMind-AI/bitmind-subnet/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/BitMind-AI/bitmind-subnet](https://github.com/BitMind-AI/bitmind-subnet)
- **Contact:** intern@bitmind.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.013696067 |
| 8104244 | 0.013696033 |
| 8104292 | 0.013696013 |
| 8104340 | 0.013695981 |
| 8104388 | 0.013695979 |
| 8104436 | 0.013695969 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

