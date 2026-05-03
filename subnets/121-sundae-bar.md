# NetUID 121 — sundae_bar (`Ⲅ`)

## Overview

A generalist AI agent designed to execute real business workflows end-to-end.

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
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CXGaDJsffVeBK4CDhBNMVK6MH7fHbL7AbnjzZ8XP6QzFLWm`

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

## Framework Compatibility and Open Ecosystem

| Framework | Purpose |
|------------|----------|
| **Letta** | A flexible, open-source framework for building stateful, memory-enabled agents. Integrates seamlessly with AETS for consistent evaluation. *(Initial priority)*  |
| **LangChain** | Tool-chaining and workflow orchestration. *(Future support)* |
| **AutoGen / CrewAI / LangGraph** | Multi-agent reasoning and collaboration frameworks. *(Future support)* |

sundae\_bar is framework-agnostic: developers may build their generalist agents using any framework they prefer, provided the agent is fully open-source and compatible with SN121’s evaluation requirements. To ensure the best customer experience at launch, SN121 will initially prioritize and reward agents built with Letta, which aligns closely with AETS and integrates seamlessly with sundae\_bar’s hosting and deployment systems.

Letta’s flexibility, memory support, and open-source design make it an ideal foundation for developers aiming to build agents optimized for measurable evaluation and commercial deployment.

sundae\_bar will continue expanding supported frameworks over time, enabling a broader ecosystem of tooling and agent architectures to contribute to the evolution of The Generalist Agent.

---

#### CPU / GPU / RAM lines (automatic grep)

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

- `| **Letta** | A flexible, open-source framework for building stateful, memory-enabled agents. Integrates seamlessly with AETS for consistent evaluation. *(Initial priority)*  |`


*Primary README URL used: `https://raw.githubusercontent.com/sundae-bar/bittensor-subnet/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


A generalist AI agent designed to execute real business workflows end-to-end.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://www.sundaebar.ai/](https://www.sundaebar.ai/)
- **GitHub:** [https://github.com/sundae-bar/bittensor-subnet](https://github.com/sundae-bar/bittensor-subnet)
- **Logo URL:** [https://www.sundaebar.ai/apple-icon.png](https://www.sundaebar.ai/apple-icon.png)
- **Contact:** hello@sundaebar.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103843 | 0.006233895 |
| 8103891 | 0.006233884 |
| 8103939 | 0.006233874 |
| 8103987 | 0.006233863 |
| 8104035 | 0.006233855 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

