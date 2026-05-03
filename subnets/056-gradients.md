# NetUID 56 — Gradients (`ج`)

## Overview

**Gradients** (NetUID **56**) (`ج`).

Best AutoML plaftorm in the world

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `184`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ58,404.453399648. **Alpha liquidity in pool (`alpha_in`)** = ‎2,668,377.267824318ج‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,286,798.405763835ج‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.021917179`** *(also **moving-average price** `0.021880003158003092` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎2,781,278.794281400ج‎`. **Owner hotkey / coldkey (chain):** `5GU4Xkd3dCGTU3s8VLcHGc5wsD5M8XyxDca5yDQhYm1mVXFu` / `5EJ1zbdwhumTRYFx3VCGnR6SW7CJWP28tEJCo2gw1dFbVL5g`.
- **Subnet registered at block:** `4312927` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎138.823062539ج‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ج‎` · α-in `‎0.000000000ج‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.02191718`
- **Market cap:** `96390365342539.71639004`
- **Liquidity:** `116887758286451`
- **Total τ:** `58404454587183`
- **Total α:** `4955162673588153`
- **α in pool:** `2668377213641034`
- **α staked:** `1729559260966544`
- **Price Δ 1h:** `0.001104168839643567`
- **Price Δ 1d:** `0.605699449448013555`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `15`
- **Active miners:** `15`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `15`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Best AutoML plaftorm in the world



**Additional commentary (on-chain)**


None

### Repository README excerpt *(everything before first `##` heading)*

<h1 align="center">G.O.D Subnet</h1>

🚀 Welcome to the [Gradients on Demand](https://gradients.io) Subnet

> Distributed intelligence for LLM and diffusion model training. Where the world's best AutoML minds compete.

**Tournaments** 🏆
Competitive events where the validator executes miners' open-source training scripts on dedicated infrastructure.

- **Duration**: 4-7 days per tournament
- **Frequency**: New tournaments start 72 hours after the previous one ends
- **Rewards**: Exponentially higher weight potential for top performers
- **Open Source**: Winning AutoML scripts are released when tournaments complete
- **Winners Repository**: First place tournament scripts is uploaded to [github.com/gradients-opensource](https://github.com/gradients-opensource) 🤙
- [Tournament Overview](docs/tournament_overview.md)

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Anyone Can Train AI on Bittensor. AI Training, Decentralized.

**Fetched document title:** Gradients | Anyone Can Train AI

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5EJ1zbdwhumTRYFx3VCGnR6SW7CJWP28tEJCo2gw1dFbVL5g`

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

## Setup Guides

- [Tournament Miner Guide](docs/tourn_miner.md)
- [Validator Setup Guide](docs/validator_setup.md)

---

## Developer Resources

For technical documentation on GRPO reward functions and implementation details, see [GRPO Safe Code Execution Guide](docs/grpo_rewards_code_execution.md).

---

## Recommended Compute Requirements

[Compute Requirements](docs/compute.md)

---

## Miner Advice

[Miner Advice](docs/tourn_miner.md)

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/gradients-ai/G.O.D/main/README.md`*

## On-chain identity — description


Best AutoML plaftorm in the world

## On-chain identity — additional field


None

## Registered contact & links


- **Website:** [https://www.gradients.io/](https://www.gradients.io/)
- **GitHub:** [https://github.com/gradients-ai/G.O.D](https://github.com/gradients-ai/G.O.D)
- **Discord (handle / invite hint):** `None`
- **Logo URL:** [https://gradients-public.s3.eu-central-003.backblazeb2.com/gradientslogo.png](https://gradients-public.s3.eu-central-003.backblazeb2.com/gradientslogo.png)
- **Contact:** info@gradients.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.021916914 |
| 8104072 | 0.021917647 |
| 8104120 | 0.02191763 |
| 8104168 | 0.021917617 |
| 8104216 | 0.021917178 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

