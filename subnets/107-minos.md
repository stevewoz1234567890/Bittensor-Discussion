# NetUID 107 — Minos (`ミ`)

## Overview

The Foundational Layer of Genomics

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 64
- **`subnetwork_n`:** 64
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.150000000
- **Owner SS58 (`owner_ss58`):** `5DA2vLrSXZxnT9G4Yrywx1Fpi4RXwMH1Ah7r8DTTWS7UZZBM`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.150000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
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

## System Prerequisites

| Component | Requirement | Notes |
|-----------|-------------|-------|
| OS | Linux (Ubuntu 20.04+), macOS 13+ | Docker + Bittensor run best on Linux |
| CPU/RAM (Validator) | ≥8 cores / 32 GB RAM | hap.py scoring benefits from cores |
| CPU/RAM (Miner) | ≥4 cores / 8–16 GB RAM | 8 GB for BCFtools/FreeBayes, 16 GB for DeepVariant |
| Disk | ≥60 GB (miner) / ≥100 GB (validator) | Reference: ~2 GB miner, ~14 GB validator (SDF expands ~6×). Plus per-round BAMs (~6 GB each) until cleaned. |
| Docker | 20.10+ (24.0+ recommended) | Required for GATK, hap.py, bcftools |
| Python | 3.10+ | We test on 3.12 |
| Bittensor | Latest pip install | Provides wallet/subtensor/dendrite APIs |

---

---

#### 1. Setup Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

#### 2. Configure Environment

```bash
cp .env.miner.example .env    # for miners
cp .env.validator.example .env # for validators
```

---

#### 3. Pull Docker Images

```bash
docker pull broadinstitute/gatk:4.5.0.0
docker pull google/deepvariant:1.5.0
docker pull staphb/freebayes:1.3.7
docker pull genonet/hap-py@sha256:03acabe84bbfba35f5a7234129d524c563f5657e1f21150a2ea2797f8e6d05f2
docker pull quay.io/biocontainers/bcftools:1.20--h8b25389_0
docker pull quay.io/biocontainers/samtools:1.20--h50ea8bc_0
```

> **Note:** The hap.py image is pinned by SHA256 digest for reproducible scoring. The tag `genonet/hap-py:0.3.15` points to the same image but the digest is what validators use internally.

---

#### 4. Run Setup Wizard

```bash

---

### Environment Variables

```bash

---

# aws_s3 = R2/AWS first. Both serve the same files; this just controls fetch order.

STORAGE_PRIMARY_BACKEND=hippius
```

---

### Running the Validator

```bash
bash start-validator.sh
bash start-validator.sh --wallet-name validator   # Pre-fill wallet name
bash start-validator.sh --setup                   # Re-run setup wizard
```

For production-style supervision, use **[Running with PM2 (optional)](#running-with-pm2-optional)** (`bash pm2-validator.sh`).

Or manually:

```bash
source .venv/bin/activate
python -m neurons.validator \
  --netuid 107 \
  --subtensor.network finney \
  --wallet.name validator \
  --wallet.hotkey default
