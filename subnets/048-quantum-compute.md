# NetUID 48 — Quantum Compute (`ק`)

## Overview

**Quantum Compute** (NetUID **48**) (`ק`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `176`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ11,708.809326655. **Alpha liquidity in pool (`alpha_in`)** = ‎2,183,397.605792405ק‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,589,939.634370637ק‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005391910`** *(also **moving-average price** `0.005304103717207909` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎644,708.379879276ק‎`. **Owner hotkey / coldkey (chain):** `5D2Qc9ud7vTJrPzk8mT1ruY8oV8UaDP3ttepD7zVNNi943ch` / `5GNH5YMkcX8jEF1PukvxKafifcqz13jp18BT73jRL3AZc4Rc`.
- **Subnet registered at block:** `3856677` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎132.420363864ק‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ק‎` · α-in `‎0.000000000ק‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.00539191`
- **Market cap:** `22143025960247.3328735`
- **Liquidity:** `23481492711293`
- **Total τ:** `11708809619283`
- **Total α:** `4773324240163042`
- **α in pool:** `2183397551519015`
- **α staked:** `1923315275706835`
- **Price Δ 1h:** `1.236753760767850035`
- **Price Δ 1d:** `-1.259294636781233679`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `6`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Quantum Computing

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Decentralized deep tech. Innovation from everywhere. Quantum computing, AI, and decentralized networks powered by Bittensor.

**Fetched document title:** qBitTensor Labs — Decentralized Deep Tech

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
- **`immunity_period` (blocks):** 2000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5GNH5YMkcX8jEF1PukvxKafifcqz13jp18BT73jRL3AZc4Rc`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `2000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `3`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Validators

To set up a Validator please see [validator.md](qbittensor/validator/validator.md).

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/qbittensor-labs/quantum-compute/main/README.md`*

## On-chain identity — description


Quantum Computing

## On-chain identity — additional field


*Unset.*

## Registered contact & links


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
| 8104024 | 0.005326032 |
| 8104072 | 0.005326028 |
| 8104120 | 0.005370669 |
| 8104168 | 0.005391913 |
| 8104216 | 0.00539191 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

