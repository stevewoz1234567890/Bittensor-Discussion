# NetUID 20 — GroundLayer (`υ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**GroundLayer** (NetUID **20**) (`υ`).

Structured OTC deals for subnet tokens.



#### SubnetIdentity `additional` *(chain)*



The Capital Layer for Bittensor

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `7`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,503.401070110. **Alpha liquidity in pool (`alpha_in`)** = ‎2,085,876.186910979υ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,826,987.633775362υ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004078607`** *(also **moving-average price** `0.004109193570911884` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎255,147.511348156υ‎`. **Owner hotkey / coldkey (chain):** `5EALa14jRfwHf69ZbNyFLxsPrZgZ47T2qhYxGjXxRM1qriNk` / `5FuzgvtfbZWdKSRxyYVPAPYNaNnf9cMnpT7phL3s2T3Kkrzo`.
- **Subnet registered at block:** `1970929` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎5.278019911υ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000467956` · α-out `‎1.000000000υ‎` · α-in `‎0.114734354υ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104428`
- **Liquidity constant `k`:** `17737041799895785203907737690`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `GroundLayer`
- **Symbol (API):** `υ`
- **Rank:** `74`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004078639`
- **Market cap:** `15750403064139.107643175`
- **Market cap Δ 1d:** `1.194845528362184273`
- **Liquidity:** `17010718606965`
- **Total τ:** `8503325941297`
- **Total α:** `4912604043543200`
- **α in pool:** `2085841052779658`
- **α staked:** `1775840028615167`
- **Price Δ 1h:** `-0.000441321738993987`
- **Price Δ 1d:** `1.057493398718867065`
#### Subnet activity (TAOStats)

- **NetUID (API):** `20`
- **Owner SS58 (API):** `5FuzgvtfbZWdKSRxyYVPAPYNaNnf9cMnpT7phL3s2T3Kkrzo`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `1970929`
- **Registration wall time:** `2023-12-20T14:36:12Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `469859`
- **Max neurons:** `256`
- **Validator slots (metadata):** `11`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Structured OTC deals for the subnet economy. Raise capital, allocate funds, and earn rewards.

**Fetched document title:** GroundLayer — The Capital Layer for Bittensor

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
- **Owner SS58 (`owner_ss58`):** `5FuzgvtfbZWdKSRxyYVPAPYNaNnf9cMnpT7phL3s2T3Kkrzo`

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

*No miner/validator sections auto-matched.* Open [https://github.com/RogueTensor/comingsoon](https://github.com/RogueTensor/comingsoon) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://groundlayer.xyz](https://groundlayer.xyz)
- **GitHub:** [https://github.com/RogueTensor/comingsoon](https://github.com/RogueTensor/comingsoon)
- **Logo URL:** [https://www.groundlayer.xyz/icon.png](https://www.groundlayer.xyz/icon.png)
- **Contact:** groundlayer@rizzo.network

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.00407864 |
| 8104244 | 0.004078628 |
| 8104292 | 0.004078621 |
| 8104340 | 0.00407861 |
| 8104388 | 0.004078609 |
| 8104436 | 0.004078607 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

