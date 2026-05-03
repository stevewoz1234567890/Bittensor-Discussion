# NetUID 115 — HashiChain (`Ѕ`)

## Overview

**HashiChain** (NetUID **115**) (`Ѕ`).

The First Public Blockchain Designed for AI Agents

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `305`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ5,977.608488747. **Alpha liquidity in pool (`alpha_in`)** = ‎808,890.077792128Ѕ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,296,898.310194424Ѕ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007401872`** *(also **moving-average price** `0.007403045194223523` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎133,823.054664511Ѕ‎`. **Owner hotkey / coldkey (chain):** `5EhTo9AXu6JCK2voyEz2ftwFq9cmYR1ACj8qobD67MGZKgTV` / `5EkNnrTjnMYaj4x1gNxAnJne9UvKgfU6NZNjhm6XFWMstbdG`.
- **Subnet registered at block:** `5683635` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎211.430805459Ѕ‎`; pending root emission `τ0.000000000`.
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
| 8104085 | 0.007402095 |
| 8104133 | 0.007402055 |
| 8104181 | 0.007402032 |
| 8104229 | 0.007401942 |
| 8104277 | 0.007401872 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.010826885 |
| 2026-03-10T23:59:48Z | 7718257 | 0.010749207 |
| 2026-03-11T23:59:48Z | 7725455 | 0.009080993 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.010200898 |
| 2026-03-13T23:59:48Z | 7739841 | 0.009786466 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.009880215 |
| 2026-03-15T23:59:48Z | 7754226 | 0.009570077 |
| 2026-03-16T23:59:48Z | 7761426 | 0.009506064 |
| 2026-03-17T23:59:48Z | 7768619 | 0.009381583 |
| 2026-03-18T23:59:48Z | 7775819 | 0.008880085 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00860197499821536998 |
| 2026-03-20T23:59:48Z | 7790201 | 0.008062989 |
| 2026-03-21T23:59:48Z | 7797398 | 0.008083953 |
| 2026-03-22T23:59:48Z | 7804598 | 0.008127463 |
| 2026-03-23T23:59:48Z | 7811798 | 0.007982155 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00797253575670896268 |
| 2026-03-25T23:59:48Z | 7826196 | 0.007937454 |
| 2026-03-26T23:59:48Z | 7833396 | 0.00792772 |
| 2026-03-27T23:59:48Z | 7840596 | 0.008019828 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.008080302 |
| 2026-03-29T23:59:48Z | 7854902 | 0.008151565 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.008193621 |
| 2026-03-31T23:59:48Z | 7869291 | 0.008256983 |
| 2026-04-01T23:59:48Z | 7876474 | 0.00825396 |
| 2026-04-02T23:59:48Z | 7883622 | 0.008311726 |
| 2026-04-03T23:59:48Z | 7890794 | 0.008304172 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.008344929 |
| 2026-04-05T23:59:48Z | 7905188 | 0.008314664 |
| 2026-04-06T23:59:48Z | 7912388 | 0.00827565 |
| 2026-04-07T23:59:48Z | 7919588 | 0.008178398 |
| 2026-04-08T23:59:48Z | 7926788 | 0.00824579 |
| 2026-04-09T23:59:48Z | 7933987 | 0.008180071 |
| 2026-04-10T23:59:48Z | 7941184 | 0.008231906 |
| 2026-04-11T23:59:48Z | 7948384 | 0.008227818 |
| 2026-04-12T23:59:48Z | 7955584 | 0.008203674 |
| 2026-04-13T23:59:48Z | 7962784 | 0.008204148 |
| 2026-04-14T23:59:48Z | 7969979 | 0.008097057 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.008033212 |
| 2026-04-16T23:59:48Z | 7984379 | 0.008001914 |
| 2026-04-17T23:59:48Z | 7991579 | 0.007992915 |
| 2026-04-18T23:59:48Z | 7998779 | 0.008000886 |
| 2026-04-19T23:59:48Z | 8005979 | 0.0078591 |
| 2026-04-20T23:59:48Z | 8013179 | 0.0078467 |
| 2026-04-21T23:59:48Z | 8020376 | 0.007818442 |
| 2026-04-22T23:59:48Z | 8027562 | 0.007854473 |
| 2026-04-23T23:59:48Z | 8034762 | 0.007906753 |
| 2026-04-24T23:59:48Z | 8041962 | 0.007902783 |
| 2026-04-25T23:59:48Z | 8049151 | 0.007867799 |
| 2026-04-26T23:59:48Z | 8056274 | 0.007710085 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.007707311 |
| 2026-04-28T23:59:48Z | 8070646 | 0.007346712 |
| 2026-04-29T23:59:48Z | 8077790 | 0.007416214 |
| 2026-04-30T23:59:48Z | 8084984 | 0.007404476 |
| 2026-05-01T23:59:48Z | 8092168 | 0.007389954 |
| 2026-05-02T23:59:48Z | 8099357 | 0.007396857 |
| 2026-05-03T16:10:00Z | 8104202 | 0.007402019 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

