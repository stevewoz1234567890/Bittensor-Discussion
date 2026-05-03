# NetUID 122 — Bitrecs (`ⲅ`)

## Overview

Bitrecs is a novel recommendation engine built on the Bittensor network

**From crawled page (site or GitHub):** Next generation product recommendations

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.001000000
- **Owner SS58 (`owner_ss58`):** `5H6fAdf7QsrZpLKyydA1pM9sxTK7qJx4S4jUgg6YMHr4Xzqs`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.001000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `2`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

## Validator

See [Validator Setup](docs/validator_setup.md)

---

## Miner

See [Miner Setup](docs/miner_setup.md)


*README source used for excerpts: `https://raw.githubusercontent.com/bitrecs/bitrecs-v2/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Bitrecs is a novel recommendation engine built on the Bittensor network

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://bitrecs.ai](https://bitrecs.ai)
- **GitHub:** [https://github.com/bitrecs/bitrecs-v2](https://github.com/bitrecs/bitrecs-v2)
- **Discord:** [https://discord.gg/gWtKvytFma](https://discord.gg/gWtKvytFma)
- **Logo URL:** [https://www.bitrecs.ai/assets/logo/x7k9m2n8/whiteonblack.png](https://www.bitrecs.ai/assets/logo/x7k9m2n8/whiteonblack.png)
- **Contact:** support@bitrecs.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.003879461 |
| 8103738 | 0.00387945 |
| 8103786 | 0.003871805 |
| 8103834 | 0.003892037 |
| 8103882 | 0.003892018 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Bitrecs
- **Meta / og:description:** Next generation product recommendations
- **Fetched from:** [https://bitrecs.ai](https://bitrecs.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

