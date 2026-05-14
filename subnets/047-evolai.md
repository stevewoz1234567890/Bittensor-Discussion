# NetUID 47 — EvolAI (`צ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**EvolAI** (NetUID **47**) (`צ`).

A subnet focused on the research, development, and evaluation of evolving AI systems

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `34`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,041.842359820. **Alpha liquidity in pool (`alpha_in`)** = ‎197,151.199744761צ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎707,135.162641692צ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005284336`** *(also **moving-average price** `0.005133649334311485` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎12,158.851588659צ‎`. **Owner hotkey / coldkey (chain):** `5GjN9n3ndtbRTir5HCRsaaFjxfoQpffnYsAc5VG9iWMfdEWj` / `5DDKR8DVDQ4UaAprFR5gfc6WXFgk3cG6WmBpdKZ8Eah4Z6Mu`.
- **Subnet registered at block:** `7340355` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎20.765392268צ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002642167` · α-out `‎1.000000000צ‎` · α-in `‎0.500000000צ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104401`
- **Liquidity constant `k`:** `205400471183425981921903020`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `EvolAI` |
| Symbol (API) | `צ` |
| Rank | `122` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.005413609` |
| Market cap | `3313045404257.663278468` |
| Market cap Δ 1d | `8.709960954361899426` |
| Liquidity | `2107734532381` |
| Total τ | `1053891178401` |
| Total α | `903950773306331` |
| α in pool | `194665583343812` |
| α staked | `417319028817440` |
| Price Δ 1h | `-0.080288536698044411` |
| Price Δ 1d | `7.386307395769340403` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `47` |
| Owner SS58 (API) | `5DDKR8DVDQ4UaAprFR5gfc6WXFgk3cG6WmBpdKZ8Eah4Z6Mu` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7340355` |
| Registration wall time | `2026-01-17T09:45:12Z` |
| Registration cost snapshot | `315101296012` |
| Active keys | `60` |
| Active validators | `13` |
| Active miners | `23` |
| Active dual-role | `0` |
| Emission | `2706808` |
| Max neurons | `256` |
| Validator slots (metadata) | `13` |
| Max validators (API) | `64` |
| Neuron reg. cost | `50000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to openevolai/evolai development by creating an account on GitHub.

**Fetched document title:** GitHub - openevolai/evolai · GitHub

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 60 |
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
| Owner SS58 (`owner_ss58`) | `5DDKR8DVDQ4UaAprFR5gfc6WXFgk3cG6WmBpdKZ8Eah4Z6Mu` |


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

## Installation

Install [uv](https://github.com/astral-sh/uv), then:

```bash
git clone https://github.com/evolai-subnet/evolai.git
uv pip install -e .
```

Or with pip:

```bash
pip install -e .
```

Verify:

```bash
evolcli --help
```

---

## Mining

Requirements:

- Model name must contain `evolai`
- Model must be public on HuggingFace
- Supported tracks: `transformer`, `mamba2`

Check eligibility:

```bash
evolcli miner check --model username/evolai-0.4b --track transformer
evolcli miner check --model username/evolai-mamba2-0.4b --track mamba2
```

Get your challenge:

```bash
evolcli miner get-challenge <validator-uid>
```

Register your model:

```bash
evolcli miner register --wallet-name miner1 --hotkey my-hotkey --track transformer
evolcli miner register --wallet-name miner1 --hotkey my-hotkey --track mamba2
```

Re-register after you publish a new model version.

---

#### CPU / GPU / RAM lines (automatic grep)

- A GPU 80 GB is required to run validator evaluations.


*Primary README URL used: `https://raw.githubusercontent.com/openevolai/evolai/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/openevolai/evolai.git](https://github.com/openevolai/evolai.git)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.005413622 |
| 8104244 | 0.005413211 |
| 8104292 | 0.005413033 |
| 8104340 | 0.005253923 |
| 8104388 | 0.005254019 |
| 8104436 | 0.005284339 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.003841145 --> 0.007411248
    line [0.006394427, 0.006357688, 0.007165034, 0.006358142, 0.005050114, 0.005993796, 0.005596769, 0.006155368, 0.005781696, 0.005567737, 0.00559987189491, 0.004664243, 0.00508443, 0.005499717, 0.005236733, 0.00523985301705, 0.005011728, 0.004547474, 0.004768256, 0.004899643, 0.004788779, 0.004615324, 0.00445047, 0.004339323, 0.004312433, 0.004775648, 0.004785473, 0.004861369, 0.004890095, 0.004530277, 0.004638877, 0.004087359, 0.004424665, 0.004371538, 0.004194216, 0.004232045, 0.004744104, 0.004471427, 0.004605288, 0.004751828, 0.004720308, 0.004425966, 0.004487512, 0.004361721, 0.004450767, 0.004634645, 0.004885585, 0.004893674, 0.004947584, 0.005076577, 0.005017478, 0.004804881, 0.004950865, 0.004904557, 0.00496418, 0.005413609]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

