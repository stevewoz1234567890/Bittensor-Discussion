# NetUID 105 — Beam (`Գ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Beam** (NetUID **105**) (`Գ`).

Decentralized bandwidth. A global network. Powering the open internet.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `92`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,343.441716411. **Alpha liquidity in pool (`alpha_in`)** = ‎362,076.938266012Գ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,333,566.251219817Գ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011967616`** *(also **moving-average price** `0.012303878786042333` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎244,747.118746649Գ‎`. **Owner hotkey / coldkey (chain):** `5HBSExJPHsaHV3TuohhRi4oajphhVXFyanhWN96Ed3DHHTY4` / `5G3ic2pAzVu1gZmeUQfKGox3P8TetJw87asvyAdkb2o8aCCX`.
- **Subnet registered at block:** `6841399` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎61.962989599Գ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.005983807` · α-out `‎1.000000000Գ‎` · α-in `‎0.500000000Գ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104343`
- **Liquidity constant `k`:** `1572660078214966847383922932`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Beam`
- **Symbol (API):** `Գ`
- **Rank:** `71`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.0121889`
- **Market cap:** `16209465805670.0217858`
- **Market cap Δ 1d:** `-3.748828659209737306`
- **Liquidity:** `8753560772535`
- **Total τ:** `4382098046273`
- **Total α:** `1695306970526699`
- **α in pool:** `358642923172888`
- **α staked:** `971211764753834`
- **Price Δ 1h:** `0.892202638300182963`
- **Price Δ 1d:** `-4.455263547765313425`
#### Subnet activity (TAOStats)

- **NetUID (API):** `105`
- **Owner SS58 (API):** `5G3ic2pAzVu1gZmeUQfKGox3P8TetJw87asvyAdkb2o8aCCX`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `6841399`
- **Registration wall time:** `2025-11-09T01:33:00.001Z`
- **Registration cost snapshot:** `284712547529`
- **Active keys:** `256`
- **Active validators:** `6`
- **Active miners:** `13`
- **Active dual-role:** `0`
- **Emission:** `6094597`
- **Max neurons:** `256`
- **Validator slots (metadata):** `6`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `72919460`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** The incentivized network powering global data transfer at scale. Built on Bittensor.

**Fetched document title:** BEAM - Decentralized distributed Bandwidth Infrastructure

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
- **`immunity_period` (blocks):** 7500
- **Registration recycle cost snapshot (`burn`):** τ0.046202388
- **Owner SS58 (`owner_ss58`):** `5G3ic2pAzVu1gZmeUQfKGox3P8TetJw87asvyAdkb2o8aCCX`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7500` blocks
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

*No miner/validator sections auto-matched.* Open [https://github.com/orgs/Beam-Network/repositories](https://github.com/orgs/Beam-Network/repositories) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://b1m.ai](https://b1m.ai)
- **GitHub:** [https://github.com/orgs/Beam-Network/repositories](https://github.com/orgs/Beam-Network/repositories)
- **Discord:** [https://discord.com/channels/799672011265015819/1437473346026475702](https://discord.com/channels/799672011265015819/1437473346026475702)
- **Logo URL:** [https://pbs.twimg.com/profile_images/2029345851412185088/vd2bTk4L_400x400.jpg](https://pbs.twimg.com/profile_images/2029345851412185088/vd2bTk4L_400x400.jpg)
- **Contact:** info@b1m.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.012208907 |
| 8104292 | 0.012186014 |
| 8104340 | 0.01220131 |
| 8104388 | 0.011976629 |
| 8104436 | 0.011967619 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

