# NetUID 64 — Chutes (`ش`)

## Overview

**Chutes** (NetUID **64**) (`ش`).

Breakthrough Serverless Compute for AI, At Scale.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `192`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ206,267.085424404. **Alpha liquidity in pool (`alpha_in`)** = ‎2,629,877.961826892ش‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,496,899.567374286ش‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.078462810`** *(also **moving-average price** `0.07899130182340741` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎4,471,569.698851922ش‎`. **Owner hotkey / coldkey (chain):** `5F4Q3cA8EvApwhBj4eLjbb1meiLtzKgWhkF5JLRMNhRfqULc` / `5FRYKhbmfXPDoHdUUDMx27E3HuMvAzwjzFMMq3rNurUhAyS9`.
- **Subnet registered at block:** `4531295` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎145.214585697ش‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ش‎` · α-in `‎0.000000000ش‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.078462815`
- **Market cap:** `386771185380278.13065187`
- **Liquidity:** `412614713415796`
- **Total τ:** `206267089613796`
- **Total α:** `5126764529201178`
- **α in pool:** `2629877908433451`
- **α staked:** `2299478569285047`
- **Price Δ 1h:** `-0.198362312101951741`
- **Price Δ 1d:** `-1.164869914092478222`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `27`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Breakthrough Serverless Compute for AI, At Scale.



**Additional commentary (on-chain)**


Chutes is a subnet operated by Chutes Global Corp, an International Business Corporation registered in Nevis with registration number C 61974

### Repository README excerpt *(everything before first `##` heading)*

# Chutes!

This package provides the command line interface and development kit for use with the chutes.ai platform.

