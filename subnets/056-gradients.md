# NetUID 56 — Gradients (`ج`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Gradients** (NetUID **56**) (`ج`).

Best AutoML plaftorm in the world



#### SubnetIdentity `additional` *(chain)*



None

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `43`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ58,418.715203001. **Alpha liquidity in pool (`alpha_in`)** = ‎2,667,726.712901977ج‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,287,668.960686176ج‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.021927861`** *(also **moving-average price** `0.02188245113939047` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎2,781,294.845012071ج‎`. **Owner hotkey / coldkey (chain):** `5GU4Xkd3dCGTU3s8VLcHGc5wsD5M8XyxDca5yDQhYm1mVXFu` / `5EJ1zbdwhumTRYFx3VCGnR6SW7CJWP28tEJCo2gw1dFbVL5g`.
- **Subnet registered at block:** `4312927` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎32.442565514ج‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ج‎` · α-in `‎0.000000000ج‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104392`
- **Liquidity constant `k`:** `155845167080458607745369232977`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Gradients` |
| Symbol (API) | `ج` |
| Rank | `9` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.02191718` |
| Market cap | `96390365342539.71639004` |
| Market cap Δ 1d | `0.716526109150182969` |
| Liquidity | `116887758286451` |
| Total τ | `58404454587183` |
| Total α | `4955162673588153` |
| α in pool | `2668377213641034` |
| α staked | `1729559260966544` |
| Price Δ 1h | `0.001104168839643567` |
| Price Δ 1d | `0.605699449448013555` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `56` |
| Owner SS58 (API) | `5EJ1zbdwhumTRYFx3VCGnR6SW7CJWP28tEJCo2gw1dFbVL5g` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4312927` |
| Registration wall time | `2024-11-21T08:47:24Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `15` |
| Active miners | `15` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `15` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<h1 align="center">G.O.D Subnet</h1>

🚀 Welcome to the [Gradients on Demand](https://gradients.io) Subnet

> Distributed intelligence for LLM and diffusion model training. Where the world's best AutoML minds compete.

**Tournaments** 🏆
Competitive events where the validator executes miners' open-source training scripts on dedicated infrastructure.

- **Duration**: 4-7 days per tournament
- **Frequency**: New tournaments start 72 hours after the previous one ends
- **Rewards**: Exponentially higher weight potential for top performers
- **Open Source**: Winning AutoML scripts are released when tournaments complete
- **Winners Repository**: First place tournament scripts is uploaded to [github.com/gradients-opensource](https://github.com/gradients-opensource) 🤙
- [Tournament Overview](docs/tournament_overview.md)

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Anyone Can Train AI on Bittensor. AI Training, Decentralized.

**Fetched document title:** Gradients | Anyone Can Train AI

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
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5EJ1zbdwhumTRYFx3VCGnR6SW7CJWP28tEJCo2gw1dFbVL5g` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
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

## Setup Guides

- [Tournament Miner Guide](docs/tourn_miner.md)
- [Validator Setup Guide](docs/validator_setup.md)

---

## Developer Resources

For technical documentation on GRPO reward functions and implementation details, see [GRPO Safe Code Execution Guide](docs/grpo_rewards_code_execution.md).

---

## Recommended Compute Requirements

[Compute Requirements](docs/compute.md)

---

## Miner Advice

[Miner Advice](docs/tourn_miner.md)

---









#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/gradients-ai/G.O.D/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.gradients.io/](https://www.gradients.io/)
- **GitHub:** [https://github.com/gradients-ai/G.O.D](https://github.com/gradients-ai/G.O.D)
- **Discord (handle / invite hint):** `None`
- **Logo URL:** [https://gradients-public.s3.eu-central-003.backblazeb2.com/gradientslogo.png](https://gradients-public.s3.eu-central-003.backblazeb2.com/gradientslogo.png)
- **Contact:** info@gradients.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.021917135 |
| 8104292 | 0.021916576 |
| 8104340 | 0.021924135 |
| 8104388 | 0.021927875 |
| 8104436 | 0.021927861 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.02041268 --> 0.02717006
    line [0.021967931, 0.021680321, 0.02179413, 0.021796277, 0.022230005, 0.021537272, 0.021450383, 0.021631075, 0.021323661, 0.020986789, 0.0208787059749, 0.020939963, 0.020888045, 0.020904061, 0.021143228, 0.0212719627301, 0.024765329, 0.024688157, 0.022283826, 0.021965159, 0.022196355, 0.022196795, 0.022315405, 0.022560247, 0.026368225, 0.026413823, 0.02670403, 0.026167347, 0.026080314, 0.025995072, 0.026188798, 0.026021889, 0.025723147, 0.025971714, 0.025854653, 0.025585397, 0.025355371, 0.024844481, 0.022273397, 0.021816607, 0.021973821, 0.021959168, 0.021703281, 0.02160501, 0.021940892, 0.022230445, 0.021724842, 0.021640213, 0.021647725, 0.021976475, 0.02181911, 0.021683142, 0.021957798, 0.021841079, 0.021822923, 0.02191718]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

