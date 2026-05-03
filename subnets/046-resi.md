# NetUID 46 — RESI (`ץ`)

## Overview

**RESI** (NetUID **46**) (`ץ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `236`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ11,796.277330122. **Alpha liquidity in pool (`alpha_in`)** = ‎1,373,704.997081455ץ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,434,213.576051496ץ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008445558`** *(also **moving-average price** `0.00791119085624814` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,072,837.349017352ץ‎`. **Owner hotkey / coldkey (chain):** `5CDnZ6oeCrXKoL2VJQuQFxSfr49yQWz2DvdaYx47hr9QdM6D` / `5Ft9E2ovN52AVMczVA3713uXmmBPczvUboB4YQpupu3aEYg7`.
- **Subnet registered at block:** `3919107` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎177.659584005ץ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004222775` · α-out `‎1.000000000ץ‎` · α-in `‎0.500000000ץ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.008451983`
- **Market cap:** `34788403620350.446190179`
- **Liquidity:** `23406173032757`
- **Total τ:** `11800526293176`
- **Total α:** `4807879525881193`
- **α in pool:** `1373127080305445`
- **α staked:** `2742877840711368`
- **Price Δ 1h:** `0.455330270144798829`
- **Price Δ 1d:** `13.390564469346653308`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `4225969`
- **Max neurons:** `256`
- **Validators (metadata):** `10`
- **Neuron reg. cost:** `100000000`

### On-chain declared purpose *(SubnetIdentity)*

The Real Estate Oracle



**Additional commentary (on-chain)**


Real Estate Super Intelligence

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


*Primary README URL used: `https://raw.githubusercontent.com/resi-labs-ai/RESI-models/master/README.md`*

## On-chain identity — description


The Real Estate Oracle

## On-chain identity — additional field


Real Estate Super Intelligence

## Registered contact & links


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
| 8104085 | 0.008460764 |
| 8104133 | 0.008459277 |
| 8104181 | 0.008451742 |
| 8104229 | 0.008452272 |
| 8104277 | 0.008445558 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

