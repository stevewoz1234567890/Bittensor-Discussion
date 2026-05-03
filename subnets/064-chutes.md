# NetUID 64 — Chutes (`ش`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Chutes** (NetUID **64**) (`ش`).

Breakthrough Serverless Compute for AI, At Scale.



#### SubnetIdentity `additional` *(chain)*



Chutes is a subnet operated by Chutes Global Corp, an International Business Corporation registered in Nevis with registration number C 61974

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `51`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ206,255.766836735. **Alpha liquidity in pool (`alpha_in`)** = ‎2,630,022.223901684ش‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,496,975.305299494ش‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.078454213`** *(also **moving-average price** `0.07895934768021107` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎4,471,582.813717310ش‎`. **Owner hotkey / coldkey (chain):** `5F4Q3cA8EvApwhBj4eLjbb1meiLtzKgWhkF5JLRMNhRfqULc` / `5FRYKhbmfXPDoHdUUDMx27E3HuMvAzwjzFMMq3rNurUhAyS9`.
- **Subnet registered at block:** `4531295` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎38.572871835ش‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ش‎` · α-in `‎0.000000000ش‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104384`
- **Liquidity constant `k`:** `542457250588496987626319561740`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Chutes`
- **Symbol (API):** `ش`
- **Rank:** `1`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.078462815`
- **Market cap:** `386771185380278.13065187`
- **Market cap Δ 1d:** `-1.021873900242927567`
- **Liquidity:** `412614713415796`
- **Total τ:** `206267089613796`
- **Total α:** `5126764529201178`
- **α in pool:** `2629877908433451`
- **α staked:** `2299478569285047`
- **Price Δ 1h:** `-0.198362312101951741`
- **Price Δ 1d:** `-1.164869914092478222`
#### Subnet activity (TAOStats)

- **NetUID (API):** `64`
- **Owner SS58 (API):** `5FRYKhbmfXPDoHdUUDMx27E3HuMvAzwjzFMMq3rNurUhAyS9`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `4531295`
- **Registration wall time:** `2024-12-21T16:53:12Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `27`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `12`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

# Chutes!

This package provides the command line interface and development kit for use with the chutes.ai platform.

The miner code is available [here](https://github.com/rayonlabs/chutes-miner), and validator/API code [here](https://github.com/rayonlabs/chutes-api).

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Deploy, scale, and run top open-source AI models with serverless GPU compute from Chutes. Explore always-on LLM, image, speech, and video models built for production workloads.

**Fetched document title:** Chutes | Serverless AI Compute for Open-Source Models

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


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
| 8104244 | 0.078462627 |
| 8104292 | 0.078458705 |
| 8104340 | 0.07845853 |
| 8104388 | 0.078455069 |
| 8104436 | 0.078454212 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

