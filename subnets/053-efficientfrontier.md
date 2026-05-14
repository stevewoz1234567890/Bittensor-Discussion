# NetUID 53 — EfficientFrontier (`ب`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**EfficientFrontier** (NetUID **53**) (`ب`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `40`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ14,864.537071162. **Alpha liquidity in pool (`alpha_in`)** = ‎2,477,471.026685844ب‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,464,773.454850655ب‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005998387`** *(also **moving-average price** `0.005983374547213316` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎464,131.370274549ب‎`. **Owner hotkey / coldkey (chain):** `5F2HTUqtk9VWQwXkkUX9oFSXUkAib74qw7s3W7KyZP88AmYe` / `5Fv2Qm2w9tnotv9xpGq9EVKaSjRtFzGdas5RBsUswpdsE5Sh`.
- **Subnet registered at block:** `4203869` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎30.173275092ب‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002999192` · α-out `‎1.000000000ب‎` · α-in `‎0.500000000ب‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104395`
- **Liquidity constant `k`:** `36826459918901508715246030728`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `EfficientFrontier` |
| Symbol (API) | `ب` |
| Rank | `37` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.006006154` |
| Market cap | `28090328604980.087654362` |
| Market cap Δ 1d | `-1.499305959202648069` |
| Liquidity | `29743204779681` |
| Total τ | `14873447629407` |
| Total α | `4942010378633353` |
| α in pool | `2475753560477179` |
| α staked | `2201170908156174` |
| Price Δ 1h | `0.166172186004779702` |
| Price Δ 1d | `-1.577392418376140717` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `53` |
| Owner SS58 (API) | `5Fv2Qm2w9tnotv9xpGq9EVKaSjRtFzGdas5RBsUswpdsE5Sh` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4203869` |
| Registration wall time | `2024-11-06T03:34:48Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `13` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `3003072` |
| Max neurons | `256` |
| Validator slots (metadata) | `13` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **EfficientFrontier-SignalPlus**

</div>

**Quick Overview of [Strategy Ranking Rules](docs/Introduction/RankingRulesEN.md)**

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to EfficientFrontier-SignalPlus/EfficientFrontier development by creating an account on GitHub.

**Fetched document title:** GitHub - EfficientFrontier-SignalPlus/EfficientFrontier · GitHub

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
| `immunity_period` (blocks) | 1 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5Fv2Qm2w9tnotv9xpGq9EVKaSjRtFzGdas5RBsUswpdsE5Sh` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `1` blocks |
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

### 2. Professional Trading Infrastructure

SignalPlus is a professionally recognized and trusted partner with most of crypto's largest exchanges, offering a comprehensive suite of trading tools and risk management features available to every user. Traders can utilize the SignalPlus platform to execute complex and algorithmic trades in a systematic way, freeing up their focus to refine trading frameworks and higher cognitive functions that ultimately generate true alpha.

Some of SignalPlus's advanced trading functions include:
- **Stop Loss/Take Profit**
- **Iceberg Orders**
- **Balance Trade**
- **TWAP (Time-Weighted Average Price)**
- **DDH (Dynamic Delta Hedging)**

In a nutshell, the **SignalPlus platform dramatically lowers the barriers to entry**, and directly expands the group of participating subnet miners into the Bittensor network.  **SignalPlus is the critical link** that ensures the authenticity of trading data and provides traders with the tools they need to succeed.

Without such a platform, it would be impossible to securely validate trades or to provide the professional trading infrastructure to promote a high quality data environment. By removing unwanted technical complexities, SignalPlus allows traders to focus on what really matters — their strategy — while ensuring a robust environment with the requisite fairness and transparency that will best accentuate the power of the Bittensor network as we unlock a new chapter in network-learning models.

---

### Miners Installation

- The miner will call the official public API to retrieve account-related metadata such as balance, equity, PnL, and drawdown, which are generated from the user's trading activities on the platform [t.signalplus.com](https://t.signalplus.com).
- This data is then passed to the validator for evaluating the strategy's performance.
- During transmission, asymmetric encryption is used to ensure the data remains untampered with, guaranteeing fairness and integrity.
- You can find detailed instructions on how to become a miner via the following link: <p> [how-to-join-the-greatest-tournament-of-crypto](docs/Introduction/HowToJoin.md)
- [running_miner_on_mainnet](docs/running_on_mainnet.md)

---

### Validator Installation

- The validator locally synchronizes the latest blockchain and retrieves all metadata uploaded by the corresponding miners.
- Initially, it verifies the authenticity of the data using asymmetric encryption.
- Once validated, the validator applies a Ranking Model to calculate the miner's weight and updates the results on the blockchain. This will determine the amount of rewards the miner can receive in the next cycle.
- During this process, risk control checks are conducted, and if any fraudulent activity is detected, penalties may be imposed, including disqualification from the competition.
- [running_validator_on_testnet](docs/running_on_testnet.md)
- [running_validator_on_mainnet](docs/running_on_mainnet.md)

---

### Registration Fee for Miners

Each miner wishing to participate in the Efficient Frontier subnet is required to pay a registration fee of **1 TAO** to Bittensor. This amount may be adjusted in the future based on the subnet's weight. Recognizing that our target miners are primarily quantitative trading teams and individuals engaged in complex derivatives trading—who may not be familiar with Bittensor or DeFi and might not have their own crypto wallets—we aim to simplify the onboarding process.

To lower the entry barrier, **SignalPlus** will directly charge miners in **USDT** and exchange it for TAO on their behalf, handling the cross-chain payment to Bittensor. Considering the current value of TAO is approximately **\$450 USD**, plus additional cross-chain and network gas fees, we plan to initially charge a registration fee of **\$500 USD**. This fee will be periodically adjusted to reflect any significant changes in TAO's market price.

If there is any surplus from the registration fee after paying the required 1 TAO to Bittensor, we will allocate the excess USDT as follows:

1. **Price Fluctuation Buffer**: To hedge against potential losses if TAO's price increases sharply before we can adjust the USDT registration fee.
2. **Community Rewards**: Periodically distribute the surplus directly to participating miners as rewards.

By handling the TAO acquisition and payment process, we aim to make it as easy as possible for miners to join the subnet, allowing them to focus on what they do best—trading.

---

### What are the expected operations for a miner?

- You need to operate with a certain cap…

---





#### CPU / GPU / RAM lines (automatic grep)

- `|  Ranking_Index <p> (Strategy Score)|  $${\frac {\text{Weighted Daily \\% Returns}}{\text{Maximum Decayed Drawdown}} \cdot 10} \cdot \text{Risk Factor}$$|**Weighted Daily Returns / Maximum Drawdown Applied Against a Decay Factor (with a Scoring Cap)**<p>Conceptually similar to a Calmar ratio, with some adjustments down to daily return weights in order to favour more recent performance.|`


*Primary README URL used: `https://raw.githubusercontent.com/EfficientFrontier-SignalPlus/EfficientFrontier/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/EfficientFrontier-SignalPlus/EfficientFrontier](https://github.com/EfficientFrontier-SignalPlus/EfficientFrontier)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.005998164 |
| 8104292 | 0.005998271 |
| 8104340 | 0.005998371 |
| 8104388 | 0.005998485 |
| 8104436 | 0.00599839 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

