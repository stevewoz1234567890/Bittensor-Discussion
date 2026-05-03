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

- **Subnet name (API):** `RESI`
- **Symbol (API):** `ץ`
- **Rank:** `31`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.008451983`
- **Market cap:** `34788403620350.446190179`
- **Market cap Δ 1d:** `13.496040462420697134`
- **Liquidity:** `23406173032757`
- **Total τ:** `11800526293176`
- **Total α:** `4807879525881193`
- **α in pool:** `1373127080305445`
- **α staked:** `2742877840711368`
- **Price Δ 1h:** `0.455330270144798829`
- **Price Δ 1d:** `13.390564469346653308`
#### Subnet activity (TAOStats)

- **NetUID (API):** `46`
- **Owner SS58 (API):** `5Ft9E2ovN52AVMczVA3713uXmmBPczvUboB4YQpupu3aEYg7`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `3919107`
- **Registration wall time:** `2024-09-27T12:53:36Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `1`
- **Active dual-role:** `1`
- **Emission:** `4225969`
- **Max neurons:** `256`
- **Validator slots (metadata):** `10`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `100000000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

# RESI - Real Estate Price Prediction Subnet

**Subnet 46** on Bittensor Mainnet | [Dashboard](https://dashboard.resilabs.ai) | [Validator Guide](docs/VALIDATOR.md) | [Miner Guide](docs/MINER.md) | [Wandb](https://wandb.ai/resi-labs/subnet-46-evaluations-main) | [Twitter](https://x.com/resilabsai)

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** RESI is the institutional-grade intelligence layer for the future of PropTech.

**Fetched document title:** RESI

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
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.100000000
- **Owner SS58 (`owner_ss58`):** `5Ft9E2ovN52AVMczVA3713uXmmBPczvUboB4YQpupu3aEYg7`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.100000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

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

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.005019782 |
| 2026-03-10T23:59:48Z | 7718257 | 0.00476857 |
| 2026-03-11T23:59:48Z | 7725455 | 0.004761341 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.004620791 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004331648 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004404216 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005015663 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005156774 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005071705 |
| 2026-03-18T23:59:48Z | 7775819 | 0.004849018 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00466142795161254554 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004979021 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005244769 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005708483 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005735353 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.0056621648043646031 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005306477 |
| 2026-03-26T23:59:48Z | 7833396 | 0.005498123 |
| 2026-03-27T23:59:48Z | 7840596 | 0.005266298 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005579558 |
| 2026-03-29T23:59:48Z | 7854902 | 0.005395702 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.005776066 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005714329 |
| 2026-04-01T23:59:48Z | 7876474 | 0.005697817 |
| 2026-04-02T23:59:48Z | 7883622 | 0.005639315 |
| 2026-04-03T23:59:48Z | 7890794 | 0.005503114 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.006170795 |
| 2026-04-05T23:59:48Z | 7905188 | 0.006051261 |
| 2026-04-06T23:59:48Z | 7912388 | 0.006736197 |
| 2026-04-07T23:59:48Z | 7919588 | 0.006767259 |
| 2026-04-08T23:59:48Z | 7926788 | 0.006750467 |
| 2026-04-09T23:59:48Z | 7933987 | 0.0060292 |
| 2026-04-10T23:59:48Z | 7941184 | 0.006858893 |
| 2026-04-11T23:59:48Z | 7948384 | 0.006944502 |
| 2026-04-12T23:59:48Z | 7955584 | 0.007140761 |
| 2026-04-13T23:59:48Z | 7962784 | 0.006945733 |
| 2026-04-14T23:59:48Z | 7969979 | 0.006682123 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.007560284 |
| 2026-04-16T23:59:48Z | 7984379 | 0.00753381 |
| 2026-04-17T23:59:48Z | 7991579 | 0.008302429 |
| 2026-04-18T23:59:48Z | 7998779 | 0.008436973 |
| 2026-04-19T23:59:48Z | 8005979 | 0.008012044 |
| 2026-04-20T23:59:48Z | 8013179 | 0.007916975 |
| 2026-04-21T23:59:48Z | 8020376 | 0.007332018 |
| 2026-04-22T23:59:48Z | 8027562 | 0.00692804 |
| 2026-04-23T23:59:48Z | 8034762 | 0.00688483 |
| 2026-04-24T23:59:48Z | 8041962 | 0.006554937 |
| 2026-04-25T23:59:48Z | 8049151 | 0.006761913 |
| 2026-04-26T23:59:48Z | 8056274 | 0.006365766 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.006362566 |
| 2026-04-28T23:59:48Z | 8070646 | 0.006745896 |
| 2026-04-29T23:59:48Z | 8077790 | 0.007328574 |
| 2026-04-30T23:59:48Z | 8084984 | 0.007159693 |
| 2026-05-01T23:59:48Z | 8092168 | 0.007864933 |
| 2026-05-02T23:59:48Z | 8099357 | 0.007815017 |
| 2026-05-03T16:10:00Z | 8104202 | 0.008451983 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

