# NetUID 100 — Plaτform (`დ`)

## Overview

An auto-research subnet where miners compete in multiple challenges to achieve top scores against a synthetic benchmark, driving continuous performance optimization.

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5FX6kmhYwTYRFaZjxEo7k9DaG8qRmqrJtLTMGRgnfjRcXiWU`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
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

## Miner

Develop and submit agents to participate in Platform challenges. Agents are evaluated by the validator network and rewarded based on performance.

**Quick Links:**
- [Agent Development Guide](AGENTS.md) - How to build agents
- [Challenges](docs/challenges.md) - Available challenges
- [Challenge Integration](docs/challenge-integration.md) - Integration guide

---

---

### Using Docker Compose (Recommended)

```bash
git clone https://github.com/PlatformNetwork/platform.git
cd platform

---

# Configure environment

cp .env.example .env

---

# Edit .env and set your VALIDATOR_SECRET_KEY (BIP39 mnemonic)

nano .env

---

# Start validator

docker compose up -d

---

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `VALIDATOR_SECRET_KEY` | BIP39 mnemonic (24 words) | Yes |
| `NETUID` | Subnet UID (default: 100) | No |
| `SUBTENSOR_ENDPOINT` | Bittensor RPC endpoint | No |
| `RPC_PORT` | RPC API port (default: 8080) | No |
| `P2P_PORT` | P2P port (default: 8090) | No |

See [Validator Operations](docs/operations/validator.md) for hardware, configuration, and monitoring.

---

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - **No GPU required**: validators run on CPU servers.
- `| CPU | 4 vCPU | 8 vCPU |`
- `| RAM | 16 GB | 32 GB |`
- `| Storage | 250 GB SSD | 500 GB NVMe |`

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - **No GPU required**: validators run on CPU servers.
- `| CPU | 4 vCPU | 8 vCPU |`
- `| RAM | 16 GB | 32 GB |`
- `| Storage | 250 GB SSD | 500 GB NVMe |`


*Primary README URL used: `https://raw.githubusercontent.com/PlatformNetwork/platform/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


An auto-research subnet where miners compete in multiple challenges to achieve top scores against a synthetic benchmark, driving continuous performance optimization.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://platform.network](https://platform.network)
- **GitHub:** [https://github.com/PlatformNetwork/platform](https://github.com/PlatformNetwork/platform)
- **Discord:** [https://discord.platform.network](https://discord.platform.network)
- **Logo URL:** [https://www.platform.network/logo.png](https://www.platform.network/logo.png)
- **Contact:** platform@cortex.foundation

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.011415597 |
| 8103891 | 0.011391129 |
| 8103939 | 0.011390967 |
| 8103987 | 0.011390858 |
| 8104035 | 0.011390738 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

