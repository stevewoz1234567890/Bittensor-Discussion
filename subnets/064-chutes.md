# NetUID 64 — Chutes (`ش`)

## Overview

Breakthrough Serverless Compute for AI, At Scale.

Chutes is a subnet operated by Chutes Global Corp, an International Business Corporation registered in Nevis with registration number C 61974

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

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
- **Registration recycle cost snapshot (`burn`):** τ0.000561237
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

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

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

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

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

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.07863035 |
| 8103843 | 0.0786284 |
| 8103891 | 0.078619384 |
| 8103939 | 0.078618379 |
| 8103987 | 0.07861914 |
| 8104035 | 0.078618979 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

