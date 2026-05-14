# NetUID 48 — Quantum Compute (`ק`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Quantum Compute** (NetUID **48**) (`ק`).

Quantum Computing

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `35`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ11,708.761699636. **Alpha liquidity in pool (`alpha_in`)** = ‎2,183,406.438908645ק‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,590,150.801254397ק‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005391867`** *(also **moving-average price** `0.005309318192303181` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎644,708.427506295ק‎`. **Owner hotkey / coldkey (chain):** `5D2Qc9ud7vTJrPzk8mT1ruY8oV8UaDP3ttepD7zVNNi943ch` / `5GNH5YMkcX8jEF1PukvxKafifcqz13jp18BT73jRL3AZc4Rc`.
- **Subnet registered at block:** `3856677` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎26.333787822ק‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ק‎` · α-in `‎0.000000000ק‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104400`
- **Liquidity constant `k`:** `25564985686632172431133753220`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Quantum Compute` |
| Symbol (API) | `ק` |
| Rank | `50` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.00539191` |
| Market cap | `22143025960247.3328735` |
| Market cap Δ 1d | `-1.085875718832325782` |
| Liquidity | `23481492711293` |
| Total τ | `11708809619283` |
| Total α | `4773324240163042` |
| α in pool | `2183397551519015` |
| α staked | `1923315275706835` |
| Price Δ 1h | `1.236753760767850035` |
| Price Δ 1d | `-1.259294636781233679` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `48` |
| Owner SS58 (API) | `5GNH5YMkcX8jEF1PukvxKafifcqz13jp18BT73jRL3AZc4Rc` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3856677` |
| Registration wall time | `2024-09-18T20:44:12Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `6` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `12` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Decentralized deep tech. Innovation from everywhere. Quantum computing, AI, and decentralized networks powered by Bittensor.

**Fetched document title:** qBitTensor Labs — Decentralized Deep Tech

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
| `immunity_period` (blocks) | 2000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5GNH5YMkcX8jEF1PukvxKafifcqz13jp18BT73jRL3AZc4Rc` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `2000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `3` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Validators

To set up a Validator please see [validator.md](qbittensor/validator/validator.md).

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/qbittensor-labs/quantum-compute/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.qbittensorlabs.com/](https://www.qbittensorlabs.com/)
- **GitHub:** [https://github.com/qbittensor-labs/quantum-compute](https://github.com/qbittensor-labs/quantum-compute)
- **Discord (handle / invite hint):** `qbittensorlabs`
- **Logo URL:** [https://qbittensorlabs.com/48.png](https://qbittensorlabs.com/48.png)
- **Contact:** qbittensorlabs@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.005391896 |
| 8104292 | 0.005391887 |
| 8104340 | 0.005391872 |
| 8104388 | 0.005391871 |
| 8104436 | 0.005391867 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.005066297 --> 0.00613024
    line [0.005946852, 0.005886146, 0.005802041, 0.005797698, 0.005650947, 0.00570952, 0.005554154, 0.005460995, 0.005378215, 0.005274149, 0.00521405482423, 0.005219287, 0.005598617, 0.005640908, 0.005444556, 0.00604659470693, 0.005446305, 0.005333612, 0.00591835, 0.005492412, 0.005733475, 0.005980614, 0.005664542, 0.005739697, 0.005566388, 0.005313196, 0.005496048, 0.00544761, 0.005480475, 0.005356887, 0.005307427, 0.005310094, 0.00526893, 0.005266132, 0.005139672, 0.005191656, 0.005156601, 0.005160929, 0.005198343, 0.005169509, 0.005175443, 0.00515798, 0.005223027, 0.005348639, 0.00533972, 0.005330535, 0.005367844, 0.005566972, 0.006056865, 0.005456548, 0.005732627, 0.005703574, 0.00560805, 0.005354062, 0.005307291, 0.00539191]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

