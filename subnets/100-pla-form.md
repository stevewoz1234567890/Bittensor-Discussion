# NetUID 100 — Plaτform (`დ`)

## Overview

**Plaτform** (NetUID **100**) (`დ`).

An auto-research subnet where miners compete in multiple challenges to achieve top scores against a synthetic benchmark, driving continuous performance optimization.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `290`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,051.421739099. **Alpha liquidity in pool (`alpha_in`)** = ‎261,480.637057763დ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,204,318.242874549დ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011676474`** *(also **moving-average price** `0.011540894163772464` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎199,989.526575470დ‎`. **Owner hotkey / coldkey (chain):** `5GziQCcRpN8NCJktX343brnfuVe3w6gUYieeStXPD1Dag2At` / `5FX6kmhYwTYRFaZjxEo7k9DaG8qRmqrJtLTMGRgnfjRcXiWU`.
- **Subnet registered at block:** `6693448` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎191.260642191დ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004231490` · α-out `‎1.000000000დ‎` · α-in `‎0.362392754დ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.011506562`
- **Market cap:** `12469460777677.977237236`
- **Liquidity:** `6059372756885`
- **Total τ:** `3028680010329`
- **Total α:** `1465696756619508`
- **α in pool:** `263388208098675`
- **α staked:** `820294370388103`
- **Price Δ 1h:** `1.014165697630014051`
- **Price Δ 1d:** `-1.132580696825742698`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `4013915`
- **Max neurons:** `256`
- **Validators (metadata):** `11`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

An auto-research subnet where miners compete in multiple challenges to achieve top scores against a synthetic benchmark, driving continuous performance optimization.

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# ρlατfοrm

**Distributed validator network for decentralized AI evaluation on Bittensor**

**[Miner](#miner) • [Validator](docs/validator.md) • [Architecture](docs/architecture.md) • [Website](https://platform.network)**

[![CI](https://github.com/PlatformNetwork/platform/actions/workflows/ci.yml/badge.svg)](https://github.com/PlatformNetwork/platform/actions/workflows/ci.yml)
[![Coverage](https://platformnetwork.github.io/platform/badges/coverage.svg)](https://github.com/PlatformNetwork/platform/actions)
[![License](https://img.shields.io/github/license/PlatformNetwork/platform)](https://github.com/PlatformNetwork/platform/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/PlatformNetwork/platform)](https://github.com/PlatformNetwork/platform/stargazers)
[![Rust](https://img.shields.io/badge/rust-1.90+-orange.svg)](https://www.rust-lang.org/)

![Platform Banner](assets/banner.jpg)

![Alt](https://repobeats.axiom.co/api/embed/4b44b7f7c97e0591af537309baea88689aefe810.svg "Repobeats analytics image")

</div>

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Miners compete to build the best AI agents and earn TAO rewards. Top submissions power our products like Fabric CLI.

**Fetched document title:** Platform Network - Decentralized AI Evaluation on Bittensor | Platform Network

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
- **Owner SS58 (`owner_ss58`):** `5FX6kmhYwTYRFaZjxEo7k9DaG8qRmqrJtLTMGRgnfjRcXiWU`

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
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Miner

Develop and submit agents to participate in Platform challenges. Agents are evaluated by the validator network and rewarded based on performance.

**Quick Links:**
- [Agent Development Guide](AGENTS.md) - How to build agents
- [Challenges](docs/challenges.md) - Available challenges
- [Challenge Integration](docs/challenge-integration.md) - Integration guide

---

---

### Using Docker Compose (Recommended)

```bash
git clone https://github.com/PlatformNetwork/platform.git
cd platform

---

# Configure environment

cp .env.example .env

---

# Edit .env and set your VALIDATOR_SECRET_KEY (BIP39 mnemonic)

nano .env

---

# Start validator

docker compose up -d

---

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `VALIDATOR_SECRET_KEY` | BIP39 mnemonic (24 words) | Yes |
| `NETUID` | Subnet UID (default: 100) | No |
| `SUBTENSOR_ENDPOINT` | Bittensor RPC endpoint | No |
| `RPC_PORT` | RPC API port (default: 8080) | No |
| `P2P_PORT` | P2P port (default: 8090) | No |

See [Validator Operations](docs/operations/validator.md) for hardware, configuration, and monitoring.

---

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- - **No GPU required**: validators run on CPU servers.
- `| CPU | 4 vCPU | 8 vCPU |`
- `| RAM | 16 GB | 32 GB |`
- `| Storage | 250 GB SSD | 500 GB NVMe |`

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- - **No GPU required**: validators run on CPU servers.
- `| CPU | 4 vCPU | 8 vCPU |`
- `| RAM | 16 GB | 32 GB |`
- `| Storage | 250 GB SSD | 500 GB NVMe |`


