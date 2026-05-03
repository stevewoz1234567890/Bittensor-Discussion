# NetUID 108 — TalkHead (`Զ`)

## Overview

**TalkHead** (NetUID **108**) (`Զ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `298`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,009.506366528. **Alpha liquidity in pool (`alpha_in`)** = ‎402,450.434341965Զ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎953,734.045659729Զ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004993254`** *(also **moving-average price** `0.004753412213176489` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎20,338.550932191Զ‎`. **Owner hotkey / coldkey (chain):** `5EHmE35kPeBBJXWv6BUJumrn5QGpGEM1xXcEY4QGn4QtWf2q` / `5HDuqw9fkqG3xdm1yZA8dfKeLBnZhg138xiMwnYQdBeLfytT`.
- **Subnet registered at block:** `7105263` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎194.256323782Զ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002496633` · α-out `‎1.000000000Զ‎` · α-in `‎0.500000000Զ‎`.

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
| 8104085 | 0.004913472 |
| 8104133 | 0.004913635 |
| 8104181 | 0.004978099 |
| 8104229 | 0.004993127 |
| 8104277 | 0.004993254 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

