# NetUID 127 — Astrid (`𑀅`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Astrid** (NetUID **127**) (`𑀅`).

The capital axis for Bittensor.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `114`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,007.248455887. **Alpha liquidity in pool (`alpha_in`)** = ‎943,919.007660471𑀅‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,258,761.533828048𑀅‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004248478`** *(also **moving-average price** `0.004249665187671781` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎545,162.249659788𑀅‎`. **Owner hotkey / coldkey (chain):** `5EKrpcqVNWfVfmKiq8v3LRrgb3E3ENBwYzmAziDhMK58gtb5` / `5FU4uxAdrZsaWaezWwXEK93MwPX5gw2566BQK2WwrGUudfSH`.
- **Subnet registered at block:** `5848837` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎82.851744173𑀅‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000𑀅‎` · α-in `‎0.000000000𑀅‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104321`
- **Liquidity constant `k`:** `3782517985929811739117142777`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Astrid` |
| Symbol (API) | `𑀅` |
| Rank | `98` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004235844` |
| Market cap | `9979802951225.038872444` |
| Market cap Δ 1d | `0.452813202368063853` |
| Liquidity | `8005532961201` |
| Total τ | `4001093053011` |
| Total α | `3202447541488519` |
| α in pool | `945370015560227` |
| α staked | `1410666455854924` |
| Price Δ 1h | `-0.025537382526860276` |
| Price Δ 1d | `0.242949011945821376` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `127` |
| Owner SS58 (API) | `5FU4uxAdrZsaWaezWwXEK93MwPX5gw2566BQK2WwrGUudfSH` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5848837` |
| Registration wall time | `2025-06-24T04:44:48Z` |
| Registration cost snapshot | `97101698382` |
| Active keys | `256` |
| Active validators | `16` |
| Active miners | `4` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `16` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Astrid Validator - Subnet 127

A production-ready Bittensor subnet validator daemon for Subnet 127 (Astrid). This validator connects to the Astrid coordination service, executes trading strategy simulations in isolated Docker environments, and manages Bittensor weight commitments.

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** Astrid Intelligence PLC

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
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5FU4uxAdrZsaWaezWwXEK93MwPX5gw2566BQK2WwrGUudfSH` |


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
| `commit_reveal_weights_enabled` | `False` |
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

## Prerequisites

- Node.js 20+
- Docker and Docker Compose
- Redis 7+ (included in docker-compose.yml)
- Bittensor validator identity (mnemonic phrase)

---

## Installation

```bash

---

# Install dependencies

npm install

---

# Validator identity (Polkadot/Substrate mnemonic or secret seed)

VALIDATOR_MNEMONIC="your twelve word seed phrase goes here"
VALIDATOR_SECRET_SEED="0x..."

---

# Docker socket path

DOCKER_SOCKET=/var/run/docker.sock

---

# Validator display name

VALIDATOR_DISPLAY_NAME=Validator Name

---

### Docker Deployment

