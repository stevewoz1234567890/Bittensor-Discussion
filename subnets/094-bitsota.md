# NetUID 94 — Bitsota (`ᚄ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Bitsota** (NetUID **94**) (`ᚄ`).

Decentralized SoTA Research



#### SubnetIdentity `additional` *(chain)*



https://discord.gg/jkJWJtPuw7

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `81`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,934.936400485. **Alpha liquidity in pool (`alpha_in`)** = ‎383,100.950933118ᚄ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎970,235.518295090ᚄ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005052094`** *(also **moving-average price** `0.004901819163933396` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎24,032.017287808ᚄ‎`. **Owner hotkey / coldkey (chain):** `5Ef5EsPQoMVmJ8rYectQ26BEvscvATEGm365bcQjo1Y6bxGr` / `5EZRCK9op9piMhQvHqrEL1SNQU8ENU8s9aqGnRKNsUxmPYP2`.
- **Subnet registered at block:** `6962737` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎52.785325380ᚄ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002526044` · α-out `‎1.000000000ᚄ‎` · α-in `‎0.500000000ᚄ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104354`
- **Liquidity constant `k`:** `741275975020907944897762230`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Bitsota` |
| Symbol (API) | `ᚄ` |
| Rank | `110` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.005051256` |
| Market cap | `4874480190357.248198784` |
| Market cap Δ 1d | `6.69115453049529816` |
| Liquidity | `3868900382399` |
| Total τ | `1934187249804` |
| Total α | `1353042789043181` |
| α in pool | `383016250333740` |
| α staked | `581987342902724` |
| Price Δ 1h | `-0.894785850588067717` |
| Price Δ 1d | `6.016659995924095835` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `94` |
| Owner SS58 (API) | `5EZRCK9op9piMhQvHqrEL1SNQU8ENU8s9aqGnRKNsUxmPYP2` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `6962737` |
| Registration wall time | `2025-11-25T22:05:48Z` |
| Registration cost snapshot | `242177138670` |
| Active keys | `256` |
| Active validators | `11` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `2525619` |
| Max neurons | `256` |
| Validator slots (metadata) | `11` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# BitSota

**Decentralized Research Network on Bittensor**

BitSota is a decentralized research network that evolves machine learning algorithms through competitive optimization. We're a problem agnostic platform and enable the optimization of different categories of problems, with a focus on self-improving and self-generating AI.
Currently, Miners develop ML algorithms using genetic programming, while validators evaluate performance and distribute rewards through smart contract voting on the Bittensor network.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** BitSota main repository. Contribute to AlveusLabs/SN94-BitSota development by creating an account on GitHub.

**Fetched document title:** GitHub - AlveusLabs/SN94-BitSota: BitSota main repository · GitHub

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
| Owner SS58 (`owner_ss58`) | `5EZRCK9op9piMhQvHqrEL1SNQU8ENU8s9aqGnRKNsUxmPYP2` |


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

### Direct Mining

Individual miners evolve algorithms locally and submit breakthroughs to validators. Requires higher compute but offers larger individual rewards.

**Best for:** Experienced miners with dedicated hardware

**[→ Direct Mining Guide](docs/mining.md)**

---

### Pool Mining

Collaborative mining where participants handle smaller evolution and evaluation tasks. Pool aggregates results and submits to validators on behalf of all participants.

**Best for:** New miners or those with limited compute resources

**[→ Pool Mining Guide](docs/pool-mining.md)**

---

### Direct Mining Flow

```
Miner → Evolve Locally → Beat SOTA → Submit to Relay → Validators Verify → Relay Consensus → Weight Update → Emissions
```

1. Miner runs genetic programming engine for up to 150 generations
2. When algorithm beats State-of-the-Art threshold, submits to relay
3. Validators download submission and independently re-evaluate
4. Validators choose weight setting mode:
   - Relay mode: Vote on relay, wait for consensus, then set weights
   - Local mode: Set weights immediately based on own evaluation
5. Validators set on-chain weights: 90% burn, 10% winner
6. Network emissions flow to winner via Yuma consensus

---

### Pool Mining Flow

```
Pool → Assigns Tasks → Miners Execute → Pool Consensus → Submit to Validators → Epoch Rewards
```

1. Pool distributes evolution and evaluation tasks to participants
2. Multiple miners evaluate each algorithm (3+ required)
3. Pool computes median consensus with 10% tolerance
4. Rewards distributed based on reputation at epoch boundaries
5. Pool submits best algorithms to validators on behalf of participants

**[→ Detailed Rewards Guide](docs/rewards.md)**

---

### For Miners

**Desktop GUI (Recommended):**
1. Download from [bitsota.ai](https://bitsota.ai)
2. Install for your platform
3. Import your Bittensor hotkey
4. Choose mining mode (Direct or Pool)
5. Start mining

See detailed setup guides:
- [Direct Mining Setup](docs/mining.md#setup)
- [Pool Mining Setup](docs/pool-mining.md#setup)

---

### For Validators

```bash
git clone https://github.com/AlveusLabs/BitSota.git
cd BitSota
pip install -r requirements.txt
pip install -e .

cp validator_config.yaml.example validator_config.yaml

---

# Edit validator_config.yaml with your wallet and burn_hotkey

python neurons/validator_node.py
```

**[→ Full Validator Setup](docs/validation.md#setup)**

---

## Requirements

**Minimum:**
- Python 3.10+
- 4GB RAM
- 2GB storage
- Stable internet connection

**For Validation:**
- 16GB RAM
- 8+ CPU cores

---









#### CPU / GPU / RAM lines (automatic grep)

- - 2GB storage
- - 16GB RAM
- - 8+ CPU cores


*Primary README URL used: `https://raw.githubusercontent.com/AlveusLabs/SN94-BitSota/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/AlveusLabs/SN94-BitSota](https://github.com/AlveusLabs/SN94-BitSota)
- **Discord (handle / invite hint):** `dev.alveuslabs`
- **Logo URL:** [https://bitsota.ai/logo.png](https://bitsota.ai/logo.png)
- **Contact:** info@bitsota.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.005051319 |
| 8104292 | 0.005051491 |
| 8104340 | 0.005051573 |
| 8104388 | 0.005051863 |
| 8104436 | 0.0050521 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.003299402 --> 0.006194315
    line [0.00517454, 0.00566154, 0.005994666, 0.005901503, 0.005299371, 0.005459002, 0.005517145, 0.005575684, 0.005264658, 0.00560901, 0.00562818508447, 0.005587722, 0.00557646, 0.005910722, 0.00582123, 0.00551324287826, 0.004782011, 0.004555003, 0.004716633, 0.004837941, 0.004474121, 0.004102921, 0.003950631, 0.003949316, 0.003923558, 0.004096633, 0.004226617, 0.004346317, 0.004232048, 0.004244558, 0.004229573, 0.003544461, 0.003879977, 0.003890286, 0.003815359, 0.003847064, 0.003789897, 0.003680854, 0.003707255, 0.003734088, 0.00366182, 0.003499051, 0.003611132, 0.00359776, 0.003626941, 0.003632555, 0.003620207, 0.003653944, 0.003836345, 0.004210434, 0.004411787, 0.004503037, 0.004567943, 0.004550181, 0.004898348, 0.005051256]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

