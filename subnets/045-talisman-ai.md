# NetUID 45 — Talisman AI (`פ`)

## Overview

**From crawled page (site or GitHub):** Real-time alpha and TAO flow signals across Bittensor subnets, ranked by composite flow score.

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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/Team-Rizzo/talisman-ai/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


*Empty — no description bytes set in `SubnetIdentity`.*

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://ai.talisman.xyz](https://ai.talisman.xyz)
- **GitHub:** [https://github.com/Team-Rizzo/talisman-ai](https://github.com/Team-Rizzo/talisman-ai)
- **Logo URL:** [https://styles.redditmedia.com/t5_53lwgb/styles/communityIcon_vb7hazik5aqf1.jpg](https://styles.redditmedia.com/t5_53lwgb/styles/communityIcon_vb7hazik5aqf1.jpg)
- **Contact:** tai@rizzo.network

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.003978098 |
| 8103690 | 0.00397809 |
| 8103738 | 0.003978086 |
| 8103786 | 0.003978049 |
| 8103834 | 0.003978046 |
| 8103882 | 0.003978039 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** TalismanAI
- **Meta / og:description:** Real-time alpha and TAO flow signals across Bittensor subnets, ranked by composite flow score.
- **Fetched from:** [https://ai.talisman.xyz](https://ai.talisman.xyz)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

