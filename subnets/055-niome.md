# NetUID 55 — NIOME (`ث`)

## Overview

NIOME is a decentralized AI subnet that enables privacy-safe genomic intelligence by replacing real human genomes with high-fidelity synthetic genomic profiles

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GeWUxaFP6duJyNg8EUv6Jfcv6ZNkoERywAcbSw4FAuEMpDq`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `2`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Guide for Miners and Validators

- [Miner Setup](docs/miner_guide.md) 
- [Validator Setup](docs/validator_guide.md)

---

#### CPU / GPU / RAM lines (automatic grep)

*Nothing in this README excerpt matched GPU/VRAM/CPU sizing patterns (`\d+ GB/TB`, `CUDA`, `H100/RTX/…`, `vCPU/cores`). Check **`docs/`**, miner/validator guides linked here, Discord, or the subnet’s homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/genomesio/subnet-niome/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


NIOME is a decentralized AI subnet that enables privacy-safe genomic intelligence by replacing real human genomes with high-fidelity synthetic genomic profiles

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://niome.genomes.io](https://niome.genomes.io)
- **GitHub:** [https://github.com/genomesio/subnet-niome](https://github.com/genomesio/subnet-niome)
- **Discord:** [https://discord.gg/7mJkaJZX](https://discord.gg/7mJkaJZX)
- **Logo URL:** [https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pgi-9hji1nosR-l7taHQeA.png](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pgi-9hji1nosR-l7taHQeA.png)
- **Contact:** info@genomes.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.004830379 |
| 8103843 | 0.004830738 |
| 8103891 | 0.00483414 |
| 8103939 | 0.004838403 |
| 8103987 | 0.004838961 |
| 8104035 | 0.004837275 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

