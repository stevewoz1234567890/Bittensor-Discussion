# NetUID 127 — Astrid (`𑀅`)

## Overview

**Astrid** (NetUID **127**) (`𑀅`).

The capital axis for Bittensor.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `255`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,001.092757130. **Alpha liquidity in pool (`alpha_in`)** = ‎945,370.085414295𑀅‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,257,090.456074224𑀅‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004235843`** *(also **moving-average price** `0.004250121535733342` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎545,050.435067859𑀅‎`. **Owner hotkey / coldkey (chain):** `5EKrpcqVNWfVfmKiq8v3LRrgb3E3ENBwYzmAziDhMK58gtb5` / `5FU4uxAdrZsaWaezWwXEK93MwPX5gw2566BQK2WwrGUudfSH`.
- **Subnet registered at block:** `5848837` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎185.324458280𑀅‎`; pending root emission `τ0.000000000`.
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
| 8104024 | 0.004235882 |
| 8104072 | 0.004235872 |
| 8104120 | 0.004235859 |
| 8104168 | 0.004235849 |
| 8104216 | 0.004235843 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