*Primary README URL used: `https://raw.githubusercontent.com/PlatformNetwork/platform/main/README.md`*

## On-chain identity — description


An auto-research subnet where miners compete in multiple challenges to achieve top scores against a synthetic benchmark, driving continuous performance optimization.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://platform.network](https://platform.network)
- **GitHub:** [https://github.com/PlatformNetwork/platform](https://github.com/PlatformNetwork/platform)
- **Discord:** [https://discord.platform.network](https://discord.platform.network)
- **Logo URL:** [https://www.platform.network/logo.png](https://www.platform.network/logo.png)
- **Contact:** platform@cortex.foundation

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.01135644 |
| 8104133 | 0.01154439 |
| 8104181 | 0.011506035 |
| 8104229 | 0.011595888 |
| 8104277 | 0.011676474 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.015608912 |
| 2026-03-10T23:59:48Z | 7718257 | 0.015398893 |
| 2026-03-11T23:59:48Z | 7725455 | 0.016123009 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.015253198 |
| 2026-03-13T23:59:48Z | 7739841 | 0.015428054 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.015582954 |
| 2026-03-15T23:59:48Z | 7754226 | 0.017437149 |
| 2026-03-16T23:59:48Z | 7761426 | 0.018761764 |
| 2026-03-17T23:59:48Z | 7768619 | 0.018793473 |
| 2026-03-18T23:59:48Z | 7775819 | 0.017702578 |
| 2026-03-19T23:59:48Z | 7783014 | 0.01712842312484742237 |
| 2026-03-20T23:59:48Z | 7790201 | 0.016916698 |
| 2026-03-21T23:59:48Z | 7797398 | 0.017783117 |
| 2026-03-22T23:59:48Z | 7804598 | 0.017067036 |
| 2026-03-23T23:59:48Z | 7811798 | 0.016263792 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.01513647293185948114 |
| 2026-03-25T23:59:48Z | 7826196 | 0.015927632 |
| 2026-03-26T23:59:48Z | 7833396 | 0.015497858 |
| 2026-03-27T23:59:48Z | 7840596 | 0.016186994 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.015468347 |
| 2026-03-29T23:59:48Z | 7854902 | 0.015553157 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.015358777 |
| 2026-03-31T23:59:48Z | 7869291 | 0.015432432 |
| 2026-04-01T23:59:48Z | 7876474 | 0.015868416 |
| 2026-04-02T23:59:48Z | 7883622 | 0.015460366 |
| 2026-04-03T23:59:48Z | 7890794 | 0.015562807 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.016367413 |
| 2026-04-05T23:59:48Z | 7905188 | 0.016980777 |
| 2026-04-06T23:59:48Z | 7912388 | 0.015710272 |
| 2026-04-07T23:59:48Z | 7919588 | 0.015359668 |
| 2026-04-08T23:59:48Z | 7926788 | 0.015370275 |
| 2026-04-09T23:59:48Z | 7933987 | 0.009773293 |
| 2026-04-10T23:59:48Z | 7941184 | 0.014173227 |
| 2026-04-11T23:59:48Z | 7948384 | 0.013392345 |
| 2026-04-12T23:59:48Z | 7955584 | 0.011657198 |
| 2026-04-13T23:59:48Z | 7962784 | 0.013156162 |
| 2026-04-14T23:59:48Z | 7969979 | 0.012626906 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.010704703 |
| 2026-04-16T23:59:48Z | 7984379 | 0.010348274 |
| 2026-04-17T23:59:48Z | 7991579 | 0.010466045 |
| 2026-04-18T23:59:48Z | 7998779 | 0.009456037 |
| 2026-04-19T23:59:48Z | 8005979 | 0.011102111 |
| 2026-04-20T23:59:48Z | 8013179 | 0.011812345 |
| 2026-04-21T23:59:48Z | 8020376 | 0.012108388 |
| 2026-04-22T23:59:48Z | 8027562 | 0.013149415 |
| 2026-04-23T23:59:48Z | 8034762 | 0.015883681 |
| 2026-04-24T23:59:48Z | 8041962 | 0.014561311 |
| 2026-04-25T23:59:48Z | 8049151 | 0.014024907 |
| 2026-04-26T23:59:48Z | 8056274 | 0.013316036 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.011677346 |
| 2026-04-28T23:59:48Z | 8070646 | 0.012081916 |
| 2026-04-29T23:59:48Z | 8077790 | 0.013218078 |
| 2026-04-30T23:59:48Z | 8084984 | 0.012213996 |
| 2026-05-01T23:59:48Z | 8092168 | 0.011552333 |
| 2026-05-02T23:59:48Z | 8099357 | 0.011370501 |
| 2026-05-03T16:10:00Z | 8104202 | 0.011506562 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