```

---

### Validator Workflow

1. **Fetch Rounds and Assignment**: Poll platform for scoring rounds and this validator's primary/secondary miner assignment
2. **Download Round Data**: Download the mutated BAM, merged truth VCF, and mutations-only VCF from platform presigned URLs
3. **Run Miner Tools**: Execute assigned miners' variant-calling configs via templates, scoring primaries first and secondaries only while enough time remains
4. **Scoring**: Validate each generated VCF with hap.py against the platform truth data, then compute the AdvancedScorer result
5. **Submit Scores**: Report each per-miner score and audit artifact pointers back to the platform
6. **Backfill and Record Round**: After the scoring window closes, fetch peer scores for miners not personally covered and record complete participation
7. **Weight Update**: Submit weight history to the platform, then set on-chain weights if the validator is registered

---

### Validator Parallelism

Each round, the validator runs many miners' variant-calling configs concurrently. Concurrency, per-job thread count, and memory ceiling are auto-tuned at startup from host CPU/RAM:

- Reserves 4 cores + 16 GB for the OS, Docker daemon, and hap.py
- Picks `threads_per_job` between 2 and 8 (DeepVariant's call_variants is single-threaded past 8)
- Pins memory at 16 GB per job (DeepVariant's documented minimum)
- `concurrency = min(usable_cores // threads_per_job, usable_ram // 16, 8)`

Examples:

| Host | Auto-tune |
|---|---|
| 8c / 32 GB | 1 concurrent × 2 threads × 16 GB |
| 16c / 64 GB | 3 concurrent × 3 threads × 16 GB |
| 32c / 128 GB | 4 concurrent × 7 threads × 16 GB |
| 64c / 256 GB | 7 concurrent × 8 threads × 16 GB |

To override, set `MINOS_VALIDATOR_CONCURRENCY`, `SCORING_THREADS`, or `SCORING_MEMORY_GB` in `.env`. Note `SCORING_MEMORY_GB < 16` will OOM-crash DeepVariant submissions.

---

---

### Environment Variables

```bash

---

# Miner

MINER_TEMPLATE=gatk

---

# aws_s3 = R2/AWS first. Both serve the same files; this just controls fetch order.

STORAGE_PRIMARY_BACKEND=hippius
```

---

### Running the Miner

```bash
bash start-miner.sh
bash start-miner.sh --wallet-name miner --miner-template deepvariant  # Pre-fill values
bash start-miner.sh --setup                                           # Re-run setup wiz…

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- `| CPU/RAM (Validator) | ≥8 cores / 32 GB RAM | hap.py scoring benefits from cores |`
- `| CPU/RAM (Miner) | ≥4 cores / 8–16 GB RAM | 8 GB for BCFtools/FreeBayes, 16 GB for DeepVariant |`
- `| Disk | ≥60 GB (miner) / ≥100 GB (validator) | Reference: ~2 GB miner, ~14 GB validator (SDF expands ~6×). Plus per-round BAMs (~6 GB each) until cleaned. |`
- Each round, the validator runs many miners' variant-calling configs concurrently. Concurrency, per-job thread count, and memory ceiling are auto-tuned at startup from host CPU/RAM:
- - Reserves 4 cores + 16 GB for the OS, Docker daemon, and hap.py
- - Pins memory at 16 GB per job (DeepVariant's documented minimum)
- `| 8c / 32 GB | 1 concurrent × 2 threads × 16 GB |`
- `| 16c / 64 GB | 3 concurrent × 3 threads × 16 GB |`
- `| 32c / 128 GB | 4 concurrent × 7 threads × 16 GB |`
- `| 64c / 256 GB | 7 concurrent × 8 threads × 16 GB |`
- `| `POST /v2/submit-score`         | Validator | Submit per-miner scores                        |`
- `| `POST /v2/get-backfill-scores`  | Validator | Fetch peer scores after scoring window closes  |`
- `| `POST /v2/submit-weight-history`| Validator | Submit EMA scores and weights after round      |`
- `| Core F1      | 60%    |`
- `| `GATK timeout`                | Insufficient resources                     | Increase threads/memory or timeout                                                                               |`
- `| DeepVariant OOM / killed      | <16 GB available to the container          | DeepVariant needs ≥16 GB. Free RAM, close other tools, or switch template to GATK/FreeBayes/BCFtools             |`
- `| `hap.py zero scores`          | VCF format issues                          | Ensure single-sample VCF output                                                                                  |`
- `| Validator: "no scoring rounds"| Round still in submission window           | Validators only score AFTER the submission window closes. Wait for the next tempo boundary                       |`


*Primary README URL used: `https://raw.githubusercontent.com/minos-protocol/minos_subnet/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


The Foundational Layer of Genomics

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://theminos.ai](https://theminos.ai)
- **GitHub:** [https://github.com/minos-protocol/minos_subnet](https://github.com/minos-protocol/minos_subnet)
- **Discord:** [https://discord.com/channels/799672011265015819/1467949024769478793](https://discord.com/channels/799672011265015819/1467949024769478793)
- **Logo URL:** [https://theminos.ai/logo.png](https://theminos.ai/logo.png)
- **Contact:** contact@theminos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.032208913 |
| 8103891 | 0.031562135 |
| 8103939 | 0.031574375 |
| 8103987 | 0.031795831 |
| 8104035 | 0.031764333 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

