# NetUID 71 — Leadpoet (`ㄴ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Leadpoet** (NetUID **71**) (`ㄴ`).

Intent-driven AI for modern sales teams.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `58`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,006.377234670. **Alpha liquidity in pool (`alpha_in`)** = ‎979,652.340173102ف‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,730,877.135713789ف‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006080465`** *(also **moving-average price** `0.006109426496550441` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,091,559.056563715ف‎`. **Owner hotkey / coldkey (chain):** `5FNVgRnrxMibhcBGEAaajGrYjsaCn441a5HuGUBUNnxEBLo9` / `5DwHzMhBXPGPSSxnPzp3J8Y12UyYmU17nppQ8oHum6yrRjSk`.
- **Subnet registered at block:** `5048438` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎43.595094750ف‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ف‎` · α-in `‎0.000000000ف‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104377`
- **Liquidity constant `k`:** `5884161513906910539875846340`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Leadpoet` |
| Symbol (API) | `ㄴ` |
| Rank | `47` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.005611801` |
| Market cap | `22903263685064.592085321` |
| Market cap Δ 1d | `-10.016838273075668445` |
| Liquidity | `11494346612864` |
| Total τ | `5761037539411` |
| Total α | `4710296475886891` |
| α in pool | `1021652242025912` |
| α staked | `3059615729711609` |
| Price Δ 1h | `-2.468747441929741291` |
| Price Δ 1d | `-10.117216943281183881` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `71` |
| Owner SS58 (API) | `5DwHzMhBXPGPSSxnPzp3J8Y12UyYmU17nppQ8oHum6yrRjSk` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5048438` |
| Registration wall time | `2025-03-03T16:41:12.001Z` |
| Registration cost snapshot | `213408488702` |
| Active keys | `256` |
| Active validators | `6` |
| Active miners | `76` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `6` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Leadpoet | AI Sales Agents Powered by Bittensor

Leadpoet is Subnet 71, the decentralized AI sales agent subnet built on Bittensor. Leadpoet's vision is streamlining the top of sales funnel, starting with high-quality lead generation today and evolving into a fully automated sales engine where meetings with your ideal customers seamlessly appear on your calendar.

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 256 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 10000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5DwHzMhBXPGPSSxnPzp3J8Y12UyYmU17nppQ8oHum6yrRjSk` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `10000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `3` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

- - **Validators**: 64GB RAM, 8-core CPU, 100GB SSD, AWS Nitro Enclaves enabled instance
- `| **Fabricating dates** | Assigning `date.today()` when no date exists in the evidence | Games the recency score — stale content appears fresh |`
- `| Tier 1 | Industry, sub-industry, role, seniority, country, employee count, duplicate company | Free |`
- `| Tier 2 | Email format, name-in-email, domain age, MX/SPF/DMARC, DNSBL, TrueList verification, LinkedIn person verification, company verification, reputation score | API calls |`
- `| Tier 3 | Each intent signal URL scraped, snippet overlap verified, LLM evaluates relevance, time decay applied, peak-weighted aggregation | LLM + scraping |`


*Primary README URL used: `https://raw.githubusercontent.com/leadpoet/leadpoet/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://leadpoet.com](https://leadpoet.com)
- **GitHub:** [https://github.com/leadpoet/leadpoet](https://github.com/leadpoet/leadpoet)
- **Logo URL:** [https://leadpoet.com/leadpoet-social-logo.png](https://leadpoet.com/leadpoet-social-logo.png)
- **Contact:** hello@leadpoet.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.005574964 |
| 8104292 | 0.005684274 |
| 8104340 | 0.005829739 |
| 8104388 | 0.005852827 |
| 8104436 | 0.006080465 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.005319149 --> 0.009562605
    line [0.007827654, 0.008290273, 0.008450625, 0.00898045, 0.008443754, 0.008481292, 0.008266816, 0.009003767, 0.009269953, 0.009009186, 0.00912042236627, 0.008034367, 0.008482563, 0.008249245, 0.00861588, 0.00791444118379, 0.007545551, 0.007420394, 0.007704308, 0.007669532, 0.007593838, 0.007543326, 0.006917593, 0.007001793, 0.006865427, 0.006791903, 0.006919686, 0.007159706, 0.007128071, 0.007129729, 0.007059763, 0.00565516, 0.006560178, 0.007643724, 0.007668744, 0.007740932, 0.007892416, 0.007643786, 0.006905994, 0.007007362, 0.00685933, 0.007040358, 0.006842105, 0.006821782, 0.006908748, 0.006928578, 0.006709413, 0.006730757, 0.006476021, 0.00709632, 0.006829726, 0.006773221, 0.006637717, 0.006456193, 0.006328434, 0.005611801]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

