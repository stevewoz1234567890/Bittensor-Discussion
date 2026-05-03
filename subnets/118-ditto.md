# NetUID 118 — Ditto (`ⲁ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Ditto** (NetUID **118**) (`ⲁ`).

Open-Source Claude Cowork



#### SubnetIdentity `additional` *(chain)*



The Ditto Agent OS and Harness enable SOTA memory, healing, and speed for 1/100th of the frontier cost.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `105`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,876.958250878. **Alpha liquidity in pool (`alpha_in`)** = ‎539,380.453070109ⲁ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,419,936.824009720ⲁ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007176782`** *(also **moving-average price** `0.007323272759094834` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎123,664.933469567ⲁ‎`. **Owner hotkey / coldkey (chain):** `5HmP9732JFjnut2RY9yg4Gz2qJ38vF8xFwZb5dQVPF7FsmZz` / `5DUJfND9r2BjiJHNKSxJxzT7ptrxiseFe1GxeMwcTov52Y55`.
- **Subnet registered at block:** `5724794` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎72.116375680ⲁ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003588381` · α-out `‎1.000000000ⲁ‎` · α-in `‎0.500000000ⲁ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104330`
- **Liquidity constant `k`:** `2091155497892472953744805702`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Ditto`
- **Symbol (API):** `ⲁ`
- **Rank:** `83`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.007124284`
- **Market cap:** `13382774130574.970169368`
- **Market cap Δ 1d:** `-1.875394031936708742`
- **Liquidity:** `7717942992664`
- **Total τ:** `3861879518433`
- **Total α:** `1959133579272516`
- **α in pool:** `541256282628818`
- **α staked:** `1337216575917384`
- **Price Δ 1h:** `-1.531304098437127466`
- **Price Δ 1d:** `-1.965537388803985952`
#### Subnet activity (TAOStats)

- **NetUID (API):** `118`
- **Owner SS58 (API):** `5DUJfND9r2BjiJHNKSxJxzT7ptrxiseFe1GxeMwcTov52Y55`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `5724794`
- **Registration wall time:** `2025-06-06T23:15:36Z`
- **Registration cost snapshot:** `110644724664`
- **Active keys:** `256`
- **Active validators:** `14`
- **Active miners:** `1`
- **Active dual-role:** `1`
- **Emission:** `3562108`
- **Max neurons:** `256`
- **Validator slots (metadata):** `14`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `723690`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** The smart home for your agents. Ditto organizes the context your AI needs and operationalizes it across every thread, tool, and workflow.

**Fetched document title:** Ditto

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
- **`immunity_period` (blocks):** 300
- **Registration recycle cost snapshot (`burn`):** τ0.000727871
- **Owner SS58 (`owner_ss58`):** `5DUJfND9r2BjiJHNKSxJxzT7ptrxiseFe1GxeMwcTov52Y55`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `300` blocks
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

*No miner/validator sections auto-matched.* Open [https://github.com/orgs/ditto-assistant/repositories](https://github.com/orgs/ditto-assistant/repositories) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://heyditto.ai](https://heyditto.ai)
- **GitHub:** [https://github.com/orgs/ditto-assistant/repositories](https://github.com/orgs/ditto-assistant/repositories)
- **Discord:** [https://discord.gg/qNKYZEMpkD](https://discord.gg/qNKYZEMpkD)
- **Logo URL:** [https://f005.backblazeb2.com/file/ditto-assets/ditto-logo.png](https://f005.backblazeb2.com/file/ditto-assets/ditto-logo.png)
- **Contact:** peyton@omniaura.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.007101465 |
| 8104292 | 0.007109591 |
| 8104340 | 0.00708018 |
| 8104388 | 0.007238449 |
| 8104436 | 0.007176801 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

