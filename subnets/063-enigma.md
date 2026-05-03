# NetUID 63 — Enigma (`س`)

## Overview

**Enigma** (NetUID **63**) (`س`).

Breaking today to build tomorrow

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `253`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ14,786.084636934. **Alpha liquidity in pool (`alpha_in`)** = ‎1,736,427.775095012س‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,123,275.165669289س‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008594358`** *(also **moving-average price** `0.008695611963048577` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,130,208.344382117س‎`. **Owner hotkey / coldkey (chain):** `5GmpedVP2r9haksUBD743wek8t89jMz96RTkV2zkVdRR4e1B` / `5CqTmNfgDchxULD1bfoz8jvj9rDYSoq76kiq98oBUUEDpWqX`.
- **Subnet registered at block:** `4885578` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎190.608690818س‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000س‎` · α-in `‎0.000000000س‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.008594529`
- **Market cap:** `35975960946011.839009071`
- **Liquidity:** `29709863504847`
- **Total τ:** `14786235677252`
- **Total α:** `4859627940764301`
- **α in pool:** `1736410200907462`
- **α staked:** `2449503994740937`
- **Price Δ 1h:** `0.678241882335300933`
- **Price Δ 1d:** `-5.622298297100156207`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Breaking today to build tomorrow

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

<img src="./logo.png"/>

# **Enigma** (SN 63) <!-- omit in toc -->
[![Discord Chat](https://img.shields.io/discord/1395424987816661103)](https://discord.gg/Gfr2mhft)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Decentralized deep tech. Innovation from everywhere. Quantum computing, AI, and decentralized networks powered by Bittensor.

**Fetched document title:** qBitTensor Labs — Decentralized Deep Tech

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

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

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

# 1. Create and activate virtual environment

python3 -m venv .venv
source .venv/bin/activate

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

---

#### CPU / GPU / RAM lines (automatic grep)

- To bind the validator to a specific GPU, use the `--neuron.device` flag:
- python neurons/validator.py --netuid 63 --logging.info --wallet.name <your_wallet_name> --wallet.hotkey <your_hotkey> --neuron.device cuda:0
- This sets the validator to use only the specified device, and system metrics will reflect only that GPU. If not specified, it defaults to the first available GPU or CPU.


*Primary README URL used: `https://raw.githubusercontent.com/qbittensor-labs/enigma/main/README.md`*

## On-chain identity — description


Breaking today to build tomorrow

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.qbittensorlabs.com/](https://www.qbittensorlabs.com/)
- **GitHub:** [https://github.com/qbittensor-labs/enigma](https://github.com/qbittensor-labs/enigma)
- **Discord (handle / invite hint):** `qbittensorlabs`
- **Logo URL:** [https://www.qbittensorlabs.com/63.png](https://www.qbittensorlabs.com/63.png)
- **Contact:** qbittensorlabs@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.008483975 |
| 8104133 | 0.008603135 |
| 8104181 | 0.008594533 |
| 8104229 | 0.008594508 |
| 8104277 | 0.008594357 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

