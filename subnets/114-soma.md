# NetUID 114 — SOMA (`Є`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**SOMA** (NetUID **114**) (`Є`).

AI solutions delivered through MCP infrastructure

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `101`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ2,129.697167266. **Alpha liquidity in pool (`alpha_in`)** = ‎183,841.081661755Є‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎719,408.005430084Є‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011588802`** *(also **moving-average price** `0.011182382004335523` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎52,913.006551372Є‎`. **Owner hotkey / coldkey (chain):** `5H1nRfbCbDGh3t17er9Y8hwFEsXCrjBbaN6jLrnez8KpUKju` / `5FHrQMjzzAhmL5zS9ys87ZrGCwG3vsVT9hXAUWZQ8SNdRqig`.
- **Subnet registered at block:** `7312241` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎61.672752005Є‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.005794397` · α-out `‎1.000000000Є‎` · α-in `‎0.500000000Є‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104334`
- **Liquidity constant `k`:** `391525830842157003470111830`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `SOMA` |
| Symbol (API) | `Є` |
| Rank | `102` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.011582899` |
| Market cap | `7519042556749.064911667` |
| Market cap Δ 1d | `10.287200878891706306` |
| Liquidity | `4256408037878` |
| Total τ | `2127802436915` |
| Total α | `902915308237220` |
| α in pool | `183771403079982` |
| α staked | `465378913844051` |
| Price Δ 1h | `0.278362973265969142` |
| Price Δ 1d | `8.797219020019971222` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `114` |
| Owner SS58 (API) | `5FHrQMjzzAhmL5zS9ys87ZrGCwG3vsVT9hXAUWZQ8SNdRqig` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7312241` |
| Registration wall time | `2026-01-13T12:01:12Z` |
| Registration cost snapshot | `307770370853` |
| Active keys | `256` |
| Active validators | `10` |
| Active miners | `59` |
| Active dual-role | `1` |
| Emission | `5791457` |
| Max neurons | `256` |
| Validator slots (metadata) | `10` |
| Max validators (API) | `64` |
| Neuron reg. cost | `50000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** SOMA connects AI subnets on Bittensor (SN114) into a decentralized intelligence bridge. Explore validators, miners and the SOMA ecosystem.

**Fetched document title:** SOMA Subnet | Bittensor Subnet 114 - Bridge for Intelligence

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
| Registration recycle cost snapshot (`burn`) | τ0.050000000 |
| Owner SS58 (`owner_ss58`) | `5FHrQMjzzAhmL5zS9ys87ZrGCwG3vsVT9hXAUWZQ8SNdRqig` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.050000000 / τ100.000000000 |
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

### Validators

Validators score miner solutions by:
- Fetching execution results from the platform
- Evaluatimg solution quality based on competition criteria
- Reporting scores to the platform for weight calculation

**Min Hardware Requirements:**
- 4 CPU cores
- 16 GB RAM
- 200 GB SSD storage

[**→ Validator Setup Guide**](docs/validator/validator-setup.md)

---

### Miners

On SOMA, any problem that can be meaningfully solved using an MCP server - and that can significantly improve agent performance - may become a competition target. Miners compete to deliver the most effective model or algorithm for a given task.


The miner’s responsibility is to design and implement model or algorithm that solves the defined problem as effectively as possible and upload it to the platform

**All a miner needs to participate is:**
- A working algorithm that solves the active MCP task
- A registered hotkey on netuid 114

The platform handles orchestration and evaluation. Validators automatically retrieve submitted solutions associated with registered hotkeys and score them according to the active competition criteria.

[**→ Miner Setup Guide**](docs/miner/miner-setup.md)

---

#### CPU / GPU / RAM lines (automatic grep)

- - 4 CPU cores
- - 16 GB RAM
- - 200 GB SSD storage


