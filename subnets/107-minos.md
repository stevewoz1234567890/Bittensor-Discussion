# NetUID 107 — Minos (`ミ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Minos** (NetUID **107**) (`ミ`).

The Foundational Layer of Genomics

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `94`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,728.541921595. **Alpha liquidity in pool (`alpha_in`)** = ‎115,479.460336436Ե‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎624,401.035594904Ե‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.032265269`** *(also **moving-average price** `0.031450099078938365` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎71,319.717602219Ե‎`. **Owner hotkey / coldkey (chain):** `5E4WJ2tAZVDTRVvSFtR1jJqAX4CokgCt9JYmPzJMWDmUT3Ju` / `5DA2vLrSXZxnT9G4Yrywx1Fpi4RXwMH1Ah7r8DTTWS7UZZBM`.
- **Subnet registered at block:** `7457580` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎55.487301550Ե‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.016128661` · α-out `‎1.000000000Ե‎` · α-in `‎0.500000000Ե‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104341`
- **Liquidity constant `k`:** `430570008947568668633735420`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Minos`
- **Symbol (API):** `ミ`
- **Rank:** `73`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.031897211`
- **Market cap:** `15802834192308.6581195`
- **Market cap Δ 1d:** `-2.576783329468781451`
- **Liquidity:** `7404385247381`
- **Total τ:** `3703448458214`
- **Total α:** `739540950423021`
- **α in pool:** `116026971422897`
- **α staked:** `379402995551603`
- **Price Δ 1h:** `0.48081913329637374`
- **Price Δ 1d:** `-4.072427379485487325`
#### Subnet activity (TAOStats)

- **NetUID (API):** `107`
- **Owner SS58 (API):** `5DA2vLrSXZxnT9G4Yrywx1Fpi4RXwMH1Ah7r8DTTWS7UZZBM`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `7457580`
- **Registration wall time:** `2026-02-02T18:12:24Z`
- **Registration cost snapshot:** `498986600980`
- **Active keys:** `64`
- **Active validators:** `12`
- **Active miners:** `2`
- **Active dual-role:** `1`
- **Emission:** `15948307`
- **Max neurons:** `64`
- **Validator slots (metadata):** `12`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `150000000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

# Minos – Decentralized Genomic Variant Calling & Benchmarking Platform

Minos (SN107) is a subnet for genomic variant calling and benchmarking powered by Bittensor. Every 72 minutes, the platform generates a fresh challenge genome (BAM file) containing hidden synthetic mutations injected using HelixForge at read level. Miners are rewarded for performing hyperparameter search and providing configurations for state-of-the-art variant calling tools that can accurately identify these hidden mutations in the genome. Once the hyperparameter space has been saturated, miners will compete to provide their own custom algorithms to identify mutations. Validators are responsible for downloading miner's hyperparam config and they will run each miner's submitted config, and evaluate the results using industry standard tools and approaches such as hap.py. Miners will never be asked to upload outputs, they submit their variant-calling configuration (and pipelines in later stages), which the validator executes trustlessly.

> **Subnet 107** on Bittensor mainnet (finney).

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Minos is a Bittensor subnet for decentralized genomic variant calling. Miners compete to detect DNA mutations with clinical-grade precision, advancing precision medicine.

**Fetched document title:** Minos | The Foundational Layer of Genomics

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://theminos.ai](https://theminos.ai)
- **GitHub:** [https://github.com/minos-protocol/minos_subnet](https://github.com/minos-protocol/minos_subnet)
- **Discord:** [https://discord.com/channels/799672011265015819/1467949024769478793](https://discord.com/channels/799672011265015819/1467949024769478793)
- **Logo URL:** [https://theminos.ai/logo.png](https://theminos.ai/logo.png)
- **Contact:** contact@theminos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.032396717 |
| 8104292 | 0.032603565 |
| 8104340 | 0.032584921 |
| 8104388 | 0.032577914 |
| 8104436 | 0.032265292 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

