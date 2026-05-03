# NetUID 91 — Bitstarter #1 (`ᚁ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Bitstarter #1** (NetUID **91**) (`ᚁ`).

A new subnet launch on Bitstarter - coming soon!

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `78`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,849.662774213. **Alpha liquidity in pool (`alpha_in`)** = ‎99,240.846056429ᚁ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎402,661.628156489ᚁ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.018638957`** *(also **moving-average price** `0.0176071145106107` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎15,676.851074067ᚁ‎`. **Owner hotkey / coldkey (chain):** `5DnPJe7FP8U1oqy2XmQRBEAKD2tdReJmzjhNdogrbN1eCztw` / `5HEe7NjS4exuP9SptWZdwWqWrMrGTTEHf5ieQH8yZXA3zXtW`.
- **Subnet registered at block:** `7633645` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎43.090872355ᚁ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.009319473` · α-out `‎1.000000000ᚁ‎` · α-in `‎0.500000000ᚁ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104357`
- **Liquidity constant `k`:** `183562098631979724884065377`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Bitstarter #1`
- **Symbol (API):** `ᚁ`
- **Rank:** `104`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.018681482`
- **Market cap:** `6353227919928.664187688`
- **Market cap Δ 1d:** `14.512571426577282223`
- **Liquidity:** `3699274575444`
- **Total τ:** `1849595838425`
- **Total α:** `501560490247684`
- **α in pool:** `99011349154155`
- **α staked:** `241070231093529`
- **Price Δ 1h:** `1.444629609045058749`
- **Price Δ 1d:** `12.004939817409259064`
#### Subnet activity (TAOStats)

- **NetUID (API):** `91`
- **Owner SS58 (API):** `5HEe7NjS4exuP9SptWZdwWqWrMrGTTEHf5ieQH8yZXA3zXtW`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `7633645`
- **Registration wall time:** `2026-02-27T05:45:12.001Z`
- **Registration cost snapshot:** `457698047451`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `9340832`
- **Max neurons:** `256`
- **Validator slots (metadata):** `9`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Bittensor's first crowdfunding platform. Discover new teams. Pledge TAO. And get liftoff All on-chain. Built for Bittensor. Open for all.

**Fetched document title:** Bitstarter | Kickstarter For Bittensor

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
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5HEe7NjS4exuP9SptWZdwWqWrMrGTTEHf5ieQH8yZXA3zXtW`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
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

*No GitHub URL on-chain; hardware notes not fetched automatically.*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://bitstarter.ai/](https://bitstarter.ai/)
- **Discord (handle / invite hint):** `officialneeve`
- **Logo URL:** [https://ibb.co/QjjRQ2KG](https://ibb.co/QjjRQ2KG)
- **Contact:** hello@bitstarter.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.01868153 |
| 8104292 | 0.018682627 |
| 8104340 | 0.018677572 |
| 8104388 | 0.01867774 |
| 8104436 | 0.018638969 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

