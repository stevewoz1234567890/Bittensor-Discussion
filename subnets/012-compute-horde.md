# NetUID 12 — Compute Horde (`μ`)

## Overview

**Compute Horde** (NetUID 12) does not currently expose a long on-chain description. Use the registered links and any website excerpt below; confirm the subnet’s purpose on official channels and explorers.

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
- **`immunity_period` (blocks):** 1466
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5ELzhHvgUqmnAYs74vFWjMMehXNeHkRtkreAa3g8QQS96PCp`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `1466` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `100`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `3`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `1`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

# ComputeHorde (Subnet 12 of Bittensor)

![ComputeHorde.svg](ComputeHorde.svg)

ComputeHorde is a specialized subnet within the [Bittensor network](https://bittensor.com) 
designed to **supercharge Bittensor with scalable and trusted GPU computing power**. 

By transforming untrusted GPUs provided by miners into trusted compute resources, 
ComputeHorde enables **validators of other subnets** to access large amounts of decentralized computing power cost-effectively, 
paving the way for Bittensor to scale beyond its current limitations to support potentially over 1,000 subnets.

---

## Using ComputeHorde to Power Other Subnets

If you're a **subnet owner or validator** looking to access scalable, decentralized GPU compute power from ComputeHorde,
check out the [ComputeHorde SDK](compute_horde_sdk/README.md#readme).

The SDK allows you to:
- **Submit jobs easily** from your own subnet validator code.
- Perform **cross-validation** to verify result integrity and protect against malicious miners.
- **Reduce infrastructure costs** by eliminating the need for physical GPUs.
- **Accelerate validation** by leveraging ComputeHorde’s ready-to-go GPU pool.
- **Fallback to other clouds** like [RunPod](https://www.runpod.io/) via SkyPilot if ComputeHorde is temporarily unavailable.

---

### Hardware Classes

- Each **hardware class** in ComputeHorde has a **configurable weight**.
- These weights adjust final scores, prioritizing hardware types based on network demand.

---

## Returning Miners — What’s New

If you're a returning miner, here's what's new in ComputeHorde:

- **🛡️ DDoS Shield Available:** Miners can now protect themselves against network attacks by running an optional shield. 
  Just run the Docker container from the [DDoS Shield repo](https://github.com/bactensor/bt-ddos-shield#running-shield-on-server-miner-side). 
  
- **💰 Collateral for Organic Jobs:** Validators may now require miners to deposit collateral. Doing so increases trust and lets you access **organic jobs**. 
  - [Miner deposit instructions](https://github.com/bactensor/collateral-contracts#recommended-miner-integration-guide-as-used-by-computehorde)

- **🐳 Smarter Preloading of Docker Images:** A global `DYNAMIC_PRELOAD_DOCKER_JOB_IMAGES` parameter lists Docker images likely to be used across jobs. 
  Miners can preload select images to reduce latency and GPU usage. [More details](miner#preloading-job-images).

Want to maximize earnings? Stake collateral with validators, preload Docker images wisely, and enable the DDoS shield.

---

### **Validator**

- Receives organic requests via the Facilitator.
- Distributes the tasks to miners and evaluates the results:
- Uses a separate GPU, called a **Trusted Miner**, to pre-run part of the validation tasks and establish expected results. 
  The Trusted Miner shares the same code as a regular miner, but is configured differently:
  - It is not registered in the metagraph.
  - It only accepts tasks from the associated validator.
- Optionally integrates with a **collateral smart contract** to filter miners by deposited funds, enabling slashing for incorrect organic results and improving task reliability.
- [See validator's README for more details](validator/README.md)

---

### **Miner**

- Accepts job requests from validators.
- Manages executors to perform tasks and sends results back to validators.
- Can **deposit collateral** to become eligible for extra paid organic jobs from validators.
- [See miner's README for more details](miner/README.md)

---

### Encouraging Actual Mining

- Scoring system incentivizing for completing organic tasks.
- Validators can require miners to deposit collateral to access organic jobs, creating economic pressure to behave honestly.
- An optional DDoS shield is available for miners to stay reliably online and resilient against attacks.

---

# Running ComputeHorde components

This repository contains the implementations of:

- **Validator**: Requires a [Trusted Miner](#validator) for cross-checking organic task results.
- **Miner**: Modifying the miner code on subnet 12 is discouraged, as the stock implementation manages only communications between components.
  The competitive edge lies in optimizing executor provisioning.
  Users can create [custom executor managers](miner#custom-executor-manager) to scale and optimize mining efficiency.
  The default executor manager runs a single executor and is not intended for mainnet use.

In the following sections, you can find instructions on running [Validator](#Validator) and [Miner](#Miner).
There are more details in each com…

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- designed to **supercharge Bittensor with scalable and trusted GPU computing power**.
- ComputeHorde introduces hardware classes to create a free market for GPU resources, balancing cost-effectiveness with performance.
- Currently, **A6000** is the supported class, with **A100** coming next.
- The end goal is to eventually support all GPU types/configurations required by validators across Bittensor subnets.
- ComputeHorde adds GPU-powered validation to this ecosystem, helping other subnets operate effectively without relying on centralized cloud services.
- If you're a **subnet owner or validator** looking to access scalable, decentralized GPU compute power from ComputeHorde,
- - **Accelerate validation** by leveraging ComputeHorde’s ready-to-go GPU pool.
- Miners can preload select images to reduce latency and GPU usage. [More details](miner#preloading-job-images).
- - Uses a separate GPU, called a **Trusted Miner**, to pre-run part of the validation tasks and establish expected results.
- - At least **500GB of shared disk space** is recommended to reliably handle docker images and job data stored in `/tmp`.
- Add support for all GPU classes required by other Bittensor subnets.
- 1. trusted miner (requires A6000 - the only GPU supported now) for cross-validation
- 1. validator machine (standard, non-GPU) - for regular validating & weight-setting
- Miner installation may occasionally fail with an error about the system being unable to install the `cuda-drivers` package.
- 1. Run the following command on the miner machine to purge any conflicting NVIDIA packages:
- sudo apt-get purge -y '^nvidia-.*'
- To verify the health of the NVIDIA setup, run the following command on the miner machine:
- docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
- To start all the core services locally and be able to schedule jobs that don't require a GPU (so to test communications
- self-contained and should run on anything that has a CPU, RAM and an operating system. And docker.


*Primary README URL used: `https://raw.githubusercontent.com/backend-developers-ltd/ComputeHorde/master/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


*Empty — no description bytes set in `SubnetIdentity`.*

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/backend-developers-ltd/ComputeHorde/](https://github.com/backend-developers-ltd/ComputeHorde/)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.006792395 |
| 8103843 | 0.006792384 |
| 8103891 | 0.006792379 |
| 8103939 | 0.006792374 |
| 8103987 | 0.00679237 |
| 8104035 | 0.006792367 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

