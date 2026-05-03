# NetUID 61 — RedTeam (`ر`)

## Overview

**RedTeam** (NetUID **61**) (`ر`).

"The RedTeam subnet by Innerworks is a decentralized platform designed to drive innovation in cybersecurity through competitive programming challenges.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `189`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,609.423037028. **Alpha liquidity in pool (`alpha_in`)** = ‎1,963,781.094211283ر‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,040,433.364063831ر‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003877588`** *(also **moving-average price** `0.0038625344168394804` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎347,541.409897667ر‎`. **Owner hotkey / coldkey (chain):** `5ECEsYL82fbXx9KfTZy7G2KXSurnScciJyAVMHZjekc8jUbn` / `5ECEsYL82fbXx9KfTZy7G2KXSurnScciJyAVMHZjekc8jUbn`.
- **Subnet registered at block:** `4457976` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎142.697561605ر‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ر‎` · α-in `‎0.000000000ر‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003877588`
- **Market cap:** `16989694547362.452170112`
- **Liquidity:** `15224157042556`
- **Total τ:** `7609423249406`
- **Total α:** `5004201458275114`
- **α in pool:** `1963781039437614`
- **α staked:** `2417729979103410`
- **Price Δ 1h:** `-0.39885788145023164`
- **Price Δ 1d:** `0.784162261547874445`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `9`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

"The RedTeam subnet by Innerworks is a decentralized platform designed to drive innovation in cybersecurity through competitive programming challenges. The subnet incentivizes miners to develop and submit code solutions to various technical challenges, with a focus on enhancing security. These solutions can be integrated into real-world products to improve their security features."

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Transform your skills in circumventing and breaking detection mechanisms into meaningful, rewarding work. Compete, innovate, and earn in a safe, decentralized platform.

**Fetched document title:** Harness Red Team Ingenuity to Tackle the Internet's Challenges | RedTeam

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
- **`immunity_period` (blocks):** 14400
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5ECEsYL82fbXx9KfTZy7G2KXSurnScciJyAVMHZjekc8jUbn`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `14400` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
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

## Scoring System: Fair, Dynamic, and Motivating

We've introduced an exciting new way to score miners that rewards innovation and long-term engagement. Here's how the new scoring system works:

---

## Validator Setup

[Read the full documentation](./docs/1.validator.md)

---

## Miner Setup

[Read the full documentation](./docs/2.miner.md)

---

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/RedTeamSubnet/RedTeam/main/README.md`*

## On-chain identity — description


"The RedTeam subnet by Innerworks is a decentralized platform designed to drive innovation in cybersecurity through competitive programming challenges. The subnet incentivizes miners to develop and submit code solutions to various technical challenges, with a focus on enhancing security. These solutions can be integrated into real-world products to improve their security features."

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.theredteam.io/](https://www.theredteam.io/)
- **GitHub:** [https://github.com/RedTeamSubnet/RedTeam](https://github.com/RedTeamSubnet/RedTeam)
- **Discord:** [https://discord.com/channels/799672011265015819/1319313447435108413](https://discord.com/channels/799672011265015819/1319313447435108413)
- **Contact:** oscar@theredteam.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.003872512 |
| 8104072 | 0.003872509 |
| 8104120 | 0.003872504 |
| 8104168 | 0.00387759 |
| 8104216 | 0.003877588 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

