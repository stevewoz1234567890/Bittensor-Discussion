# NetUID 77 — Liquidity (`ه`)

## Overview

Supply liquidity on external chains via uniswap, incentivize any project

**From crawled page (site or GitHub):** Incentivizing $289,037.21 worth of liquidity on chain via Bittensor

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
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GxxsUeYRyJSJKCuPeG1jZZiCummHJttmTNsfgDRSfxVnhGi`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
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

### Validator (`validator/index.ts`)

- **Weight Fetching**: Retrieves calculated weights from the server
- **On-chain Updates**: Sets miner weights on the Bittensor network
- **Version Management**: Includes automatic version checking and update capabilities

---

# Fill in the required variables (see Environment section below)

```

3. **Query current pool weights**

```bash
bun run pools
```

---

### ⚡ Validators

Validators read weights from the server and periodically push them to subnet 77.

**What you can do:**
- **Run weight calculation**: Process votes and compute final miner weights
- **Submit weights to subnet**: Push calculated weights to the Bittensor network
- **Monitor system health**: Track voting patterns and pool performance

**Key commands:**
```bash

---

# Start the validator (processes votes and submits weights)

just validate

---

# Run in test mode (compute weights but skip submission)

TEST_MODE=true just validate

---

### ⛏️ Miners

Miners provide liquidity to pools and can register their addresses to participate in the system.

**What you can do:**
- **Register your address**: Link your Bittensor public key to an EVM address
- **Provide liquidity**: Add liquidity to pools to earn rewards
- **Monitor earnings**: Track your pool performance and rewards

**Key commands:**
```bash

---

# VALIDATOR ONLY: used to fetch uniswap v3 LP positions for miners

THEGRAPH_API_KEY=

---

# VALIDATOR ONLY: set to 'true' to run in test mode (weights saved to files, not submitted to network)

TEST_MODE=false

---

# VALIDATOR ONLY: OPT-IN: will automatically git pull when a new minor version is live

AUTO_UPDATE_ENABLED=false
```

*Everything else has sensible defaults or is only required for specific tasks.*

---

### Obtaining required API keys

• **The Graph**: Log in to [Subgraph Studio](https://thegraph.com/studio/apikeys/) → **API Keys** in the sidebar → *Create API Key* → copy the generated token. See the official guide for details ([docs](https://thegraph.com/docs/en/subgraphs/querying/managing-api-keys/)).


*README source used for excerpts: `https://raw.githubusercontent.com/creativebuilds/sn77/master/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Supply liquidity on external chains via uniswap, incentivize any project

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://sn77.xyz](https://sn77.xyz)
- **GitHub:** [https://github.com/creativebuilds/sn77](https://github.com/creativebuilds/sn77)
- **Discord (handle / invite hint):** `CreativeBuilds`
- **Logo URL:** [https://sn77.xyz/assets/Logo.svg](https://sn77.xyz/assets/Logo.svg)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.004168869 |
| 8103690 | 0.004168861 |
| 8103738 | 0.004168857 |
| 8103786 | 0.004168823 |
| 8103834 | 0.00416882 |
| 8103882 | 0.004168809 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** SN77 - Liquidity
- **Meta / og:description:** Incentivizing $289,037.21 worth of liquidity on chain via Bittensor
- **Fetched from:** [https://sn77.xyz](https://sn77.xyz)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

