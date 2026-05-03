# NetUID 71 — Leadpoet (`ㄴ`)

## Overview

Intent-driven AI for modern sales teams.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

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

## Miner / validator compute notes (README excerpts)

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

## Installation

```bash

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

**Size Limit:** Model tarball must be under **200KB**. Submissions exceeding this limit will be rejected.

**Required Function:**
```python
def find_leads(icp: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Find a lead matching the ICP's natural language prompt.
    
    Config is injected in icp["_config"]:
        - SUPABASE_URL, SUPABASE_ANON_KEY - Database credentials
        - QUALIFICATION_LEADS_TABLE - Table name (use "test_leads_for_miners" for local testing)
        - PROXY_URL - For paid API calls (e.g., "http://localhost:8001")
    
    Returns: Dict with lead_id + 14 fields + intent_signals list, or None
    """
    config = icp.get("_config", {})
    supabase_url = config.get("SUPABASE_URL")
    table_name = config.get("QUALIFICATION_LEADS_TABLE")
    proxy_url = config.get("PROXY_URL")
    # ... your logic ...
```

**Paid API Calls (via Proxy):**
```python

---

### Fulfillment Request Schema (What Miners See)

When a client submits a request, miners receive an ICP with this structure:

```json
{
  "prompt": "VP of Sales and Heads of Revenue at Series A-C SaaS companies in the US showing signals of evaluating outbound sales tools, hiring SDRs, or researching competitors.",
  "industry": "Software",
  "sub_industry": "SaaS",
  "target_role_types": ["Sales", "Business Development"],
  "target_roles": ["VP of Sales", "Head of Revenue", "Director of Sales"],
  "target_seniority": "VP",
  "employee_count": "50-500",
  "company_stage": "Series A",
  "geography": "United States",
  "country": "United States",
  "product_service": "outbound sales automation platform",
  "intent_signals": ["hiring SDRs", "evaluating sales tools", "researching competitors"],
  "num_leads": 2
}
```

- `prompt` — Natural language description of the ideal lead. Your model should interpret this.
- `target_roles` — Exact role titles the client wants. Your lead's `role` must match one of these (fuzzy matching is applied, e.g. "VP, Corporate Sales" matches "VP of Sales").
- `target_seniority` — Required seniority level.
- `intent_signals` — The types of buying signals the client cares about. Find real evidence for these.
- `num_leads` — How many winning leads the client wants. Only the top N by score earn rewards.

---

### Auditor Validator

For validators who want to run a lightweight alternative that copies TEE-verified weights from the primary validator:

```bash
python neurons/auditor_validator.py \
   …


*README source used for excerpts: `https://raw.githubusercontent.com/leadpoet/leadpoet/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

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
| 8103642 | 0.006153165 |
| 8103690 | 0.006019587 |
| 8103738 | 0.005988231 |
| 8103786 | 0.005979134 |
| 8103834 | 0.005951897 |
| 8103882 | 0.005771609 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

