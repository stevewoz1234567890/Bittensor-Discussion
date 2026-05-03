# NetUID 56 — Gradients (`ج`)

## Overview

**Gradients** (NetUID **56**) (`ج`).

Best AutoML plaftorm in the world

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `246`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ58,403.655449649. **Alpha liquidity in pool (`alpha_in`)** = ‎2,668,413.675835575ج‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,286,823.997752578ج‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.021916582`** *(also **moving-average price** `0.021880623884499073` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎2,781,279.592231399ج‎`. **Owner hotkey / coldkey (chain):** `5GU4Xkd3dCGTU3s8VLcHGc5wsD5M8XyxDca5yDQhYm1mVXFu` / `5EJ1zbdwhumTRYFx3VCGnR6SW7CJWP28tEJCo2gw1dFbVL5g`.
- **Subnet registered at block:** `4312927` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎185.600363904ج‎`; pending root emission `τ0.000000000`.
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
| 8104085 | 0.021917645 |
| 8104133 | 0.021917626 |
| 8104181 | 0.021917186 |
| 8104229 | 0.021917144 |
| 8104277 | 0.021916582 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.021967931 |
| 2026-03-10T23:59:48Z | 7718257 | 0.021680321 |
| 2026-03-11T23:59:48Z | 7725455 | 0.02179413 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.021796277 |
| 2026-03-13T23:59:48Z | 7739841 | 0.022230005 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.021537272 |
| 2026-03-15T23:59:48Z | 7754226 | 0.021450383 |
| 2026-03-16T23:59:48Z | 7761426 | 0.021631075 |
| 2026-03-17T23:59:48Z | 7768619 | 0.021323661 |
| 2026-03-18T23:59:48Z | 7775819 | 0.020986789 |
| 2026-03-19T23:59:48Z | 7783014 | 0.02087870597490453528 |
| 2026-03-20T23:59:48Z | 7790201 | 0.020939963 |
| 2026-03-21T23:59:48Z | 7797398 | 0.020888045 |
| 2026-03-22T23:59:48Z | 7804598 | 0.020904061 |
| 2026-03-23T23:59:48Z | 7811798 | 0.021143228 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.02127196273014438861 |
| 2026-03-25T23:59:48Z | 7826196 | 0.024765329 |
| 2026-03-26T23:59:48Z | 7833396 | 0.024688157 |
| 2026-03-27T23:59:48Z | 7840596 | 0.022283826 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.021965159 |
| 2026-03-29T23:59:48Z | 7854902 | 0.022196355 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.022196795 |
| 2026-03-31T23:59:48Z | 7869291 | 0.022315405 |
| 2026-04-01T23:59:48Z | 7876474 | 0.022560247 |
| 2026-04-02T23:59:48Z | 7883622 | 0.026368225 |
| 2026-04-03T23:59:48Z | 7890794 | 0.026413823 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.02670403 |
| 2026-04-05T23:59:48Z | 7905188 | 0.026167347 |
| 2026-04-06T23:59:48Z | 7912388 | 0.026080314 |
| 2026-04-07T23:59:48Z | 7919588 | 0.025995072 |
| 2026-04-08T23:59:48Z | 7926788 | 0.026188798 |
| 2026-04-09T23:59:48Z | 7933987 | 0.026021889 |
| 2026-04-10T23:59:48Z | 7941184 | 0.025723147 |
| 2026-04-11T23:59:48Z | 7948384 | 0.025971714 |
| 2026-04-12T23:59:48Z | 7955584 | 0.025854653 |
| 2026-04-13T23:59:48Z | 7962784 | 0.025585397 |
| 2026-04-14T23:59:48Z | 7969979 | 0.025355371 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.024844481 |
| 2026-04-16T23:59:48Z | 7984379 | 0.022273397 |
| 2026-04-17T23:59:48Z | 7991579 | 0.021816607 |
| 2026-04-18T23:59:48Z | 7998779 | 0.021973821 |
| 2026-04-19T23:59:48Z | 8005979 | 0.021959168 |
| 2026-04-20T23:59:48Z | 8013179 | 0.021703281 |
| 2026-04-21T23:59:48Z | 8020376 | 0.02160501 |
| 2026-04-22T23:59:48Z | 8027562 | 0.021940892 |
| 2026-04-23T23:59:48Z | 8034762 | 0.022230445 |
| 2026-04-24T23:59:48Z | 8041962 | 0.021724842 |
| 2026-04-25T23:59:48Z | 8049151 | 0.021640213 |
| 2026-04-26T23:59:48Z | 8056274 | 0.021647725 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.021976475 |
| 2026-04-28T23:59:48Z | 8070646 | 0.02181911 |
| 2026-04-29T23:59:48Z | 8077790 | 0.021683142 |
| 2026-04-30T23:59:48Z | 8084984 | 0.021957798 |
| 2026-05-01T23:59:48Z | 8092168 | 0.021841079 |
| 2026-05-02T23:59:48Z | 8099357 | 0.021822923 |
| 2026-05-03T16:10:00Z | 8104202 | 0.02191718 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

