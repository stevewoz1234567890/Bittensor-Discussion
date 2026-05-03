# NetUID 44 — Score (`ף`)

## Overview

**Score** (NetUID **44**) (`ף`).

Making every camera intelligent

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `172`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ57,629.862466523. **Alpha liquidity in pool (`alpha_in`)** = ‎1,645,772.009506884ף‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,254,722.544741976ף‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.034981923`** *(also **moving-average price** `0.03515456756576896` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,667,391.258678217ף‎`. **Owner hotkey / coldkey (chain):** `5FsREvyUXSZWYRqVyQLDdpYmZZPnkhZyW6HjooozKP1nQkwu` / `5CaCekuxb9pKQyLoxh3jbkEXig8fxjkeS4AQ6UmZa12xfQ9H`.
- **Subnet registered at block:** `3550319` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎129.663828478ף‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.015694642` · α-out `‎1.000000000ף‎` · α-in `‎0.448650054ף‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.034981927`
- **Market cap:** `159126896741954.483867871`
- **Liquidity:** `115201730535565`
- **Total τ:** `57629660343592`
- **Total α:** `4900475719433509`
- **α in pool:** `1645766117800595`
- **α staked:** `2903065532953078`
- **Price Δ 1h:** `-0.091854453217389149`
- **Price Δ 1d:** `-1.605311760375272082`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `6`
- **Active dual:** `0`
- **Emission:** `15689458`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Making every camera intelligent

### Repository README excerpt *(everything before first `##` heading)*

# Score Vision (SN44)

Score Vision is a decentralised computer vision framework built on Bittensor that drastically reduces the cost and time required for complex video analysis. By leveraging innovative lightweight validation techniques and aligned incentives, we're making advanced computer vision accessible and scalable.

Our initial focus is Game State Recognition (GSR) in football - a strategic entry point into the $600 billion football industry, with $50 billion in betting and $30 billion in data services. Current solutions are prohibitively expensive: a single football match requires hundreds of hours of manual annotation, costing thousands of dollars. Score Vision aims to reduce these costs by 10x to 100x while dramatically improving speed and accuracy, unlocking new possibilities in sports analytics and beyond.

**Get Started:**

- [Miner Setup](miner/README.md)
- [Validator Setup](validator/README.md)

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Democratising visual intelligence by building an open, permissionless computer vision layer for sports and beyond.

**Fetched document title:** We Are Score | Making Every Camera Intelligent

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
- **`immunity_period` (blocks):** 7500
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CaCekuxb9pKQyLoxh3jbkEXig8fxjkeS4AQ6UmZa12xfQ9H`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7500` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `2`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

##### Extra scrape: `README.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- - Manages GPU memory for optimal performance
- - Monitors system resources (GPU/CPU usage)
- DEVICE=cuda                                   # Computing device (cuda/cpu/mps)
- - Check CUDA/GPU availability
- - Monitor GPU memory usage

---

##### Extra scrape: `README.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- - Manages GPU memory for optimal performance
- - Monitors system resources (GPU/CPU usage)
- DEVICE=cuda                                   # Computing device (cuda/cpu/mps)
- - Check CUDA/GPU availability
- - Monitor GPU memory usage


*Primary README URL used: `https://raw.githubusercontent.com/score-technologies/score-vision/main/README.md`*

## On-chain identity — description


