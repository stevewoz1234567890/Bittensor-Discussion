# NetUID 46 — RESI (`ץ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**RESI** (NetUID **46**) (`ץ`).

The Real Estate Oracle



#### SubnetIdentity `additional` *(chain)*



Real Estate Super Intelligence

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `33`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ11,801.590136428. **Alpha liquidity in pool (`alpha_in`)** = ‎1,373,234.057926753ץ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,434,769.121995518ץ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008452095`** *(also **moving-average price** `0.007933907676488161` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,072,979.833113185ץ‎`. **Owner hotkey / coldkey (chain):** `5CDnZ6oeCrXKoL2VJQuQFxSfr49yQWz2DvdaYx47hr9QdM6D` / `5Ft9E2ovN52AVMczVA3713uXmmBPczvUboB4YQpupu3aEYg7`.
- **Subnet registered at block:** `3919107` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎24.842369143ץ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004226042` · α-out `‎1.000000000ץ‎` · α-in `‎0.500000000ץ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104402`
- **Liquidity constant `k`:** `16206345513035364992101058284`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `RESI` |
| Symbol (API) | `ץ` |
| Rank | `31` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.008451983` |
| Market cap | `34788403620350.446190179` |
| Market cap Δ 1d | `13.496040462420697134` |
| Liquidity | `23406173032757` |
| Total τ | `11800526293176` |
| Total α | `4807879525881193` |
| α in pool | `1373127080305445` |
| α staked | `2742877840711368` |
| Price Δ 1h | `0.455330270144798829` |
| Price Δ 1d | `13.390564469346653308` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `46` |
| Owner SS58 (API) | `5Ft9E2ovN52AVMczVA3713uXmmBPczvUboB4YQpupu3aEYg7` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3919107` |
| Registration wall time | `2024-09-27T12:53:36Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `10` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `4225969` |
| Max neurons | `256` |
| Validator slots (metadata) | `10` |
| Max validators (API) | `64` |
| Neuron reg. cost | `100000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# RESI - Real Estate Price Prediction Subnet

**Subnet 46** on Bittensor Mainnet | [Dashboard](https://dashboard.resilabs.ai) | [Validator Guide](docs/VALIDATOR.md) | [Miner Guide](docs/MINER.md) | [Wandb](https://wandb.ai/resi-labs/subnet-46-evaluations-main) | [Twitter](https://x.com/resilabsai)

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** RESI is the institutional-grade intelligence layer for the future of PropTech.

**Fetched document title:** RESI

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
| Registration recycle cost snapshot (`burn`) | τ0.100000000 |
| Owner SS58 (`owner_ss58`) | `5Ft9E2ovN52AVMczVA3713uXmmBPczvUboB4YQpupu3aEYg7` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.100000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `10800` blocks |
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
| `yuma_version` | `3` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### For Validators

See the [Validator Setup Guide](docs/VALIDATOR.md) for complete setup instructions.

---

### For Miners

See the [Miner Guide](docs/MINER.md) for complete setup instructions.

---

---

## Model Requirements

| Requirement | Specification |
|-------------|---------------|
| **Format** | ONNX (`.onnx` file) |
| **Max Size** | 200 MB |
| **License** | MIT (verified via HuggingFace metadata) |
| **Commit Age** | Must be committed ~30 days before evaluation |
| **Input** | Property features (see documentation) |
| **Output** | Predicted price in USD |

---

---

### Prerequisites

- Python >=3.11, <3.14
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager
- Docker (for validators)

---

### Install

```bash

---

# Install uv

curl -LsSf https://astral.sh/uv/install.sh | sh

---

# Clone and setup

git clone https://github.com/resi-labs-ai/RESI-models.git
cd RESI-models
uv sync

---









#### CPU / GPU / RAM lines (automatic grep)

- `| **Non-winners** | 1% | Shared proportionally by score among valid models |`
- `| **Max Size** | 200 MB |`


*Primary README URL used: `https://raw.githubusercontent.com/resi-labs-ai/RESI-models/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://resilabs.ai](https://resilabs.ai)
- **GitHub:** [https://github.com/resi-labs-ai/RESI-models](https://github.com/resi-labs-ai/RESI-models)
- **Discord:** [https://discord.gg/9Hxmh7H6Pt](https://discord.gg/9Hxmh7H6Pt)
- **Logo URL:** [https://resi-public.nyc3.cdn.digitaloceanspaces.com/color_3_r.png](https://resi-public.nyc3.cdn.digitaloceanspaces.com/color_3_r.png)
- **Contact:** support@resilabs.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.008451915 |
| 8104244 | 0.008452293 |
| 8104292 | 0.008446431 |
| 8104340 | 0.008446391 |
| 8104388 | 0.008426605 |
| 8104436 | 0.008452107 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.004002021 --> 0.00878161
    line [0.005019782, 0.00476857, 0.004761341, 0.004620791, 0.004331648, 0.004404216, 0.005015663, 0.005156774, 0.005071705, 0.004849018, 0.00466142795161, 0.004979021, 0.005244769, 0.005708483, 0.005735353, 0.00566216480436, 0.005306477, 0.005498123, 0.005266298, 0.005579558, 0.005395702, 0.005776066, 0.005714329, 0.005697817, 0.005639315, 0.005503114, 0.006170795, 0.006051261, 0.006736197, 0.006767259, 0.006750467, 0.0060292, 0.006858893, 0.006944502, 0.007140761, 0.006945733, 0.006682123, 0.007560284, 0.00753381, 0.008302429, 0.008436973, 0.008012044, 0.007916975, 0.007332018, 0.00692804, 0.00688483, 0.006554937, 0.006761913, 0.006365766, 0.006362566, 0.006745896, 0.007328574, 0.007159693, 0.007864933, 0.007815017, 0.008451983]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

