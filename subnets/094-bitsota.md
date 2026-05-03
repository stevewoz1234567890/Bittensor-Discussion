# NetUID 94 — Bitsota (`ᚄ`)

## Overview

Decentralized SoTA Research

https://discord.gg/jkJWJtPuw7

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
- **Owner SS58 (`owner_ss58`):** `5EZRCK9op9piMhQvHqrEL1SNQU8ENU8s9aqGnRKNsUxmPYP2`

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

### Direct Mining

Individual miners evolve algorithms locally and submit breakthroughs to validators. Requires higher compute but offers larger individual rewards.

**Best for:** Experienced miners with dedicated hardware

**[→ Direct Mining Guide](docs/mining.md)**

---

### Pool Mining

Collaborative mining where participants handle smaller evolution and evaluation tasks. Pool aggregates results and submits to validators on behalf of all participants.

**Best for:** New miners or those with limited compute resources

**[→ Pool Mining Guide](docs/pool-mining.md)**

---

### Direct Mining Flow

```
Miner → Evolve Locally → Beat SOTA → Submit to Relay → Validators Verify → Relay Consensus → Weight Update → Emissions
```

1. Miner runs genetic programming engine for up to 150 generations
2. When algorithm beats State-of-the-Art threshold, submits to relay
3. Validators download submission and independently re-evaluate
4. Validators choose weight setting mode:
   - Relay mode: Vote on relay, wait for consensus, then set weights
   - Local mode: Set weights immediately based on own evaluation
5. Validators set on-chain weights: 90% burn, 10% winner
6. Network emissions flow to winner via Yuma consensus

---

### Pool Mining Flow

```
Pool → Assigns Tasks → Miners Execute → Pool Consensus → Submit to Validators → Epoch Rewards
```

1. Pool distributes evolution and evaluation tasks to participants
2. Multiple miners evaluate each algorithm (3+ required)
3. Pool computes median consensus with 10% tolerance
4. Rewards distributed based on reputation at epoch boundaries
5. Pool submits best algorithms to validators on behalf of participants

**[→ Detailed Rewards Guide](docs/rewards.md)**

---

### For Miners

**Desktop GUI (Recommended):**
1. Download from [bitsota.ai](https://bitsota.ai)
2. Install for your platform
3. Import your Bittensor hotkey
4. Choose mining mode (Direct or Pool)
5. Start mining

See detailed setup guides:
- [Direct Mining Setup](docs/mining.md#setup)
- [Pool Mining Setup](docs/pool-mining.md#setup)

---

### For Validators

```bash
git clone https://github.com/AlveusLabs/BitSota.git
cd BitSota
pip install -r requirements.txt
pip install -e .

cp validator_config.yaml.example validator_config.yaml

---

# Edit validator_config.yaml with your wallet and burn_hotkey

python neurons/validator_node.py
```

**[→ Full Validator Setup](docs/validation.md#setup)**

---

## Requirements

**Minimum:**
- Python 3.10+
- 4GB RAM
- 2GB storage
- Stable internet connection

**For Validation:**
- 16GB RAM
- 8+ CPU cores

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - 2GB storage
- - 16GB RAM
- - 8+ CPU cores


*Primary README URL used: `https://raw.githubusercontent.com/AlveusLabs/SN94-BitSota/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Decentralized SoTA Research

## On-chain identity — additional field


https://discord.gg/jkJWJtPuw7

## Registered contact & links


- **GitHub:** [https://github.com/AlveusLabs/SN94-BitSota](https://github.com/AlveusLabs/SN94-BitSota)
- **Discord (handle / invite hint):** `dev.alveuslabs`
- **Logo URL:** [https://bitsota.ai/logo.png](https://bitsota.ai/logo.png)
- **Contact:** info@bitsota.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.005091304 |
| 8103891 | 0.005096818 |
| 8103939 | 0.00509709 |
| 8103987 | 0.005066297 |
| 8104035 | 0.005066564 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

