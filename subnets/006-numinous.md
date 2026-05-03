# NetUID 6 — Numinous (`ζ`)

## Overview

**Numinous** (NetUID **6**) (`ζ`).

Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `134`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ10,479.184232012. **Alpha liquidity in pool (`alpha_in`)** = ‎2,219,119.724212580ζ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,552,558.899405846ζ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004729466`** *(also **moving-average price** `0.004702162928879261` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎595,596.308921320ζ‎`. **Owner hotkey / coldkey (chain):** `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA` / `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA`.
- **Subnet registered at block:** `3219949` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎100.817451827ζ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ζ‎` · α-in `‎0.000000000ζ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004729466`
- **Market cap:** `21922620167845.56710651`
- **Liquidity:** `20974435517595`
- **Total τ:** `10479184493058`
- **Total α:** `4771665623618426`
- **α in pool:** `2219119669014892`
- **α staked:** `2416207060862343`
- **Price Δ 1h:** `0.334408001522369992`
- **Price Δ 1d:** `1.606138305220201925`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `138`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `245297887`

### On-chain declared purpose *(SubnetIdentity)*

Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters.

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Numinous**



[Discord](https://discord.gg/qKPeYPc3) • [Dashboard](https://app.hex.tech/1644b22a-abe5-4113-9d5f-3ad05e4a8de7/app/Numinous-031erYRYSssIrH3W3KcyHg/latest) • [Website](https://numinouslabs.io/) • [Twitter](https://x.com/numinous_ai) •
[Network](https://taostats.io/subnets/6/chart)
---

</div>

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** Numinous

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
- **`immunity_period` (blocks):** 50400
- **Registration recycle cost snapshot (`burn`):** τ0.237398782
- **Owner SS58 (`owner_ss58`):** `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.200000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `50400` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `6000` blocks
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

## 🏗 System Architecture

The Numinous subnet operates on a strictly defined lifecycle: **Code Submission $\to$ Sandbox Execution $\to$ Resolution $\to$ Weight Setting.**

Validators spin up parallel sandboxes where miners are evaluated on batches of events. Agents operate inside Docker containers with a secure proxy gateway to access external tools.

---

### For Miners

Develop and deploy forecasting agents that compete for the daily reward pool.

  * [**Miner Setup Guide**](docs/miner-setup.md) – Installation, wallet registration, and deployment.
  * [**Gateway Guide**](docs/gateway-guide.md) – How to use the Desearch and Chutes APIs.

---

### For Validators

Run the physical infrastructure that executes and scores the agents.

  * [**Validator Setup Guide**](docs/validator-setup.md) – Hardware requirements and node configuration.

-----

---

#### CPU / GPU / RAM lines (automatic grep)

- Agents must adhere to the interface defined in the architecture. Code size is limited to **2MB**.


*Primary README URL used: `https://raw.githubusercontent.com/numinouslabs/numinous/main/README.md`*

## On-chain identity — description


Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://numinouslabs.io/](https://numinouslabs.io/)
- **GitHub:** [https://github.com/numinouslabs/numinous](https://github.com/numinouslabs/numinous)
- **Discord (handle / invite hint):** `amedeo_ma`
- **Logo URL:** [https://numinouslabs.io/numinous-logo.svg](https://numinouslabs.io/numinous-logo.svg)
- **Contact:** marc@infinitemech.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8103976 | 0.004713699 |
| 8104024 | 0.0047035 |
| 8104072 | 0.004705287 |
| 8104120 | 0.004705117 |
| 8104168 | 0.004729289 |
| 8104216 | 0.004729466 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

