# NetUID 116 — TaoLend (`ⴵ`)

## Overview

TaoLend is a decentralized lending protocol for the Bittensor ($TAO) ecosystem.It allows users to lend TAO with confidence while borrowers secure their loans using subnet ALPHA as collateral.By unlocking TAO liquidity and keeping ALPHA staked within the subnet, TaoLend strengthens both capital efficiency and network security.

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
- **`immunity_period` (blocks):** 360
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GgjJXbcDyiGenKGfPrPhRxJ7p91EdC22fcAAF4ccbATgu6H`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `360` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `1000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `500000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

### Prerequisites

Install NodeJS (latest LTS version) and PM2:

```bash

---

# Install build essentials

sudo apt install build-essential libssl-dev git

---

# Install NVM (Node Version Manager)

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
source ~/.bashrc

---

# Install NodeJS (latest LTS version)

nvm install --lts
nvm use --lts

---

# Install TypeScript and PM2

npm install -g typescript ts-node pm2
```

---

### Installation

Download code and install dependencies:

```bash

---

# Install Python dependencies

pip install -r requirement.txt
```

---

### Running Validator

Start validator with auto-upgrade:

```bash
pm2 start --name sn116-auto-upgrade python3 -- start_validator.py \
  --wallet.name <your_wallet_name> \
  --wallet.hotkey <your_hotkey>
```

**Parameters**:
- `--wallet.name`: Your Bittensor wallet name
- `--wallet.hotkey`: Your validator hotkey

**Monitoring**:
```bash


*README source used for excerpts: `https://raw.githubusercontent.com/xpenlab/taolend/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


TaoLend is a decentralized lending protocol for the Bittensor ($TAO) ecosystem.It allows users to lend TAO with confidence while borrowers secure their loans using subnet ALPHA as collateral.By unlocking TAO liquidity and keeping ALPHA staked within the subnet, TaoLend strengthens both capital efficiency and network security.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://taolend.io](https://taolend.io)
- **GitHub:** [https://github.com/xpenlab/taolend](https://github.com/xpenlab/taolend)
- **Discord:** [https://discord.gg/DNeq2fWCQW](https://discord.gg/DNeq2fWCQW)
- **Logo URL:** [https://raw.githubusercontent.com/xpenlab/taolend/logo/TaoLend.png](https://raw.githubusercontent.com/xpenlab/taolend/logo/TaoLend.png)
- **Contact:** elsieyy@taolend.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.004108288 |
| 8103738 | 0.004108381 |
| 8103786 | 0.004111606 |
| 8103834 | 0.004111706 |
| 8103882 | 0.004111792 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Taolend
- **Fetched from:** [https://taolend.io](https://taolend.io)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

