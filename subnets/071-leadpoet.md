# NetUID 71 — Leadpoet (`ㄴ`)

## Overview

Intent-driven AI for modern sales teams.

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
- **`immunity_period` (blocks):** 10000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5DwHzMhBXPGPSSxnPzp3J8Y12UyYmU17nppQ8oHum6yrRjSk`

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
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Hardware Requirements

- **Validators**: 64GB RAM, 8-core CPU, 100GB SSD, AWS Nitro Enclaves enabled instance
- **Miners**: Variable depending on your model — no strict minimum
- **Network**: Stable internet connection

---

### Software Requirements

- Python 3.9 - 3.12       
- Bittensor CLI: `pip install bittensor>=9.10`
- Bittensor Wallet: `btcli wallet create`

---

### For Miners

Miners choose their own tools and APIs for sourcing leads. Common examples include web scraping APIs (ScrapingDog, Firecrawl), LLMs (OpenRouter), and search APIs — but miners are free to use any approach (that is in compliance with out ToS).

For **qualification models**, paid API calls (LLM, ScrapingDog) go through the validator's proxy which injects keys server-side. Your model never needs API keys directly.

---

### For Validators

**TIP**: Copy `env.example` to `.env` and fill in your API keys for easier configuration.

```bash

---

#    - Environment: "live"

export COMPANIES_HOUSE_API_KEY="your_companies_house_key"

```

See [`env.example`](env.example) for complete configuration template.

---

## Installation

```bash

---

# 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

---

# 3. Install the packages

pip install --upgrade pip
pip install -e .

```

---

### How Miners Work

1. **Continuous Sourcing**: Actively search for new prospects
2. **Secure Submission**: Get pre-signed S3 URL, hash lead data, sign with private key, and upload
3. **Consensus Validation**: Prospects validated by multiple validators using commit/reveal protocol
4. **Approved Leads**: Only consensus-approved leads enter the main lead pool

---

### Lead Requirements

**Email Quality:**
- **Only "Valid" emails accepted** - Catch-all, invalid, and unknown emails will be rejected
- **No general purpose emails** - Addresses like hello@, info@, team@, support@, contact@ are not accepted
- **Proper email format required** - Must follow standard `name@domain.com` structure

**Name-Email Matching:**

Contact's first or last name must appear in the email address. We accept 26 common patterns plus partial matches to ensure quality while capturing the majority of legitimate business emails:

**Starting with first name:**
```
johndoe, john.doe, john_doe, john-doe
johnd, john.d, john_d, john-d
jdoe, j.doe, j_doe, j-doe
```

**Starting with last name:**
```
doejohn, doe.john, doe_john, doe-john
doej, doe.j, doe_j, doe-j
djohn, d.john, d_john, d-john
```

**Single tokens:**
```
john, doe
```

These strict requirements at initial go-live demonstrate our dedication to quality leads, while still capturing majority of good emails.

---

### Reward System

Miners earn rewards based on the **quality and validity** of leads they submit, with rewards weighted entirely by a rolling 30-epoch history to incentivize consistent long-term quality:

**How It Works:**
1. Each epoch, validators receive leads to validate
2. Validators run automated checks on all leads (email verification, domain checks, LinkedIn validation, reputation scoring)
3. Each validator calculates weights proportionally: miners who submitted **VALID** (approved) leads receive rewards
4. Rewards are weighted by each lead's reputation score (0-48 points: domain history, regulatory filings, and press coverage)
5. Formula: `miner_reward ∝ Σ(rep_score for all approved leads from that miner)`

**Example:** If Miner A submitted 3 valid leads (scores: 10, 15, 12) and Miner B submitted 2 valid leads (scores: 8, 20), then:
- Miner A total: 37 points
- Miner B total: 28 points
- Weights distributed proportionally: 57% to Miner A, 43% to Miner B

---

## Qualification Model System (Lead Curation)

In addition to sourcing leads, miners can submit **qualification models** - AI/ML models that curate leads from the approved lead pool based on Ideal Customer Profiles (ICPs).

---

### Qualification Model Requirements

Your model must follow these **strict requirements**:

---

# Get a specific day's ICPs

resp = requests.get(url, headers=headers, params={"select": "*", "set_id": "eq.20260311"})
```

Each row contains `set_id`, `active_from`, `active_until`, and the full `icps` array (100 ICP prompts with industry, geography, target roles, intent signals, etc.). Active ICP sets are never exposed.

---

### Model Requirements (Quick Reference)

**File Structure:**
```
your_model/
├── qualify.py          # Required: must contain find_leads() or qualify()
└── requirements.txt    # Optional: additional dependencies
```

**Size Limit:** Model tarball must be under **200KB**. Submissions exceeding…

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- - **Validators**: 64GB RAM, 8-core CPU, 100GB SSD, AWS Nitro Enclaves enabled instance
- `| **Fabricating dates** | Assigning `date.today()` when no date exists in the evidence | Games the recency score — stale content appears fresh |`
- `| Tier 1 | Industry, sub-industry, role, seniority, country, employee count, duplicate company | Free |`
- `| Tier 2 | Email format, name-in-email, domain age, MX/SPF/DMARC, DNSBL, TrueList verification, LinkedIn person verification, company verification, reputation score | API calls |`
- `| Tier 3 | Each intent signal URL scraped, snippet overlap verified, LLM evaluates relevance, time decay applied, peak-weighted aggregation | LLM + scraping |`


*Primary README URL used: `https://raw.githubusercontent.com/leadpoet/leadpoet/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Intent-driven AI for modern sales teams.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://leadpoet.com](https://leadpoet.com)
- **GitHub:** [https://github.com/leadpoet/leadpoet](https://github.com/leadpoet/leadpoet)
- **Logo URL:** [https://leadpoet.com/leadpoet-social-logo.png](https://leadpoet.com/leadpoet-social-logo.png)
- **Contact:** hello@leadpoet.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.005923718 |
| 8103891 | 0.005715259 |
| 8103939 | 0.005762323 |
| 8103987 | 0.005767028 |
| 8104035 | 0.005772646 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

