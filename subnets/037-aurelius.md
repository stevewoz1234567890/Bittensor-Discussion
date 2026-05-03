# NetUID 37 — Aurelius (`ל`)

## Overview

**Aurelius** (NetUID **37**) (`ל`).

Decentralized Alignment of Artificial Intelligence

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `227`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,751.097143227. **Alpha liquidity in pool (`alpha_in`)** = ‎2,160,510.589333419ל‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,883,926.162024018ל‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004052747`** *(also **moving-average price** `0.004053447395563126` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎314,241.414202095ל‎`. **Owner hotkey / coldkey (chain):** `5DXqqdrvu5FK3dASRVTCdGPZKx4Q9nkAZZSmibKG6PEEeW4j` / `5GRBbS3aDep7cvR1NRm9Awp5HAF1o4HC7t59Y8HoheLZ6ZaP`.
- **Subnet registered at block:** `3212175` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎171.487006558ל‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ל‎` · α-in `‎0.000000000ל‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004052756`
- **Market cap:** `16813595068227.525120656`
- **Liquidity:** `17507119397142`
- **Total τ:** `8751106949316`
- **Total α:** `5044363480990036`
- **α in pool:** `2160508169706283`
- **α staked:** `1988173633053993`
- **Price Δ 1h:** `0.000271420975166215`
- **Price Δ 1d:** `0.046088648689213652`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `14`
- **Active miners:** `15`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `14`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Decentralized Alignment of Artificial Intelligence

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
- **Registration recycle cost snapshot (`burn`):** τ0.002177719
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

## On-chain identity — description


Decentralized Alignment of Artificial Intelligence

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://aureliusaligned.ai](https://aureliusaligned.ai)
- **GitHub:** [https://github.com/Aurelius-Protocol/Aurelius-Protocol](https://github.com/Aurelius-Protocol/Aurelius-Protocol)
- **Logo URL:** [https://raw.githubusercontent.com/Aurelius-Protocol/aurelius-whitepaper/main/aurelius_logo.png](https://raw.githubusercontent.com/Aurelius-Protocol/aurelius-whitepaper/main/aurelius_logo.png)
- **Contact:** aurelius.subnet@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.004052672 |
| 8104133 | 0.00405276 |
| 8104181 | 0.004052757 |
| 8104229 | 0.004052754 |
| 8104277 | 0.004052747 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.00447575 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004492594 |
| 2026-03-11T23:59:48Z | 7725455 | 0.004505496 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.004481772 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004369965 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004398833 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004271934 |
| 2026-03-16T23:59:48Z | 7761426 | 0.004326045 |
| 2026-03-17T23:59:48Z | 7768619 | 0.004228058 |
| 2026-03-18T23:59:48Z | 7775819 | 0.004036184 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00412082146452153481 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004089433 |
| 2026-03-21T23:59:48Z | 7797398 | 0.004168773 |
| 2026-03-22T23:59:48Z | 7804598 | 0.004125279 |
| 2026-03-23T23:59:48Z | 7811798 | 0.004207364 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00437513182829399812 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004201207 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004177357 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004220779 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004154796 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004177842 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004184547 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004214974 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004268798 |
| 2026-04-02T23:59:48Z | 7883622 | 0.00420703 |
| 2026-04-03T23:59:48Z | 7890794 | 0.00418792 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004235882 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004206458 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004234474 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004220495 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004395833 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004262418 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004262712 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004279957 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004213982 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004325365 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004233549 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004159235 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004184172 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004176991 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004180951 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004168448 |
| 2026-04-20T23:59:48Z | 8013179 | 0.00420424 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004146961 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004159142 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004174723 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004177985 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003886179 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003972712 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.00394209 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004024505 |
| 2026-04-29T23:59:48Z | 8077790 | 0.003991638 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004033725 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004067266 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004052229 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004052756 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

