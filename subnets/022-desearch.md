# NetUID 22 — Desearch (`χ`)

## Overview

Decentralized search engine

**From crawled page (site or GitHub):** AI-powered search APIs for web and Twitter/X data. Build intelligent agents with real-time search, semantic retrieval, and structured responses.

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
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5DFuaMasyQtPhXcsuoYEyJmCVSRtzKxsTKFTA4SrpcGXBxJn`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `10`
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

### For Miners

Miners contribute search capacity and are rewarded based on result quality and volume.
Expected setup steps:

- Prepare a server with Python ≥ 3.10, PM2, and a registered hotkey on netuid 22.
- Configure credentials for OpenAI, SerpAPI, and Apify.
- Declare per-search-type concurrency in `neurons/miners/manifest.json`.
- Run the axon with PM2.

See the [Miner Setup Guide](./docs/running_a_miner.md) for full instructions.

---

### For Validators

Validators verify miner outputs and write weights on-chain. Expected setup steps:

- Prepare a server with Python ≥ 3.10, PM2, Redis, `jq`, and a registered validator hotkey.
- Configure credentials for OpenAI, Apify, ScrapingDog, and W&B.
- Generate a public API access key and run the autoupdate script.

See the [Validator Setup Guide](./docs/running_a_validator.md) for full instructions.


*README source used for excerpts: `https://raw.githubusercontent.com/datura-ai/desearch/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Decentralized search engine

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://desearch.ai](https://desearch.ai)
- **GitHub:** [https://github.com/datura-ai/desearch](https://github.com/datura-ai/desearch)
- **Discord:** [https://discord.gg/P44zrJmdFy](https://discord.gg/P44zrJmdFy)
- **Logo URL:** [https://desearch.ai/assets/logo-icon-C18R0lAC.png](https://desearch.ai/assets/logo-icon-C18R0lAC.png)
- **Contact:** giga@desearch.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.004840561 |
| 8103690 | 0.00484055 |
| 8103738 | 0.004840545 |
| 8103786 | 0.004840521 |
| 8103834 | 0.004840418 |
| 8103882 | 0.004840409 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Desearch - AI Search APIs for Web and X Data
- **Meta / og:description:** AI-powered search APIs for web and Twitter/X data. Build intelligent agents with real-time search, semantic retrieval, and structured responses.
- **Fetched from:** [https://desearch.ai](https://desearch.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

