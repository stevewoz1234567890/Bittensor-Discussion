# NetUID 68 — NOVA (`ظ`)

## Overview

**NOVA** (NetUID **68**) (`ظ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `196`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ36,641.941713993. **Alpha liquidity in pool (`alpha_in`)** = ‎2,019,377.722159077ظ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,818,156.884704262ظ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.018144328`** *(also **moving-average price** `0.0181091062258929` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,369,222.111178082ظ‎`. **Owner hotkey / coldkey (chain):** `5CSuegTfX4Gf7SoXXJoPEyMEicXBjm5Z1QgoPPcU424rQbbb` / `5EcdJLAeYoxM3Tsf5VZ3NQPenPku218gqnjSoo3iJNy4V12V`.
- **Subnet registered at block:** `4972413` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎147.615231439ظ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.009072164` · α-out `‎1.000000000ظ‎` · α-in `‎0.500000000ظ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.018144322`
- **Market cap:** `77416824124981.66712384`
- **Liquidity:** `73281945468262`
- **Total τ:** `36641817236475`
- **Total α:** `4837515522060466`
- **α in pool:** `2019371582569343`
- **α staked:** `2247352967677377`
- **Price Δ 1h:** `0.047525039420859506`
- **Price Δ 1d:** `-0.822154660579085795`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `64`
- **Active validators:** `6`
- **Active miners:** `3`
- **Active dual:** `0`
- **Emission:** `9072161`
- **Max neurons:** `64`
- **Validators (metadata):** `6`
- **Neuron reg. cost:** `141653716`

### On-chain declared purpose *(SubnetIdentity)*

Accelerating drug discovery.

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** METANOVA LABS is a crypto-native biotech company at the forefront of drug discovery. We are developing next generation therapeutics that regulate mental states and restore critical biological processes.

**Fetched document title:** Metanova Labs

## Operational parameters — registration, limits, economics (chain)


### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 64
- **`subnetwork_n`:** 64
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.137092167
- **Owner SS58 (`owner_ss58`):** `5EcdJLAeYoxM3Tsf5VZ3NQPenPku218gqnjSoo3iJNy4V12V`

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
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `1`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## System Requirements for validators

- Ubuntu 24.04 LTS (recommended)
- Python 3.10 - 3.12
- CUDA 12.6 (for GPU support)
- Sufficient RAM for ML model operations
- 2 GPU devices for parallel inference. If only one is available, inference will run sequentially which may result in delayed/missing scoring rounds.
- Internet connection for network participation

---

## Installation and Running

1. Clone the repository:
```bash
git clone --recurse-submodules https://github.com/metanova-labs/nova.git
cd nova
```

2. Prepare your .env file as in example.env:
```

---

# GitHub configs - FOR MINERS

GITHUB_REPO_NAME="repo-name"
GITHUB_REPO_BRANCH="repo-branch"
GITHUB_REPO_OWNER="repo-owner"
GITHUB_REPO_PATH="" # path within repo or ""

---

# For validators

VALIDATOR_API_KEY="your_api_key"
AUTO_UPDATE="1" # Set to "0" to disable auto-updates (not recommended)
```

3. Install dependencies:
   ```bash
   ./install_deps.sh [--cuda <version>]  #cuda version is optional, default is 12.6
   ```

4. Run:
```bash

---

# Activate your virtual environment:

source .venv/bin/activate

---

# miner:

python3 neurons/miner.py --wallet.name <your_wallet> --wallet.hotkey <your_hotkey> --logging.info

---

# validator:

python3 neurons/validator/validator.py --wallet.name <your_wallet> --wallet.hotkey <your_hotkey> --logging.debug
```

---

## For Validators

DM the NOVA team to obtain an API key.

---

#### CPU / GPU / RAM lines (automatic grep)

- - CUDA 12.6 (for GPU support)
- - Sufficient RAM for ML model operations
- - 2 GPU devices for parallel inference. If only one is available, inference will run sequentially which may result in delayed/missing scoring rounds.
- DEVICE_OVERRIDE="cpu" # None to run on GPU
- ./install_deps.sh [--cuda <version>]  #cuda version is optional, default is 12.6


*Primary README URL used: `https://raw.githubusercontent.com/metanova-labs/nova/main/README.md`*

## On-chain identity — description


Accelerating drug discovery.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.metanova-labs.ai](https://www.metanova-labs.ai)
- **GitHub:** [https://github.com/metanova-labs/nova/](https://github.com/metanova-labs/nova/)
- **Logo URL:** [https://raw.githubusercontent.com/metanova-labs/nova/refs/heads/main/assets/subnet-logo.png](https://raw.githubusercontent.com/metanova-labs/nova/refs/heads/main/assets/subnet-logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.018136397 |
| 8104072 | 0.018136617 |
| 8104120 | 0.018143922 |
| 8104168 | 0.018144198 |
| 8104216 | 0.018144328 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

