# NetUID 51 — lium.io (`ת`)

## Overview

revolutionizing the democratization of compute

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
- **Registration recycle cost snapshot (`burn`):** τ0.005000000
- **Owner SS58 (`owner_ss58`):** `5FqACMtcegZxxopgu1g7TgyrnyD8skurr9QDPLPhxNQzsThe`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.005000000 / τ0.100000001
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `12000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `500000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### For Miners

Miners can contribute their GPU-equipped machines to the network. The machines are scored and validated based on factors like GPU type, number of GPUs, bandwidth, and overall GPU performance. Higher performance results in better compensation for miners.

If you are a miner and want to contribute GPU resources to the subnet, please refer to the [Miner Setup Guide](neurons/miners/README.md) for instructions on how to:

- Set up your environment.
- Install the miner software.
- Register your miner and connect to the network.
- Get compensated for providing GPUs!

---

### For Validators

Validators play a crucial role in maintaining the integrity of the Compute Subnet by verifying the hardware specifications and performance of miners’ machines. Validators ensure that miners are fairly compensated based on their GPU contributions and prevent fraudulent activities.

For more details, visit the [Validator Setup Guide](neurons/validators/README.md).

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- Welcome to **Lium.io powered by Bittensor Subnet 51**! This project enables a decentralized, peer-to-peer GPU rental marketplace, connecting miners who contribute GPU resources with users who need computational power. Our frontend interface is available at [lium.io](https://lium.io), where you can easily rent machines from the subnet.
- The Compute Subnet on Bittensor is a decentralized network that allows miners to contribute their GPU resources to a global pool. Users can rent these resources for computational tasks, such as machine learning, data analysis, and more. The system ensures fair compensation for miners based on the quality and performance of their GPUs.
- - **Miners**: Provide GPU resources to the network, evaluated and scored by validators.
- 2. **Browse** available GPU resources.
- 3. **Select** machines based on GPU type, performance, and price.
- **Command-Line Alternative**: For renters who prefer working from the terminal, you can also use [lium-cli](https://github.com/Datura-ai/lium-cli) - a command-line interface that allows you to manage GPU pods, SSH into machines, transfer files, and execute commands directly from your terminal. Install it with `pip install lium-cli`.
- Miners can contribute their GPU-equipped machines to the network. The machines are scored and validated based on factors like GPU type, number of GPUs, bandwidth, and overall GPU performance. Higher performance results in better compensation for miners.
- If you are a miner and want to contribute GPU resources to the subnet, please refer to the [Miner Setup Guide](neurons/miners/README.md) for instructions on how to:
- Validators play a crucial role in maintaining the integrity of the Compute Subnet by verifying the hardware specifications and performance of miners’ machines. Validators ensure that miners are fairly compensated based on their GPU contributions and prevent fraudulent activities.


*Primary README URL used: `https://raw.githubusercontent.com/Datura-ai/lium-io/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


revolutionizing the democratization of compute

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/Datura-ai/lium-io](https://github.com/Datura-ai/lium-io)
- **Discord (handle / invite hint):** `p383_54249`
- **Logo URL:** [https://raw.githubusercontent.com/Datura-ai/lium-logos/refs/heads/main/Celium_Icon_FullColor.png](https://raw.githubusercontent.com/Datura-ai/lium-logos/refs/heads/main/Celium_Icon_FullColor.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.063840848 |
| 8103843 | 0.063843984 |
| 8103891 | 0.063847569 |
| 8103939 | 0.06397184 |
| 8103987 | 0.063975204 |
| 8104035 | 0.06399009 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

