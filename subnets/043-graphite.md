# NetUID 43 — Graphite (`ע`)

## Overview

**From crawled page (site or GitHub):** Awesome repository for Bittensor's Subnet 43. Join us in graphing the future. - GraphiteAI/Graphite-Subnet

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.100000000
- **Owner SS58 (`owner_ss58`):** `5HjMs5JDrLH3Hknmfm1gDq7nFYAv6M7t9v3EWMctSRXJS9HC`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.100000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
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

## Installation 🛠️

Here at Graphite, we aim to make the installation process as seamless as possible, regardless of your technical knowledge. To get you started, we have crafted step-by-step guides and tutorials:

- Basic Installation Guide: [Installation Guide](./docs/installation.md)
- For Miners: [Miner Installation Guide](./docs/miner.md)
- For Validators: [Validator Installation Guide](./docs/validator.md)


*README source used for excerpts: `https://raw.githubusercontent.com/GraphiteAI/Graphite-Subnet/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


*Empty — no description bytes set in `SubnetIdentity`.*

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/GraphiteAI/Graphite-Subnet](https://github.com/GraphiteAI/Graphite-Subnet)
- **Contact:** team@graphite-ai.net

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.006338933 |
| 8103690 | 0.006338921 |
| 8103738 | 0.006338914 |
| 8103786 | 0.006338887 |
| 8103834 | 0.006338923 |
| 8103882 | 0.006339011 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** GitHub - GraphiteAI/Graphite-Subnet: Awesome repository for Bittensor's Subnet 43. Join us in graphing the future. · GitHub
- **Meta / og:description:** Awesome repository for Bittensor's Subnet 43. Join us in graphing the future. - GraphiteAI/Graphite-Subnet
- **Fetched from:** [https://github.com/GraphiteAI/Graphite-Subnet](https://github.com/GraphiteAI/Graphite-Subnet)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

