# NetUID 37 — Aurelius (`ל`)

## Overview

Decentralized Alignment of Artificial Intelligence

**From crawled page (site or GitHub):** Aurelius is a decentralized AI alignment protocol. Alignment you can

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
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GRBbS3aDep7cvR1NRm9Awp5HAF1o4HC7t59Y8HoheLZ6ZaP`

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
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

## Recommended setup: the published Docker image

We publish validator, miner, and simulation images to **public GHCR** — no registry auth
required:

| | Testnet (subnet **455**, `test`) | Mainnet (subnet **37**, `finney`) |
|---|---|---|
| Validator image | `ghcr.io/aurelius-protocol/aurelius-validator:testnet` | `ghcr.io/aurelius-protocol/aurelius-validator:latest` |
| Miner image | `ghcr.io/aurelius-protocol/aurelius-miner:testnet` | `ghcr.io/aurelius-protocol/aurelius-miner:latest` |
| Simulation sidecar | `…/aurelius-concordia:testnet` (pulled automatically) | `…/aurelius-concordia:latest` |

The published image is the supported path for running a validator. The validator's
stage-7 pipeline launches sandboxed Concordia simulation containers via a Docker socket,
so it expects to run inside a container that has access to the host's Docker daemon via
the socket proxy — which the quickstart below sets up for you. Source checkouts are great
for development, CI, and reading the code; for operating a validator, the image is the
path that has working simulation out of the box.

Every push to `main` rebuilds the mainnet `:latest` tag; every push to `testnet` rebuilds
the `:testnet` tag.

---

---

## Quickstart — Mainnet validator (SN 37)

Prerequisites:

- Docker 20.10+ and `docker compose`
- A Bittensor wallet registered on mainnet `netuid 37`
  (`btcli subnet register --netuid 37 --network finney`) — registration costs TAO
- An OpenAI-compatible LLM API key — [DeepSeek](https://platform.deepseek.com/) is the
  default and cheapest.

---

## Quickstart — Testnet validator (SN 455)

Identical shape, different tag and environment:

```bash
cat > .env <<'EOF'
ENVIRONMENT=testnet
WALLET_NAME=<your-wallet>
WALLET_HOTKEY=<your-hotkey>
LLM_API_KEY=<your-openai-compatible-api-key>
EOF
```

Register on `netuid 455` on `network test`, and swap `:latest` → `:testnet` in the
compose file. Everything else — socket proxy, volumes, labels — is identical.

---

---

### What the miner does

A miner is a Bittensor axon that serves a **library of operator-authored scenario
configs**. When a validator queries with a `ScenarioConfigSynapse`
([`aurelius/protocol.py`](aurelius/protocol.py)), the miner returns the next config from
its library in round-robin order, stamped with a `work_id` and signed by the miner's
hotkey so the validator can charge the submission against the miner's work-token balance
on acceptance. The validator runs the returned config through an 8-stage pipeline
(schema, rate-limit, novelty, classifier, Concordia simulation, etc.) and sets on-chain
weights based on the outcome. Miners do **not** generate configs at request time — the
library is loaded at startup from a directory on disk.

That shape means two things for an operator: you need to (a) author some scenario JSON
files, and (b) have a work-token balance that validators can spend.

---

### Prerequisites

- Docker 20.10+
- A Bittensor wallet registered on mainnet `netuid 37`
  (`btcli subnet register --netuid 37 --network finney`)
- A publicly reachable IP and an open inbound TCP port for the axon (default `8091`)
- One or more scenario config files (see below)
- A work-token balance (see [Work tokens](#work-tokens) below)

---

### 3. Run the miner

```bash
docker pull ghcr.io/aurelius-protocol/aurelius-miner:latest   # :testnet for testnet

cat > .env <<'EOF'
ENVIRONMENT=mainnet
WALLET_NAME=<your-wallet>
WALLET_HOTKEY=<your-hotkey>
AXON_EXTERNAL_IP=<your-public-ip>
AXON_EXTERNAL_PORT=8091
EOF

mkdir -p data configs

---

# E2E (requires a running testnet and a funded wallet)

pytest tests/e2e/ -m e2e


*README source used for excerpts: `https://raw.githubusercontent.com/Aurelius-Protocol/Aurelius-Protocol/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Decentralized Alignment of Artificial Intelligence

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://aureliusaligned.ai](https://aureliusaligned.ai)
- **GitHub:** [https://github.com/Aurelius-Protocol/Aurelius-Protocol](https://github.com/Aurelius-Protocol/Aurelius-Protocol)
- **Logo URL:** [https://raw.githubusercontent.com/Aurelius-Protocol/aurelius-whitepaper/main/aurelius_logo.png](https://raw.githubusercontent.com/Aurelius-Protocol/aurelius-whitepaper/main/aurelius_logo.png)
- **Contact:** aurelius.subnet@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.004052837 |
| 8103690 | 0.00405283 |
| 8103738 | 0.004052825 |
| 8103786 | 0.004052756 |
| 8103834 | 0.004052754 |
| 8103882 | 0.004052747 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Aurelius — Decentralized Alignment of Artificial Intelligence
- **Meta / og:description:** Aurelius is a decentralized AI alignment protocol. Alignment you can
- **Fetched from:** [https://aureliusaligned.ai](https://aureliusaligned.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

