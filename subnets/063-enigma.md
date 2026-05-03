# NetUID 63 — Enigma (`س`)

## Overview

**Enigma** (NetUID **63**) (`س`).

Breaking today to build tomorrow

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `191`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ14,786.235230770. **Alpha liquidity in pool (`alpha_in`)** = ‎1,736,410.252857939س‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,123,230.687906362س‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008594529`** *(also **moving-average price** `0.008697398472577333` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,130,208.193788281س‎`. **Owner hotkey / coldkey (chain):** `5GmpedVP2r9haksUBD743wek8t89jMz96RTkV2zkVdRR4e1B` / `5CqTmNfgDchxULD1bfoz8jvj9rDYSoq76kiq98oBUUEDpWqX`.
- **Subnet registered at block:** `4885578` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎143.898285785س‎`; pending root emission `τ0.000000000`.
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

## Operational parameters — registration, limits, economics (chain)


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
| 8104024 | 0.008483984 |
| 8104072 | 0.008483976 |
| 8104120 | 0.008603137 |
| 8104168 | 0.008594534 |
| 8104216 | 0.008594529 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.008639695 |
| 2026-03-10T23:59:48Z | 7718257 | 0.008746981 |
| 2026-03-11T23:59:48Z | 7725455 | 0.00881197 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.008430985 |
| 2026-03-13T23:59:48Z | 7739841 | 0.008318581 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.009053096 |
| 2026-03-15T23:59:48Z | 7754226 | 0.008962449 |
| 2026-03-16T23:59:48Z | 7761426 | 0.008517915 |
| 2026-03-17T23:59:48Z | 7768619 | 0.008563888 |
| 2026-03-18T23:59:48Z | 7775819 | 0.008665121 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00854123733046230959 |
| 2026-03-20T23:59:48Z | 7790201 | 0.009104631 |
| 2026-03-21T23:59:48Z | 7797398 | 0.010056926 |
| 2026-03-22T23:59:48Z | 7804598 | 0.010163888 |
| 2026-03-23T23:59:48Z | 7811798 | 0.011172351 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.01186039799161872071 |
| 2026-03-25T23:59:48Z | 7826196 | 0.010194359 |
| 2026-03-26T23:59:48Z | 7833396 | 0.010838232 |
| 2026-03-27T23:59:48Z | 7840596 | 0.012556027 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.012323437 |
| 2026-03-29T23:59:48Z | 7854902 | 0.011465776 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.01216482 |
| 2026-03-31T23:59:48Z | 7869291 | 0.011721255 |
| 2026-04-01T23:59:48Z | 7876474 | 0.011922363 |
| 2026-04-02T23:59:48Z | 7883622 | 0.010699862 |
| 2026-04-03T23:59:48Z | 7890794 | 0.009827909 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.009989516 |
| 2026-04-05T23:59:48Z | 7905188 | 0.009783873 |
| 2026-04-06T23:59:48Z | 7912388 | 0.010154643 |
| 2026-04-07T23:59:48Z | 7919588 | 0.009788695 |
| 2026-04-08T23:59:48Z | 7926788 | 0.00947439 |
| 2026-04-09T23:59:48Z | 7933987 | 0.009254492 |
| 2026-04-10T23:59:48Z | 7941184 | 0.008907943 |
| 2026-04-11T23:59:48Z | 7948384 | 0.008778666 |
| 2026-04-12T23:59:48Z | 7955584 | 0.00853962 |
| 2026-04-13T23:59:48Z | 7962784 | 0.00816814 |
| 2026-04-14T23:59:48Z | 7969979 | 0.008146093 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.008065891 |
| 2026-04-16T23:59:48Z | 7984379 | 0.008063285 |
| 2026-04-17T23:59:48Z | 7991579 | 0.008300126 |
| 2026-04-18T23:59:48Z | 7998779 | 0.008470781 |
| 2026-04-19T23:59:48Z | 8005979 | 0.008615588 |
| 2026-04-20T23:59:48Z | 8013179 | 0.008447296 |
| 2026-04-21T23:59:48Z | 8020376 | 0.008547917 |
| 2026-04-22T23:59:48Z | 8027562 | 0.008556575 |
| 2026-04-23T23:59:48Z | 8034762 | 0.008828374 |
| 2026-04-24T23:59:48Z | 8041962 | 0.009156579 |
| 2026-04-25T23:59:48Z | 8049151 | 0.00950938 |
| 2026-04-26T23:59:48Z | 8056274 | 0.009234042 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.008673047 |
| 2026-04-28T23:59:48Z | 8070646 | 0.008623189 |
| 2026-04-29T23:59:48Z | 8077790 | 0.008570244 |
| 2026-04-30T23:59:48Z | 8084984 | 0.008561103 |
| 2026-05-01T23:59:48Z | 8092168 | 0.008921508 |
| 2026-05-02T23:59:48Z | 8099357 | 0.008880602 |
| 2026-05-03T16:10:00Z | 8104202 | 0.008594529 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

