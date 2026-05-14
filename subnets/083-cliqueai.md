# NetUID 83 — CliqueAI (`ᚦ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**CliqueAI** (NetUID **83**) (`ᚦ`).

CliqueAI - AI-Powered Maximum Clique Solver Network

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `70`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ5,195.309320585. **Alpha liquidity in pool (`alpha_in`)** = ‎997,177.009003729ᚦ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,744,509.790002944ᚦ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005207708`** *(also **moving-average price** `0.005218382691964507` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎103,786.236368337ᚦ‎`. **Owner hotkey / coldkey (chain):** `5EHGayLmiXfwz6oYmQFYmDz12RPXkhJw8Ty8RYVDeVZH9Q5L` / `5DqEjRLyNN8k3WbEXhA36tyGG4YpWyPEcVSTa47XxspNHhc3`.
- **Subnet registered at block:** `5231190` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎50.057329634ᚦ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002603854` · α-out `‎1.000000000ᚦ‎` · α-in `‎0.500000000ᚦ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104365`
- **Liquidity constant `k`:** `5180643009150145738721461465`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `CliqueAI` |
| Symbol (API) | `ᚦ` |
| Rank | `88` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.005188247` |
| Market cap | `12534670051428.210723745` |
| Market cap Δ 1d | `-1.929317951582419084` |
| Liquidity | `10367681458220` |
| Total τ | `5184972810051` |
| Total α | `2741350799460975` |
| α in pool | `998932519629307` |
| α staked | `1417041517734028` |
| Price Δ 1h | `-0.228475145227194408` |
| Price Δ 1d | `-2.325017047125370829` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `83` |
| Owner SS58 (API) | `5DqEjRLyNN8k3WbEXhA36tyGG4YpWyPEcVSTa47XxspNHhc3` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5231190` |
| Registration wall time | `2025-03-29T01:51:36Z` |
| Registration cost snapshot | `261361408796` |
| Active keys | `256` |
| Active validators | `9` |
| Active miners | `246` |
| Active dual-role | `0` |
| Emission | `2594124` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `64` |
| Neuron reg. cost | `300000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** CliqueAI - AI-Powered Maximum Clique Solver Network

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
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.300000000 |
| Owner SS58 (`owner_ss58`) | `5DqEjRLyNN8k3WbEXhA36tyGG4YpWyPEcVSTa47XxspNHhc3` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.300000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Miner Selection

Smart allocation engine filters eligible miners and samples each miner with the same difficulty-adjusted probability, keeping problem distribution fair while scaling participation by challenge difficulty.

---

### Miner

```
./start_miner.sh --wallet.name <coldkey-name> --wallet.hotkey <hotkey-name> --subtensor.network finney --netuid 83 --logging.info --axon.ip <your-miner-ip> --axon.port <your-miner-port>
```

---

### Validator

```
./start_validator.sh --wallet.name <coldkey-name> --wallet.hotkey <hotkey-name> --subtensor.network finney --netuid 83 --logging.info --axon.ip <your-validator-ip> --axon.port <your-validator-port>
```

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/toptensor/CliqueAI/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://cliqueai.toptensor.ai/](https://cliqueai.toptensor.ai/)
- **GitHub:** [https://github.com/toptensor/CliqueAI](https://github.com/toptensor/CliqueAI)
- **Discord:** [https://discord.com/channels/799672011265015819/1355560253076410428](https://discord.com/channels/799672011265015819/1355560253076410428)
- **Contact:** CliqueAI@toptensor.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.00518822 |
| 8104292 | 0.005188209 |
| 8104340 | 0.005227699 |
| 8104388 | 0.005207889 |
| 8104436 | 0.005207709 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

