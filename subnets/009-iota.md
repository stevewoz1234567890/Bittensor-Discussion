# NetUID 9 — iota (`ι`)

## Overview

**iota** (NetUID **9**) (`ι`).

The world's first permissionless pipeline parallel training architecture

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `137`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ48,971.113578796. **Alpha liquidity in pool (`alpha_in`)** = ‎2,067,487.492779010ι‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,000,217.037386223ι‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.023687899`** *(also **moving-average price** `0.02373872767202556` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎716,759.281220080ι‎`. **Owner hotkey / coldkey (chain):** `5FsbubeciqtB5Nik3umL2iD4fG8FcC9GbT9nHJfXMj4mJJZ9` / `5FsbubeciqtB5Nik3umL2iD4fG8FcC9GbT9nHJfXMj4mJJZ9`.
- **Subnet registered at block:** `1489797` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎103.530895725ι‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ι‎` · α-in `‎0.000000000ι‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.023687901`
- **Market cap:** `99657330340595.317823304`
- **Liquidity:** `97945552626476`
- **Total τ:** `48971114841562`
- **Total α:** `5067691530165233`
- **α in pool:** `2067487439470224`
- **α staked:** `2139610958171480`
- **Price Δ 1h:** `-0.000996279276838022`
- **Price Δ 1d:** `-0.624530950482424862`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `11`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

The world's first permissionless pipeline parallel training architecture

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

## On-chain identity — description


The world's first permissionless pipeline parallel training architecture

## On-chain identity — additional field


*Unset.*

## Registered contact & links


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
| 8103976 | 0.023688115 |
| 8104024 | 0.023688103 |
| 8104072 | 0.023688086 |
| 8104120 | 0.023688063 |
| 8104168 | 0.023688045 |
| 8104216 | 0.023687899 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

