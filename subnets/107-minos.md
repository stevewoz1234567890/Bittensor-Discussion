# NetUID 107 — Minos (`ミ`)

## Overview

The Foundational Layer of Genomics

**From crawled page (site or GitHub):** Minos is a Bittensor subnet for decentralized genomic variant calling. Miners compete to detect DNA mutations with clinical-grade precision, advancing precision medicine.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

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

## Miner / validator compute notes (README excerpts)

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

#### 4. Run Setup Wizard

```bash

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

# Miner

MINER_TEMPLATE=gatk

---

### Running the Miner

```bash
bash start-miner.sh
bash start-miner.sh --wallet-name miner --miner-template deepvariant  # Pre-fill values
bash start-miner.sh --setup                                           # Re-run setup wizard
```

For production-style supervision, use **[Running with PM2 (optional)](#running-with-pm2-optional)** (`bash pm2-miner.sh`).

Or manually:

```bash
source .venv/bin/activate
python -m neurons.miner \
  --netuid 107 \
  --subtensor.network finney \
  --wallet.name miner \
  --wallet.hotkey default
```

---

### Miner Workflow

1. **Registration**: Register with platform via hotkey authentication
2. **Task Poll**: Poll platform for pending evaluation tasks
3. **BAM Download**: Fetch benchmark BAM from platform via presigned URL
4. **Variant Calling**: Run configured variant caller (GATK, DeepVariant, freebayes, or bcftools)
5. **Config Submit**: Submit tool config you've used (hyperparameters only based on the template)
6. **Reward**: Earn alpha based on accuracy score — validators re-run the config to verify

---

---

# PM2 (recommended)

pm2 logs minos-miner
pm2 logs minos-validator


*README source used for excerpts: `https://raw.githubusercontent.com/minos-protocol/minos_subnet/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

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
| 8103690 | 0.032214739 |
| 8103738 | 0.032241442 |
| 8103786 | 0.032206376 |
| 8103834 | 0.032203994 |
| 8103882 | 0.032050915 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Minos | The Foundational Layer of Genomics
- **Meta / og:description:** Minos is a Bittensor subnet for decentralized genomic variant calling. Miners compete to detect DNA mutations with clinical-grade precision, advancing precision medicine.
- **Fetched from:** [https://theminos.ai](https://theminos.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

