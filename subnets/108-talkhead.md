# NetUID 108 — TalkHead (`Զ`)

## Overview

**TalkHead** (NetUID **108**) (`Զ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `236`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,009.340832330. **Alpha liquidity in pool (`alpha_in`)** = ‎402,421.586259039Զ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎953,683.691923795Զ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004993204`** *(also **moving-average price** `0.0047497202176600695` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎20,338.423883039Զ‎`. **Owner hotkey / coldkey (chain):** `5EHmE35kPeBBJXWv6BUJumrn5QGpGEM1xXcEY4QGn4QtWf2q` / `5HDuqw9fkqG3xdm1yZA8dfKeLBnZhg138xiMwnYQdBeLfytT`.
- **Subnet registered at block:** `7105263` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎153.840069965Զ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002494115` · α-out `‎1.000000000Զ‎` · α-in `‎0.500000000Զ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004988168`
- **Market cap:** `4857278049594.981207344`
- **Liquidity:** `4016621954208`
- **Total τ:** `2008295142074`
- **Total α:** `1356088669251979`
- **α in pool:** `402618117941211`
- **α staked:** `571141797441547`
- **Price Δ 1h:** `1.721540340164298818`
- **Price Δ 1d:** `8.867110865021332914`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `127`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `2494077`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `10000000`

### On-chain declared purpose *(SubnetIdentity)*

Talking Head Generation

### Repository README excerpt *(everything before first `##` heading)*

# TalkHead Subnet

---

- [Overview](#overview)
- [How it works](#how-it-works)
- [How to Run](#how-to-run)
- [Executor & Scoring](#executor-and-scoring)

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Decentralized photorealistic talking head subnet on bittensor ecosystem - talkheadai/talkhead-subnet

**Fetched document title:** GitHub - talkheadai/talkhead-subnet: Decentralized photorealistic talking head subnet on bittensor ecosystem · GitHub

## Operational parameters — registration, limits, economics (chain)


### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 127
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.010000000
- **Owner SS58 (`owner_ss58`):** `5HDuqw9fkqG3xdm1yZA8dfKeLBnZhg138xiMwnYQdBeLfytT`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.010000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `720` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `True`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Requirements

- Python 3.11+
- A registered Bittensor wallet + hotkey
- Access to the subnet API and executor endpoints
- A published miner image digest in `repo@sha256:...` format

---

### Setup

Install the project and create a local environment file:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
```

Set the required values in `.env`:

- `WALLET_NAME` and `HOTKEY_NAME` for the registered wallet/hotkey
- `NETWORK` and `NETUID` for the target subnet
- `SUBNET_API_URL` for the coordination API
- `EXECUTOR_API_URL` for the executor API used by the validator
- `IMAGE_REF` for the miner's published Docker image digest in `repo@sha256:...` format

---

### Run Miner

The miner is submission-only. It sends the configured Docker image digest to the subnet API.

You can use the [talkheadai/talkhead-miner-image](https://github.com/talkheadai/talkhead-miner-image) repository as a base Docker image/template for your miner container.

```bash
python -m neurons.miner
```

You can also override the image ref from the CLI:

```bash
python -m neurons.miner --image-ref your-registry/your-image@sha256:...
```

---

### Run Validator

The validator continuously:

1. Pulls miner submissions from the subnet API and forwards them to the executor
2. Reads executor metrics and sets on-chain weights

Start it with:

```bash
export WANDB_API_KEY=your-wandb-api-key
python -m neurons.validator
```

Common CLI overrides:

```bash
python -m neurons.validator \
  --wallet.name default \
  --wallet.hotkey default \
  --subtensor.network finney \
  --netuid 108
```

---

#### CPU / GPU / RAM lines (automatic grep)

- TalkHead is a subnet where miners submit Dockerized talking-head models, and validators evaluate them in a secure GPU executor to rank performance and set weights.


*Primary README URL used: `https://raw.githubusercontent.com/talkheadai/talkhead-subnet/main/README.md`*

## On-chain identity — description


Talking Head Generation

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/talkheadai/talkhead-subnet](https://github.com/talkheadai/talkhead-subnet)
- **Contact:** contact@talkhead.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.004913239 |
| 8104072 | 0.004913415 |
| 8104120 | 0.004913582 |
| 8104168 | 0.004978033 |
| 8104216 | 0.004993204 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.0048405 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004861477 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005534949 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005203834 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004694322 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004993519 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004733476 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005308644 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005136965 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005119106 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00506713615800357285 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004818593 |
| 2026-03-21T23:59:48Z | 7797398 | 0.004923702 |
| 2026-03-22T23:59:48Z | 7804598 | 0.004985383 |
| 2026-03-23T23:59:48Z | 7811798 | 0.004954176 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00495413496740350525 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004708503 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004424473 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004977647 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005143661 |
| 2026-03-29T23:59:48Z | 7854902 | 0.005190422 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.005039375 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004847049 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004263602 |
| 2026-04-02T23:59:48Z | 7883622 | 0.00423943 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004264528 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004499537 |
| 2026-04-05T23:59:48Z | 7905188 | 0.00450148 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004213667 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004351982 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004275501 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003855483 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004175571 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004142971 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004042961 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004129029 |
| 2026-04-14T23:59:48Z | 7969979 | 0.00427845 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.0040776 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004191962 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004223037 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004234086 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004178172 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004274091 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004035295 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004101508 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004173521 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004037324 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003972431 |
| 2026-04-26T23:59:48Z | 8056274 | 0.00408771 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004028273 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004226994 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004371896 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004459583 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004366056 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004660855 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004988168 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

