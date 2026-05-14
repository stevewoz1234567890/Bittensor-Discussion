# NetUID 6 — Numinous (`ζ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Numinous** (NetUID **6**) (`ζ`).

Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `354`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ10,474.315063681. **Alpha liquidity in pool (`alpha_in`)** = ‎2,220,149.738991654ζ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,551,748.884626772ζ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004725094`** *(also **moving-average price** `0.004703448386862874` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎595,615.834398650ζ‎`. **Owner hotkey / coldkey (chain):** `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA` / `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA`.
- **Subnet registered at block:** `3219949` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎266.338999088ζ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ζ‎` · α-in `‎0.000000000ζ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104081`
- **Liquidity constant `k`:** `23254547854747721895737518374`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Numinous` |
| Symbol (API) | `ζ` |
| Rank | `51` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004729466` |
| Market cap | `21922620167845.56710651` |
| Market cap Δ 1d | `1.759511289204292486` |
| Liquidity | `20974435517595` |
| Total τ | `10479184493058` |
| Total α | `4771665623618426` |
| α in pool | `2219119669014892` |
| α staked | `2416207060862343` |
| Price Δ 1h | `0.334408001522369992` |
| Price Δ 1d | `1.606138305220201925` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `6` |
| Owner SS58 (API) | `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3219949` |
| Registration wall time | `2024-06-20T13:03:12.010Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `138` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `12` |
| Max validators (API) | `64` |
| Neuron reg. cost | `245297887` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `6000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Numinous**



[Discord](https://discord.gg/qKPeYPc3) • [Dashboard](https://app.hex.tech/1644b22a-abe5-4113-9d5f-3ad05e4a8de7/app/Numinous-031erYRYSssIrH3W3KcyHg/latest) • [Website](https://numinouslabs.io/) • [Twitter](https://x.com/numinous_ai) •
[Network](https://taostats.io/subnets/6/chart)
---

</div>

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** Numinous

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
| `immunity_period` (blocks) | 50400 |
| Registration recycle cost snapshot (`burn`) | τ0.200000000 |
| Owner SS58 (`owner_ss58`) | `5CfSg4e23Z3aTXvc2XZie8ZE1xkqRPoyVRFdWUuyyjGxJrMA` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.200000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `50400` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `6000` blocks |
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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


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
| 8104196 | 0.004729467 |
| 8104244 | 0.004724183 |
| 8104292 | 0.004724447 |
| 8104340 | 0.004724578 |
| 8104388 | 0.004725025 |
| 8104436 | 0.004725094 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

