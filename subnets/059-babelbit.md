# NetUID 59 — Babelbit (`د`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Babelbit** (NetUID **59**) (`د`).

Babelbit: harnessing the predictive power of LLMs to deliver state-of-the-art translation services

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `46`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,933.557424615. **Alpha liquidity in pool (`alpha_in`)** = ‎1,757,067.412042691د‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,155,306.951412024د‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003938148`** *(also **moving-average price** `0.0038884305395185947` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎496,490.635273601د‎`. **Owner hotkey / coldkey (chain):** `5EF9dnwEup1QD1vAg6j9Z7yqYKbpQSMK2Rax2JhhUEFjNdve` / `5DkPyHKTXK3eTJarh2hAL4FnkpQ5k7QivRucY8yXVN1wug4y`.
- **Subnet registered at block:** `4401833` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎34.683859800د‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000د‎` · α-in `‎0.000000000د‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104389`
- **Liquidity constant `k`:** `12182727800317663646394238965`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Babelbit`
- **Symbol (API):** `د`
- **Rank:** `61`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003987233`
- **Market cap:** `18553467449781.987331498`
- **Market cap Δ 1d:** `9.95857062064597829`
- **Liquidity:** `13939124370212`
- **Total τ:** `6977053935431`
- **Total α:** `4912141868674199`
- **α in pool:** `1746090693666775`
- **α staked:** `2907128079798931`
- **Price Δ 1h:** `0.139539194163665209`
- **Price Δ 1d:** `9.846001434223391175`
#### Subnet activity (TAOStats)

- **NetUID (API):** `59`
- **Owner SS58 (API):** `5DkPyHKTXK3eTJarh2hAL4FnkpQ5k7QivRucY8yXVN1wug4y`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `4401833`
- **Registration wall time:** `2024-12-03T17:11:00Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `8`
- **Active miners:** `179`
- **Active dual-role:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `8`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `1179018`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <img width="265" height="281" alt="Babelbit logo Black" src="https://github.com/user-attachments/assets/055577f8-0ff4-4d67-9153-e66c00688bb2" />
</p>

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** BabelBit — Real-time speech translation

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
- **Registration recycle cost snapshot (`burn`):** τ0.001185878
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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


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
| 8104244 | 0.00395353 |
| 8104292 | 0.003930099 |
| 8104340 | 0.003930914 |
| 8104388 | 0.003939343 |
| 8104436 | 0.003938238 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.005602458 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005127457 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005166135 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005346615 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004990422 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005517315 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005011877 |
| 2026-03-16T23:59:48Z | 7761426 | 0.004963218 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005039102 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005042989 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00484866948305321481 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004866919 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005180828 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005406131 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005270795 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00488513370648703868 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004394887 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004140425 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004185344 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004405668 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004464846 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004359076 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004238829 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004335013 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004211953 |
| 2026-04-03T23:59:48Z | 7890794 | 0.00440419 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004736553 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004906332 |
| 2026-04-06T23:59:48Z | 7912388 | 0.00460825 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004318721 |
| 2026-04-08T23:59:48Z | 7926788 | 0.00456212 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003841535 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004059825 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004094346 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004152315 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004377719 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004026117 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.003998582 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004114953 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004245239 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004204879 |
| 2026-04-19T23:59:48Z | 8005979 | 0.00428981 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004360707 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004311428 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004249403 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004133908 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004098762 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004045043 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004109324 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.003941673 |
| 2026-04-28T23:59:48Z | 8070646 | 0.003918416 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004011696 |
| 2026-04-30T23:59:48Z | 8084984 | 0.00395172 |
| 2026-05-01T23:59:48Z | 8092168 | 0.003812481 |
| 2026-05-02T23:59:48Z | 8099357 | 0.003915166 |
| 2026-05-03T16:10:00Z | 8104202 | 0.003987233 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

