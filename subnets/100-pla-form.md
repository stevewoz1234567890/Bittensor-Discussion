# NetUID 100 — Plaτform (`დ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Plaτform** (NetUID **100**) (`დ`).

An auto-research subnet where miners compete in multiple challenges to achieve top scores against a synthetic benchmark, driving continuous performance optimization.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `87`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,050.306317444. **Alpha liquidity in pool (`alpha_in`)** = ‎261,690.585511979დ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,204,323.433285208დ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011662923`** *(also **moving-average price** `0.011545992223545909` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎199,992.000142957დ‎`. **Owner hotkey / coldkey (chain):** `5GziQCcRpN8NCJktX343brnfuVe3w6gUYieeStXPD1Dag2At` / `5FX6kmhYwTYRFaZjxEo7k9DaG8qRmqrJtLTMGRgnfjRcXiWU`.
- **Subnet registered at block:** `6693448` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎57.380408093დ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004210971` · α-out `‎1.000000000დ‎` · α-in `‎0.361056235დ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104348`
- **Liquidity constant `k`:** `798236446202808842838661676`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Plaτform` |
| Symbol (API) | `დ` |
| Rank | `89` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.011506562` |
| Market cap | `12469460777677.977237236` |
| Market cap Δ 1d | `-0.503428273078229691` |
| Liquidity | `6059372756885` |
| Total τ | `3028680010329` |
| Total α | `1465696756619508` |
| α in pool | `263388208098675` |
| α staked | `820294370388103` |
| Price Δ 1h | `1.014165697630014051` |
| Price Δ 1d | `-1.132580696825742698` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `100` |
| Owner SS58 (API) | `5FX6kmhYwTYRFaZjxEo7k9DaG8qRmqrJtLTMGRgnfjRcXiWU` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `6693448` |
| Registration wall time | `2025-10-19T12:15:48.001Z` |
| Registration cost snapshot | `650607714640` |
| Active keys | `256` |
| Active validators | `11` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `4013915` |
| Max neurons | `256` |
| Validator slots (metadata) | `11` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

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
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000574361 |
| Owner SS58 (`owner_ss58`) | `5FX6kmhYwTYRFaZjxEo7k9DaG8qRmqrJtLTMGRgnfjRcXiWU` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


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
| 8104244 | 0.0118103 |
| 8104292 | 0.011676409 |
| 8104340 | 0.011675729 |
| 8104388 | 0.011663112 |
| 8104436 | 0.011662923 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

