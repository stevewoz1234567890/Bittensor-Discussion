# NetUID 63 — Enigma (`س`)

## Overview

Breaking today to build tomorrow

**From crawled page (site or GitHub):** Decentralized deep tech. Innovation from everywhere. Quantum computing, AI, and decentralized networks powered by Bittensor.

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
- **`immunity_period` (blocks):** 4096
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CqTmNfgDchxULD1bfoz8jvj9rDYSoq76kiq98oBUUEDpWqX`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `4096` blocks
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

## Installation & Setup (Validator Only)

**Note**: Miner code is deprecated. Only validators are currently supported. The validator automatically sets weights to the treasury wallet.

---

### Prerequisites

- Python 3.12+
- PM2 (recommended)
- Git
- [Validator Compute Requirements](min_compute.yml)

---

### Quick Setup

```bash

---

# 3. Run the validator with PM2

pm2 start --interpreter .venv/bin/python --name enigma-validator neurons/validator.py -- --netuid 63 --logging.info --wallet.name <your_wallet_name> --wallet.hotkey <your_hotkey>
```

**Note**: Replace `<your_wallet_name>` and `<your_hotkey>` with your Bittensor wallet details (defaults to 'default' if not specified). For localnet testing, add `--subtensor.network local`.

---

### Choosing GPU Device

To bind the validator to a specific GPU, use the `--neuron.device` flag:

```bash
python neurons/validator.py --netuid 63 --logging.info --wallet.name <your_wallet_name> --wallet.hotkey <your_hotkey> --neuron.device cuda:0
```

This sets the validator to use only the specified device, and system metrics will reflect only that GPU. If not specified, it defaults to the first available GPU or CPU.

---

### Additional Setup

```bash
pip install -r requirements-dev.txt
```

Run Tests:
```bash
pytest .
```


*README source used for excerpts: `https://raw.githubusercontent.com/qbittensor-labs/enigma/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Breaking today to build tomorrow

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://www.qbittensorlabs.com/](https://www.qbittensorlabs.com/)
- **GitHub:** [https://github.com/qbittensor-labs/enigma](https://github.com/qbittensor-labs/enigma)
- **Discord (handle / invite hint):** `qbittensorlabs`
- **Logo URL:** [https://www.qbittensorlabs.com/63.png](https://www.qbittensorlabs.com/63.png)
- **Contact:** qbittensorlabs@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.008544734 |
| 8103690 | 0.008544716 |
| 8103738 | 0.008544705 |
| 8103786 | 0.008538928 |
| 8103834 | 0.008536651 |
| 8103882 | 0.008536634 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** qBitTensor Labs — Decentralized Deep Tech
- **Meta / og:description:** Decentralized deep tech. Innovation from everywhere. Quantum computing, AI, and decentralized networks powered by Bittensor.
- **Fetched from:** [https://www.qbittensorlabs.com/](https://www.qbittensorlabs.com/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

