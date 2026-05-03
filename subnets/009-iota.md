# NetUID 9 — iota (`ι`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**iota** (NetUID **9**) (`ι`).

The world's first permissionless pipeline parallel training architecture

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `357`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ48,966.735502893. **Alpha liquidity in pool (`alpha_in`)** = ‎2,067,672.332608332ι‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,000,252.197556901ι‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.023683665`** *(also **moving-average price** `0.023735565831884742` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎716,763.659295983ι‎`. **Owner hotkey / coldkey (chain):** `5FsbubeciqtB5Nik3umL2iD4fG8FcC9GbT9nHJfXMj4mJJZ9` / `5FsbubeciqtB5Nik3umL2iD4fG8FcC9GbT9nHJfXMj4mJJZ9`.
- **Subnet registered at block:** `1489797` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎269.785281949ι‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ι‎` · α-in `‎0.000000000ι‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104078`
- **Liquidity constant `k`:** `101247164217481994198421904476`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `iota`
- **Symbol (API):** `ι`
- **Rank:** `8`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.023687901`
- **Market cap:** `99657330340595.317823304`
- **Market cap Δ 1d:** `-0.524282011840386968`
- **Liquidity:** `97945552626476`
- **Total τ:** `48971114841562`
- **Total α:** `5067691530165233`
- **α in pool:** `2067487439470224`
- **α staked:** `2139610958171480`
- **Price Δ 1h:** `-0.000996279276838022`
- **Price Δ 1d:** `-0.624530950482424862`
#### Subnet activity (TAOStats)

- **NetUID (API):** `9`
- **Owner SS58 (API):** `5FsbubeciqtB5Nik3umL2iD4fG8FcC9GbT9nHJfXMj4mJJZ9`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `1489797`
- **Registration wall time:** `2023-10-14T15:06:24.004Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `11`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# IOTA

</div>

**I**ncentivized **O**rchestrated **T**raining **A**rchitecture (IOTA) is a framework for pretraining large language models across a network of heterogeneous, unreliable, permissionless and token incentivized machines. IOTA employs a data- and pipeline-parallel architecture to accelerate training and reduce hardware requirements for participants.

<div align="center">

<a href="https://iota.macrocosmos.ai">
  <img src="./docs/assets/iota-page.png" alt="iota" width="600"/>
</a>

</div>

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Incentivised Orchestrated Training Architecture from Macrocosmos.ai

**Fetched document title:** IOTA | Macrocosmos.ai

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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5FsbubeciqtB5Nik3umL2iD4fG8FcC9GbT9nHJfXMj4mJJZ9`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
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

## Installation

1. First install uv (<https://docs.astral.sh/uv/>)
2. Run `bash setup.sh` and choose Miner or Validator
3. Configure your `.env` file

---

## Additional Miner Documentation

Running the miner is as easy as `bash ./start_miner.sh`. For more information, reference [the official miner docs](https://docs.macrocosmos.ai/subnets/subnet-9-pre-training/subnet-9-iota-mining-setup-guide).

Use PM2 to run the miner in the background: `pm2 start pm2/miner.config.js`

---

## Compute Requirements

The runs are currently in bfloat16, resulting in a total footprint of ~2GB for a 1B parameter model. As such, we recommend:

1. Cuda GPU with >= 16GB VRAM (RTX 4090, for example).
2. Ubuntu 22.04 (Jammy)

---

#### CPU / GPU / RAM lines (automatic grep)

- The runs are currently in bfloat16, resulting in a total footprint of ~2GB for a 1B parameter model. As such, we recommend:
- 1. Cuda GPU with >= 16GB VRAM (RTX 4090, for example).


*Primary README URL used: `https://raw.githubusercontent.com/macrocosm-os/iota/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://iota.macrocosmos.ai/](https://iota.macrocosmos.ai/)
- **GitHub:** [https://github.com/macrocosm-os/iota](https://github.com/macrocosm-os/iota)
- **Discord (handle / invite hint):** `macrocrux`
- **Logo URL:** [https://www.macrocosmos.ai/images/mc_logo_black.png](https://www.macrocosmos.ai/images/mc_logo_black.png)
- **Contact:** support@macrocosmos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.023687905 |
| 8104244 | 0.023687839 |
| 8104292 | 0.0236878 |
| 8104340 | 0.023686586 |
| 8104388 | 0.023686581 |
| 8104436 | 0.023683665 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

