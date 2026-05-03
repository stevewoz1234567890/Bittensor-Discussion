# NetUID 1 — Apex (`α`)

## Overview

Open competitions for algorithmic and agentic optimization

**From crawled page (site or GitHub):** Mining intelligence

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 256
- **Max validators allowed (`max_allowed_validators`):** 128
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 99
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5HCFWvRqzSHWRPecN7q8J6c7aKQnrCZTMHstPv39xL1wgDHh`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `1000000000000000000`)
- **`target_regs_per_interval`:** `2`
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

### [Miner Docs](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup)

See miner docs for an overview on the [Apex CLI](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup/apex-cli) and [incentive mechanism](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/incentive-mechanism).

---

### [Validator Docs](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/validating)

See validator docs for an overview on validator setup.

---

### [Current Competitions](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup/current-competitions)

**[RL Battleship](https://docs.macrocosmos.ai/subnets/subnet-1-apex/subnet-1-current-competitions#id-1.-reinforcement-learning-battleship)**: A strategy game competition in which miners compete to sink ships on a 10x10 grid in as few turns as possible, now with reinforcement learning. Miners train and submit models that compete in the game environment.

**[Iota Simulator](https://docs.macrocosmos.ai/subnets/subnet-1-apex/subnet-1-current-competitions#id-2.-iota-simulator)**: A distributed training simulation competition where miners submit routing and balancing algorithms that orchestrate activations across a network of heterogeneous nodes. Miners are scored on how efficiently their code moves forward and backward activations through layered pipelines under realistic conditions including node churn, variable latency, and bandwidth constraints.


*README source used for excerpts: `https://raw.githubusercontent.com/macrocosm-os/apex/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Open competitions for algorithmic and agentic optimization

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://apex.macrocosmos.ai](https://apex.macrocosmos.ai)
- **GitHub:** [https://github.com/macrocosm-os/apex](https://github.com/macrocosm-os/apex)
- **Discord (handle / invite hint):** `macrocrux`
- **Logo URL:** [https://www.macrocosmos.ai/images/mc_logo_black.png](https://www.macrocosmos.ai/images/mc_logo_black.png)
- **Contact:** support@macrocosmos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.010633687 |
| 8103690 | 0.010633671 |
| 8103738 | 0.010633663 |
| 8103786 | 0.010633632 |
| 8103834 | 0.010633626 |
| 8103882 | 0.010633612 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** APEX | Macrocosmos.ai
- **Meta / og:description:** Mining intelligence
- **Fetched from:** [https://apex.macrocosmos.ai](https://apex.macrocosmos.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

