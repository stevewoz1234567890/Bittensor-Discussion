# NetUID 103 — Djinn (`Ա`)

## Overview

**Djinn** (NetUID **103**) (`Ա`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `231`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ5,401.256190609. **Alpha liquidity in pool (`alpha_in`)** = ‎852,678.939791471Ա‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,438,044.173164921Ա‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005534225`** *(also **moving-average price** `0.005564012797549367` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎391,808.327189260Ա‎`. **Owner hotkey / coldkey (chain):** `5FqBe8tHboYWtNxJaBjz95a94GfHPcPkR9kStsMirSJwanaN` / `5E6wTZZipkTmm6mci5jZp1FwXoUSGgG8CemFeC3DsV2nUGiM`.
- **Subnet registered at block:** `5515448` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎168.331268624Ա‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000023802` · α-out `‎1.000000000Ա‎` · α-in `‎0.004300894Ա‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005534226`
- **Market cap:** `15223704120139.692450204`
- **Liquidity:** `10120173529745`
- **Total τ:** `5401256294834`
- **Total α:** `3290710057022097`
- **α in pool:** `852678809089452`
- **α staked:** `1898149241687602`
- **Price Δ 1h:** `-1.545725908730174967`
- **Price Δ 1d:** `-0.072243337082427282`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `237`
- **Active dual:** `1`
- **Emission:** `23794`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `614863`

### On-chain declared purpose *(SubnetIdentity)*

Information X Execution

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Djinn Protocol** <!-- omit in toc -->

### Intelligence × Execution

Buy intelligence you can trust.
Sell analysis you can prove.
Signals stay secret forever — even from us.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/Djinn-Inc/djinn/actions/workflows/ci.yml/badge.svg)](https://github.com/Djinn-Inc/djinn/actions/workflows/ci.yml)

---

Bittensor Subnet 103 · Base Chain · USDC

[Whitepaper](docs/whitepaper.md) · [djinn.gg](https://djinn.gg)
</div>

---

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Architecture](#architecture)
- [Web Attestation](#web-attestation)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Running a Validator](#running-a-validator)
- [Running a Miner](#running-a-miner)
- [Hardware Requirements](#hardware-requirements)
- [Observability](#observability)
- [Operations & Runbooks](#operations--runbooks)
- [Development](#development)
- [Contract Addresses](#contract-addresses)
- [License](#license)

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Unbundling information from execution. Encrypted predictions, verifiable track records, settled in USDC on Base.

**Fetched document title:** Djinn | Sports Intelligence Marketplace

## Operational parameters — registration, limits, economics (chain)


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
- **Registration recycle cost snapshot (`burn`):** τ0.000595055
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

- - **CPU:** 2+ cores, 2.0 GHz+
- - **RAM:** 4 GB minimum
- - **Storage:** 5 GB SSD
- - **GPU:** Not required

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- - **CPU:** 4+ cores, 2.5 GHz+
- - **RAM:** 8 GB minimum
- - **Storage:** 10 GB SSD
- - **GPU:** Not required
- `| `SPORTS_API_KEY` | No | Deprecated. Scores now come from ESPN (free). Kept for backward compatibility but ignored. |`

---

##### Extra scrape: `README.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

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

## On-chain identity — description


Information X Execution

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://djinn.gg/](https://djinn.gg/)
- **GitHub:** [https://github.com/Djinn-Inc/djinn/](https://github.com/Djinn-Inc/djinn/)
- **Logo URL:** [https://raw.githubusercontent.com/Djinn-Inc/djinn-assets/main/djinn-logo-black.png](https://raw.githubusercontent.com/Djinn-Inc/djinn-assets/main/djinn-logo-black.png)
- **Contact:** info@djinn.gg

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.005628943 |
| 8104072 | 0.005615014 |
| 8104120 | 0.005614997 |
| 8104168 | 0.005614985 |
| 8104216 | 0.005534225 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