*Primary README URL used: `https://raw.githubusercontent.com/DendriteHQ/SOMA/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://thesoma.ai](https://thesoma.ai)
- **GitHub:** [https://github.com/DendriteHQ/SOMA](https://github.com/DendriteHQ/SOMA)
- **Discord:** [https://discord.gg/durr4Sg6sM](https://discord.gg/durr4Sg6sM)
- **Logo URL:** [https://thesoma.ai/images/1200x1200.png](https://thesoma.ai/images/1200x1200.png)
- **Contact:** https://x.com/SomaSubnet

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.01162004 |
| 8104292 | 0.011698096 |
| 8104340 | 0.011588433 |
| 8104388 | 0.011588753 |
| 8104436 | 0.01158881 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.014145113 |
| 2026-03-10T23:59:48Z | — | 0.018708213 |
| 2026-03-11T23:59:48Z | — | 0.018787112 |
| 2026-03-12T23:59:48Z | — | 0.017341685 |
| 2026-03-13T23:59:48Z | — | 0.013509706 |
| 2026-03-14T23:59:48Z | — | 0.013736897 |
| 2026-03-15T23:59:48Z | — | 0.012874071 |
| 2026-03-16T23:59:48Z | — | 0.013342145 |
| 2026-03-17T23:59:48Z | — | 0.012856672 |
| 2026-03-18T23:59:48Z | — | 0.011486531 |
| 2026-03-19T23:59:48Z | — | 0.0106870819451 |
| 2026-03-20T23:59:48Z | — | 0.011878434 |
| 2026-03-21T23:59:48Z | — | 0.014982406 |
| 2026-03-22T23:59:48Z | — | 0.014045295 |
| 2026-03-23T23:59:48Z | — | 0.013360018 |
| 2026-03-24T23:59:48Z | — | 0.0133915907418 |
| 2026-03-25T23:59:48Z | — | 0.013089942 |
| 2026-03-26T23:59:48Z | — | 0.012007244 |
| 2026-03-27T23:59:48Z | — | 0.011995967 |
| 2026-03-28T23:59:48Z | — | 0.012825505 |
| 2026-03-29T23:59:48Z | — | 0.011578931 |
| 2026-03-30T23:59:48Z | — | 0.010711026 |
| 2026-03-31T23:59:48Z | — | 0.009728639 |
| 2026-04-01T23:59:48Z | — | 0.009298366 |
| 2026-04-02T23:59:48Z | — | 0.009688953 |
| 2026-04-03T23:59:48Z | — | 0.009034444 |
| 2026-04-04T23:59:48Z | — | 0.009879299 |
| 2026-04-05T23:59:48Z | — | 0.009824813 |
| 2026-04-06T23:59:48Z | — | 0.009761609 |
| 2026-04-07T23:59:48Z | — | 0.010231365 |
| 2026-04-08T23:59:48Z | — | 0.009936956 |
| 2026-04-09T23:59:48Z | — | 0.009043035 |
| 2026-04-10T23:59:48Z | — | 0.00975133 |
| 2026-04-11T23:59:48Z | — | 0.009809263 |
| 2026-04-12T23:59:48Z | — | 0.009501632 |
| 2026-04-13T23:59:48Z | — | 0.008984958 |
| 2026-04-14T23:59:48Z | — | 0.009325484 |
| 2026-04-15T23:59:48Z | — | 0.008828686 |
| 2026-04-16T23:59:48Z | — | 0.010187139 |
| 2026-04-17T23:59:48Z | — | 0.010028218 |
| 2026-04-18T23:59:48Z | — | 0.009673318 |
| 2026-04-19T23:59:48Z | — | 0.009534026 |
| 2026-04-20T23:59:48Z | — | 0.010386676 |
| 2026-04-21T23:59:48Z | — | 0.010923253 |
| 2026-04-22T23:59:48Z | — | 0.009883125 |
| 2026-04-23T23:59:48Z | — | 0.009556061 |
| 2026-04-24T23:59:48Z | — | 0.009881534 |
| 2026-04-25T23:59:48Z | — | 0.009714538 |
| 2026-04-26T23:59:48Z | — | 0.009233026 |
| 2026-04-27T23:59:48Z | — | 0.009689883 |
| 2026-04-28T23:59:48Z | — | 0.010036834 |
| 2026-04-29T23:59:48Z | — | 0.009972559 |
| 2026-04-30T23:59:48Z | — | 0.009939907 |
| 2026-05-01T23:59:48Z | — | 0.01086625 |
| 2026-05-02T23:59:48Z | — | 0.011195959 |
| 2026-05-03T23:59:48Z | — | 0.011582899 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

