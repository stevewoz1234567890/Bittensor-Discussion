# NetUID 88 — Investing (`ᛉ`)

## Overview

Decentralized AUM

https://x.com/Investing88ai

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
- **`immunity_period` (blocks):** 21600
- **Registration recycle cost snapshot (`burn`):** τ0.100000000
- **Owner SS58 (`owner_ss58`):** `5FhMsGJS7WYdwBzcgsTWxEtY7UCYLZdmBVLcNPmCxr3ppiKS`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.100000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `21600` blocks
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

## Installation

For first-time miners, please follow the [Bittensor document](https://docs.learnbittensor.org/miners/) to register a hotkey.

The [KYM app](https://kym.investing88.ai) (Know Your Miner) provides a simple zero-code mining interface, making PM2 setup below optional. Even without involving PM2, it's recommended to install the repo in order to take advantage of the stand-alone tool `Investing/bin/simst` (Sim Strat) for back-testing strategies.

Please avoid using the root account, and make sure Python3 is available as command `python` under a regular user account. Ubuntu 22.04 is the only officially supported OS, although many other OSes can also work with minimum tweaks, including macOS.

---

#### Setup

```bash
sudo apt update
sudo apt install npm -y
sudo npm install pm2 -g
git clone https://github.com/mobiusfund/investing
cd investing

---

#### Miner

```bash

---

#### Validator

```bash


*README source used for excerpts: `https://raw.githubusercontent.com/mobiusfund/investing/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Decentralized AUM

## On-chain identity — additional field


https://x.com/Investing88ai

## Registered contact & links


- **Website:** [https://Investing88.ai](https://Investing88.ai)
- **GitHub:** [https://github.com/mobiusfund/investing](https://github.com/mobiusfund/investing)
- **Logo URL:** [https://Investing88.ai/logo.png](https://Investing88.ai/logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.00355002 |
| 8103738 | 0.003548676 |
| 8103786 | 0.003548513 |
| 8103834 | 0.003548254 |
| 8103882 | 0.003548246 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Investing88
- **Fetched from:** [https://Investing88.ai](https://Investing88.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

