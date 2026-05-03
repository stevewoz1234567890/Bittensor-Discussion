# NetUID 121 — sundae_bar (`Ⲅ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**sundae_bar** (NetUID **121**) (`Ⲅ`).

A generalist AI agent designed to execute real business workflows end-to-end.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `108`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,282.451330470. **Alpha liquidity in pool (`alpha_in`)** = ‎1,175,340.806159718Ⲅ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,207,810.055454289Ⲅ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006233692`** *(also **moving-average price** `0.006197166861966252` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎520,008.583637813Ⲅ‎`. **Owner hotkey / coldkey (chain):** `5EL9y2gdesAcPiPmoyFKABToiui3RkXewiKxdTMmes34ZdNf` / `5CXGaDJsffVeBK4CDhBNMVK6MH7fHbL7AbnjzZ8XP6QzFLWm`.
- **Subnet registered at block:** `5766528` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎78.911237962Ⲅ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Ⲅ‎` · α-in `‎0.000000000Ⲅ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104327`
- **Liquidity constant `k`:** `8559362217573520720420007460`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `sundae_bar`
- **Symbol (API):** `Ⲅ`
- **Rank:** `75`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.006233813`
- **Market cap:** `15313506705389.927818691`
- **Market cap Δ 1d:** `2.521298722825114298`
- **Liquidity:** `14609306126446`
- **Total τ:** `7282523080968`
- **Total α:** `3382917861614007`
- **α in pool:** `1175329296127115`
- **α staked:** `1281193975486892`
- **Price Δ 1h:** `-0.001058730848000098`
- **Price Δ 1d:** `2.344353603946007055`
#### Subnet activity (TAOStats)

- **NetUID (API):** `121`
- **Owner SS58 (API):** `5CXGaDJsffVeBK4CDhBNMVK6MH7fHbL7AbnjzZ8XP6QzFLWm`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `5766528`
- **Registration wall time:** `2025-06-12T18:22:24Z`
- **Registration cost snapshot:** `111988743976`
- **Active keys:** `256`
- **Active validators:** `16`
- **Active miners:** `1`
- **Active dual-role:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `16`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Discover autonomous AI agents, reusable skills, multi-step workflows, and expert prompts on sundae_bar — the marketplace for production-ready AI.

**Fetched document title:** AI Agent Marketplace - Discover & Monetize AI Agents | sundae_bar

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

- `| **Letta** | A flexible, open-source framework for building stateful, memory-enabled agents. Integrates seamlessly with AETS for consistent evaluation. *(Initial priority)*  |`


*Primary README URL used: `https://raw.githubusercontent.com/sundae-bar/bittensor-subnet/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.sundaebar.ai/](https://www.sundaebar.ai/)
- **GitHub:** [https://github.com/sundae-bar/bittensor-subnet](https://github.com/sundae-bar/bittensor-subnet)
- **Logo URL:** [https://www.sundaebar.ai/apple-icon.png](https://www.sundaebar.ai/apple-icon.png)
- **Contact:** hello@sundaebar.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.006233774 |
| 8104292 | 0.006233749 |
| 8104340 | 0.006233707 |
| 8104388 | 0.006233704 |
| 8104436 | 0.006233692 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

