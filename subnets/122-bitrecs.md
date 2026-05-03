# NetUID 122 — Bitrecs (`ⲅ`)

## Overview

**Bitrecs** (NetUID **122**) (`ⲅ`).

Bitrecs is a novel recommendation engine built on the Bittensor network

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `250`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,210.624497116. **Alpha liquidity in pool (`alpha_in`)** = ‎1,056,458.634616834ⲅ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,254,810.304062503ⲅ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004016412`** *(also **moving-average price** `0.0037397723644971848` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎293,056.788888495ⲅ‎`. **Owner hotkey / coldkey (chain):** `5HVPptMPpMx3jUtUEjUfB8zLKkNM4fPnt4CLYT5Gc3BYzRX4` / `5H6fAdf7QsrZpLKyydA1pM9sxTK7qJx4S4jUgg6YMHr4Xzqs`.
- **Subnet registered at block:** `5778578` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎182.286926978ⲅ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ⲅ‎` · α-in `‎0.000000000ⲅ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004037063`
- **Market cap:** `10979057705521.885055641`
- **Liquidity:** `8475389441177`
- **Total τ:** `4241629089565`
- **Total α:** `3311255938679337`
- **α in pool:** `1048722883842169`
- **α staked:** `1670842727475238`
- **Price Δ 1h:** `3.726863193930749974`
- **Price Δ 1d:** `12.057062996070985945`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `2`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `10`
- **Neuron reg. cost:** `1000000`

### On-chain declared purpose *(SubnetIdentity)*

Bitrecs is a novel recommendation engine built on the Bittensor network

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# Bitrecs V2

<img src="docs/light-logo.svg#gh-light-mode-only" width="400" height="auto" alt="Bitrecs Logo"/>
<img src="docs/dark-logo.svg#gh-dark-mode-only" width="400" height="auto" alt="Bitrecs Logo"/>

[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[X](https://x.com/bitrecs) • [Discord](https://discord.gg/bittensor) • [Website](https://bitrecs.ai/) • [Dashboard](https://dashboard.bitrecs.ai/)
</div>


**What is Bitrecs V2?**

Bitrecs V2 is a prompt evolution subnet which rewards miners who optimize an artifact.yaml, an object containing a prompt, model, temperature and other parameters against a rotating set of challenging ecommerce evaluations. Miners submit artifacts via the CLI by making an onchain commitment to begin evaluation.

**What does Bitrecs do?**

Bitrecs is a novel recommendation engine powered by Bittensor. Our flagship product is an ecommerce recommendation widget which drives sales for merchants by utilizing the newest state of the art models and novel generative recommendation techniques. Merchants can expect to see personalized customer journey experiences drive higher average order values, resulting in more sales.

**Scoring**

Bitrecs V2 employs a winnter take all (WTA) scoring engine to evaluate miner submissions against a diverse set of ecommerce tasks. Submissions are scored based on performance across multiple environments, using ε-Pareto dominance to identify non-dominated miners on the frontier rewarding genuine improvements. Scores incorporate statistical robustness via epsilon tolerances, account for sample sizes, and apply linear decay factors over time (with a 3-day grace period and 5% daily reduction to a 25% floor). The engine then computes winner-takes-all weights, prioritizing miners who surpass thresholds set by earlier participants, and sets these weights onchain for the top-performing miner to receive emissions.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Next generation product recommendations

**Fetched document title:** Bitrecs

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
- **Registration recycle cost snapshot (`burn`):** τ0.001000000
- **Owner SS58 (`owner_ss58`):** `5H6fAdf7QsrZpLKyydA1pM9sxTK7qJx4S4jUgg6YMHr4Xzqs`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.001000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `2`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Validator

See [Validator Setup](docs/validator_setup.md)

---

## Miner

See [Miner Setup](docs/miner_setup.md)

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/bitrecs/bitrecs-v2/main/README.md`*

## On-chain identity — description


Bitrecs is a novel recommendation engine built on the Bittensor network

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://bitrecs.ai](https://bitrecs.ai)
- **GitHub:** [https://github.com/bitrecs/bitrecs-v2](https://github.com/bitrecs/bitrecs-v2)
- **Discord:** [https://discord.gg/gWtKvytFma](https://discord.gg/gWtKvytFma)
- **Logo URL:** [https://www.bitrecs.ai/assets/logo/x7k9m2n8/whiteonblack.png](https://www.bitrecs.ai/assets/logo/x7k9m2n8/whiteonblack.png)
- **Contact:** support@bitrecs.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.003875421 |
| 8104072 | 0.003875412 |
| 8104120 | 0.003875402 |
| 8104168 | 0.003865157 |
| 8104216 | 0.004016411 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

