# NetUID 114 — SOMA (`Є`)

## Overview

**SOMA** (NetUID **114**) (`Є`).

AI solutions delivered through MCP infrastructure

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `242`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,128.144558506. **Alpha liquidity in pool (`alpha_in`)** = ‎183,754.870291037Є‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎719,179.048375664Є‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011618376`** *(also **moving-average price** `0.011159873800352216` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎52,886.076543366Є‎`. **Owner hotkey / coldkey (chain):** `5H1nRfbCbDGh3t17er9Y8hwFEsXCrjBbaN6jLrnez8KpUKju` / `5FHrQMjzzAhmL5zS9ys87ZrGCwG3vsVT9hXAUWZQ8SNdRqig`.
- **Subnet registered at block:** `7312241` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎147.758690599Є‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.005792894` · α-out `‎1.000000000Є‎` · α-in `‎0.500000000Є‎`.

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
| 8104024 | 0.011551973 |
| 8104072 | 0.011558276 |
| 8104120 | 0.011560978 |
| 8104168 | 0.011582803 |
| 8104216 | 0.011618376 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

