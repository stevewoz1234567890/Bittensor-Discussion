# NetUID 59 — Babelbit (`د`)

## Overview

**Babelbit** (NetUID **59**) (`د`).

Babelbit: harnessing the predictive power of LLMs to deliver state-of-the-art translation services

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `187`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,993.045631994. **Alpha liquidity in pool (`alpha_in`)** = ‎1,742,089.052853496د‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,170,065.815820703د‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004005356`** *(also **moving-average price** `0.0038849946577101946` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎496,389.076684030د‎`. **Owner hotkey / coldkey (chain):** `5EF9dnwEup1QD1vAg6j9Z7yqYKbpQSMK2Rax2JhhUEFjNdve` / `5DkPyHKTXK3eTJarh2hAL4FnkpQ5k7QivRucY8yXVN1wug4y`.
- **Subnet registered at block:** `4401833` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎140.996436042د‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000د‎` · α-in `‎0.000000000د‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003987233`
- **Market cap:** `18553467449781.987331498`
- **Liquidity:** `13939124370212`
- **Total τ:** `6977053935431`
- **Total α:** `4912141868674199`
- **α in pool:** `1746090693666775`
- **α staked:** `2907128079798931`
- **Price Δ 1h:** `0.139539194163665209`
- **Price Δ 1d:** `9.846001434223391175`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `8`
- **Active miners:** `179`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `8`
- **Neuron reg. cost:** `1179018`

### On-chain declared purpose *(SubnetIdentity)*

Babelbit: harnessing the predictive power of LLMs to deliver state-of-the-art translation services

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <img width="265" height="281" alt="Babelbit logo Black" src="https://github.com/user-attachments/assets/055577f8-0ff4-4d67-9153-e66c00688bb2" />
</p>

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** BabelBit — Real-time speech translation

## Operational parameters — registration, limits, economics (chain)


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
- **Registration recycle cost snapshot (`burn`):** τ0.001141043
- **Owner SS58 (`owner_ss58`):** `5DkPyHKTXK3eTJarh2hAL4FnkpQ5k7QivRucY8yXVN1wug4y`

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
- **`commit_reveal_period`:** `3`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## 4: A Fairer Approach to Mining Challenges

The text prediction challenge we designed in October 2025, was a task designed to reward miners that make useful predictions early, including predictions that are semantically right before the full utterance is revealed. This allowed us to prove that it was possible to reduce translation latency in a new way.

However, we noticed that some creative approaches to prediction didn't score well, but inspired some good ideas. So it occurred to us that while we still want to reward the biggest performance gains, we don't want any hard-working machine learning engineer to be working for nothing.

So we have come up with a two phase contest - a qualifying round where every contestant gets a proportion of the allotted emissions, and The Arena where the qualifying contestants compete to win the rest.

This is a new evolution of our development, and we will need our mining community to remain ever adaptable with us as we progress - after all we are trying to maximise the performance of the world's first machine interpreter. So this is how we're planning things at launch:

**The Qualifying Round** will share 20% of the emissions between all the contestants (unless they're caught cheating), in proportion to their scores. It probably won't make anyone rich, but our hope is that the hard work will be rewarded in another way - getting better and better - until you qualify for the second phase.

The qualifiers then compete in **The Arena** for a chance at winning the remaining 80%.

---

## 5: Babelbit Mining Setup

This repository is the operator guide and reference implementation for the Babelbit validator stack. It is primarily for:

- validators running the validator, runner, signer, and supporting services
- miners who need the validator-facing compatibility requirements for qualifying and arena participation

Some submission, scoring, and managed deployment workflows are handled by Babelbit-operated services and are intentionally described here only at a high level.

`qualifying` is round 1. `arena` is round 2.

**This repo isn't intended for mining:** Please refer to the [Babelbit Miner repo](https://github.com/babelbit/babelbit_miner) for further instructions on how to run your miner and submit it to the arena.

---

### 6.1: Prerequisites

- A Bittensor wallet and hotkey
- Python 3.10-3.13 if running locally
- Docker if using the recommended deployment path
- (Optional) S3-compatible object storage for logs/artifacts and Postgres database

---

### 6.2: Install `btcli`

```bash
pip install bittensor-cli
```

---

### 6.4: Required validator environment

Set the required wallet, network, service, and database settings in `.env`:

```bash
BITTENSOR_WALLET_PATH=~/.bittensor/wallets/my-wallet/hotkeys/my-hotkey
BITTENSOR_WALLET_COLD=my-wallet
BITTENSOR_WALLET_HOT=my-hotkey

