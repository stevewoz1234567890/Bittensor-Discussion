# NetUID 13 — Data Universe (`ν`)

## Overview

Scraping the world's social media data

**From crawled page (site or GitHub):** Data collection from billions of social media conversations. Access data from X, Reddit, and YouTube — ready for AI, analytics, research and brand and campaign monitoring.

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 12000
- **Registration recycle cost snapshot (`burn`):** τ0.000619173
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

## Miner / validator compute notes (README excerpts)

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

## Miner Credibility

Validators remain suspicious of Miners and so they periodically check a sample of data from each Miner's MinerIndex, to verify the data correctness. The Validator uses these checks to track a Miner's credibility, which it then uses to scale a Miner's score. The scaling is done in such a way that it is **always** worse for a Miner to misrepresent what types and how much data it has.


*README source used for excerpts: `https://raw.githubusercontent.com/macrocosm-os/data-universe/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Scraping the world's social media data

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://www.macrocosmos.ai/gravity](https://www.macrocosmos.ai/gravity)
- **GitHub:** [https://github.com/macrocosm-os/data-universe](https://github.com/macrocosm-os/data-universe)
- **Discord (handle / invite hint):** `macrocrux`
- **Logo URL:** [https://www.macrocosmos.ai/images/mc_logo_black.png](https://www.macrocosmos.ai/images/mc_logo_black.png)
- **Contact:** support@macrocosmos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.007803605 |
| 8103690 | 0.007803595 |
| 8103738 | 0.007803484 |
| 8103786 | 0.007803438 |
| 8103834 | 0.007803432 |
| 8103882 | 0.007803422 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Data Universe | Macrocosmos.ai
- **Meta / og:description:** Data collection from billions of social media conversations. Access data from X, Reddit, and YouTube — ready for AI, analytics, research and brand and campaign monitoring.
- **Fetched from:** [https://www.macrocosmos.ai/gravity](https://www.macrocosmos.ai/gravity)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

