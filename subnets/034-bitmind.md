# NetUID 34 — BitMind (`י`)

## Overview

**BitMind** (NetUID **34**) (`י`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `224`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ36,243.472303073. **Alpha liquidity in pool (`alpha_in`)** = ‎2,646,064.744483049י‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,051,805.315691210י‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.013696017`** *(also **moving-average price** `0.01371523248963058` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎596,388.825090897י‎`. **Owner hotkey / coldkey (chain):** `5HjBSeeoz52CLfvDWDkzupqrYLHz1oToDPHjdmJjc4TF68LQ` / `5DthmKBR83sUdudSfgFnsxBkTYtYTFLJUgovNfb1TSKVLiTH`.
- **Subnet registered at block:** `3493948` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎168.332158037י‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000י‎` · α-in `‎0.000000000י‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.013696065`
- **Market cap:** `59571419474742.254532945`
- **Liquidity:** `72484147037559`
- **Total τ:** `36243536103830`
- **Total α:** `4697795060174259`
- **α in pool:** `2646060086143657`
- **α staked:** `1703468006395496`
- **Price Δ 1h:** `-0.077495021225771042`
- **Price Δ 1d:** `-0.182048829520552518`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `68`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

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

- `| Track | What You Do | How You're Scored |`
- `| **Discriminative Mining** | Submit AI-generated content detection models (image, video, audio) | `sn34_score` -- geometric mean of MCC and Brier score, measuring both accuracy and calibration |`
- - **Cloud-evaluated**: Discriminator models are benchmarked on cloud infrastructure -- no GPU hosting required
- Discriminative miners submit detection models for evaluation against a wide variety of real and synthetic media across **image, video, and audio** modalities. Models are evaluated on cloud infrastructure and rewarded based on their accuracy and calibration. This significantly reduces the capital required to mine compared to previous versions that required GPU hosting, and allows the subnet to more reliably identify unique models and reward novel contributions proportionally to their accuracy.


*Primary README URL used: `https://raw.githubusercontent.com/BitMind-AI/bitmind-subnet/main/README.md`*

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/BitMind-AI/bitmind-subnet](https://github.com/BitMind-AI/bitmind-subnet)
- **Contact:** intern@bitmind.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.013706451 |
| 8104133 | 0.013706437 |
| 8104181 | 0.01370643 |
| 8104229 | 0.01369604 |
| 8104277 | 0.013696017 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

