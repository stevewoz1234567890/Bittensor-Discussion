# NetUID 45 — Talisman AI (`פ`)

## Overview

**Talisman AI** (NetUID **45**) (`פ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `235`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,971.590931433. **Alpha liquidity in pool (`alpha_in`)** = ‎2,014,629.735497228פ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,752,829.838653054פ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003977924`** *(also **moving-average price** `0.003977326909080148` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎700,315.617102897פ‎`. **Owner hotkey / coldkey (chain):** `5Hmiaz4bLLbLw4LgTksJvJYPYp1XJ1GYkUfRiv4HGXX674DD` / `5FbcZiAHA75i2bPVrF7wa9mFaxV1eM27HR63kJtbpb8spvmf`.
- **Subnet registered at block:** `3633154` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎176.794719684פ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000פ‎` · α-in `‎0.000000000פ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003977941`
- **Market cap:** `16092620970417.358461644`
- **Liquidity:** `15985669155987`
- **Total τ:** `7971608456495`
- **Total α:** `4767384574150282`
- **α in pool:** `2014625329911178`
- **α staked:** `2030839640639506`
- **Price Δ 1h:** `-0.002413250555487543`
- **Price Δ 1d:** `-0.185655427140469822`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `4`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Real-time alpha and TAO flow signals across Bittensor subnets, ranked by composite flow score.

**Fetched document title:** TalismanAI

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
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5FbcZiAHA75i2bPVrF7wa9mFaxV1eM27HR63kJtbpb8spvmf`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
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

### 🪬 Miner (V3)

- Receives TweetBatch requests from validators over the Bittensor network
- Analyzes each tweet using LLM to determine:
  - Subnet relevance (which subnet the tweet is about)
  - Sentiment (very_bullish, bullish, neutral, bearish, very_bearish)
  - Content type (technical_insight, announcement, etc.)
- Returns enriched tweets with analysis data for validator verification

---

---

### Miner Configuration (`.miner_env`)

Copy `.miner_env_tmpl` to `.miner_env` and configure the following variables:

| Variable | Description |
|----------|-------------|
| `MODEL` | LLM model identifier for analysis (e.g., `deepseek-ai/DeepSeek-V3-0324`) |
| `API_KEY` | API key for the LLM service |
| `LLM_BASE` | Base URL for the LLM API endpoint |

**Note**: V3 miners do not need X/Twitter API credentials. They receive tweets from validators over the network.

---

### Validator Configuration (`.vali_env`)

Copy `.vali_env_tmpl` to `.vali_env` and configure the following variables:

| Variable | Description |
|----------|-------------|
| `MODEL` | LLM model identifier for re-analysis (e.g., `deepseek-ai/DeepSeek-V3-0324`) |
| `API_KEY` | API key for the LLM service |
| `LLM_BASE` | Base URL for the LLM API endpoint |
| `MINER_API_URL` | Base URL of the coordination API server (e.g., `http://localhost:8000`) |
| `BATCH_HTTP_TIMEOUT` | HTTP timeout in seconds for API requests (default: `30.0`) |
| `VALIDATION_POLL_SECONDS` | Seconds between poll attempts (default: `10`) |
| `MINER_BATCH_SIZE` | Tweets per miner batch (default: `3`) |
| `TWEET_MAX_PROCESS_TIME` | Local processing timeout in seconds before requeue (default: `300.0`) |
| `VALIDATOR_BROADCAST_MAX_TARGETS` | Max validators to broadcast epoch snapshots to (default: `32`) |

---

---

# edit .miner_env to include your LLM information (MODEL, API_KEY, LLM_BASE)

.venv/bin/python -m neurons.miner \
  --netuid 45 \
  --wallet.name your_coldkey_here \
  --wallet.hotkey your_hotkey_here \
  --logging.info
```

*Optional: Add `--axon.external_port` and `--axon.external_ip`

**Run Validator**

```bash
pip install -r requirements.txt
pip install -e .
cp .vali_env_tmpl .vali_env

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/Team-Rizzo/talisman-ai/main/README.md`*

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://ai.talisman.xyz](https://ai.talisman.xyz)
- **GitHub:** [https://github.com/Team-Rizzo/talisman-ai](https://github.com/Team-Rizzo/talisman-ai)
- **Logo URL:** [https://styles.redditmedia.com/t5_53lwgb/styles/communityIcon_vb7hazik5aqf1.jpg](https://styles.redditmedia.com/t5_53lwgb/styles/communityIcon_vb7hazik5aqf1.jpg)
- **Contact:** tai@rizzo.network

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.00397795 |
| 8104133 | 0.003977946 |
| 8104181 | 0.003977943 |
| 8104229 | 0.003977932 |
| 8104277 | 0.003977924 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

