# NetUID 114 — SOMA (`Є`)

## Overview

**SOMA** (NetUID **114**) (`Є`).

AI solutions delivered through MCP infrastructure

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `304`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,131.825610194. **Alpha liquidity in pool (`alpha_in`)** = ‎183,499.687745233Є‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎719,522.970237578Є‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011621888`** *(also **moving-average price** `0.011166510405018926` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎52,889.721073661Є‎`. **Owner hotkey / coldkey (chain):** `5H1nRfbCbDGh3t17er9Y8hwFEsXCrjBbaN6jLrnez8KpUKju` / `5FHrQMjzzAhmL5zS9ys87ZrGCwG3vsVT9hXAUWZQ8SNdRqig`.
- **Subnet registered at block:** `7312241` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎185.615518768Є‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.005810992` · α-out `‎1.000000000Є‎` · α-in `‎0.500000000Є‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.011582899`
- **Market cap:** `7519042556749.064911667`
- **Liquidity:** `4256408037878`
- **Total τ:** `2127802436915`
- **Total α:** `902915308237220`
- **α in pool:** `183771403079982`
- **α staked:** `465378913844051`
- **Price Δ 1h:** `0.278362973265969142`
- **Price Δ 1d:** `8.797219020019971222`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `59`
- **Active dual:** `1`
- **Emission:** `5791457`
- **Max neurons:** `256`
- **Validators (metadata):** `10`
- **Neuron reg. cost:** `50000000`

### On-chain declared purpose *(SubnetIdentity)*

AI solutions delivered through MCP infrastructure

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** SOMA connects AI subnets on Bittensor (SN114) into a decentralized intelligence bridge. Explore validators, miners and the SOMA ecosystem.

**Fetched document title:** SOMA Subnet | Bittensor Subnet 114 - Bridge for Intelligence

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
- **Registration recycle cost snapshot (`burn`):** τ0.050000000
- **Owner SS58 (`owner_ss58`):** `5FHrQMjzzAhmL5zS9ys87ZrGCwG3vsVT9hXAUWZQ8SNdRqig`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.050000000 / τ100.000000000
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

### Validators

Validators score miner solutions by:
- Fetching execution results from the platform
- Evaluatimg solution quality based on competition criteria
- Reporting scores to the platform for weight calculation

**Min Hardware Requirements:**
- 4 CPU cores
- 16 GB RAM
- 200 GB SSD storage

[**→ Validator Setup Guide**](docs/validator/validator-setup.md)

---

### Miners

On SOMA, any problem that can be meaningfully solved using an MCP server - and that can significantly improve agent performance - may become a competition target. Miners compete to deliver the most effective model or algorithm for a given task.


The miner’s responsibility is to design and implement model or algorithm that solves the defined problem as effectively as possible and upload it to the platform

**All a miner needs to participate is:**
- A working algorithm that solves the active MCP task
- A registered hotkey on netuid 114

The platform handles orchestration and evaluation. Validators automatically retrieve submitted solutions associated with registered hotkeys and score them according to the active competition criteria.

[**→ Miner Setup Guide**](docs/miner/miner-setup.md)

---

#### CPU / GPU / RAM lines (automatic grep)

- - 4 CPU cores
- - 16 GB RAM
- - 200 GB SSD storage


*Primary README URL used: `https://raw.githubusercontent.com/DendriteHQ/SOMA/main/README.md`*

## On-chain identity — description


