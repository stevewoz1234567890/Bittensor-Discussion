# NetUID 121 — sundae_bar (`Ⲅ`)

## Overview

**sundae_bar** (NetUID **121**) (`Ⲅ`).

A generalist AI agent designed to execute real business workflows end-to-end.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `249`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,282.522632918. **Alpha liquidity in pool (`alpha_in`)** = ‎1,175,329.368002833Ⲅ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,207,601.493611174Ⲅ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006233812`** *(also **moving-average price** `0.006194918882101774` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎520,008.512335365Ⲅ‎`. **Owner hotkey / coldkey (chain):** `5EL9y2gdesAcPiPmoyFKABToiui3RkXewiKxdTMmes34ZdNf` / `5CXGaDJsffVeBK4CDhBNMVK6MH7fHbL7AbnjzZ8XP6QzFLWm`.
- **Subnet registered at block:** `5766528` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎181.932595201Ⲅ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Ⲅ‎` · α-in `‎0.000000000Ⲅ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.006233813`
- **Market cap:** `15313506705389.927818691`
- **Liquidity:** `14609306126446`
- **Total τ:** `7282523080968`
- **Total α:** `3382917861614007`
- **α in pool:** `1175329296127115`
- **α staked:** `1281193975486892`
- **Price Δ 1h:** `-0.001058730848000098`
- **Price Δ 1d:** `2.344353603946007055`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `16`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `16`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

A generalist AI agent designed to execute real business workflows end-to-end.

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Discover autonomous AI agents, reusable skills, multi-step workflows, and expert prompts on sundae_bar — the marketplace for production-ready AI.

**Fetched document title:** AI Agent Marketplace - Discover & Monetize AI Agents | sundae_bar

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

## On-chain identity — description


A generalist AI agent designed to execute real business workflows end-to-end.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.sundaebar.ai/](https://www.sundaebar.ai/)
- **GitHub:** [https://github.com/sundae-bar/bittensor-subnet](https://github.com/sundae-bar/bittensor-subnet)
- **Logo URL:** [https://www.sundaebar.ai/apple-icon.png](https://www.sundaebar.ai/apple-icon.png)
- **Contact:** hello@sundaebar.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.006233857 |
| 8104072 | 0.006233845 |
| 8104120 | 0.006233831 |
| 8104168 | 0.006233819 |
| 8104216 | 0.006233811 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.007437472 |
| 2026-03-10T23:59:48Z | 7718257 | 0.007463724 |
| 2026-03-11T23:59:48Z | 7725455 | 0.007559711 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.007368489 |
| 2026-03-13T23:59:48Z | 7739841 | 0.006867162 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.006961497 |
| 2026-03-15T23:59:48Z | 7754226 | 0.006761831 |
| 2026-03-16T23:59:48Z | 7761426 | 0.006729144 |
| 2026-03-17T23:59:48Z | 7768619 | 0.006389947 |
| 2026-03-18T23:59:48Z | 7775819 | 0.006416551 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00630411298617886084 |
| 2026-03-20T23:59:48Z | 7790201 | 0.00612007 |
| 2026-03-21T23:59:48Z | 7797398 | 0.006110323 |
| 2026-03-22T23:59:48Z | 7804598 | 0.006121712 |
| 2026-03-23T23:59:48Z | 7811798 | 0.006189547 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.0060061304206474156 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005996028 |
| 2026-03-26T23:59:48Z | 7833396 | 0.005968322 |
| 2026-03-27T23:59:48Z | 7840596 | 0.00598132 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005978315 |
| 2026-03-29T23:59:48Z | 7854902 | 0.005922738 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.00600255 |
| 2026-03-31T23:59:48Z | 7869291 | 0.006094015 |
| 2026-04-01T23:59:48Z | 7876474 | 0.006317829 |
| 2026-04-02T23:59:48Z | 7883622 | 0.006822781 |
| 2026-04-03T23:59:48Z | 7890794 | 0.006711265 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.006853713 |
| 2026-04-05T23:59:48Z | 7905188 | 0.006755698 |
| 2026-04-06T23:59:48Z | 7912388 | 0.006709635 |
| 2026-04-07T23:59:48Z | 7919588 | 0.007081717 |
| 2026-04-08T23:59:48Z | 7926788 | 0.007936628 |
| 2026-04-09T23:59:48Z | 7933987 | 0.008070924 |
| 2026-04-10T23:59:48Z | 7941184 | 0.008753092 |
| 2026-04-11T23:59:48Z | 7948384 | 0.008240602 |
| 2026-04-12T23:59:48Z | 7955584 | 0.008600477 |
| 2026-04-13T23:59:48Z | 7962784 | 0.008729431 |
| 2026-04-14T23:59:48Z | 7969979 | 0.008925632 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.008936711 |
| 2026-04-16T23:59:48Z | 7984379 | 0.009385074 |
| 2026-04-17T23:59:48Z | 7991579 | 0.009119198 |
| 2026-04-18T23:59:48Z | 7998779 | 0.008316043 |
| 2026-04-19T23:59:48Z | 8005979 | 0.007715115 |
| 2026-04-20T23:59:48Z | 8013179 | 0.008082048 |
| 2026-04-21T23:59:48Z | 8020376 | 0.007739485 |
| 2026-04-22T23:59:48Z | 8027562 | 0.007616576 |
| 2026-04-23T23:59:48Z | 8034762 | 0.007171347 |
| 2026-04-24T23:59:48Z | 8041962 | 0.007167974 |
| 2026-04-25T23:59:48Z | 8049151 | 0.007082292 |
| 2026-04-26T23:59:48Z | 8056274 | 0.006947483 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.006643032 |
| 2026-04-28T23:59:48Z | 8070646 | 0.006337854 |
| 2026-04-29T23:59:48Z | 8077790 | 0.006156832 |
| 2026-04-30T23:59:48Z | 8084984 | 0.006324632 |
| 2026-05-01T23:59:48Z | 8092168 | 0.006210258 |
| 2026-05-02T23:59:48Z | 8099357 | 0.006180439 |
| 2026-05-03T16:10:00Z | 8104202 | 0.006233813 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

