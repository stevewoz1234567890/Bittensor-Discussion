# NetUID 115 — HashiChain (`Ѕ`)

## Overview

**HashiChain** (NetUID **115**) (`Ѕ`).

The First Public Blockchain Designed for AI Agents

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `243`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ5,977.667317868. **Alpha liquidity in pool (`alpha_in`)** = ‎808,882.129991527Ѕ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,296,844.257995025Ѕ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007402016`** *(also **moving-average price** `0.007403086172416806` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎133,822.995835390Ѕ‎`. **Owner hotkey / coldkey (chain):** `5EhTo9AXu6JCK2voyEz2ftwFq9cmYR1ACj8qobD67MGZKgTV` / `5EkNnrTjnMYaj4x1gNxAnJne9UvKgfU6NZNjhm6XFWMstbdG`.
- **Subnet registered at block:** `5683635` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎168.451275655Ѕ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Ѕ‎` · α-in `‎0.000000000Ѕ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.007402019`
- **Market cap:** `11363097238338.379648488`
- **Liquidity:** `11965028212813`
- **Total τ:** `5977668070029`
- **Total α:** `2105713387986552`
- **α in pool:** `808882028374174`
- **α staked:** `726252809612378`
- **Price Δ 1h:** `-0.002188544160160364`
- **Price Δ 1d:** `-0.03271009924989611`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `18`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `18`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

The First Public Blockchain Designed for AI Agents

### Repository README excerpt *(everything before first `##` heading)*

**HashiChain**: The First Public Blockchain Designed for AI Agents

Abstract

**HashiChain** is a sovereign Layer 1 infrastructure designed to serve as the backbone of the Agent Economy. As the digital locus migrates from human interaction to Autonomous Agents, the rigid, deterministic architecture of traditional blockchains—built solely for binary financial transfers—has become obsolete for the fuzzy, high-dimensional needs of AI. HashiChain introduces a new cryptographic primitive: the Probabilistic State Machine, transforming the blockchain from a ledger of assets into a ledger of intents.

The Architecture: From Hash to Connection

Existing smart contracts cannot natively process unstructured intents, such as complex agent transaction matching, as these requests require semantic understanding beyond simple arithmetic verification. HashiChain bridges this gap by leveraging the Bittensor network as its consensus engine and computational substrate.
Yuma Consensus Integration: We utilize Yuma Consensus not just for reward distribution, but to achieve network-wide agreement on the validity of probabilistic agent interactions.

Miners as Solver Nodes: Miners operate as sovereign Solver Nodes within the HashiChain network. By running distributed AI models inside Trusted Execution Environments (TEEs), these nodes simulate potential interactions in secure sandboxes.
Proof of Entanglement (PoE): We replace the deterministic verification of code with the probabilistic verification of semantic compatibility. Nodes calculate the probability of a successful "match" between private agent intents, finalizing the state transition on the Intent Ledger.

The Philosophy

The protocol is architected around the concept of "Hashi" (Bridge & Chopsticks).
As a Bridge: It connects isolated agent silos across the dark forest of the internet via privacy-preserving tunnels.
As Chopsticks: It enforces the economic law of coordination—just as a single chopstick cannot seize food, a solitary agent cannot capture value. HashiChain provides the immutable infrastructure for agents to pair, coordinate, and settle value, establishing the fundamental economic fabric of the future Agent Civilization.


![logo](./assets/intro.png)

*(Often repeats the headline blurb — check deeper headings for runbooks.)*


### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** The digital landscape is currently undergoing a fundamental shift, where the locus of interaction is migrating from humans to Autonomous Agents. Unlike traditional Agents acting merely as passive t...

## Operational parameters — registration, limits, economics (chain)


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
- **`immunity_period` (blocks):** 21845
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5EkNnrTjnMYaj4x1gNxAnJne9UvKgfU6NZNjhm6XFWMstbdG`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `21845` blocks
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
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/hashi115/hashichain/main/README.md`*

## On-chain identity — description


The First Public Blockchain Designed for AI Agents

## On-chain identity — additional field


The First Public Blockchain Designed for AI Agents

## Registered contact & links


- **GitHub:** [https://github.com/hashi115/hashichain](https://github.com/hashi115/hashichain)
- **Logo URL:** [https://raw.githubusercontent.com/hashi115/hashichain/refs/heads/main/assets/intro.png](https://raw.githubusercontent.com/hashi115/hashichain/refs/heads/main/assets/intro.png)
- **Contact:** hashichain@outlook.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.007402128 |
| 8104072 | 0.007402099 |
| 8104120 | 0.007402064 |
| 8104168 | 0.007402035 |
| 8104216 | 0.007402016 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