Making every camera intelligent

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.wearescore.com/](https://www.wearescore.com/)
- **GitHub:** [https://github.com/score-technologies/score-vision](https://github.com/score-technologies/score-vision)
- **Logo URL:** [https://www.wearescore.com/android-chrome-512x512.png](https://www.wearescore.com/android-chrome-512x512.png)
- **Contact:** hello@wearescore.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.034977693 |
| 8104072 | 0.034975951 |
| 8104120 | 0.034981334 |
| 8104168 | 0.034981954 |
| 8104216 | 0.034981923 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.030358849 |
| 2026-03-10T23:59:48Z | 7718257 | 0.029903154 |
| 2026-03-11T23:59:48Z | 7725455 | 0.028435257 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.027498422 |
| 2026-03-13T23:59:48Z | 7739841 | 0.029225969 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.029557898 |
| 2026-03-15T23:59:48Z | 7754226 | 0.028063755 |
| 2026-03-16T23:59:48Z | 7761426 | 0.030943765 |
| 2026-03-17T23:59:48Z | 7768619 | 0.029703251 |
| 2026-03-18T23:59:48Z | 7775819 | 0.032287887 |
| 2026-03-19T23:59:48Z | 7783014 | 0.03042276639596456062 |
| 2026-03-20T23:59:48Z | 7790201 | 0.031284104 |
| 2026-03-21T23:59:48Z | 7797398 | 0.029502348 |
| 2026-03-22T23:59:48Z | 7804598 | 0.030172707 |
| 2026-03-23T23:59:48Z | 7811798 | 0.028908879 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.0310816210157460227 |
| 2026-03-25T23:59:48Z | 7826196 | 0.030359735 |
| 2026-03-26T23:59:48Z | 7833396 | 0.031914092 |
| 2026-03-27T23:59:48Z | 7840596 | 0.029982715 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.02962583 |
| 2026-03-29T23:59:48Z | 7854902 | 0.029185775 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.030418192 |
| 2026-03-31T23:59:48Z | 7869291 | 0.030128411 |
| 2026-04-01T23:59:48Z | 7876474 | 0.030658798 |
| 2026-04-02T23:59:48Z | 7883622 | 0.029084897 |
| 2026-04-03T23:59:48Z | 7890794 | 0.029913742 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.030248639 |
| 2026-04-05T23:59:48Z | 7905188 | 0.029569831 |
| 2026-04-06T23:59:48Z | 7912388 | 0.029539415 |
| 2026-04-07T23:59:48Z | 7919588 | 0.029228075 |
| 2026-04-08T23:59:48Z | 7926788 | 0.030444136 |
| 2026-04-09T23:59:48Z | 7933987 | 0.029256262 |
| 2026-04-10T23:59:48Z | 7941184 | 0.029830419 |
| 2026-04-11T23:59:48Z | 7948384 | 0.031262626 |
| 2026-04-12T23:59:48Z | 7955584 | 0.031115615 |
| 2026-04-13T23:59:48Z | 7962784 | 0.03114932 |
| 2026-04-14T23:59:48Z | 7969979 | 0.031639618 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.035818598 |
| 2026-04-16T23:59:48Z | 7984379 | 0.035639021 |
| 2026-04-17T23:59:48Z | 7991579 | 0.036198966 |
| 2026-04-18T23:59:48Z | 7998779 | 0.03661732 |
| 2026-04-19T23:59:48Z | 8005979 | 0.036566889 |
| 2026-04-20T23:59:48Z | 8013179 | 0.037855267 |
| 2026-04-21T23:59:48Z | 8020376 | 0.037458089 |
| 2026-04-22T23:59:48Z | 8027562 | 0.037560169 |
| 2026-04-23T23:59:48Z | 8034762 | 0.036351341 |
| 2026-04-24T23:59:48Z | 8041962 | 0.034618369 |
| 2026-04-25T23:59:48Z | 8049151 | 0.033981624 |
| 2026-04-26T23:59:48Z | 8056274 | 0.035385104 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.035223109 |
| 2026-04-28T23:59:48Z | 8070646 | 0.033758028 |
| 2026-04-29T23:59:48Z | 8077790 | 0.033764557 |
| 2026-04-30T23:59:48Z | 8084984 | 0.035209021 |
| 2026-05-01T23:59:48Z | 8092168 | 0.036086238 |
| 2026-05-02T23:59:48Z | 8099357 | 0.035106966 |
| 2026-05-03T16:10:00Z | 8104202 | 0.034981927 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

