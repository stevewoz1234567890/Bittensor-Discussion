# NetUID 52 — Dojo (`ا`)

## Overview

**From crawled page (site or GitHub):** Contribute to tensorplex-labs/dojo development by creating an account on GitHub.

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
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.999999999
- **Owner SS58 (`owner_ss58`):** `5Fv1ZvNPsEvUN6jfia6Mv3ZoefZ6KdoowGMjkPMX61QwRLXx`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.999999999 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
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

## Miner

Miners do not need to spin up any server or code level things to mine! You just need to register to the network, and load your hotkey wallet onto a browser wallet e.g. Talisman and wait to receive tasks.
Start mining at [Testnet](https://testnet.dojo.network) | [Mainnet](https://dojo.network)

```bash

---

## Validator

Please refer the [setup guide](docs/validator.md).

---

### Git hooks (required)

This repo uses lefthook to enforce quality gates:

- pre-commit: make fmt, make vet, make lint
- pre-push: go test ./...
  Install and keep it current:
- make preflight
- lefthook install -f # force reinstall if hooks don’t run
- git config --get core.hooksPath (should be unset for default)


*README source used for excerpts: `https://raw.githubusercontent.com/tensorplex-labs/dojo/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


*Empty — no description bytes set in `SubnetIdentity`.*

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/tensorplex-labs/dojo](https://github.com/tensorplex-labs/dojo)
- **Contact:** jarvis@tensorplex.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.007225402 |
| 8103690 | 0.007225392 |
| 8103738 | 0.007225386 |
| 8103786 | 0.007225339 |
| 8103834 | 0.007225334 |
| 8103882 | 0.007225325 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** GitHub - tensorplex-labs/dojo · GitHub
- **Meta / og:description:** Contribute to tensorplex-labs/dojo development by creating an account on GitHub.
- **Fetched from:** [https://github.com/tensorplex-labs/dojo](https://github.com/tensorplex-labs/dojo)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

