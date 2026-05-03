# NetUID 88 — Investing (`ᛉ`)

## Overview

**Investing** (NetUID **88**) (`ᛉ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `278`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,276.745039927. **Alpha liquidity in pool (`alpha_in`)** = ‎1,773,193.100351647ᛉ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,421,511.233890979ᛉ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003541445`** *(also **moving-average price** `0.0035437424667179585` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎534,651.275043664ᛉ‎`. **Owner hotkey / coldkey (chain):** `5HK4vbGgLQdFKarN3hLVqNRbgQtQR5w3WTZ2tTnFHHLPgXpY` / `5FhMsGJS7WYdwBzcgsTWxEtY7UCYLZdmBVLcNPmCxr3ppiKS`.
- **Subnet registered at block:** `5299805` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎207.046448305ᛉ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ᛉ‎` · α-in `‎0.000000000ᛉ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003541464`
- **Market cap:** `14575096911828.892848768`
- **Liquidity:** `12556444569768`
- **Total τ:** `6276762162940`
- **Total α:** `4194629334242626`
- **α in pool:** `1773188265313072`
- **α staked:** `2342368722370240`
- **Price Δ 1h:** `-0.191080433025462736`
- **Price Δ 1d:** `-0.57636256546192947`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `169`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `10`
- **Neuron reg. cost:** `100000000`

### On-chain declared purpose *(SubnetIdentity)*

Decentralized AUM



**Additional commentary (on-chain)**


https://x.com/Investing88ai

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# Investing - Decentralized AUM
[Dashboard](https://db.investing88.ai) • [Discord](https://discord.com/channels/799672011265015819/1358854051634221328) • [X](https://x.com/Investing88ai) • [KYM](https://kym.investing88.ai)
</div>

---
- [Intro](#Intro)
- [Roadmap](#Roadmap)
- [Installation](#installation)
- [Mining](#Mining)
- [Scoring](#Scoring)
- [Disclaimer](#Disclaimer)
- [License](#license)

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** Investing88

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

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/mobiusfund/investing/main/README.md`*

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

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.003548233 |
| 8104133 | 0.003548228 |
| 8104181 | 0.003548225 |
| 8104229 | 0.003541454 |
| 8104277 | 0.003541445 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

