# NetUID 44 — Score (`ף`)

## Overview

**Score** (NetUID **44**) (`ף`).

Making every camera intelligent

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `234`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ57,630.683018640. **Alpha liquidity in pool (`alpha_in`)** = ‎1,645,804.118436906ף‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,254,780.218543725ף‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.034981742`** *(also **moving-average price** `0.035151573130860925` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,667,391.410016518ף‎`. **Owner hotkey / coldkey (chain):** `5FsREvyUXSZWYRqVyQLDdpYmZZPnkhZyW6HjooozKP1nQkwu` / `5CaCekuxb9pKQyLoxh3jbkEXig8fxjkeS4AQ6UmZa12xfQ9H`.
- **Subnet registered at block:** `3550319` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎176.403118071ף‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.015639294` · α-out `‎1.000000000ף‎` · α-in `‎0.447070052ף‎`.

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
| 8104085 | 0.034975946 |
| 8104133 | 0.034981323 |
| 8104181 | 0.034981943 |
| 8104229 | 0.03498183 |
| 8104277 | 0.034981742 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

