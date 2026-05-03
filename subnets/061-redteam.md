# NetUID 61 — RedTeam (`ر`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**RedTeam** (NetUID **61**) (`ر`).

"The RedTeam subnet by Innerworks is a decentralized platform designed to drive innovation in cybersecurity through competitive programming challenges. The subnet incentivizes miners to develop and submit code solutions to various technical challenges, with a focus on enhancing security. These solutions can be integrated into real-world products to improve their security features."

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `48`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,609.048314603. **Alpha liquidity in pool (`alpha_in`)** = ‎1,963,877.736999041ر‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,040,556.721276073ر‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003877208`** *(also **moving-average price** `0.00386336469091475` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎347,541.784620092ر‎`. **Owner hotkey / coldkey (chain):** `5ECEsYL82fbXx9KfTZy7G2KXSurnScciJyAVMHZjekc8jUbn` / `5ECEsYL82fbXx9KfTZy7G2KXSurnScciJyAVMHZjekc8jUbn`.
- **Subnet registered at block:** `4457976` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎36.240899313ر‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ر‎` · α-in `‎0.000000000ر‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104387`
- **Liquidity constant `k`:** `14943240584798906616077295723`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `RedTeam`
- **Symbol (API):** `ر`
- **Rank:** `65`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003877588`
- **Market cap:** `16989694547362.452170112`
- **Market cap Δ 1d:** `0.915800416854565208`
- **Liquidity:** `15224157042556`
- **Total τ:** `7609423249406`
- **Total α:** `5004201458275114`
- **α in pool:** `1963781039437614`
- **α staked:** `2417729979103410`
- **Price Δ 1h:** `-0.39885788145023164`
- **Price Δ 1d:** `0.784162261547874445`
#### Subnet activity (TAOStats)

- **NetUID (API):** `61`
- **Owner SS58 (API):** `5ECEsYL82fbXx9KfTZy7G2KXSurnScciJyAVMHZjekc8jUbn`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `4457976`
- **Registration wall time:** `2024-12-11T12:23:48.001Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `9`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `13`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Transform your skills in circumventing and breaking detection mechanisms into meaningful, rewarding work. Compete, innovate, and earn in a safe, decentralized platform.

**Fetched document title:** Harness Red Team Ingenuity to Tackle the Internet's Challenges | RedTeam

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.theredteam.io/](https://www.theredteam.io/)
- **GitHub:** [https://github.com/RedTeamSubnet/RedTeam](https://github.com/RedTeamSubnet/RedTeam)
- **Discord:** [https://discord.com/channels/799672011265015819/1319313447435108413](https://discord.com/channels/799672011265015819/1319313447435108413)
- **Contact:** oscar@theredteam.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.00387723 |
| 8104292 | 0.003877223 |
| 8104340 | 0.003877212 |
| 8104388 | 0.003877211 |
| 8104436 | 0.003877208 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