The miner code is available [here](https://github.com/rayonlabs/chutes-miner), and validator/API code [here](https://github.com/rayonlabs/chutes-api).

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Deploy, scale, and run top open-source AI models with serverless GPU compute from Chutes. Explore always-on LLM, image, speech, and video models built for production workloads.

**Fetched document title:** Chutes | Serverless AI Compute for Open-Source Models

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
- **Owner SS58 (`owner_ss58`):** `5FRYKhbmfXPDoHdUUDMx27E3HuMvAzwjzFMMq3rNurUhAyS9`

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

#### max_instances (int, default=1)

Maximum number of instances that can be active at a time.

---

#### CPU / GPU / RAM lines (automatic grep)

- - Contain a cuda installation, preferably version 12.2-12.6
- GraVal is the graphics card validation library used to help ensure the GPUs that miners claim to be running are authentic/correct.
- The library performs VRAM capacity checks, matrix multiplications seeded by device information, etc.
- This SDK includes an image creation helper library as well, and we have a recommended base image which includes python 3.12 and all necessary cuda packages: `parachutes/python:3.12`
- You are charged a one-time deployment fee per chute, equivalent to 3 times the hourly rate based on the node selector (meaning, `gpu_count` * cheapest compatible GPU type hourly rate). There is no deployment fee for any updates to existing chutes. See https://api.chutes.ai/pricing for current GPU rates (subject to change).
- The most important fields are `gpu_count` and `min_vram_gb_per_gpu`.  If you wish to include specific GPUs, you can do so, where the `include` (or `exclude`) fields are the short identifier per model, e.g. `"a6000"`, `"a100"`, etc.  [All supported GPUs, their short identifiers, and current pricing](https://api.chutes.ai/pricing)
- You can also set `max_hourly_price_per_gpu` to cap the per-GPU hourly rate. For example, `max_hourly_price_per_gpu=1.50` will exclude any GPU type that costs more than $1.50/hr. This is useful when you want to control costs without having to manually specify `include`/`exclude` lists. The value must be greater than 0 and less than 10.
- All user-created chutes are billed based on the actual GPU type each instance is running on: https://api.chutes.ai/pricing
- For example, if your chute's node selector allows both a100 and h100, an instance running on an a100 is billed at the a100 hourly rate, and an instance running on an h100 is billed at the h100 hourly rate.
- Deployment fee: You are charged a one-time deployment fee per chute, equivalent to 3 times the hourly rate based on the node selector (meaning, `gpu_count` * cheapest compatible GPU type hourly rate). No deployment fee for any updates to existing chutes.
- You are charged the actual hourly rate of the GPU your instance is running on while any instance is hot, up through last request timestamp + `shutdown_after_seconds`. See https://api.chutes.ai/pricing for current GPU rates (subject to change).
- For example, suppose the GPU your instance lands on costs $0.50/hr (see https://api.chutes.ai/pricing for current rates):
- Image(username="chutes", name="foo", tag="0.1", readme="## Base python+cuda image for chutes")


*Primary README URL used: `https://raw.githubusercontent.com/chutesai/chutes/main/README.md`*

## On-chain identity — description


Breakthrough Serverless Compute for AI, At Scale.

## On-chain identity — additional field


Chutes is a subnet operated by Chutes Global Corp, an International Business Corporation registered in Nevis with registration number C 61974

## Registered contact & links


- **Website:** [https://chutes.ai](https://chutes.ai)
- **GitHub:** [https://github.com/chutesai/chutes](https://github.com/chutesai/chutes)
- **Discord:** [https://discord.gg/chutes](https://discord.gg/chutes)
- **Logo URL:** [https://storage.googleapis.com/chutes-random/logo-chutes.png](https://storage.googleapis.com/chutes-random/logo-chutes.png)
- **Contact:** support@chutes.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.078619049 |
| 8104072 | 0.078612155 |
| 8104120 | 0.078452241 |
| 8104168 | 0.07844972 |
| 8104216 | 0.07846281 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.095066844 |
| 2026-03-10T23:59:48Z | 7718257 | 0.092855538 |
| 2026-03-11T23:59:48Z | 7725455 | 0.090705135 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.093865455 |
| 2026-03-13T23:59:48Z | 7739841 | 0.091041652 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.090614953 |
| 2026-03-15T23:59:48Z | 7754226 | 0.090630919 |
| 2026-03-16T23:59:48Z | 7761426 | 0.091024506 |
| 2026-03-17T23:59:48Z | 7768619 | 0.091051454 |
| 2026-03-18T23:59:48Z | 7775819 | 0.088670182 |
| 2026-03-19T23:59:48Z | 7783014 | 0.0876271028382086398 |
| 2026-03-20T23:59:48Z | 7790201 | 0.088282293 |
| 2026-03-21T23:59:48Z | 7797398 | 0.091325947 |
| 2026-03-22T23:59:48Z | 7804598 | 0.089083183 |
| 2026-03-23T23:59:48Z | 7811798 | 0.08861654 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.08630003056206187644 |
| 2026-03-25T23:59:48Z | 7826196 | 0.088014381 |
| 2026-03-26T23:59:48Z | 7833396 | 0.088243578 |
| 2026-03-27T23:59:48Z | 7840596 | 0.087751783 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.086899739 |
| 2026-03-29T23:59:48Z | 7854902 | 0.085904573 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.086585199 |
| 2026-03-31T23:59:48Z | 7869291 | 0.086752105 |
| 2026-04-01T23:59:48Z | 7876474 | 0.086814521 |
| 2026-04-02T23:59:48Z | 7883622 | 0.08822558 |
| 2026-04-03T23:59:48Z | 7890794 | 0.087270536 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.087669311 |
| 2026-04-05T23:59:48Z | 7905188 | 0.087891039 |
| 2026-04-06T23:59:48Z | 7912388 | 0.087114764 |
| 2026-04-07T23:59:48Z | 7919588 | 0.085846834 |
| 2026-04-08T23:59:48Z | 7926788 | 0.08497512 |
| 2026-04-09T23:59:48Z | 7933987 | 0.081975335 |
| 2026-04-10T23:59:48Z | 7941184 | 0.082812321 |
| 2026-04-11T23:59:48Z | 7948384 | 0.082587459 |
| 2026-04-12T23:59:48Z | 7955584 | 0.086585504 |
| 2026-04-13T23:59:48Z | 7962784 | 0.087317482 |
| 2026-04-14T23:59:48Z | 7969979 | 0.086232366 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.08460036 |
| 2026-04-16T23:59:48Z | 7984379 | 0.083371927 |
| 2026-04-17T23:59:48Z | 7991579 | 0.085499873 |
| 2026-04-18T23:59:48Z | 7998779 | 0.084394924 |
| 2026-04-19T23:59:48Z | 8005979 | 0.083571147 |
| 2026-04-20T23:59:48Z | 8013179 | 0.082958404 |
| 2026-04-21T23:59:48Z | 8020376 | 0.083073467 |
| 2026-04-22T23:59:48Z | 8027562 | 0.082451356 |
| 2026-04-23T23:59:48Z | 8034762 | 0.082698964 |
| 2026-04-24T23:59:48Z | 8041962 | 0.08281153 |
| 2026-04-25T23:59:48Z | 8049151 | 0.08149026 |
| 2026-04-26T23:59:48Z | 8056274 | 0.082049598 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.080807242 |
| 2026-04-28T23:59:48Z | 8070646 | 0.079895814 |
| 2026-04-29T23:59:48Z | 8077790 | 0.080193617 |
| 2026-04-30T23:59:48Z | 8084984 | 0.079772207 |
| 2026-05-01T23:59:48Z | 8092168 | 0.079895538 |
| 2026-05-02T23:59:48Z | 8099357 | 0.079321306 |
| 2026-05-03T16:10:00Z | 8104202 | 0.078462815 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

