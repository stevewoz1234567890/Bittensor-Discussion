# NetUID 27 — Nodexo (`ג`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Nodexo** (NetUID **27**) (`ג`).

Decentralized AI compute platfrom

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `14`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,739.328216956. **Alpha liquidity in pool (`alpha_in`)** = ‎1,843,210.645383020ג‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,220,287.410780980ג‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004727991`** *(also **moving-average price** `0.004703634884208441` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎608,234.260026068ג‎`. **Owner hotkey / coldkey (chain):** `5Cyfk5Jjee6uCafjZyUUjtKd7Q4qh1yJ48Ts7bkT9xXaDqe1` / `5CopvHeTZHNy6RMztuRFvViwwZbsZaVkJPA9zmRRnPAna73M`.
- **Subnet registered at block:** `1727132` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎10.579213107ג‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002363994` · α-out `‎1.000000000ג‎` · α-in `‎0.500000000ג‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104421`
- **Liquidity constant `k`:** `16108422802989506190278487120`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Nodexo` |
| Symbol (API) | `ג` |
| Rank | `58` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004727609` |
| Market cap | `19749618960333.004475377` |
| Market cap Δ 1d | `2.539442240069949118` |
| Liquidity | `17452205884142` |
| Total τ | `8738421918729` |
| Total α | `5063232098171489` |
| α in pool | `1843169341079829` |
| α staked | `2334337504417124` |
| Price Δ 1h | `0.146800915715726488` |
| Price Δ 1d | `2.406913124981858527` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `27` |
| Owner SS58 (API) | `5CopvHeTZHNy6RMztuRFvViwwZbsZaVkJPA9zmRRnPAna73M` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `1727132` |
| Registration wall time | `2023-11-16T17:10:48Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `17` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `2363801` |
| Max neurons | `256` |
| Validator slots (metadata) | `17` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 256 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 7200 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5CopvHeTZHNy6RMztuRFvViwwZbsZaVkJPA9zmRRnPAna73M` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `7200` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `2` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No miner/validator sections auto-matched.* Open [https://github.com/neuralinternet/compute-subnet](https://github.com/neuralinternet/compute-subnet) for requirements.

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/neuralinternet/compute-subnet](https://github.com/neuralinternet/compute-subnet)
- **Discord:** [https://discord.com/invite/nodexo](https://discord.com/invite/nodexo)
- **Logo URL:** [https://console.nodexo.ai/assets/images/logo/logo-dark.svg](https://console.nodexo.ai/assets/images/logo/logo-dark.svg)
- **Contact:** neuralinternet@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.004727599 |
| 8104244 | 0.004727672 |
| 8104292 | 0.00472775 |
| 8104340 | 0.004727822 |
| 8104388 | 0.004727909 |
| 8104436 | 0.004727992 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

