# NetUID 68 — NOVA (`ظ`)

## Overview

Accelerating drug discovery.

**From crawled page (site or GitHub):** METANOVA LABS is a crypto-native biotech company at the forefront of drug discovery. We are developing next generation therapeutics that regulate mental states and restore critical biological processes.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 64
- **`subnetwork_n`:** 64
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.164271046
- **Owner SS58 (`owner_ss58`):** `5EcdJLAeYoxM3Tsf5VZ3NQPenPku218gqnjSoo3iJNy4V12V`

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
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `1`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

## System Requirements for validators

- Ubuntu 24.04 LTS (recommended)
- Python 3.10 - 3.12
- CUDA 12.6 (for GPU support)
- Sufficient RAM for ML model operations
- 2 GPU devices for parallel inference. If only one is available, inference will run sequentially which may result in delayed/missing scoring rounds.
- Internet connection for network participation

---

## Installation and Running

1. Clone the repository:
```bash
git clone --recurse-submodules https://github.com/metanova-labs/nova.git
cd nova
```

2. Prepare your .env file as in example.env:
```

---

# GitHub configs - FOR MINERS

GITHUB_REPO_NAME="repo-name"
GITHUB_REPO_BRANCH="repo-branch"
GITHUB_REPO_OWNER="repo-owner"
GITHUB_REPO_PATH="" # path within repo or ""

---

# For validators

VALIDATOR_API_KEY="your_api_key"
AUTO_UPDATE="1" # Set to "0" to disable auto-updates (not recommended)
```

3. Install dependencies:
   ```bash
   ./install_deps.sh [--cuda <version>]  #cuda version is optional, default is 12.6
   ```

4. Run:
```bash

---

# miner:

python3 neurons/miner.py --wallet.name <your_wallet> --wallet.hotkey <your_hotkey> --logging.info

---

# validator:

python3 neurons/validator/validator.py --wallet.name <your_wallet> --wallet.hotkey <your_hotkey> --logging.debug
```

---

## For Validators

DM the NOVA team to obtain an API key.


*README source used for excerpts: `https://raw.githubusercontent.com/metanova-labs/nova/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Accelerating drug discovery.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://www.metanova-labs.ai](https://www.metanova-labs.ai)
- **GitHub:** [https://github.com/metanova-labs/nova/](https://github.com/metanova-labs/nova/)
- **Logo URL:** [https://raw.githubusercontent.com/metanova-labs/nova/refs/heads/main/assets/subnet-logo.png](https://raw.githubusercontent.com/metanova-labs/nova/refs/heads/main/assets/subnet-logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.018138764 |
| 8103690 | 0.018141308 |
| 8103738 | 0.018141555 |
| 8103786 | 0.018141721 |
| 8103834 | 0.018141736 |
| 8103882 | 0.018135701 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Metanova Labs
- **Meta / og:description:** METANOVA LABS is a crypto-native biotech company at the forefront of drug discovery. We are developing next generation therapeutics that regulate mental states and restore critical biological processes.
- **Fetched from:** [https://www.metanova-labs.ai](https://www.metanova-labs.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

