# NetUID 128 — ByteLeap (`න`)

## Overview

Pioneering the Future of Cloud & Blockchain

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
- **Owner SS58 (`owner_ss58`):** `5GgMeLFN4YssT6f9i9pZpRmczt8GYDsCZ1nYPiGRcTPWn3AA`

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
- **`commit_reveal_weights_enabled`:** `False`
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

# ByteLeap Miner - Bittensor SN128 Compute Network

ByteLeap Miner is the resource aggregation component of the ByteLeap distributed compute platform. Miners connect to the Bittensor network (SN128), aggregate worker resources, and earn rewards through active compute leases and computational challenges.

---

## Scoring System

Miners earn rewards through two main factors:

---

### Prerequisites

- Python 3.8+
- Bittensor wallet with registered hotkey

---

### Installation

```bash

---

# Setup environment

python3 -m venv venv
source ./venv/bin/activate

---

# Install dependencies

pip install -r requirements.txt
```

---

### Running the Miner

**Start Miner** (aggregates workers, communicates with Bittensor):
```bash
python scripts/run_miner.py --config config/miner_config.yaml
```

---

#### CPU / GPU / RAM lines (automatic grep)

*Nothing in this README excerpt matched GPU/VRAM/CPU sizing patterns (`\d+ GB/TB`, `CUDA`, `H100/RTX/…`, `vCPU/cores`). Check **`docs/`**, miner/validator guides linked here, Discord, or the subnet’s homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/byteleapai/byteleap-Miner/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Pioneering the Future of Cloud & Blockchain

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/byteleapai/byteleap-Miner](https://github.com/byteleapai/byteleap-Miner)
- **Discord:** [https://discord.com/channels/799672011265015819/1387438124132733110](https://discord.com/channels/799672011265015819/1387438124132733110)
- **Logo URL:** [https://avatars.githubusercontent.com/u/217718200](https://avatars.githubusercontent.com/u/217718200)
- **Contact:** byteleap.ai@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.003302267 |
| 8103891 | 0.00330252 |
| 8103939 | 0.003302514 |
| 8103987 | 0.003302509 |
| 8104035 | 0.003304141 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

