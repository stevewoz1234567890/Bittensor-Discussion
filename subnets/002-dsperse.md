# NetUID 2 — DSperse (`β`)

## Overview

Verifiable and distributed inference on Bittensor

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

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
- **`difficulty` (PoW field on info view):** 258042570695
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5EcYQ3W77ndrmMWdvVQusoFqY8doxfP3U2zrh7xZQiaz7avY`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `258042570695` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `2`
- **`liquid_alpha_enabled`:** `True`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `True` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 10.0, `65534`, `6554`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Miners

- Receive input data from validators on the subnet
- Generate predictions using custom, verifiable AI models that have been converted into zero-knowledge circuits
- Return the generated content to the requesting validator for validation and distribution

---

### Validators

- Produce input data and distribute requests for verified inference throughout miners participating on the subnet
- Confirm that miners are acting faithfully, by verifying the authenticity of the miner's returned zero-knowledge proof
- Score results from miners based on performance metrics such as proof size and response time

---

### Prerequisites

| Tool | Description |
|------|-------------|
| [Rust](https://rustup.rs/) | Required to build from source. Install via `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| [PM2](https://pm2.keymetrics.io/) | Process manager used to run and monitor the binaries in the background |
| [btcli](https://docs.bittensor.com/getting-started/installation) | CLI for interacting with the Bittensor network (wallet creation, registration) |

Alternatively, use Docker — no Rust toolchain needed. See the Docker instructions under [Run the Miner](#run-the-miner) and [Run the Validator](#run-the-validator) below.

---

### Install from pre-built binary

Automatically detects your platform, downloads the latest release, verifies the SHA256 checksum, and installs to `/usr/local/bin`:

```console
curl -fsSL https://raw.githubusercontent.com/inference-labs-inc/subnet-2/main/install.sh | bash
```

To install only the miner or validator:

```console
curl -fsSL https://raw.githubusercontent.com/inference-labs-inc/subnet-2/main/install.sh | bash -s -- sn2-miner
curl -fsSL https://raw.githubusercontent.com/inference-labs-inc/subnet-2/main/install.sh | bash -s -- sn2-validator
```

For testnet builds (from the `testnet` branch):

```console
curl -fsSL https://raw.githubusercontent.com/inference-labs-inc/subnet-2/testnet/install.sh | NETWORK=testnet bash
curl -fsSL https://raw.githubusercontent.com/inference-labs-inc/subnet-2/testnet/install.sh | NETWORK=testnet bash -s -- sn2-miner
curl -fsSL https://raw.githubusercontent.com/inference-labs-inc/subnet-2/testnet/install.sh | NETWORK=testnet bash -s -- sn2-validator
```

Or download manually from [GitHub Releases](https://github.com/inference-labs-inc/subnet-2/releases).

---

### Run the Miner

<details>
<summary>Docker</summary>

---

#### With docker compose (recommended)

```yaml
---
services:

  subnet-2-miner:
    image: ghcr.io/inference-labs-inc/subnet-2:latest
    restart: unless-stopped
    ports:
      - 8091:8091
    volumes:
      - {path_to_your_.bittensor_directory}:/home/subnet2/.bittensor
    environment:
      - PUID=1000
      - HOME=/home/subnet2
    labels:
      - com.centurylinklabs.watchtower.enable=true
    command: sn2-miner --wallet-name {your_miner_key_name} --wallet-hotkey {your_miner_hotkey_name} --netuid 2

  watchtower:
    image: containrrr/watchtower:latest
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    command: --interval 60 --cleanup --label-enable
```

---

#### With docker cli

```console
docker run -d \
  --name subnet-2-miner \
  -p 8091:8091 \
  -v {path_to_your_.bittensor_directory}:/home/subnet2/.bittensor \
  -e PUID=1000 \
  -e HOME=/home/subnet2 \
  --restart unless-stopped \
  ghcr.io/inference-labs-inc/subnet-2:latest \
  sn2-miner \
  --wallet-name {your_miner_key_name} \
  --wallet-hotkey {your_miner_hotkey_name} \
  --netuid 2
```

</details>

---

### Run the Validator

<details>
<summary>Docker</summary>

---

#### With docker compose (recommended)

```yaml
---
services:

  subnet-2-validator:
    image: ghcr.io/inference-labs-inc/subnet-2:latest
    restart: unless-stopped
    ports:
      - 8443:8443
      - 9090:9090
    volumes:
      - {path_to_your_.bittensor_directory}:/home/subnet2/.bittensor
    environment:
      - PUID=1000
      - HOME=/home/subnet2
    labels:
      - com.centurylinklabs.watchtower.enable=true
    command: sn2-validator --wallet-name {validator_key_name} --wallet-hotkey {validator_hotkey_name} --netuid 2

  watchtower:
    image: containrrr/watchtower:latest
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    command: --interval 60 --cleanup --label-enable
```

---

#### With docker cli

```console
docker run -d \
  --name subnet-2-validator \
  -p 8443:8443 \
  -p 9090:9090 \
  -v {path_to_your_.bittensor_directory}:/home/subnet2/.bittensor \
  -e PUID=1000 \
  -e HOME=…

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- Subnet 2 incentivizes miners and validators to contribute to the generation and validation of high-quality, secure, and efficient verified AI predictions using a specialized reward mechanism aligned with the unique aspects of zero-knowledge machine learning (zk-ML) and decentralized AI. Zero-knowledge proofs are generally more CPU computationally intensive and open the opportunity for non-GPU miners to participate, however the end goal is to further incentivize the development of proving systems optimized for GPU-based operations. The incentives are based around miners creating succinct and efficient models which can be circuitized with a zero-knowledge proving system.
- `| CPU            | 8 core 3.2GHz |`
- `| RAM            | 32GB          |`
- `| Storage        | 1TB           |`
- `| Storage Medium | NVMe SSD      |`
- > Exceeding these requirements in terms of storage, network and CPU speed will most likely result in higher rewards due to performance incentivization.
- `| CPU            | 8 core 3.6GHz+  |`
- `| RAM            | 64GB+           |`
- `| Storage        | 2TB             |`
- `| RAM          | 16GB          |`
- `| CPU            | 8 core 3.4GHz  |`
- `| Storage Medium | SSD            |`


*Primary README URL used: `https://raw.githubusercontent.com/inference-labs-inc/subnet-2/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Verifiable and distributed inference on Bittensor

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://subnet2.inferencelabs.com](https://subnet2.inferencelabs.com)
- **GitHub:** [https://github.com/inference-labs-inc/subnet-2](https://github.com/inference-labs-inc/subnet-2)
- **Logo URL:** [https://dsperse.inferencelabs.com/logo-512.png](https://dsperse.inferencelabs.com/logo-512.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.006472281 |
| 8103843 | 0.006472267 |
| 8103891 | 0.006472261 |
| 8103939 | 0.006469027 |
| 8103987 | 0.00646893 |
| 8104035 | 0.006467372 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