AI solutions delivered through MCP infrastructure

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://thesoma.ai](https://thesoma.ai)
- **GitHub:** [https://github.com/DendriteHQ/SOMA](https://github.com/DendriteHQ/SOMA)
- **Discord:** [https://discord.gg/durr4Sg6sM](https://discord.gg/durr4Sg6sM)
- **Logo URL:** [https://thesoma.ai/images/1200x1200.png](https://thesoma.ai/images/1200x1200.png)
- **Contact:** https://x.com/SomaSubnet

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.011558337 |
| 8104133 | 0.01156099 |
| 8104181 | 0.01158287 |
| 8104229 | 0.011620149 |
| 8104277 | 0.011621888 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.014145113 |
| 2026-03-10T23:59:48Z | 7718257 | 0.018708213 |
| 2026-03-11T23:59:48Z | 7725455 | 0.018787112 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.017341685 |
| 2026-03-13T23:59:48Z | 7739841 | 0.013509706 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.013736897 |
| 2026-03-15T23:59:48Z | 7754226 | 0.012874071 |
| 2026-03-16T23:59:48Z | 7761426 | 0.013342145 |
| 2026-03-17T23:59:48Z | 7768619 | 0.012856672 |
| 2026-03-18T23:59:48Z | 7775819 | 0.011486531 |
| 2026-03-19T23:59:48Z | 7783014 | 0.01068708194513178542 |
| 2026-03-20T23:59:48Z | 7790201 | 0.011878434 |
| 2026-03-21T23:59:48Z | 7797398 | 0.014982406 |
| 2026-03-22T23:59:48Z | 7804598 | 0.014045295 |
| 2026-03-23T23:59:48Z | 7811798 | 0.013360018 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.01339159074182323973 |
| 2026-03-25T23:59:48Z | 7826196 | 0.013089942 |
| 2026-03-26T23:59:48Z | 7833396 | 0.012007244 |
| 2026-03-27T23:59:48Z | 7840596 | 0.011995967 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.012825505 |
| 2026-03-29T23:59:48Z | 7854902 | 0.011578931 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.010711026 |
| 2026-03-31T23:59:48Z | 7869291 | 0.009728639 |
| 2026-04-01T23:59:48Z | 7876474 | 0.009298366 |
| 2026-04-02T23:59:48Z | 7883622 | 0.009688953 |
| 2026-04-03T23:59:48Z | 7890794 | 0.009034444 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.009879299 |
| 2026-04-05T23:59:48Z | 7905188 | 0.009824813 |
| 2026-04-06T23:59:48Z | 7912388 | 0.009761609 |
| 2026-04-07T23:59:48Z | 7919588 | 0.010231365 |
| 2026-04-08T23:59:48Z | 7926788 | 0.009936956 |
| 2026-04-09T23:59:48Z | 7933987 | 0.009043035 |
| 2026-04-10T23:59:48Z | 7941184 | 0.00975133 |
| 2026-04-11T23:59:48Z | 7948384 | 0.009809263 |
| 2026-04-12T23:59:48Z | 7955584 | 0.009501632 |
| 2026-04-13T23:59:48Z | 7962784 | 0.008984958 |
| 2026-04-14T23:59:48Z | 7969979 | 0.009325484 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.008828686 |
| 2026-04-16T23:59:48Z | 7984379 | 0.010187139 |
| 2026-04-17T23:59:48Z | 7991579 | 0.010028218 |
| 2026-04-18T23:59:48Z | 7998779 | 0.009673318 |
| 2026-04-19T23:59:48Z | 8005979 | 0.009534026 |
| 2026-04-20T23:59:48Z | 8013179 | 0.010386676 |
| 2026-04-21T23:59:48Z | 8020376 | 0.010923253 |
| 2026-04-22T23:59:48Z | 8027562 | 0.009883125 |
| 2026-04-23T23:59:48Z | 8034762 | 0.009556061 |
| 2026-04-24T23:59:48Z | 8041962 | 0.009881534 |
| 2026-04-25T23:59:48Z | 8049151 | 0.009714538 |
| 2026-04-26T23:59:48Z | 8056274 | 0.009233026 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.009689883 |
| 2026-04-28T23:59:48Z | 8070646 | 0.010036834 |
| 2026-04-29T23:59:48Z | 8077790 | 0.009972559 |
| 2026-04-30T23:59:48Z | 8084984 | 0.009939907 |
| 2026-05-01T23:59:48Z | 8092168 | 0.01086625 |
| 2026-05-02T23:59:48Z | 8099357 | 0.011195959 |
| 2026-05-03T16:10:00Z | 8104202 | 0.011582899 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

