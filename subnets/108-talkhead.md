# NetUID 108 — TalkHead (`Զ`)

## Overview

Talking Head Generation

**From crawled page (site or GitHub):** Decentralized photorealistic talking head subnet on bittensor ecosystem - talkheadai/talkhead-subnet

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/talkheadai/talkhead-subnet/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Talking Head Generation

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/talkheadai/talkhead-subnet](https://github.com/talkheadai/talkhead-subnet)
- **Contact:** contact@talkhead.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.004861022 |
| 8103738 | 0.004861166 |
| 8103786 | 0.004903619 |
| 8103834 | 0.004903567 |
| 8103882 | 0.004903682 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** GitHub - talkheadai/talkhead-subnet: Decentralized photorealistic talking head subnet on bittensor ecosystem · GitHub
- **Meta / og:description:** Decentralized photorealistic talking head subnet on bittensor ecosystem - talkheadai/talkhead-subnet
- **Fetched from:** [https://github.com/talkheadai/talkhead-subnet](https://github.com/talkheadai/talkhead-subnet)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

