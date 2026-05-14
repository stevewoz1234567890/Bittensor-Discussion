# NetUID 37 — Aurelius (`ל`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Aurelius** (NetUID **37**) (`ל`).

Decentralized Alignment of Artificial Intelligence

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `24`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,751.288982681. **Alpha liquidity in pool (`alpha_in`)** = ‎2,160,463.254744164ל‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,884,131.496613273ל‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004052924`** *(also **moving-average price** `0.004053397104144096` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎314,241.642256899ל‎`. **Owner hotkey / coldkey (chain):** `5DXqqdrvu5FK3dASRVTCdGPZKx4Q9nkAZZSmibKG6PEEeW4j` / `5GRBbS3aDep7cvR1NRm9Awp5HAF1o4HC7t59Y8HoheLZ6ZaP`.
- **Subnet registered at block:** `3212175` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎18.130920221ל‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ל‎` · α-in `‎0.000000000ל‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104411`
- **Liquidity constant `k`:** `18906838278729737118481823684`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Aurelius` |
| Symbol (API) | `ל` |
| Rank | `67` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004052756` |
| Market cap | `16813595068227.525120656` |
| Market cap Δ 1d | `0.164054546471200779` |
| Liquidity | `17507119397142` |
| Total τ | `8751106949316` |
| Total α | `5044363480990036` |
| α in pool | `2160508169706283` |
| α staked | `1988173633053993` |
| Price Δ 1h | `0.000271420975166215` |
| Price Δ 1d | `0.046088648689213652` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `37` |
| Owner SS58 (API) | `5GRBbS3aDep7cvR1NRm9Awp5HAF1o4HC7t59Y8HoheLZ6ZaP` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3212175` |
| Registration wall time | `2024-06-19T11:02:48.001Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `14` |
| Active miners | `15` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `14` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Aurelius Protocol

A Bittensor subnet for moral reasoning alignment. Miners submit structured ethical-dilemma
scenario configurations; validators score them through an 8-stage pipeline and run
accepted scenarios through [Concordia](https://github.com/google-deepmind/concordia)
generative-agent simulations. The resulting transcripts form training data that improves
LLM performance on moral reasoning benchmarks (MoReBench).

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Aurelius is a decentralized AI alignment protocol. Alignment you can

**Fetched document title:** Aurelius — Decentralized Alignment of Artificial Intelligence

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
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.001603354 |
| Owner SS58 (`owner_ss58`) | `5GRBbS3aDep7cvR1NRm9Awp5HAF1o4HC7t59Y8HoheLZ6ZaP` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
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

### 2. Docker compose with socket-proxy sidecar

The validator reaches the Docker daemon through
[`tecnativa/docker-socket-proxy`](https://github.com/Tecnativa/docker-socket-proxy), which
restricts the socket to only the API calls the validator actually uses.

```bash
cat > docker-compose.yml <<'EOF'
services:
  aurelius-validator:
    image: ghcr.io/aurelius-protocol/aurelius-validator:latest
    container_name: aurelius-validator
    restart: unless-stopped
    env_file: .env
    environment:
      DOCKER_HOST: tcp://docker-proxy:2375
    cap_add: [NET_ADMIN]
    volumes:
      - ~/.bittensor/wallets:/home/appuser/.bittensor/wallets:ro
      - ./data:/app/data
      - ./simdata:/sim-data
    depends_on: [docker-proxy]
    labels:
      com.centurylinklabs.watchtower.enable: "true"

  docker-proxy:
    image: tecnativa/docker-socket-proxy:0.3.0
    container_name: docker-proxy
    restart: unless-stopped
    environment: { CONTAINERS: 1, IMAGES: 1, POST: 1, NETWORKS: 1 }
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
EOF
```

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

mkdir -p data con…

---









#### CPU / GPU / RAM lines (automatic grep)

- CPU/RAM limits scaled to the scenario's agent count, and its LLM egress is firewalled to
- capped RAM / CPU, egress limited to `SIM_ALLOWED_LLM_HOSTS`, and no persistent


*Primary README URL used: `https://raw.githubusercontent.com/Aurelius-Protocol/Aurelius-Protocol/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://aureliusaligned.ai](https://aureliusaligned.ai)
- **GitHub:** [https://github.com/Aurelius-Protocol/Aurelius-Protocol](https://github.com/Aurelius-Protocol/Aurelius-Protocol)
- **Logo URL:** [https://raw.githubusercontent.com/Aurelius-Protocol/aurelius-whitepaper/main/aurelius_logo.png](https://raw.githubusercontent.com/Aurelius-Protocol/aurelius-whitepaper/main/aurelius_logo.png)
- **Contact:** aurelius.subnet@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.004052757 |
| 8104244 | 0.004052753 |
| 8104292 | 0.004052746 |
| 8104340 | 0.004052928 |
| 8104388 | 0.004052927 |
| 8104436 | 0.004052924 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

