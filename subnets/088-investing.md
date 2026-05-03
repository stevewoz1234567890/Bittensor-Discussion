# NetUID 88 — Investing (`ᛉ`)

## Overview

Decentralized AUM

https://x.com/Investing88ai

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

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

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

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

---

## Mining

When a strategy is filed under the `Investing/strat/` directory, it will be automatically submitted by the miner. Please see [README](https://github.com/mobiusfund/investing/tree/main/Investing/strat) for further info.

A strategy can be revised or "rebalanced" whenever necessary. It will be automatically resubmitted based on the file timestamp. Rebalancing can happen when updating the timestamp without changing the strategy file. A change in asset allocation will incur [slippage](https://docs.learnbittensor.org/learn/slippage) costs as well as [staking/unstaking](https://github.com/opentensor/subtensor/pull/1386) fees for Tao/Alpha, and transaction fees for other assets.

For US stocks, rebalancing is currently supported via two order types in a trading session: Market on Open (MOO) and Market on Close (MOC), to take advantage of maximum liquidity. Per NYSE and NASDAQ rules, only strategies submitted before 09:28 and 15:50 Eastern time will be counted. Currently supported [ticker symbols](https://api.investing88.ai/assets) are generally large cap assets.

To accommodate multiple asset classes, the UID space and subnet emissions are partitioned based on [asset ratio](https://api.investing88.ai/ratio), which will be adjusted over time as the subnet evolves.

All strategy updates are shown on the [dashboard](https://db.investing88.ai) immediately. Daily score calculation takes place at 00:00 UTC for Tao/Alpha, and 06:00 UTC for US stocks. The dashboard emphasizes raw performance rankings and comparisons between asset classes. To see adjusted rankings and scores set by validators that match on-chain incentives, use the `Investing/bin/validator` command.

One machine can run multiple miners with their corresponding strategies, with an extra argument e.g. `--axon.port 8092` added to the `pm2` command. However a new or revised strategy that is overly similar to a pre-existing one will receive a reduced score.

To curb UID spam, each miner requires a certain amount of alpha token stake. The total required stake is reflected on the coldkey.

A newly registered miner goes live on the dashboard after day 1, with an immunity period of 3 days.

---

#### CPU / GPU / RAM lines (automatic grep)

*Nothing in this README excerpt matched GPU/VRAM/CPU sizing patterns (`\d+ GB/TB`, `CUDA`, `H100/RTX/…`, `vCPU/cores`). Check **`docs/`**, miner/validator guides linked here, Discord, or the subnet’s homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/mobiusfund/investing/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

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
| 8103843 | 0.003548249 |
| 8103891 | 0.003548246 |
| 8103939 | 0.003548242 |
| 8103987 | 0.003548239 |
| 8104035 | 0.003548237 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