```bash

---

### 1. Docker Image Tasks

Executes arbitrary Docker images with mounted volumes and environment variables:
- Secure sandbox isolation
- Resource limits and timeout controls
- Output capture and error handling

---

### Validator fails to register

- Verify `API_URL` is correct and accessible
- Check that `VALIDATOR_MNEMONIC` or `VALIDATOR_SECRET_SEED` is valid
- Ensure network connectivity to the coordinator

---








#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/astridintelligence/sn-127/master/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.astrid.global/](https://www.astrid.global/)
- **GitHub:** [https://github.com/astridintelligence/sn-127](https://github.com/astridintelligence/sn-127)
- **Logo URL:** [https://cdn.prod.website-files.com/68b07769f32da8fcc36dc172/69f2325c06235848691480b7_Astrid%20Square.png](https://cdn.prod.website-files.com/68b07769f32da8fcc36dc172/69f2325c06235848691480b7_Astrid%20Square.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004235809 |
| 8104292 | 0.004235787 |
| 8104340 | 0.004248489 |
| 8104388 | 0.004248487 |
| 8104436 | 0.004248477 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.005809285 |
| 2026-03-10T23:59:48Z | — | 0.005648115 |
| 2026-03-11T23:59:48Z | — | 0.005542028 |
| 2026-03-12T23:59:48Z | — | 0.005660948 |
| 2026-03-13T23:59:48Z | — | 0.006148097 |
| 2026-03-14T23:59:48Z | — | 0.006597684 |
| 2026-03-15T23:59:48Z | — | 0.006681642 |
| 2026-03-16T23:59:48Z | — | 0.006039994 |
| 2026-03-17T23:59:48Z | — | 0.006363369 |
| 2026-03-18T23:59:48Z | — | 0.006541233 |
| 2026-03-19T23:59:48Z | — | 0.00701513323664 |
| 2026-03-20T23:59:48Z | — | 0.007695518 |
| 2026-03-21T23:59:48Z | — | 0.007724054 |
| 2026-03-22T23:59:48Z | — | 0.007314718 |
| 2026-03-23T23:59:48Z | — | 0.007836318 |
| 2026-03-24T23:59:48Z | — | 0.00796138827896 |
| 2026-03-25T23:59:48Z | — | 0.006793259 |
| 2026-03-26T23:59:48Z | — | 0.006650208 |
| 2026-03-27T23:59:48Z | — | 0.005991768 |
| 2026-03-28T23:59:48Z | — | 0.00655125 |
| 2026-03-29T23:59:48Z | — | 0.006479118 |
| 2026-03-30T23:59:48Z | — | 0.00624211 |
| 2026-03-31T23:59:48Z | — | 0.005905817 |
| 2026-04-01T23:59:48Z | — | 0.006021613 |
| 2026-04-02T23:59:48Z | — | 0.006137771 |
| 2026-04-03T23:59:48Z | — | 0.005611533 |
| 2026-04-04T23:59:48Z | — | 0.005642115 |
| 2026-04-05T23:59:48Z | — | 0.005618943 |
| 2026-04-06T23:59:48Z | — | 0.005680479 |
| 2026-04-07T23:59:48Z | — | 0.00588408 |
| 2026-04-08T23:59:48Z | — | 0.005854613 |
| 2026-04-09T23:59:48Z | — | 0.005630892 |
| 2026-04-10T23:59:48Z | — | 0.00561583 |
| 2026-04-11T23:59:48Z | — | 0.005610165 |
| 2026-04-12T23:59:48Z | — | 0.005520023 |
| 2026-04-13T23:59:48Z | — | 0.00546645 |
| 2026-04-14T23:59:48Z | — | 0.005368509 |
| 2026-04-15T23:59:48Z | — | 0.005074587 |
| 2026-04-16T23:59:48Z | — | 0.005217572 |
| 2026-04-17T23:59:48Z | — | 0.005123813 |
| 2026-04-18T23:59:48Z | — | 0.004994469 |
| 2026-04-19T23:59:48Z | — | 0.005019145 |
| 2026-04-20T23:59:48Z | — | 0.004999958 |
| 2026-04-21T23:59:48Z | — | 0.004915441 |
| 2026-04-22T23:59:48Z | — | 0.004832213 |
| 2026-04-23T23:59:48Z | — | 0.00501135 |
| 2026-04-24T23:59:48Z | — | 0.004837463 |
| 2026-04-25T23:59:48Z | — | 0.004854719 |
| 2026-04-26T23:59:48Z | — | 0.004787913 |
| 2026-04-27T23:59:48Z | — | 0.004671918 |
| 2026-04-28T23:59:48Z | — | 0.004721567 |
| 2026-04-29T23:59:48Z | — | 0.004668195 |
| 2026-04-30T23:59:48Z | — | 0.004598505 |
| 2026-05-01T23:59:48Z | — | 0.004371739 |
| 2026-05-02T23:59:48Z | — | 0.004177856 |
| 2026-05-03T23:59:48Z | — | 0.004235844 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

