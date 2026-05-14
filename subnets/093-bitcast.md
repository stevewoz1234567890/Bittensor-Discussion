# NetUID 93 — Bitcast (`ᚃ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Bitcast** (NetUID **93**) (`ᚃ`).

The Decentralized Creators Economy

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `80`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ20,144.468865562. **Alpha liquidity in pool (`alpha_in`)** = ‎1,325,661.463521005ᚃ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,720,494.579192174ᚃ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.015195847`** *(also **moving-average price** `0.014830001397058368` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎810,538.458198690ᚃ‎`. **Owner hotkey / coldkey (chain):** `5DAoDtMxVqtMu2Nd5E7QhPEGXDMgrySvE1b3rRT5ARDhfNNK` / `5FLfN276taTF6Ud62soChQhPNbtF2EPK4dr3pJB9oTsTpUvr`.
- **Subnet registered at block:** `5370681` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎59.402730611ᚃ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ᚃ‎` · α-in `‎0.000000000ᚃ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104355`
- **Liquidity constant `k`:** `26704746078174240238508129810`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Bitcast` |
| Symbol (API) | `ᚃ` |
| Rank | `22` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.015196797` |
| Market cap | `49084607871830.900218311` |
| Market cap Δ 1d | `6.728626147190394987` |
| Liquidity | `40290276997444` |
| Total τ | `20145102500971` |
| Total α | `4045923042713179` |
| α in pool | `1325619766880728` |
| α staked | `1904311373992635` |
| Price Δ 1h | `0.680718606385867702` |
| Price Δ 1d | `6.58027122821639738` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `93` |
| Owner SS58 (API) | `5FLfN276taTF6Ud62soChQhPNbtF2EPK4dr3pJB9oTsTpUvr` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5370681` |
| Registration wall time | `2025-04-17T10:49:48Z` |
| Registration cost snapshot | `290836604849` |
| Active keys | `256` |
| Active validators | `9` |
| Active miners | `7` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `64` |
| Neuron reg. cost | `5000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <a href="https://www.bitcast.network/">
    <img src="assets/lockup_gradient.svg" alt="Bitcast Logo" width="800" />
  </a>
</p>

# Bitcast — The Decentralized Creator Economy

Bitcast is a decentralized platform that incentivizes content creators to connect brands with audiences. Creators publish YouTube videos to satisfy defined briefs and earn rewards based on engagement metrics.

---

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** bitcast

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
| `immunity_period` (blocks) | 50400 |
| Registration recycle cost snapshot (`burn`) | τ0.005000000 |
| Owner SS58 (`owner_ss58`) | `5FLfN276taTF6Ud62soChQhPNbtF2EPK4dr3pJB9oTsTpUvr` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.005000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `50400` blocks |
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

### For Miners

1. **Review Requirements**  
   Ensure your YouTube account and videos meet the [minimum requirements](bitcast/miner/README.md).

2. **Publish Content**  
   Create videos targeting one or more active briefs.

3. **Earn Rewards**  
   Videos that satisfy briefs are rewarded based on **YouTube Premium revenue** stats.

4. **Agency Operations**  
   Run a single miner with up to 5 YouTube accounts to operate as a content agency, aggregating multiple creators under one mining operation.

See the [Miner Setup Guide](bitcast/miner/README.md) for:
- Installation and configuration  
- OAuth and account integration  
- Miner registration on the network  
- Reward tracking and monitoring

---

### For Validators

Validators maintain the integrity of the network by:
- Retrieving analytics data via OAuth  
- Verifying content engagement  
- Disbursing on-chain rewards to Miners

Refer to the [Validator Setup Guide](bitcast/validator/README.md) for detailed instructions.

---

---

## 📊 Scoring & Rewards System

Bitcast employs a dynamic, multi-layered scoring and rewards mechanism to fairly distribute emissions and incentivize high-quality participation. The system is designed to prioritize genuine engagement and prevent manipulation.

---









#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/bitcast-network/bitcast/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.bitcast.network/](https://www.bitcast.network/)
- **GitHub:** [https://github.com/bitcast-network/bitcast](https://github.com/bitcast-network/bitcast)
- **Logo URL:** [https://bitcast-logo.s3.us-west-2.amazonaws.com/Bitcast+logo+multi+white.webp](https://bitcast-logo.s3.us-west-2.amazonaws.com/Bitcast+logo+multi+white.webp)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.015196724 |
| 8104292 | 0.015196677 |
| 8104340 | 0.015196596 |
| 8104388 | 0.015196591 |
| 8104436 | 0.015195847 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.01376619 --> 0.02002008
    line [0.014681327, 0.015452756, 0.015542639, 0.015039283, 0.01537258, 0.017112115, 0.017628603, 0.017727804, 0.017487896, 0.017305098, 0.0166683873757, 0.016273718, 0.016851925, 0.01630232, 0.017154247, 0.0167551901483, 0.016541456, 0.015357557, 0.01500895, 0.014960884, 0.015654304, 0.015239573, 0.015759797, 0.01658201, 0.017431599, 0.017071177, 0.017836104, 0.018532904, 0.018826392, 0.019588773, 0.017897013, 0.019309276, 0.018716664, 0.01857412, 0.018798972, 0.019517525, 0.018271891, 0.018159473, 0.017296797, 0.016741414, 0.015352218, 0.015563486, 0.015522951, 0.015257377, 0.0146232, 0.015102341, 0.014587818, 0.015449286, 0.015308365, 0.014951104, 0.015256595, 0.01541044, 0.014999507, 0.014197495, 0.014860874, 0.015196797]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

