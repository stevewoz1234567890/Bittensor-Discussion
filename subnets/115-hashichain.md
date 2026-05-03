# NetUID 115 — HashiChain (`Ѕ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**HashiChain** (NetUID **115**) (`Ѕ`).

The First Public Blockchain Designed for AI Agents

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `102`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ5,977.546414040. **Alpha liquidity in pool (`alpha_in`)** = ‎808,898.464248581Ѕ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,297,047.923737971Ѕ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007401719`** *(also **moving-average price** `0.007402934832498431` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎133,823.116739218Ѕ‎`. **Owner hotkey / coldkey (chain):** `5EhTo9AXu6JCK2voyEz2ftwFq9cmYR1ACj8qobD67MGZKgTV` / `5EkNnrTjnMYaj4x1gNxAnJne9UvKgfU6NZNjhm6XFWMstbdG`.
- **Subnet registered at block:** `5683635` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎70.709260486Ѕ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Ѕ‎` · α-in `‎0.000000000Ѕ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104333`
- **Liquidity constant `k`:** `4835228114291568499708477240`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `HashiChain`
- **Symbol (API):** `Ѕ`
- **Rank:** `92`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.007402019`
- **Market cap:** `11363097238338.379648488`
- **Market cap Δ 1d:** `0.244148408488583792`
- **Liquidity:** `11965028212813`
- **Total τ:** `5977668070029`
- **Total α:** `2105713387986552`
- **α in pool:** `808882028374174`
- **α staked:** `726252809612378`
- **Price Δ 1h:** `-0.002188544160160364`
- **Price Δ 1d:** `-0.03271009924989611`
#### Subnet activity (TAOStats)

- **NetUID (API):** `115`
- **Owner SS58 (API):** `5EkNnrTjnMYaj4x1gNxAnJne9UvKgfU6NZNjhm6XFWMstbdG`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `5683635`
- **Registration wall time:** `2025-06-01T06:02:00Z`
- **Registration cost snapshot:** `98002215656`
- **Active keys:** `256`
- **Active validators:** `18`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `18`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

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

*(README prelude often echoes the subnet tagline — miner/validator runbooks typically live further down in-repo.)*


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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/hashi115/hashichain](https://github.com/hashi115/hashichain)
- **Logo URL:** [https://raw.githubusercontent.com/hashi115/hashichain/refs/heads/main/assets/intro.png](https://raw.githubusercontent.com/hashi115/hashichain/refs/heads/main/assets/intro.png)
- **Contact:** hashichain@outlook.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.007401922 |
| 8104292 | 0.007401861 |
| 8104340 | 0.007401756 |
| 8104388 | 0.007401749 |
| 8104436 | 0.007401718 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

