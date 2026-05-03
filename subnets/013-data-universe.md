# NetUID 13 — Data Universe (`ν`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Data Universe** (NetUID **13**) (`ν`).

Scraping the world's social media data

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `0`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ23,339.271676398. **Alpha liquidity in pool (`alpha_in`)** = ‎2,991,253.541658200ν‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,050,970.968555086ν‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007803015`** *(also **moving-average price** `0.007840533275157213` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎950,522.644756815ν‎`. **Owner hotkey / coldkey (chain):** `5HBswBt1A9Ahx6U76abXXGd7VmabmCNBGhSK2vrP71GSxtgZ` / `5HBswBt1A9Ahx6U76abXXGd7VmabmCNBGhSK2vrP71GSxtgZ`.
- **Subnet registered at block:** `1907637` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎0.000000000ν‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ν‎` · α-in `‎0.000000000ν‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104435`
- **Liquidity constant `k`:** `69813679061748432242723163600`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Data Universe`
- **Symbol (API):** `ν`
- **Rank:** `28`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.007803058`
- **Market cap:** `36376910122290.578700744`
- **Market cap Δ 1d:** `-1.094199230214482085`
- **Liquidity:** `46680196554309`
- **Total τ:** `23339336641073`
- **Total α:** `5041991510213286`
- **α in pool:** `2991245216072496`
- **α staked:** `1670633514329172`
- **Price Δ 1h:** `-0.004638991621622314`
- **Price Δ 1d:** `-1.202201871661816499`
#### Subnet activity (TAOStats)

- **NetUID (API):** `13`
- **Owner SS58 (API):** `5HBswBt1A9Ahx6U76abXXGd7VmabmCNBGhSK2vrP71GSxtgZ`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `1907637`
- **Registration wall time:** `2023-12-11T19:24:48Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `240`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `12`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `596903`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

<picture>
    <source srcset="./assets/macrocosmos-white.png"  media="(prefers-color-scheme: dark)">
    <source srcset="./assets/macrocosmos-black.png"  media="(prefers-color-scheme: light)">
    <img src="macrocosmos-black.png">
</picture>

<div align="center">

# **Bittensor Subnet 13: Data Universe** <!-- omit in toc -->
[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---
</div>

---

# MUST READ: Miner Data Compliance Policy

By participating as a miner on Subnet 13, you are agreeing to adhere to our [Miner Policy](docs/miner_policy.md) below.
<details>
  <summary>
    Macrocosmos Miner Data Compliance Policy
  </summary>

---

*Version 1.0, March 2025*

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Data collection from billions of social media conversations. Access data from X, Reddit, and YouTube — ready for AI, analytics, research and brand and campaign monitoring.

**Fetched document title:** Data Universe | Macrocosmos.ai

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
- **`immunity_period` (blocks):** 12000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5HBswBt1A9Ahx6U76abXXGd7VmabmCNBGhSK2vrP71GSxtgZ`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `12000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `50`
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

# MUST READ: Miner Data Compliance Policy

By participating as a miner on Subnet 13, you are agreeing to adhere to our [Miner Policy](docs/miner_policy.md) below. 
<details>
  <summary>
    Macrocosmos Miner Data Compliance Policy
  </summary>

---

*Version 1.0, March 2025*

---

---

## **GDPR Guidance and Resources**

1. Overview of GDPR Requirements
    - The UK Information Commissioner's Office (ICO) provides a comprehensive guide to GDPR obligations, including lawful bases for processing, data minimization, and security requirements:
    - [ICO Guide to GDPR](https://ico.org.uk/media/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr-1-1.pdf)
2. Lawful Basis for Processing Data
    - Understand the six lawful bases for processing personal data as defined under GDPR:
    - [ICO Lawful Basis Guide](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/)
3. Transparency and Privacy Notices
    - Guidance on providing clear and accessible privacy notices to individuals:
    - [ICO Privacy Notice Checklist](https://ico.org.uk/media/for-organisations/documents/1625126/privacy-notice-checklist.pdf)
4. Handling Data Subject Rights
    - Information on responding to requests from individuals to access, rectify, or delete their personal data:
    - [ICO Individual Rights Guide](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/)
5. Data Security and Minimization
    - Best practices for securing personal data and ensuring data minimization:
    - [ICO Security Guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/security/a-guide-to-data-security/)
6. Reporting Data Breaches
    - Guidance on recognizing and reporting data breaches to the ICO within the required 72-hour window:
    - [ICO Guide to Data Breach Reporting](https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/)

---

## **General Resources**

1. UK GDPR Key Definitions
    - A quick reference guide to key GDPR definitions and principles:
    - [ICO Key Definitions](https://ico.org.uk/for-organisations/guide-to-eidas/key-definitions/)
2. Data Protection Impact Assessments (DPIAs)
    - Information on when and how to conduct a DPIA for high-risk data processing activities:
    - [ICO DPIA Guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/)
3. FAQs on GDPR Compliance
    - Practical answers to common GDPR compliance questions:
    - [GDPR FAQs from the European Data Protection Board](https://edpb.europa.eu/our-work-tools/our-documents/faqs_en)

---

## Miner Credibility

Validators remain suspicious of Miners and so they periodically check a sample of data from each Miner's MinerIndex, to verify the data correctness. The Validator uses these checks to track a Miner's credibility, which it then uses to scale a Miner's score. The scaling is done in such a way that it is **always** worse for a Miner to misrepresent what types and how much data it has.

---

#### CPU / GPU / RAM lines (automatic grep)

- Data Universe was built from the ground-up with a focus on decentralization and scalability. There is no centralized entity that controls the data; the data is stored across all Miners on the network, and is queryable via the Validators. At launch, Data Universe is able to support up to 50 Petabytes of data across 200 miners, while only requiring ~10GB of storage on the Validator.

---

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- Miners do not require a GPU and should be able to run on a low-tier machine, as long as it has sufficient network bandwidth and disk space. Must have python >= 3.10.

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- Validators require at least 32 GB of RAM but do not require a GPU. We recommend a decent CPU (4+ cores) and sufficient network bandwidth to handle protocol traffic. Must have python >= 3.10.

---

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- Miners do not require a GPU and should be able to run on a low-tier machine, as long as it has sufficient network bandwidth and disk space. Must have python >= 3.10.

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- Validators require at least 32 GB of RAM but do not require a GPU. We recommend a decent CPU (4+ cores) and sufficient network bandwidth to handle protocol traffic. Must have python >= 3.10.


*Primary README URL used: `https://raw.githubusercontent.com/macrocosm-os/data-universe/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.macrocosmos.ai/gravity](https://www.macrocosmos.ai/gravity)
- **GitHub:** [https://github.com/macrocosm-os/data-universe](https://github.com/macrocosm-os/data-universe)
- **Discord (handle / invite hint):** `macrocrux`
- **Logo URL:** [https://www.macrocosmos.ai/images/mc_logo_black.png](https://www.macrocosmos.ai/images/mc_logo_black.png)
- **Contact:** support@macrocosmos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.007803059 |
| 8104244 | 0.007803044 |
| 8104292 | 0.007803035 |
| 8104340 | 0.007803019 |
| 8104388 | 0.007803018 |
| 8104436 | 0.007803015 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

