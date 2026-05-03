# NetUID 107 — Minos (`ミ`)

## Overview

**Minos** (NetUID **107**) (`ミ`).

The Foundational Layer of Genomics

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `235`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,763.559750431. **Alpha liquidity in pool (`alpha_in`)** = ‎114,185.363131611Ե‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎625,374.520279279Ե‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.032497813`** *(also **moving-average price** `0.031393509823828936` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎71,006.038270810Ե‎`. **Owner hotkey / coldkey (chain):** `5E4WJ2tAZVDTRVvSFtR1jJqAX4CokgCt9JYmPzJMWDmUT3Ju` / `5DA2vLrSXZxnT9G4Yrywx1Fpi4RXwMH1Ah7r8DTTWS7UZZBM`.
- **Subnet registered at block:** `7457580` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎138.704397430Ե‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.016362814` · α-out `‎1.000000000Ե‎` · α-in `‎0.500000000Ե‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.031897211`
- **Market cap:** `15802834192308.6581195`
- **Liquidity:** `7404385247381`
- **Total τ:** `3703448458214`
- **Total α:** `739540950423021`
- **α in pool:** `116026971422897`
- **α staked:** `379402995551603`
- **Price Δ 1h:** `0.48081913329637374`
- **Price Δ 1d:** `-4.072427379485487325`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `64`
- **Active validators:** `12`
- **Active miners:** `2`
- **Active dual:** `1`
- **Emission:** `15948307`
- **Max neurons:** `64`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `150000000`

### On-chain declared purpose *(SubnetIdentity)*

The Foundational Layer of Genomics

### Repository README excerpt *(everything before first `##` heading)*

# Minos – Decentralized Genomic Variant Calling & Benchmarking Platform

Minos (SN107) is a subnet for genomic variant calling and benchmarking powered by Bittensor. Every 72 minutes, the platform generates a fresh challenge genome (BAM file) containing hidden synthetic mutations injected using HelixForge at read level. Miners are rewarded for performing hyperparameter search and providing configurations for state-of-the-art variant calling tools that can accurately identify these hidden mutations in the genome. Once the hyperparameter space has been saturated, miners will compete to provide their own custom algorithms to identify mutations. Validators are responsible for downloading miner's hyperparam config and they will run each miner's submitted config, and evaluate the results using industry standard tools and approaches such as hap.py. Miners will never be asked to upload outputs, they submit their variant-calling configuration (and pipelines in later stages), which the validator executes trustlessly.

> **Subnet 107** on Bittensor mainnet (finney).

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Minos is a Bittensor subnet for decentralized genomic variant calling. Miners compete to detect DNA mutations with clinical-grade precision, advancing precision medicine.

**Fetched document title:** Minos | The Foundational Layer of Genomics

## Operational parameters — registration, limits, economics (chain)


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

## On-chain identity — description


The Foundational Layer of Genomics

## On-chain identity — additional field


*Unset.*

## Registered contact & links


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
| 8104024 | 0.031781783 |
| 8104072 | 0.03170377 |
| 8104120 | 0.031695762 |
| 8104168 | 0.032122062 |
| 8104216 | 0.032497813 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.016228162 |
| 2026-03-10T23:59:48Z | 7718257 | 0.017969988 |
| 2026-03-11T23:59:48Z | 7725455 | 0.019072162 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.017147097 |
| 2026-03-13T23:59:48Z | 7739841 | 0.015334254 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.016489581 |
| 2026-03-15T23:59:48Z | 7754226 | 0.018461422 |
| 2026-03-16T23:59:48Z | 7761426 | 0.018085895 |
| 2026-03-17T23:59:48Z | 7768619 | 0.017273633 |
| 2026-03-18T23:59:48Z | 7775819 | 0.015030126 |
| 2026-03-19T23:59:48Z | 7783014 | 0.01525408396641907099 |
| 2026-03-20T23:59:48Z | 7790201 | 0.015870436 |
| 2026-03-21T23:59:48Z | 7797398 | 0.014420292 |
| 2026-03-22T23:59:48Z | 7804598 | 0.017215124 |
| 2026-03-23T23:59:48Z | 7811798 | 0.017256873 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.01617109548305753579 |
| 2026-03-25T23:59:48Z | 7826196 | 0.014584997 |
| 2026-03-26T23:59:48Z | 7833396 | 0.012398202 |
| 2026-03-27T23:59:48Z | 7840596 | 0.014157179 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.015261685 |
| 2026-03-29T23:59:48Z | 7854902 | 0.014169084 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.013521378 |
| 2026-03-31T23:59:48Z | 7869291 | 0.012243332 |
| 2026-04-01T23:59:48Z | 7876474 | 0.013340896 |
| 2026-04-02T23:59:48Z | 7883622 | 0.014446052 |
| 2026-04-03T23:59:48Z | 7890794 | 0.013563785 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.012640638 |
| 2026-04-05T23:59:48Z | 7905188 | 0.012693516 |
| 2026-04-06T23:59:48Z | 7912388 | 0.012991087 |
| 2026-04-07T23:59:48Z | 7919588 | 0.013023395 |
| 2026-04-08T23:59:48Z | 7926788 | 0.012848112 |
| 2026-04-09T23:59:48Z | 7933987 | 0.010937909 |
| 2026-04-10T23:59:48Z | 7941184 | 0.012648895 |
| 2026-04-11T23:59:48Z | 7948384 | 0.013120392 |
| 2026-04-12T23:59:48Z | 7955584 | 0.011893189 |
| 2026-04-13T23:59:48Z | 7962784 | 0.012088598 |
| 2026-04-14T23:59:48Z | 7969979 | 0.013341169 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.012556012 |
| 2026-04-16T23:59:48Z | 7984379 | 0.01209753 |
| 2026-04-17T23:59:48Z | 7991579 | 0.013074389 |
| 2026-04-18T23:59:48Z | 7998779 | 0.013512584 |
| 2026-04-19T23:59:48Z | 8005979 | 0.012158522 |
| 2026-04-20T23:59:48Z | 8013179 | 0.013215935 |
| 2026-04-21T23:59:48Z | 8020376 | 0.015262965 |
| 2026-04-22T23:59:48Z | 8027562 | 0.017115719 |
| 2026-04-23T23:59:48Z | 8034762 | 0.016384407 |
| 2026-04-24T23:59:48Z | 8041962 | 0.01599422 |
| 2026-04-25T23:59:48Z | 8049151 | 0.018118389 |
| 2026-04-26T23:59:48Z | 8056274 | 0.021777483 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.027428748 |
| 2026-04-28T23:59:48Z | 8070646 | 0.022380463 |
| 2026-04-29T23:59:48Z | 8077790 | 0.023489626 |
| 2026-04-30T23:59:48Z | 8084984 | 0.025662659 |
| 2026-05-01T23:59:48Z | 8092168 | 0.030631721 |
| 2026-05-02T23:59:48Z | 8099357 | 0.030166116 |
| 2026-05-03T16:10:00Z | 8104202 | 0.031897211 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

