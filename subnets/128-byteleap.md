# NetUID 128 — ByteLeap (`න`)

## Overview

**ByteLeap** (NetUID **128**) (`න`).

Pioneering the Future of Cloud & Blockchain

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `256`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,006.223111055. **Alpha liquidity in pool (`alpha_in`)** = ‎1,207,173.943674649න‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,093,243.975465547න‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003304118`** *(also **moving-average price** `0.0033066614996641874` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎74,002.142590420න‎`. **Owner hotkey / coldkey (chain):** `5FpsgU3JFa8S2GnngH92J9vtHHi4PYgZzxGXnwdFNwEwt9h8` / `5GgMeLFN4YssT6f9i9pZpRmczt8GYDsCZ1nYPiGRcTPWn3AA`.
- **Subnet registered at block:** `5856038` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎186.602306965න‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000න‎` · α-in `‎0.000000000න‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003304118`
- **Market cap:** `10343739933201.364912248`
- **Liquidity:** `7994868267471`
- **Total τ:** `4006223337268`
- **Total α:** `3300404919140196`
- **α in pool:** `1207173875207727`
- **α staked:** `1923386211690309`
- **Price Δ 1h:** `0.048478175888269462`
- **Price Δ 1d:** `-0.147899131221041205`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `41`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Pioneering the Future of Cloud & Blockchain

### Repository README excerpt *(everything before first `##` heading)*

# ByteLeap Miner - Bittensor SN128 Compute Network

ByteLeap Miner is the resource aggregation component of the ByteLeap distributed compute platform. Miners connect to the Bittensor network (SN128), aggregate worker resources, and earn rewards through active compute leases and computational challenges.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to byteleapai/byteleap-Miner development by creating an account on GitHub.

**Fetched document title:** GitHub - byteleapai/byteleap-Miner · GitHub

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
- **Owner SS58 (`owner_ss58`):** `5GgMeLFN4YssT6f9i9pZpRmczt8GYDsCZ1nYPiGRcTPWn3AA`

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

# ByteLeap Miner - Bittensor SN128 Compute Network

ByteLeap Miner is the resource aggregation component of the ByteLeap distributed compute platform. Miners connect to the Bittensor network (SN128), aggregate worker resources, and earn rewards through active compute leases and computational challenges.

---

## Scoring System

Miners earn rewards through two main factors:

---

### Prerequisites

- Python 3.8+
- Bittensor wallet with registered hotkey

---

### Installation

```bash

---

# Setup environment

python3 -m venv venv
source ./venv/bin/activate

---

# Install dependencies

pip install -r requirements.txt
```

---

### Running the Miner

**Start Miner** (aggregates workers, communicates with Bittensor):
```bash
python scripts/run_miner.py --config config/miner_config.yaml
```

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/byteleapai/byteleap-Miner/main/README.md`*

## On-chain identity — description


Pioneering the Future of Cloud & Blockchain

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/byteleapai/byteleap-Miner](https://github.com/byteleapai/byteleap-Miner)
- **Discord:** [https://discord.com/channels/799672011265015819/1387438124132733110](https://discord.com/channels/799672011265015819/1387438124132733110)
- **Logo URL:** [https://avatars.githubusercontent.com/u/217718200](https://avatars.githubusercontent.com/u/217718200)
- **Contact:** byteleap.ai@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.003302669 |
| 8104072 | 0.003304135 |
| 8104120 | 0.003304127 |
| 8104168 | 0.003304122 |
| 8104216 | 0.003304118 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

