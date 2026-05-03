# NetUID 59 — Babelbit (`د`)

## Overview

Babelbit: harnessing the predictive power of LLMs to deliver state-of-the-art translation services

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.001367454
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

## Miner / validator compute notes (README excerpts)

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

If running locally, make sure the signer URL points to a reachable local signer:

```bash
SIGNER_URL=http://127.0.0.1:8080
```

Then run the services you need:

```bash
bb -vv signer
bb -vv subtensor-gateway
bb -vv runner
bb -vv validate
```

---

### 7.2: What miners need to do

Miners participating in Babelbit need to maintain two things:

1. A reachable qualifying miner that validators can discover through Bittensor axon metadata.
2. Submission artifacts for the broader Babelbit flow: a Docker image and a Hugging Face repository handle.

This repo documents the public compatibility requirements. Private submission and managed deployment mechanics are intentionally omitted.

---

### 7.3: Prerequisites

- Python 3.10-3.13
- Enough RAM or VRAM for the chosen model
- A Bittensor wallet and registered hotkey
- A reachable public IP and port for your axon-compatible miner
- Hugging Face access if your model is gated or private

---

### 7.4: Shared miner-related environment

The validator stack and related tooling currently reference these shared miner-related settings:

```bash
BITTENSOR_WALLET_PATH=~/.bittensor/wallets/my-wallet/hotkeys/my-hotkey
BITTENSOR_WALLET_COLD=my-wallet
BITTENSOR_WALLET_HOT=my-hotkey
BITTENSOR_SUBTENSOR_ENDPOINT=finney
BABELBIT_NETUID=59

HUGGINGFACE_USERNAME=your-username
HUGGINGFACE_API_KEY=your-api-key

MINER_MODEL_ID=babelbit-ai/base-miner
MINER_AXON_PORT=8091
MINER_DEVICE=cpu
MINER_LOAD_IN_8BIT=0
MINER_LOAD_IN_4BIT=0

---

# MINER_EXTERNAL_IP=your-public-ip

```

Model-specific generation knobs belong in the external miner repo, not in this validator stack.

---

### 7.7: Compatibility requirements

Your external miner implementation should satisfy these validator-facing expectations:

- Register on netuid `59` with a hotkey that is discoverable through Bittensor axon metadata.
- Expose a prediction endpoint at `POST /predict` by default. Validators can be pointed at a different path with `BB_MINER_PREDICT_ENDPOINT`, but `/predict` is the current default.
- Optionally expose `GET /healthz` for operational monitoring.
- Accept Bittensor-style signed request headers. The validator currently sends `bt_header_*` headers such as hotkey, nonce, UUID, signature, axon IP, and axon port.
- Return JSON compatible with the validator schema: `success`, `model`, `utterance`, `context_used`, optional `error`, and `complete`.

---

## 8: Miner Submission Artifacts

Running a qualifying miner is only one part o…


*README source used for excerpts: `https://raw.githubusercontent.com/babelbit/babelbit_subnet/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Babelbit: harnessing the predictive power of LLMs to deliver state-of-the-art translation services

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://babelbit.ai](https://babelbit.ai)
- **GitHub:** [https://github.com/babelbit/babelbit_subnet](https://github.com/babelbit/babelbit_subnet)
- **Discord:** [https://discord.com/channels/799672011265015819/1407849009976053832](https://discord.com/channels/799672011265015819/1407849009976053832)
- **Logo URL:** [https://babelbit.ai/babelbit-tower-logo-rev-no-text.png](https://babelbit.ai/babelbit-tower-logo-rev-no-text.png)
- **Contact:** mk@babelbit.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.003957265 |
| 8103690 | 0.003981574 |
| 8103738 | 0.003981569 |
| 8103786 | 0.003981465 |
| 8103834 | 0.003981629 |
| 8103882 | 0.003981421 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** BabelBit — Real-time speech translation
- **Fetched from:** [https://babelbit.ai](https://babelbit.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

