# NetUID 68 — NOVA (`ظ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**NOVA** (NetUID **68**) (`ظ`).

Accelerating drug discovery.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `55`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ36,644.008185232. **Alpha liquidity in pool (`alpha_in`)** = ‎2,019,483.831463273ظ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,818,374.131828793ظ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.018144398`** *(also **moving-average price** `0.018111180048435926` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,369,222.959728592ظ‎`. **Owner hotkey / coldkey (chain):** `5CSuegTfX4Gf7SoXXJoPEyMEicXBjm5Z1QgoPPcU424rQbbb` / `5EcdJLAeYoxM3Tsf5VZ3NQPenPku218gqnjSoo3iJNy4V12V`.
- **Subnet registered at block:** `4972413` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎41.423000944ظ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.009072198` · α-out `‎1.000000000ظ‎` · α-in `‎0.500000000ظ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104380`
- **Liquidity constant `k`:** `74001982050083856587788984336`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `NOVA` |
| Symbol (API) | `ظ` |
| Rank | `12` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.018144322` |
| Market cap | `77416824124981.66712384` |
| Market cap Δ 1d | `-0.648989834150088384` |
| Liquidity | `73281945468262` |
| Total τ | `36641817236475` |
| Total α | `4837515522060466` |
| α in pool | `2019371582569343` |
| α staked | `2247352967677377` |
| Price Δ 1h | `0.047525039420859506` |
| Price Δ 1d | `-0.822154660579085795` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `68` |
| Owner SS58 (API) | `5EcdJLAeYoxM3Tsf5VZ3NQPenPku218gqnjSoo3iJNy4V12V` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4972413` |
| Registration wall time | `2025-02-21T03:15:12.001Z` |
| Registration cost snapshot | `199768252064` |
| Active keys | `64` |
| Active validators | `6` |
| Active miners | `3` |
| Active dual-role | `0` |
| Emission | `9072161` |
| Max neurons | `64` |
| Validator slots (metadata) | `6` |
| Max validators (API) | `64` |
| Neuron reg. cost | `141653716` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** METANOVA LABS is a crypto-native biotech company at the forefront of drug discovery. We are developing next generation therapeutics that regulate mental states and restore critical biological processes.

**Fetched document title:** Metanova Labs

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 64 |
| `subnetwork_n` | 64 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.089753096 |
| Owner SS58 (`owner_ss58`) | `5EcdJLAeYoxM3Tsf5VZ3NQPenPku218gqnjSoo3iJNy4V12V` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `1` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.metanova-labs.ai](https://www.metanova-labs.ai)
- **GitHub:** [https://github.com/metanova-labs/nova/](https://github.com/metanova-labs/nova/)
- **Logo URL:** [https://raw.githubusercontent.com/metanova-labs/nova/refs/heads/main/assets/subnet-logo.png](https://raw.githubusercontent.com/metanova-labs/nova/refs/heads/main/assets/subnet-logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.018144296 |
| 8104292 | 0.018144219 |
| 8104340 | 0.018144347 |
| 8104388 | 0.01814437 |
| 8104436 | 0.018144399 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.013840065 |
| 2026-03-10T23:59:48Z | — | 0.013907116 |
| 2026-03-11T23:59:48Z | — | 0.014084052 |
| 2026-03-12T23:59:48Z | — | 0.01501682 |
| 2026-03-13T23:59:48Z | — | 0.015738321 |
| 2026-03-14T23:59:48Z | — | 0.018059707 |
| 2026-03-15T23:59:48Z | — | 0.018664951 |
| 2026-03-16T23:59:48Z | — | 0.017121727 |
| 2026-03-17T23:59:48Z | — | 0.017065796 |
| 2026-03-18T23:59:48Z | — | 0.017069551 |
| 2026-03-19T23:59:48Z | — | 0.0174377566203 |
| 2026-03-20T23:59:48Z | — | 0.018170698 |
| 2026-03-21T23:59:48Z | — | 0.017651077 |
| 2026-03-22T23:59:48Z | — | 0.017863398 |
| 2026-03-23T23:59:48Z | — | 0.019340727 |
| 2026-03-24T23:59:48Z | — | 0.021190424485 |
| 2026-03-25T23:59:48Z | — | 0.021101577 |
| 2026-03-26T23:59:48Z | — | 0.019798476 |
| 2026-03-27T23:59:48Z | — | 0.018987454 |
| 2026-03-28T23:59:48Z | — | 0.019449019 |
| 2026-03-29T23:59:48Z | — | 0.020880866 |
| 2026-03-30T23:59:48Z | — | 0.01988991 |
| 2026-03-31T23:59:48Z | — | 0.020455833 |
| 2026-04-01T23:59:48Z | — | 0.020907998 |
| 2026-04-02T23:59:48Z | — | 0.019326655 |
| 2026-04-03T23:59:48Z | — | 0.019804262 |
| 2026-04-04T23:59:48Z | — | 0.020359935 |
| 2026-04-05T23:59:48Z | — | 0.019255266 |
| 2026-04-06T23:59:48Z | — | 0.019647776 |
| 2026-04-07T23:59:48Z | — | 0.020033713 |
| 2026-04-08T23:59:48Z | — | 0.019557568 |
| 2026-04-09T23:59:48Z | — | 0.018527039 |
| 2026-04-10T23:59:48Z | — | 0.017476984 |
| 2026-04-11T23:59:48Z | — | 0.017884536 |
| 2026-04-12T23:59:48Z | — | 0.018034255 |
| 2026-04-13T23:59:48Z | — | 0.017172659 |
| 2026-04-14T23:59:48Z | — | 0.017209607 |
| 2026-04-15T23:59:48Z | — | 0.01741249 |
| 2026-04-16T23:59:48Z | — | 0.016925965 |
| 2026-04-17T23:59:48Z | — | 0.016810096 |
| 2026-04-18T23:59:48Z | — | 0.016793726 |
| 2026-04-19T23:59:48Z | — | 0.016538118 |
| 2026-04-20T23:59:48Z | — | 0.016558534 |
| 2026-04-21T23:59:48Z | — | 0.016416344 |
| 2026-04-22T23:59:48Z | — | 0.016358458 |
| 2026-04-23T23:59:48Z | — | 0.017010385 |
| 2026-04-24T23:59:48Z | — | 0.016802285 |
| 2026-04-25T23:59:48Z | — | 0.016750438 |
| 2026-04-26T23:59:48Z | — | 0.016508554 |
| 2026-04-27T23:59:48Z | — | 0.016792803 |
| 2026-04-28T23:59:48Z | — | 0.016623458 |
| 2026-04-29T23:59:48Z | — | 0.017054322 |
| 2026-04-30T23:59:48Z | — | 0.017691333 |
| 2026-05-01T23:59:48Z | — | 0.017397609 |
| 2026-05-02T23:59:48Z | — | 0.018247804 |
| 2026-05-03T23:59:48Z | — | 0.018144322 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