BABELBIT_NETUID=59
BITTENSOR_SUBTENSOR_ENDPOINT=finney

SIGNER_URL=http://127.0.0.1:8080
SUBTENSOR_GATEWAY_URL=http://127.0.0.1:8090

BB_UTTERANCE_ENGINE_URL=https://api.babelbit.ai/
BB_SUBMIT_API_URL=https://scoring.babelbit.ai/
BB_ARENA_GATEWAY_URL=https://gw.babelbit.ai/
BB_SUBMIT_TIMEOUT_S=30
BB_MINER_TIMEOUT_SEC=10
```

---

### 6.5: Optional validator settings

Optional Postgres and S3-compatible storage:

```bash
PG_HOST=your-pg-host
PG_PORT=your-pg-port
PG_DB=your-pg-db-name
PG_USER=your-pg-user
PG_PASSWORD=your-pg-password

BB_ENABLE_S3_UPLOADS=1
S3_ENDPOINT_URL=your-s3-endpoint-url
S3_REGION=s3-region
S3_ACCESS_KEY_ID=your-s3-access-key
S3_SECRET_ACCESS_KEY=your-s3-secret
S3_BUCKET_NAME=your-s3-bucket
S3_SUBMISSIONS_DIR=challenges
S3_LOG_DIR=logs
S3_ADDRESSING_STYLE=path
S3_SIGNATURE_VERSION=s3v4
S3_USE_SSL=true
```

Additional runner, arena, metrics, and scoring settings are available in [`env.example`](./env.example).

---

### 6.7: Local setup

If you want to run outside Docker:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate
uv sync
```

The CLI entrypoint is:

```bash
bb
```

---

### 6.8: Validator services

The main validator-side commands are:

- `bb runner`: evaluates miners on the active challenge cadence
- `bb validate`: calculates and submits weights
- `bb signer`: runs the signing service used by validator components
- `bb subtensor-gateway`: runs the gateway used by the validator stack

---

### 6.9: Recommended validator deployment

Run the validator stack with Docker:

```bash
docker compose down
docker compose pull
docker compose up --build -d
docker compose logs -f --tail 100
```

---

### 6.10: Local validator run

If running locally, make s…

---

#### CPU / GPU / RAM lines (automatic grep)

- - Enough RAM or VRAM for the chosen model
- MINER_DEVICE=cpu
- - Small models are suitable for CPU testing.
- - Large models on CPU will usually be too slow for competitive inference.
- - Set `MINER_DEVICE=cuda` on NVIDIA systems.
- - Use quantization if you need to reduce VRAM pressure.
- If MPS is unstable for your model, switch to CPU:
- Curate a dataset of source speech paired with high-quality interpretations (not literal translations), and fine-tune. This can be done with LoRA or with full fine-tuning of some or all layers — though full fine-tuning risks catastrophic forgetting and requires a lot more VRAM (all tensors must track gradients). Or if you're really constrained, use prompt tuning (learn embeddings for a few soft tokens)


*Primary README URL used: `https://raw.githubusercontent.com/babelbit/babelbit_subnet/main/README.md`*

## On-chain identity — description


Babelbit: harnessing the predictive power of LLMs to deliver state-of-the-art translation services

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://babelbit.ai](https://babelbit.ai)
- **GitHub:** [https://github.com/babelbit/babelbit_subnet](https://github.com/babelbit/babelbit_subnet)
- **Discord:** [https://discord.com/channels/799672011265015819/1407849009976053832](https://discord.com/channels/799672011265015819/1407849009976053832)
- **Logo URL:** [https://babelbit.ai/babelbit-tower-logo-rev-no-text.png](https://babelbit.ai/babelbit-tower-logo-rev-no-text.png)
- **Contact:** mk@babelbit.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.003984757 |
| 8104072 | 0.003985094 |
| 8104120 | 0.00398631 |
| 8104168 | 0.003986421 |
| 8104216 | 0.004005356 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

