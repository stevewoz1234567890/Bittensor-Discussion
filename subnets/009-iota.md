# NetUID 9 — iota (`ι`)

## Overview

**iota** (NetUID **9**) (`ι`).

The world's first permissionless pipeline parallel training architecture

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `199`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ48,971.017925281. **Alpha liquidity in pool (`alpha_in`)** = ‎2,067,491.530863968ι‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,000,274.999301265ι‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.023687807`** *(also **moving-average price** `0.023737830109894276` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎716,759.376873595ι‎`. **Owner hotkey / coldkey (chain):** `5FsbubeciqtB5Nik3umL2iD4fG8FcC9GbT9nHJfXMj4mJJZ9` / `5FsbubeciqtB5Nik3umL2iD4fG8FcC9GbT9nHJfXMj4mJJZ9`.
- **Subnet registered at block:** `1489797` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎150.384265524ι‎`; pending root emission `τ0.000000000`.
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
| 8104037 | 0.023688095 |
| 8104085 | 0.023688083 |
| 8104133 | 0.023688057 |
| 8104181 | 0.023687909 |
| 8104229 | 0.023687852 |
| 8104277 | 0.023687807 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.028170584 |
| 2026-03-10T23:59:48Z | 7718257 | 0.027965406 |
| 2026-03-11T23:59:48Z | 7725455 | 0.028046979 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.028001949 |
| 2026-03-13T23:59:48Z | 7739841 | 0.027745335 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.027805417 |
| 2026-03-15T23:59:48Z | 7754226 | 0.027876657 |
| 2026-03-16T23:59:48Z | 7761426 | 0.028120113 |
| 2026-03-17T23:59:48Z | 7768619 | 0.028452994 |
| 2026-03-18T23:59:48Z | 7775819 | 0.028151728 |
| 2026-03-19T23:59:48Z | 7783014 | 0.02802165628897722379 |
| 2026-03-20T23:59:48Z | 7790201 | 0.029355291 |
| 2026-03-21T23:59:48Z | 7797398 | 0.029166649 |
| 2026-03-22T23:59:48Z | 7804598 | 0.02923899 |
| 2026-03-23T23:59:48Z | 7811798 | 0.031337427 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.03287854360338058721 |
| 2026-03-25T23:59:48Z | 7826196 | 0.032232037 |
| 2026-03-26T23:59:48Z | 7833396 | 0.031155857 |
| 2026-03-27T23:59:48Z | 7840596 | 0.029576489 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.02928002 |
| 2026-03-29T23:59:48Z | 7854902 | 0.029077056 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.028386471 |
| 2026-03-31T23:59:48Z | 7869291 | 0.027097379 |
| 2026-04-01T23:59:48Z | 7876474 | 0.026593312 |
| 2026-04-02T23:59:48Z | 7883622 | 0.024903037 |
| 2026-04-03T23:59:48Z | 7890794 | 0.023955946 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.023902887 |
| 2026-04-05T23:59:48Z | 7905188 | 0.024219356 |
| 2026-04-06T23:59:48Z | 7912388 | 0.024104069 |
| 2026-04-07T23:59:48Z | 7919588 | 0.023968396 |
| 2026-04-08T23:59:48Z | 7926788 | 0.023534272 |
| 2026-04-09T23:59:48Z | 7933987 | 0.023033174 |
| 2026-04-10T23:59:48Z | 7941184 | 0.022241229 |
| 2026-04-11T23:59:48Z | 7948384 | 0.022737405 |
| 2026-04-12T23:59:48Z | 7955584 | 0.022741569 |
| 2026-04-13T23:59:48Z | 7962784 | 0.024461706 |
| 2026-04-14T23:59:48Z | 7969979 | 0.024018785 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.023521774 |
| 2026-04-16T23:59:48Z | 7984379 | 0.02329759 |
| 2026-04-17T23:59:48Z | 7991579 | 0.023820018 |
| 2026-04-18T23:59:48Z | 7998779 | 0.023691052 |
| 2026-04-19T23:59:48Z | 8005979 | 0.023841285 |
| 2026-04-20T23:59:48Z | 8013179 | 0.023919095 |
| 2026-04-21T23:59:48Z | 8020376 | 0.023873129 |
| 2026-04-22T23:59:48Z | 8027562 | 0.023829252 |
| 2026-04-23T23:59:48Z | 8034762 | 0.023755874 |
| 2026-04-24T23:59:48Z | 8041962 | 0.023635317 |
| 2026-04-25T23:59:48Z | 8049151 | 0.023611307 |
| 2026-04-26T23:59:48Z | 8056274 | 0.023587284 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.023669186 |
| 2026-04-28T23:59:48Z | 8070646 | 0.023662898 |
| 2026-04-29T23:59:48Z | 8077790 | 0.023628771 |
| 2026-04-30T23:59:48Z | 8084984 | 0.023569551 |
| 2026-05-01T23:59:48Z | 8092168 | 0.02377557 |
| 2026-05-02T23:59:48Z | 8099357 | 0.023812093 |
| 2026-05-03T16:10:00Z | 8104202 | 0.023687901 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

