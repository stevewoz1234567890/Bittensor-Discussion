# NetUID 18 — Zeus (`σ`)

## Overview

Pushing weather forecasts beyond state-of-the-art

Powered by Ørpheus AI

**From crawled page (site or GitHub):** Orpheus AI is a company that operates at the intersection of weather and energy markets.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 257
- **`subnetwork_n`:** 257
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 65535
- **Registration recycle cost snapshot (`burn`):** τ0.999999999
- **Owner SS58 (`owner_ss58`):** `5DHwWLjtpwnZQUQKKXE2N5Gdy2N8PpqhgjLUuzgSB7yuGZkF`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.999999999 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `65535` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `5`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

No matching README sections were auto-detected for [https://github.com/Orpheus-AI/Zeus](https://github.com/Orpheus-AI/Zeus). Open the repository for miner/validator machine requirements, dependencies, and cloud sizing.

## On-chain identity — description


Pushing weather forecasts beyond state-of-the-art

## On-chain identity — additional field


Powered by Ørpheus AI

## Registered contact & links


- **Website:** [https://www.zeussubnet.com/](https://www.zeussubnet.com/)
- **GitHub:** [https://github.com/Orpheus-AI/Zeus](https://github.com/Orpheus-AI/Zeus)
- **Discord (handle / invite hint):** `wouter_orpheusai`
- **Logo URL:** [https://raw.githubusercontent.com/Orpheus-AI/Zeus/refs/heads/main/static/zeus-icon.png](https://raw.githubusercontent.com/Orpheus-AI/Zeus/refs/heads/main/static/zeus-icon.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.006544672 |
| 8103690 | 0.006544657 |
| 8103738 | 0.006544649 |
| 8103786 | 0.006544498 |
| 8103834 | 0.006544493 |
| 8103882 | 0.006544479 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Orpheus AI
- **Meta / og:description:** Orpheus AI is a company that operates at the intersection of weather and energy markets.
- **Fetched from:** [https://www.zeussubnet.com/](https://www.zeussubnet.com/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

