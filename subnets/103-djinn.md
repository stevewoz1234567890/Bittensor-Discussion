# NetUID 103 — Djinn (`Ա`)

## Overview

Information X Execution

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
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 10000
- **Registration recycle cost snapshot (`burn`):** τ0.000669271
- **Owner SS58 (`owner_ss58`):** `5E6wTZZipkTmm6mci5jZp1FwXoUSGgG8CemFeC3DsV2nUGiM`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10000` blocks
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

### Prerequisites

- [Foundry](https://book.getfoundry.sh/getting-started/installation) (forge, cast, anvil)
- [Node.js](https://nodejs.org/) 20+ with [pnpm](https://pnpm.io/)
- [Python](https://www.python.org/) 3.11+ with [uv](https://docs.astral.sh/uv/)

---

# Start local stack (Anvil + Validator + Miner + Web)

cp validator/.env.example validator/.env
cp miner/.env.example miner/.env
cp web/.env.example web/.env
docker compose up
```

Or run components individually:

```bash

---

# Validator

cd validator && uv sync && uv run pytest

---

# Miner

cd miner && uv sync && uv run pytest

---

## Running a Validator

Validators hold Shamir key shares, coordinate MPC for executability checks, and attest game outcomes.

```bash
cd validator
cp .env.example .env

---

## Running a Miner

Miners verify real-time betting line availability and generate TLSNotary proofs.

```bash
cd miner
cp .env.example .env

---

### Validator

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | 4 cores | 8 cores |
| RAM | 8 GB | 16 GB |
| Disk | 40 GB SSD | 100 GB SSD |
| Network | 100 Mbps | 1 Gbps |

Validators run the API server, MPC coordination, outcome attestation, and burn ledger. MPC operations are CPU-intensive during purchase flows.

---

### Miner

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | 4 cores | 8+ cores |
| RAM | 8 GB | 16 GB |
| Disk | 20 GB SSD | 50 GB SSD |
| Network | 100 Mbps | 1 Gbps |

Miners run TLSNotary proof generation (30-90s CPU per attestation) and sports line checking. CPU is the bottleneck for TLSNotary MPC.

---

---

# Validator tests (1600+ tests)

cd validator && uv run pytest

---

# Miner tests (450+ tests)

cd miner && uv run pytest

---

### Docker

```bash

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- `| CPU | 4 cores | 8 cores |`
- `| RAM | 8 GB | 16 GB |`
- `| Disk | 40 GB SSD | 100 GB SSD |`
- Validators run the API server, MPC coordination, outcome attestation, and burn ledger. MPC operations are CPU-intensive during purchase flows.
- `| CPU | 4 cores | 8+ cores |`
- `| Disk | 20 GB SSD | 50 GB SSD |`
- Miners run TLSNotary proof generation (30-90s CPU per attestation) and sports line checking. CPU is the bottleneck for TLSNotary MPC.
- - **System Dashboard** — CPU, memory, disk, network

---

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - **CPU:** 2+ cores, 2.0 GHz+
- - **RAM:** 4 GB minimum
- - **Storage:** 5 GB SSD
- - **GPU:** Not required

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - **CPU:** 4+ cores, 2.5 GHz+
- - **RAM:** 8 GB minimum
- - **Storage:** 10 GB SSD
- - **GPU:** Not required
- `| `SPORTS_API_KEY` | No | Deprecated. Scores now come from ESPN (free). Kept for backward compatibility but ignored. |`

---

##### Extra scrape: `README.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- `| macOS | Intel x86_64 | Untested but should work with the Linux x86_64 TLSNotary binary via Rosetta. |`
- `| Capability | 10%    | System resource bonus based on advertised hardware (see below) |`
- `| Total RAM | Score |`
- `| 8 GB      | 0.1   |`
- `| 16 GB     | 0.2   |`
- `| 32 GB     | 0.3   |`
- `| 64 GB+    | 0.4   |`
- **CPU (0 to 0.2)**
- `| Cores | Score |`
- Computed as `(available_mb / total_mb) * 0.2`. Miners with most of their RAM free score higher.
- The `ATTEST_MAX_CONCURRENT` environment variable (default 5) controls how many TLSNotary attestation sessions can run simultaneously. Each session consumes significant RAM. Recommended settings:
- `| RAM   | ATTEST_MAX_CONCURRENT |`
- `| 8 GB  | 2                     |`
- `| 16 GB | 3                     |`
- `| 32 GB | 5                     |`
- `| 64 GB | 8                     |`
- `| `max_recv_data`    | 8 MB    | A target site that advertises a huge `Content-Length` (legitimately or maliciously) used to make the prover allocate a multi-gigabyte MPC circuit per request. Targets larger than 8 MB now fail at preflight with an actionable error ("try a smaller endpoint") instead of OOM-killing the prover. |`
- `| Tier        | RAM    | CPU Cores | Disk   | Notes |`
- `| Minimum     | 8 GB   | 4         | 50 GB  | Can run basic line checks. Limited attestation capacity (set `ATTEST_MAX_CONCURRENT=2`). Capability score around 0.15-0.25. |`
- `| Recommended | 32 GB  | 8+        | 100 GB | Handles concurrent attestations comfortably. Capability score around 0.5-0.7. |`
- `| Optimal     | 64 GB  | 16+       | 200 GB | Maximum capability score. Handles 8+ concurrent attestation sessions. Gets priority routing from validators. |`
- More resources translate directly to a higher capability score, which means more attestation work routed to your miner and higher emissions. The relationship is not linear; the biggest gains come from crossing tier thresholds (8 to 16 GB, 16 to 32 GB, etc.).


*Primary README URL used: `https://raw.githubusercontent.com/Djinn-Inc/djinn/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Information X Execution

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://djinn.gg/](https://djinn.gg/)
- **GitHub:** [https://github.com/Djinn-Inc/djinn/](https://github.com/Djinn-Inc/djinn/)
- **Logo URL:** [https://raw.githubusercontent.com/Djinn-Inc/djinn-assets/main/djinn-logo-black.png](https://raw.githubusercontent.com/Djinn-Inc/djinn-assets/main/djinn-logo-black.png)
- **Contact:** info@djinn.gg

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.005561798 |
| 8103891 | 0.005621119 |
| 8103939 | 0.005631027 |
| 8103987 | 0.005631016 |
| 8104035 | 0.005628941 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

