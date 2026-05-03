# NetUID 21 — AdTAO (`φ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**AdTAO** (NetUID **21**) (`φ`).

Counterfactual impact prediction for advertising interventions

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `8`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,989.048727218. **Alpha liquidity in pool (`alpha_in`)** = ‎1,742,679.365284923φ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,203,917.524716854φ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005152614`** *(also **moving-average price** `0.0050750491209328175` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎434,426.576877810φ‎`. **Owner hotkey / coldkey (chain):** `5HiWPApiuXz9DDnkyFu4M2tWs2ar6LTKt54Bo18EL6pgZsdn` / `5HjCYVfrWSkzTfJM5rkWBW3qTTJqXEFUzZrKty5hodpgfjyW`.
- **Subnet registered at block:** `3156578` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎6.035047011φ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000661004` · α-out `‎1.000000000φ‎` · α-in `‎0.128285293φ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104427`
- **Liquidity constant `k`:** `15665029730463509187075134214`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `AdTAO`
- **Symbol (API):** `φ`
- **Rank:** `48`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005152665`
- **Market cap:** `22645802011180.505456145`
- **Market cap Δ 1d:** `3.231388550696833015`
- **Liquidity:** `17968183161216`
- **Total τ:** `8988938912062`
- **Total α:** `4946333950308591`
- **α in pool:** `1742640798335304`
- **α staked:** `2652328020941809`
- **Price Δ 1h:** `0.065232091470190352`
- **Price Δ 1d:** `3.128418740210369233`
#### Subnet activity (TAOStats)

- **NetUID (API):** `21`
- **Owner SS58 (API):** `5HjCYVfrWSkzTfJM5rkWBW3qTTJqXEFUzZrKty5hodpgfjyW`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `3156578`
- **Registration wall time:** `2024-06-11T16:58:24Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `663692`
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

**Landing meta / crawler:** AI-powered Google Ads management that works 24/7. Join the rebellion against outdated PPC management.

**Fetched document title:** AdTAO by PPC Rebel - Your 24/7 Google Ads Manager | AI-Powered PPC Optimization

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
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5HjCYVfrWSkzTfJM5rkWBW3qTTJqXEFUzZrKty5hodpgfjyW`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `100`
- **`weights_rate_limit`:** `180`
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

*No GitHub URL on-chain; hardware notes not fetched automatically.*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://ppcrebel.com](https://ppcrebel.com)
- **Logo URL:** [https://www.ppcrebel.com/i/adtao.png](https://www.ppcrebel.com/i/adtao.png)
- **Contact:** adtao@ppcrebel.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.005152666 |
| 8104244 | 0.005152648 |
| 8104292 | 0.005152637 |
| 8104340 | 0.00515262 |
| 8104388 | 0.005152618 |
| 8104436 | 0.005152614 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

