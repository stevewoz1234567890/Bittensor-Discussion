# NetUID 117 — Unknown (`Ⲁ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Unknown** (NetUID **117**) (`Ⲁ`).

~

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `104`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,094.302309978. **Alpha liquidity in pool (`alpha_in`)** = ‎754,618.626016719Ⲁ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,257,954.324862950Ⲁ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004100519`** *(also **moving-average price** `0.004077306017279625` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎96,911.784546375Ⲁ‎`. **Owner hotkey / coldkey (chain):** `5CyXUidjedyVBR2UsuafJ128DMhWsxzaAxB1Zi7Uyf7jjKVG` / `5D9j5tWvXahPCbHnkhNAhB6Dg4cgGFuDiz4KNHBBxPRTSAYX`.
- **Subnet registered at block:** `5710859` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎71.679045415Ⲁ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002050258` · α-out `‎1.000000000Ⲁ‎` · α-in `‎0.500000000Ⲁ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104331`
- **Liquidity constant `k`:** `2335018157635958090548522182`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Unknown` |
| Symbol (API) | `Ⲁ` |
| Rank | `103` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004160487` |
| Market cap | `7232177306298.767133318` |
| Market cap Δ 1d | `3.545249305608156923` |
| Liquidity | `6232750953798` |
| Total τ | `3116465219579` |
| Total α | `2012271968567872` |
| α in pool | `749019461956985` |
| α staked | `989281200032529` |
| Price Δ 1h | `-0.111784877494002007` |
| Price Δ 1d | `2.971187777166732914` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `117` |
| Owner SS58 (API) | `5D9j5tWvXahPCbHnkhNAhB6Dg4cgGFuDiz4KNHBBxPRTSAYX` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5710859` |
| Registration wall time | `2025-06-05T00:48:24Z` |
| Registration cost snapshot | `107183582952` |
| Active keys | `70` |
| Active validators | `1` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `2080241` |
| Max neurons | `256` |
| Validator slots (metadata) | `1` |
| Max validators (API) | `64` |
| Neuron reg. cost | `10000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `720` |

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <img src="voibes.jpeg" alt="voibes">
</p>

# Chi: A Vibe-Codable Bittensor Subnet Template.

1. Clone this repo into Cursor
2. Ask your agent: "How do I make: [your subnet idea]? @knowledge"

Made by Const <3

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Vibe-codable Bittensor Subnet Template. Contribute to helionlink/Chi development by creating an account on GitHub.

**Fetched document title:** GitHub - helionlink/Chi: Vibe-codable Bittensor Subnet Template · GitHub

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 72 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 21600 |
| Registration recycle cost snapshot (`burn`) | τ0.013120673 |
| Owner SS58 (`owner_ss58`) | `5D9j5tWvXahPCbHnkhNAhB6Dg4cgGFuDiz4KNHBBxPRTSAYX` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.010000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `21600` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `720` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `True` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `3` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `52429`, `3277` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/helionlink/Chi/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/helionlink/Chi](https://github.com/helionlink/Chi)
- **Discord (handle / invite hint):** `~`
- **Logo:** `~`
- **Contact:** hello@helionlink.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004143995 |
| 8104292 | 0.004170597 |
| 8104340 | 0.004144077 |
| 8104388 | 0.004144169 |
| 8104436 | 0.004100521 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

