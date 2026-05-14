# NetUID 11 — TrajectoryRL (`λ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**TrajectoryRL** (NetUID **11**) (`λ`).

Agentic RL as a Service, Optimize agent trajectories to make agents cheaper, safer, and more reliable.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `359`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ23,578.085818579. **Alpha liquidity in pool (`alpha_in`)** = ‎2,072,527.896483271λ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,841,495.956271786λ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011385460`** *(also **moving-average price** `0.011456589912995696` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎824,738.864786794λ‎`. **Owner hotkey / coldkey (chain):** `5ECzcM7sixWNEeD6RbpeEHW1YcYMFejwHuvDBgQxVSjGyrMS` / `5D2Jhtbnm7iAdKfjRk6DisXBnr1MEsYat8kXqaPNrVqJP3uE`.
- **Subnet registered at block:** `2918568` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎270.690043520λ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000λ‎` · α-in `‎0.000000000λ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104076`
- **Liquidity constant `k`:** `48866240604681577691414491909`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `TrajectoryRL` |
| Symbol (API) | `λ` |
| Rank | `25` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.011346027` |
| Market cap | `44367605731640.375071272` |
| Market cap Δ 1d | `-0.536749910855577071` |
| Liquidity | `47092972229722` |
| Total τ | `23537088251013` |
| Total α | `4913790852755057` |
| α in pool | `2076135018778737` |
| α staked | `1834273949192199` |
| Price Δ 1h | `0.310975662047769518` |
| Price Δ 1d | `-0.674329181262877465` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `11` |
| Owner SS58 (API) | `5D2Jhtbnm7iAdKfjRk6DisXBnr1MEsYat8kXqaPNrVqJP3uE` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `2918568` |
| Registration wall time | `2024-05-09T10:17:36.002Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `10` |
| Active miners | `2` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `10` |
| Max validators (API) | `64` |
| Neuron reg. cost | `200000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# TrajectoryRL

> **Bittensor Subnet 11** — A reinforcement learning playground that continuously produces state-of-the-art skills for AI agents

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Bittensor](https://img.shields.io/badge/bittensor-7.0+-green.svg)](https://github.com/opentensor/bittensor)

Every platform shift creates a new software category. PCs gave us desktop apps. Smartphones gave us mobile apps. Agents are the next platform, and **skills are the software that runs on them**. The world needs far more skills than human developers can ship. Agents will write skills for other agents. TrajectoryRL is the RL playground where that happens.

The competition runs 24/7 on Bittensor. Miners compete every epoch to produce the best agent skills, validators evaluate them in real sandboxes with real protocols, and the winning skills surface automatically. Every season the bar rises. You don't bring us your prompt. **Skills ship, you install them.**


One install gives any agent (Claude Code, Cursor, Codex, OpenClaw, Hermes, Manus, …) access to every skill the subnet has shipped. Source, catalog, and docs: [`trajrl`](https://github.com/trajectoryRL/trajrl).

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** The open factory for AI agent skills. Open-source skills, vetted by continuous competition, that work with any agent harness. TrajectoryRL runs a 24/7 competition on Bittensor Subnet 11 to produce the best skills. The winners surface automatically and anyone can use them.

**Fetched document title:** TrajectoryRL | Bittensor Subnet 11

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 256 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 10800 |
| Registration recycle cost snapshot (`burn`) | τ0.200000000 |
| Owner SS58 (`owner_ss58`) | `5D2Jhtbnm7iAdKfjRk6DisXBnr1MEsYat8kXqaPNrVqJP3uE` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.200000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `10800` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `10` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `100000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### For Validators

Validators run in Docker, auto-updated by Watchtower. The validator pulls the latest TrajRL-Bench image before each eval cycle — new scenarios are picked up automatically.

```bash

---

### For Miners

Mining means writing a **SKILL.md** — instructions and strategies that teach an AI agent how to handle operational scenarios. The testee agent SSHes into an isolated sandbox (shell + mock services + scenario files), reads your SKILL.md, solves the task. A judge agent then SSHes in, grounds its evaluation in the sandbox state, and scores the work. No GPU, no server, no uptime required.

---

#### 1. Prerequisites (one-time)

```bash
pip install bittensor-cli

btcli wallet create --wallet-name my-miner
btcli subnets register --wallet-name my-miner --hotkey default --netuid 11
```

---

# Upload to S3-compatible storage (configure S3_BUCKET, AWS_* in .env.miner)

trajectoryrl-miner upload pack.json

---

# Get the two Docker images (pull from GHCR is fastest):

docker pull ghcr.io/trajectoryrl/trajrl-bench:latest
docker pull ghcr.io/trajectoryrl/hermes-agent:latest

---









#### CPU / GPU / RAM lines (automatic grep)

- - **No server required** — Miners upload packs to any HTTP endpoint and commit on-chain. No GPU, no uptime needed.
- Mining means writing a **SKILL.md** — instructions and strategies that teach an AI agent how to handle operational scenarios. The testee agent SSHes into an isolated sandbox (shell + mock services + scenario files), reads your SKILL.md, solves the task. A judge agent then SSHes in, grounds its evaluation in the sandbox state, and scores the work. No GPU, no server, no uptime required.
- Prereqs: Docker, [uv](https://docs.astral.sh/uv/), an LLM API key, ~6 GB free disk.


*Primary README URL used: `https://raw.githubusercontent.com/trajectoryRL/trajectoryRL/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://trajrl.com](https://trajrl.com)
- **GitHub:** [https://github.com/trajectoryRL/trajectoryRL](https://github.com/trajectoryRL/trajectoryRL)
- **Logo URL:** [https://pbs.twimg.com/profile_images/2018928039716089856/2PZ-Bhm2_400x400.jpg](https://pbs.twimg.com/profile_images/2018928039716089856/2PZ-Bhm2_400x400.jpg)
- **Contact:** trajectoryrl@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.011346029 |
| 8104244 | 0.011345321 |
| 8104292 | 0.0113451 |
| 8104340 | 0.011393141 |
| 8104388 | 0.011393139 |
| 8104436 | 0.01138546 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

