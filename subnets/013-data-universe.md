# NetUID 13 — Data Universe (`ν`)

## Overview

**Data Universe** (NetUID **13**) (`ν`).

Scraping the world's social media data

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `141`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ23,339.336223517. **Alpha liquidity in pool (`alpha_in`)** = ‎2,991,245.269585396ν‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,050,759.240627890ν‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007803058`** *(also **moving-average price** `0.007842969382181764` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎950,522.580209696ν‎`. **Owner hotkey / coldkey (chain):** `5HBswBt1A9Ahx6U76abXXGd7VmabmCNBGhSK2vrP71GSxtgZ` / `5HBswBt1A9Ahx6U76abXXGd7VmabmCNBGhSK2vrP71GSxtgZ`.
- **Subnet registered at block:** `1907637` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎106.514763810ν‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ν‎` · α-in `‎0.000000000ν‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.007803058`
- **Market cap:** `36376910122290.578700744`
- **Liquidity:** `46680196554309`
- **Total τ:** `23339336641073`
- **Total α:** `5041991510213286`
- **α in pool:** `2991245216072496`
- **α staked:** `1670633514329172`
- **Price Δ 1h:** `-0.004638991621622314`
- **Price Δ 1d:** `-1.202201871661816499`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `240`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `596903`

### On-chain declared purpose *(SubnetIdentity)*

Scraping the world's social media data

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

## Operational parameters — registration, limits, economics (chain)


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
- **Registration recycle cost snapshot (`burn`):** τ0.000577674
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

## On-chain identity — description


Scraping the world's social media data

## On-chain identity — additional field


*Unset.*

## Registered contact & links


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
| 8103976 | 0.007803415 |
| 8104024 | 0.007803412 |
| 8104072 | 0.007803079 |
| 8104120 | 0.007803075 |
| 8104168 | 0.00780307 |
| 8104216 | 0.007803058 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.010238023 |
| 2026-03-10T23:59:48Z | 7718257 | 0.009712034 |
| 2026-03-11T23:59:48Z | 7725455 | 0.009933652 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.01003077 |
| 2026-03-13T23:59:48Z | 7739841 | 0.009908343 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.009710704 |
| 2026-03-15T23:59:48Z | 7754226 | 0.009249894 |
| 2026-03-16T23:59:48Z | 7761426 | 0.009079805 |
| 2026-03-17T23:59:48Z | 7768619 | 0.008897834 |
| 2026-03-18T23:59:48Z | 7775819 | 0.008795534 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00866789208054410662 |
| 2026-03-20T23:59:48Z | 7790201 | 0.008651207 |
| 2026-03-21T23:59:48Z | 7797398 | 0.009001115 |
| 2026-03-22T23:59:48Z | 7804598 | 0.008723413 |
| 2026-03-23T23:59:48Z | 7811798 | 0.008913305 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00876715279582959213 |
| 2026-03-25T23:59:48Z | 7826196 | 0.0087994 |
| 2026-03-26T23:59:48Z | 7833396 | 0.008936906 |
| 2026-03-27T23:59:48Z | 7840596 | 0.00875357 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.00871684 |
| 2026-03-29T23:59:48Z | 7854902 | 0.008495857 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.008609917 |
| 2026-03-31T23:59:48Z | 7869291 | 0.008550431 |
| 2026-04-01T23:59:48Z | 7876474 | 0.00857853 |
| 2026-04-02T23:59:48Z | 7883622 | 0.008449399 |
| 2026-04-03T23:59:48Z | 7890794 | 0.008443536 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.008435406 |
| 2026-04-05T23:59:48Z | 7905188 | 0.008418459 |
| 2026-04-06T23:59:48Z | 7912388 | 0.008431973 |
| 2026-04-07T23:59:48Z | 7919588 | 0.008352981 |
| 2026-04-08T23:59:48Z | 7926788 | 0.008325812 |
| 2026-04-09T23:59:48Z | 7933987 | 0.008182509 |
| 2026-04-10T23:59:48Z | 7941184 | 0.008108775 |
| 2026-04-11T23:59:48Z | 7948384 | 0.008327366 |
| 2026-04-12T23:59:48Z | 7955584 | 0.008454186 |
| 2026-04-13T23:59:48Z | 7962784 | 0.008191422 |
| 2026-04-14T23:59:48Z | 7969979 | 0.008260859 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.008198765 |
| 2026-04-16T23:59:48Z | 7984379 | 0.008308937 |
| 2026-04-17T23:59:48Z | 7991579 | 0.008078726 |
| 2026-04-18T23:59:48Z | 7998779 | 0.007976433 |
| 2026-04-19T23:59:48Z | 8005979 | 0.007991795 |
| 2026-04-20T23:59:48Z | 8013179 | 0.008077406 |
| 2026-04-21T23:59:48Z | 8020376 | 0.008052432 |
| 2026-04-22T23:59:48Z | 8027562 | 0.008025754 |
| 2026-04-23T23:59:48Z | 8034762 | 0.008068171 |
| 2026-04-24T23:59:48Z | 8041962 | 0.008256332 |
| 2026-04-25T23:59:48Z | 8049151 | 0.008182952 |
| 2026-04-26T23:59:48Z | 8056274 | 0.008224318 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.008110138 |
| 2026-04-28T23:59:48Z | 8070646 | 0.007955307 |
| 2026-04-29T23:59:48Z | 8077790 | 0.007904234 |
| 2026-04-30T23:59:48Z | 8084984 | 0.007994681 |
| 2026-05-01T23:59:48Z | 8092168 | 0.007980863 |
| 2026-05-02T23:59:48Z | 8099357 | 0.007897901 |
| 2026-05-03T16:10:00Z | 8104202 | 0.007803058 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

