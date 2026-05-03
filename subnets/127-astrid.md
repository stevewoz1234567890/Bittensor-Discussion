# NetUID 127 — Astrid (`𑀅`)

## Overview

**Astrid** (NetUID **127**) (`𑀅`).

The capital axis for Bittensor.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `317`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,001.067328817. **Alpha liquidity in pool (`alpha_in`)** = ‎945,376.088591976𑀅‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,257,146.452896543𑀅‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004235791`** *(also **moving-average price** `0.004249876132234931` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎545,050.460496172𑀅‎`. **Owner hotkey / coldkey (chain):** `5EKrpcqVNWfVfmKiq8v3LRrgb3E3ENBwYzmAziDhMK58gtb5` / `5FU4uxAdrZsaWaezWwXEK93MwPX5gw2566BQK2WwrGUudfSH`.
- **Subnet registered at block:** `5848837` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎230.383796081𑀅‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000𑀅‎` · α-in `‎0.000000000𑀅‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004235844`
- **Market cap:** `9979802951225.038872444`
- **Liquidity:** `8005532961201`
- **Total τ:** `4001093053011`
- **Total α:** `3202447541488519`
- **α in pool:** `945370015560227`
- **α staked:** `1410666455854924`
- **Price Δ 1h:** `-0.025537382526860276`
- **Price Δ 1d:** `0.242949011945821376`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `16`
- **Active miners:** `4`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `16`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

The capital axis for Bittensor.

### Repository README excerpt *(everything before first `##` heading)*

# Astrid Validator - Subnet 127

A production-ready Bittensor subnet validator daemon for Subnet 127 (Astrid). This validator connects to the Astrid coordination service, executes trading strategy simulations in isolated Docker environments, and manages Bittensor weight commitments.

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** Astrid Intelligence PLC

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
- **Owner SS58 (`owner_ss58`):** `5FU4uxAdrZsaWaezWwXEK93MwPX5gw2566BQK2WwrGUudfSH`

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

# Astrid Validator - Subnet 127

A production-ready Bittensor subnet validator daemon for Subnet 127 (Astrid). This validator connects to the Astrid coordination service, executes trading strategy simulations in isolated Docker environments, and manages Bittensor weight commitments.

---

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

## On-chain identity — description


The capital axis for Bittensor.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.astrid.global/](https://www.astrid.global/)
- **GitHub:** [https://github.com/astridintelligence/sn-127](https://github.com/astridintelligence/sn-127)
- **Logo URL:** [https://cdn.prod.website-files.com/68b07769f32da8fcc36dc172/69f2325c06235848691480b7_Astrid%20Square.png](https://cdn.prod.website-files.com/68b07769f32da8fcc36dc172/69f2325c06235848691480b7_Astrid%20Square.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.004235871 |
| 8104133 | 0.004235856 |
| 8104181 | 0.004235848 |
| 8104229 | 0.004235816 |
| 8104277 | 0.004235791 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.005809285 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005648115 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005542028 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005660948 |
| 2026-03-13T23:59:48Z | 7739841 | 0.006148097 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.006597684 |
| 2026-03-15T23:59:48Z | 7754226 | 0.006681642 |
| 2026-03-16T23:59:48Z | 7761426 | 0.006039994 |
| 2026-03-17T23:59:48Z | 7768619 | 0.006363369 |
| 2026-03-18T23:59:48Z | 7775819 | 0.006541233 |
| 2026-03-19T23:59:48Z | 7783014 | 0.0070151332366353924 |
| 2026-03-20T23:59:48Z | 7790201 | 0.007695518 |
| 2026-03-21T23:59:48Z | 7797398 | 0.007724054 |
| 2026-03-22T23:59:48Z | 7804598 | 0.007314718 |
| 2026-03-23T23:59:48Z | 7811798 | 0.007836318 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00796138827896450226 |
| 2026-03-25T23:59:48Z | 7826196 | 0.006793259 |
| 2026-03-26T23:59:48Z | 7833396 | 0.006650208 |
| 2026-03-27T23:59:48Z | 7840596 | 0.005991768 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.00655125 |
| 2026-03-29T23:59:48Z | 7854902 | 0.006479118 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.00624211 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005905817 |
| 2026-04-01T23:59:48Z | 7876474 | 0.006021613 |
| 2026-04-02T23:59:48Z | 7883622 | 0.006137771 |
| 2026-04-03T23:59:48Z | 7890794 | 0.005611533 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.005642115 |
| 2026-04-05T23:59:48Z | 7905188 | 0.005618943 |
| 2026-04-06T23:59:48Z | 7912388 | 0.005680479 |
| 2026-04-07T23:59:48Z | 7919588 | 0.00588408 |
| 2026-04-08T23:59:48Z | 7926788 | 0.005854613 |
| 2026-04-09T23:59:48Z | 7933987 | 0.005630892 |
| 2026-04-10T23:59:48Z | 7941184 | 0.00561583 |
| 2026-04-11T23:59:48Z | 7948384 | 0.005610165 |
| 2026-04-12T23:59:48Z | 7955584 | 0.005520023 |
| 2026-04-13T23:59:48Z | 7962784 | 0.00546645 |
| 2026-04-14T23:59:48Z | 7969979 | 0.005368509 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.005074587 |
| 2026-04-16T23:59:48Z | 7984379 | 0.005217572 |
| 2026-04-17T23:59:48Z | 7991579 | 0.005123813 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004994469 |
| 2026-04-19T23:59:48Z | 8005979 | 0.005019145 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004999958 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004915441 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004832213 |
| 2026-04-23T23:59:48Z | 8034762 | 0.00501135 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004837463 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004854719 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004787913 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004671918 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004721567 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004668195 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004598505 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004371739 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004177856 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004235844 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

