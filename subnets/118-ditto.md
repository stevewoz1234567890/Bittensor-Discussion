# NetUID 118 — Ditto (`ⲁ`)

## Overview

Open-Source Claude Cowork

The Ditto Agent OS and Harness enable SOTA memory, healing, and speed for 1/100th of the frontier cost.

**From crawled page (site or GitHub):** The smart home for your agents. Ditto organizes the context your AI needs and operationalizes it across every thread, tool, and workflow.

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
- **`immunity_period` (blocks):** 300
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5DUJfND9r2BjiJHNKSxJxzT7ptrxiseFe1GxeMwcTov52Y55`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `300` blocks
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

No matching README sections were auto-detected for [https://github.com/orgs/ditto-assistant/repositories](https://github.com/orgs/ditto-assistant/repositories). Open the repository for miner/validator machine requirements, dependencies, and cloud sizing.

## On-chain identity — description


Open-Source Claude Cowork

## On-chain identity — additional field


The Ditto Agent OS and Harness enable SOTA memory, healing, and speed for 1/100th of the frontier cost.

## Registered contact & links


- **Website:** [https://heyditto.ai](https://heyditto.ai)
- **GitHub:** [https://github.com/orgs/ditto-assistant/repositories](https://github.com/orgs/ditto-assistant/repositories)
- **Discord:** [https://discord.gg/qNKYZEMpkD](https://discord.gg/qNKYZEMpkD)
- **Logo URL:** [https://f005.backblazeb2.com/file/ditto-assets/ditto-logo.png](https://f005.backblazeb2.com/file/ditto-assets/ditto-logo.png)
- **Contact:** peyton@omniaura.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.007276984 |
| 8103738 | 0.007311324 |
| 8103786 | 0.007259702 |
| 8103834 | 0.007306319 |
| 8103882 | 0.007320868 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Ditto
- **Meta / og:description:** The smart home for your agents. Ditto organizes the context your AI needs and operationalizes it across every thread, tool, and workflow.
- **Fetched from:** [https://heyditto.ai](https://heyditto.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

