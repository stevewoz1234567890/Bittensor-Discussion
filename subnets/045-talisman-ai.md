# NetUID 45 — Talisman AI (`פ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Talisman AI** (NetUID **45**) (`פ`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `32`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,971.572587330. **Alpha liquidity in pool (`alpha_in`)** = ‎2,014,634.347013674פ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,752,983.227136608פ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003977906`** *(also **moving-average price** `0.0039773136377334595` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎700,315.635447000פ‎`. **Owner hotkey / coldkey (chain):** `5Hmiaz4bLLbLw4LgTksJvJYPYp1XJ1GYkUfRiv4HGXX674DD` / `5FbcZiAHA75i2bPVrF7wa9mFaxV1eM27HR63kJtbpb8spvmf`.
- **Subnet registered at block:** `3633154` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎24.074358267פ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000פ‎` · α-in `‎0.000000000פ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104403`
- **Liquidity constant `k`:** `16059803934147678307069150420`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Talisman AI` |
| Symbol (API) | `פ` |
| Rank | `72` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.003977941` |
| Market cap | `16092620970417.358461644` |
| Market cap Δ 1d | `-0.069105331146858757` |
| Liquidity | `15985669155987` |
| Total τ | `7971608456495` |
| Total α | `4767384574150282` |
| α in pool | `2014625329911178` |
| α staked | `2030839640639506` |
| Price Δ 1h | `-0.002413250555487543` |
| Price Δ 1d | `-0.185655427140469822` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `45` |
| Owner SS58 (API) | `5FbcZiAHA75i2bPVrF7wa9mFaxV1eM27HR63kJtbpb8spvmf` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3633154` |
| Registration wall time | `2024-08-18T13:44:36.004Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `13` |
| Active miners | `4` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `13` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Real-time alpha and TAO flow signals across Bittensor subnets, ranked by composite flow score.

**Fetched document title:** TalismanAI

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
| `immunity_period` (blocks) | 7200 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5FbcZiAHA75i2bPVrF7wa9mFaxV1eM27HR63kJtbpb8spvmf` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `7200` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://ai.talisman.xyz](https://ai.talisman.xyz)
- **GitHub:** [https://github.com/Team-Rizzo/talisman-ai](https://github.com/Team-Rizzo/talisman-ai)
- **Logo URL:** [https://styles.redditmedia.com/t5_53lwgb/styles/communityIcon_vb7hazik5aqf1.jpg](https://styles.redditmedia.com/t5_53lwgb/styles/communityIcon_vb7hazik5aqf1.jpg)
- **Contact:** tai@rizzo.network

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.003977942 |
| 8104244 | 0.00397793 |
| 8104292 | 0.003977923 |
| 8104340 | 0.00397791 |
| 8104388 | 0.00397791 |
| 8104436 | 0.003977906 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.004555737 |
| 2026-03-10T23:59:48Z | — | 0.004887678 |
| 2026-03-11T23:59:48Z | — | 0.004808972 |
| 2026-03-12T23:59:48Z | — | 0.004609306 |
| 2026-03-13T23:59:48Z | — | 0.004525048 |
| 2026-03-14T23:59:48Z | — | 0.00456886 |
| 2026-03-15T23:59:48Z | — | 0.004226278 |
| 2026-03-16T23:59:48Z | — | 0.004346498 |
| 2026-03-17T23:59:48Z | — | 0.004204267 |
| 2026-03-18T23:59:48Z | — | 0.004223203 |
| 2026-03-19T23:59:48Z | — | 0.00422272416207 |
| 2026-03-20T23:59:48Z | — | 0.004181629 |
| 2026-03-21T23:59:48Z | — | 0.004164169 |
| 2026-03-22T23:59:48Z | — | 0.004206222 |
| 2026-03-23T23:59:48Z | — | 0.004141567 |
| 2026-03-24T23:59:48Z | — | 0.00400722794659 |
| 2026-03-25T23:59:48Z | — | 0.003990534 |
| 2026-03-26T23:59:48Z | — | 0.003983495 |
| 2026-03-27T23:59:48Z | — | 0.004111547 |
| 2026-03-28T23:59:48Z | — | 0.004096421 |
| 2026-03-29T23:59:48Z | — | 0.004098957 |
| 2026-03-30T23:59:48Z | — | 0.004093724 |
| 2026-03-31T23:59:48Z | — | 0.004196317 |
| 2026-04-01T23:59:48Z | — | 0.004263726 |
| 2026-04-02T23:59:48Z | — | 0.004331642 |
| 2026-04-03T23:59:48Z | — | 0.004228236 |
| 2026-04-04T23:59:48Z | — | 0.00429117 |
| 2026-04-05T23:59:48Z | — | 0.004234591 |
| 2026-04-06T23:59:48Z | — | 0.004219053 |
| 2026-04-07T23:59:48Z | — | 0.004270278 |
| 2026-04-08T23:59:48Z | — | 0.004542875 |
| 2026-04-09T23:59:48Z | — | 0.004309186 |
| 2026-04-10T23:59:48Z | — | 0.004504439 |
| 2026-04-11T23:59:48Z | — | 0.004318205 |
| 2026-04-12T23:59:48Z | — | 0.004264227 |
| 2026-04-13T23:59:48Z | — | 0.004150712 |
| 2026-04-14T23:59:48Z | — | 0.004503914 |
| 2026-04-15T23:59:48Z | — | 0.004353644 |
| 2026-04-16T23:59:48Z | — | 0.004371692 |
| 2026-04-17T23:59:48Z | — | 0.004309006 |
| 2026-04-18T23:59:48Z | — | 0.00431678 |
| 2026-04-19T23:59:48Z | — | 0.004302122 |
| 2026-04-20T23:59:48Z | — | 0.00430903 |
| 2026-04-21T23:59:48Z | — | 0.004294888 |
| 2026-04-22T23:59:48Z | — | 0.004284379 |
| 2026-04-23T23:59:48Z | — | 0.004236716 |
| 2026-04-24T23:59:48Z | — | 0.004199133 |
| 2026-04-25T23:59:48Z | — | 0.00418907 |
| 2026-04-26T23:59:48Z | — | 0.004217848 |
| 2026-04-27T23:59:48Z | — | 0.004231049 |
| 2026-04-28T23:59:48Z | — | 0.004132563 |
| 2026-04-29T23:59:48Z | — | 0.004130438 |
| 2026-04-30T23:59:48Z | — | 0.004028301 |
| 2026-05-01T23:59:48Z | — | 0.003996309 |
| 2026-05-02T23:59:48Z | — | 0.003974209 |
| 2026-05-03T23:59:48Z | — | 0.003977941 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

