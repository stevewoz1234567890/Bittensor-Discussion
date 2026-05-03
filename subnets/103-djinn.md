# NetUID 103 — Djinn (`Ա`)

## Overview

Information X Execution

**From crawled page (site or GitHub):** Unbundling information from execution. Encrypted predictions, verifiable track records, settled in USDC on Base.

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
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 10000
- **Registration recycle cost snapshot (`burn`):** τ0.000566044
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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/Djinn-Inc/djinn/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

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
| 8103690 | 0.0055821 |
| 8103738 | 0.00554243 |
| 8103786 | 0.005542118 |
| 8103834 | 0.005561814 |
| 8103882 | 0.00562112 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Djinn | Sports Intelligence Marketplace
- **Meta / og:description:** Unbundling information from execution. Encrypted predictions, verifiable track records, settled in USDC on Base.
- **Fetched from:** [https://djinn.gg/](https://djinn.gg/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

