# NetUID 67 — Harnyx (`ط`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Harnyx** (NetUID **67**) (`ط`).

Deep research as a commodity. Faster, cheaper, traceable research — produced by a competitive swarm of miners on Bittensor SN67.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `54`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ911.310509759. **Alpha liquidity in pool (`alpha_in`)** = ‎81,061.968798962ط‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎272,091.527839868ط‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011242498`** *(also **moving-average price** `0.010235117748379707` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎7,211.737233264ط‎`. **Owner hotkey / coldkey (chain):** `5Cm4fATsr3S1AUX9WTkwaV1qiYtzPVdRpLWSEDmvvEkoT7Rt` / `5HEAv3TU1yNei4GwiTsxfmDCDW9pMCKLeDVky9iaVJfYiVeY`.
- **Subnet registered at block:** `7236936` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎28.173785907ط‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.005621246` · α-out `‎1.000000000ط‎` · α-in `‎0.500000000ط‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104381`
- **Liquidity constant `k`:** `73872624108250213210070158`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Harnyx` |
| Symbol (API) | `ط` |
| Rank | `123` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.011257247` |
| Market cap | `2762165544959.355043922` |
| Market cap Δ 1d | `20.723503979787426565` |
| Liquidity | `1821220818295` |
| Total τ | `910596079835` |
| Total α | `352808476577485` |
| α in pool | `80892312166610` |
| α staked | `164475453589916` |
| Price Δ 1h | `-0.728790073908117812` |
| Price Δ 1d | `17.034905619870608415` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `67` |
| Owner SS58 (API) | `5HEAv3TU1yNei4GwiTsxfmDCDW9pMCKLeDVky9iaVJfYiVeY` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7236936` |
| Registration wall time | `2026-01-03T00:53:12Z` |
| Registration cost snapshot | `217350301782` |
| Active keys | `256` |
| Active validators | `10` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `5628700` |
| Max neurons | `256` |
| Validator slots (metadata) | `10` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# Harnyx Subnet

**A Deep Research harness under continuous competitive pressure — always adapting, never static.**

Harnyx (SN 67) is a Bittensor subnet for deep research. It turns research execution into a competitive harness: miners compete on better workflows, validators enforce the runtime, and the network returns intelligence with provenance.

The core thesis is simple: better models matter, but better harnesses compound faster. Deep research is not one reasoning step. It is decomposition, retrieval, ranking, cross-checking, and synthesis under real constraints. Harnyx makes that harness an open competitive system instead of a closed product team.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Deep research, native to agents. Harnyx delivers synthesis, comprehensiveness, and full citation at a cost that makes repeated calling viable.

**Fetched document title:** Harnyx — Deep Research API for AI Agents | Bittensor SN67

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
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5HEAv3TU1yNei4GwiTsxfmDCDW9pMCKLeDVky9iaVJfYiVeY` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
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

## Install dependencies (local dev)

```bash
uv sync --all-packages --dev
```

---





#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/harnyx/harnyx/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://harnyx.ai/](https://harnyx.ai/)
- **GitHub:** [https://github.com/harnyx/harnyx](https://github.com/harnyx/harnyx)
- **Discord:** [https://discord.com/channels/799672011265015819/1457737666316472351](https://discord.com/channels/799672011265015819/1457737666316472351)
- **Logo URL:** [https://harnyx.ai/favicon.svg](https://harnyx.ai/favicon.svg)
- **Contact:** harnyx@brightmount.co

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.011278087 |
| 8104292 | 0.011268174 |
| 8104340 | 0.011264238 |
| 8104388 | 0.011264221 |
| 8104436 | 0.011242503 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in -0.3148767 --> 4.362078
    line [3.060954731, 3.077191211, 3.077191211, 3.077191211, 3.077191211, 3.077191211, 3.077191211, 3.144717429, 3.179010537, 3.211378172, 3.21316843485, 3.229804312, 3.28248757, 3.322050835, 3.322050835, 3.35944049383, 3.395085633, 4.039528999, 0.073222219, 0.029670777, 0.016461034, 0.010714248, 0.008485298, 0.008593921, 0.012684775, 0.015236002, 0.013109345, 0.012230371, 0.011724319, 0.010691769, 0.00924635, 0.007969183, 0.009014247, 0.009295781, 0.00894262, 0.008619606, 0.008965553, 0.008213446, 0.007671855, 0.007788273, 0.007732799, 0.007822405, 0.007877391, 0.007712271, 0.008012284, 0.008211135, 0.008295963, 0.008285725, 0.008273486, 0.008658187, 0.008851534, 0.009256736, 0.009368019, 0.009053366, 0.009886244, 0.011257247]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

