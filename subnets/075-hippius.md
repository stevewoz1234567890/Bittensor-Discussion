# NetUID 75 — Hippius (`م`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Hippius** (NetUID **75**) (`م`).

Blockchain-backed cloud: storage, VMs, and apps with unmatched transparency, trust, and power.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `62`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ37,779.461606597. **Alpha liquidity in pool (`alpha_in`)** = ‎1,601,695.772574658م‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,956,848.335368528م‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.023546688`** *(also **moving-average price** `0.023556157713755965` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,269,375.519351411م‎`. **Owner hotkey / coldkey (chain):** `5G1Qj93Fy22grpiGKq6BEvqqmS2HVRs3jaEdMhq9absQzs6g` / `5DAQpczEK4vzBn1waHkC4BZGqGPZ1dwPxKVsj36JDofHAw3a`.
- **Subnet registered at block:** `5102795` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎46.484536443م‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000م‎` · α-in `‎0.000000000م‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104373`
- **Liquidity constant `k`:** `60511203945433012055807818826`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Hippius` |
| Symbol (API) | `م` |
| Rank | `10` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.023547976` |
| Market cap | `95906272000473.929857552` |
| Market cap Δ 1d | `-0.085810883058705399` |
| Liquidity | `75496155189951` |
| Total τ | `37780499394282` |
| Total α | `4558311107943186` |
| α in pool | `1601651700157568` |
| α staked | `2471151499594034` |
| Price Δ 1h | `0.068379562453241634` |
| Price Δ 1d | `-0.190561284554041284` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `75` |
| Owner SS58 (API) | `5DAQpczEK4vzBn1waHkC4BZGqGPZ1dwPxKVsj36JDofHAw3a` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5102795` |
| Registration wall time | `2025-03-11T05:52:36Z` |
| Registration cost snapshot | `247485227056` |
| Active keys | `256` |
| Active validators | `13` |
| Active miners | `141` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `13` |
| Max validators (API) | `64` |
| Neuron reg. cost | `100000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Hippius - Decentralized Infrastructure Subnet

A comprehensive Bittensor subnet providing distributed storage, compute, and blockchain management capabilities.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Decentralized and transparent storage. Cloud solutions. Storage, virtual machines, apps backed by a blockchain for unmatched transparency and trust.

**Fetched document title:** Hippius – Decentralized Cloud Storage

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
| Registration recycle cost snapshot (`burn`) | τ0.100000000 |
| Owner SS58 (`owner_ss58`) | `5DAQpczEK4vzBn1waHkC4BZGqGPZ1dwPxKVsj36JDofHAw3a` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.100000000 / τ100.000000000 |
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

*Same content as **Overview → Repository README excerpt** above; see repo for full runbooks.*








#### CPU / GPU / RAM lines (automatic grep)

- - System specifications (CPU, memory, GPU)
- "params": ["5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKv3gB"],


*Primary README URL used: `https://raw.githubusercontent.com/thenervelab/thebrain/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://hippius.com/](https://hippius.com/)
- **GitHub:** [https://github.com/thenervelab/thebrain](https://github.com/thenervelab/thebrain)
- **Logo URL:** [https://hippius.com/logo.png](https://hippius.com/logo.png)
- **Contact:** hello@hippius.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.023547248 |
| 8104292 | 0.023547187 |
| 8104340 | 0.023547087 |
| 8104388 | 0.023565308 |
| 8104436 | 0.023546688 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

