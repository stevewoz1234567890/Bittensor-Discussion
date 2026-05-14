# NetUID 51 — lium.io (`ת`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**lium.io** (NetUID **51**) (`ת`).

revolutionizing the democratization of compute

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `38`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ125,580.966804719. **Alpha liquidity in pool (`alpha_in`)** = ‎1,960,544.137924943ת‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,926,933.523553090ת‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.064051813`** *(also **moving-average price** `0.0636856984347105` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,581,897.748249361ת‎`. **Owner hotkey / coldkey (chain):** `5FTVrwEpjvpNeKwczFtYjs62GHKKLHLCdqCThtj2unZouKg1` / `5FqACMtcegZxxopgu1g7TgyrnyD8skurr9QDPLPhxNQzsThe`.
- **Subnet registered at block:** `3966206` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎28.641174414ת‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.032025870` · α-out `‎1.000000000ת‎` · α-in `‎0.500000000ת‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104397`
- **Liquidity constant `k`:** `246207028303938695561760206017`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `lium.io` |
| Symbol (API) | `ת` |
| Rank | `3` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.06403018` |
| Market cap | `247794939697704.58226628` |
| Market cap Δ 1d | `2.48233855454220855` |
| Liquidity | `251100038054316` |
| Total τ | `125552279938008` |
| Total α | `4887512691930109` |
| α in pool | `1960759100104184` |
| α staked | `1909211899472962` |
| Price Δ 1h | `0.284829729508470552` |
| Price Δ 1d | `2.52318077346229111` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `51` |
| Owner SS58 (API) | `5FqACMtcegZxxopgu1g7TgyrnyD8skurr9QDPLPhxNQzsThe` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3966206` |
| Registration wall time | `2024-10-04T01:55:00Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `9` |
| Active miners | `38` |
| Active dual-role | `0` |
| Emission | `32014949` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `64` |
| Neuron reg. cost | `5000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `12000` |

### Repository README excerpt *(everything before first `##` heading)*

# lium.io

**[Lium Subnet Documentation](https://docs.lium.io/bittensor-subnet/overview)**

<img width="469" height="468" alt="image" src="https://github.com/user-attachments/assets/69550b83-91a9-492a-bd7a-09d35c6106d3" />

Welcome to **Lium.io powered by Bittensor Subnet 51**! This project enables a decentralized, peer-to-peer GPU rental marketplace, connecting miners who contribute GPU resources with users who need computational power. Our frontend interface is available at [lium.io](https://lium.io), where you can easily rent machines from the subnet.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to Datura-ai/lium-io development by creating an account on GitHub.

**Fetched document title:** GitHub - Datura-ai/lium-io · GitHub

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
| Registration recycle cost snapshot (`burn`) | τ0.005000000 |
| Owner SS58 (`owner_ss58`) | `5FqACMtcegZxxopgu1g7TgyrnyD8skurr9QDPLPhxNQzsThe` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.005000000 / τ0.100000001 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `12000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `500000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### For Miners

Miners can contribute their GPU-equipped machines to the network. The machines are scored and validated based on factors like GPU type, number of GPUs, bandwidth, and overall GPU performance. Higher performance results in better compensation for miners.

If you are a miner and want to contribute GPU resources to the subnet, please refer to the [Miner Setup Guide](neurons/miners/README.md) for instructions on how to:

- Set up your environment.
- Install the miner software.
- Register your miner and connect to the network.
- Get compensated for providing GPUs!

---

### For Validators

Validators play a crucial role in maintaining the integrity of the Compute Subnet by verifying the hardware specifications and performance of miners’ machines. Validators ensure that miners are fairly compensated based on their GPU contributions and prevent fraudulent activities.

For more details, visit the [Validator Setup Guide](neurons/validators/README.md).

---









#### CPU / GPU / RAM lines (automatic grep)

- Welcome to **Lium.io powered by Bittensor Subnet 51**! This project enables a decentralized, peer-to-peer GPU rental marketplace, connecting miners who contribute GPU resources with users who need computational power. Our frontend interface is available at [lium.io](https://lium.io), where you can easily rent machines from the subnet.
- The Compute Subnet on Bittensor is a decentralized network that allows miners to contribute their GPU resources to a global pool. Users can rent these resources for computational tasks, such as machine learning, data analysis, and more. The system ensures fair compensation for miners based on the quality and performance of their GPUs.
- - **Miners**: Provide GPU resources to the network, evaluated and scored by validators.
- 2. **Browse** available GPU resources.
- 3. **Select** machines based on GPU type, performance, and price.
- **Command-Line Alternative**: For renters who prefer working from the terminal, you can also use [lium-cli](https://github.com/Datura-ai/lium-cli) - a command-line interface that allows you to manage GPU pods, SSH into machines, transfer files, and execute commands directly from your terminal. Install it with `pip install lium-cli`.
- Miners can contribute their GPU-equipped machines to the network. The machines are scored and validated based on factors like GPU type, number of GPUs, bandwidth, and overall GPU performance. Higher performance results in better compensation for miners.
- If you are a miner and want to contribute GPU resources to the subnet, please refer to the [Miner Setup Guide](neurons/miners/README.md) for instructions on how to:
- Validators play a crucial role in maintaining the integrity of the Compute Subnet by verifying the hardware specifications and performance of miners’ machines. Validators ensure that miners are fairly compensated based on their GPU contributions and prevent fraudulent activities.


*Primary README URL used: `https://raw.githubusercontent.com/Datura-ai/lium-io/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/Datura-ai/lium-io](https://github.com/Datura-ai/lium-io)
- **Discord (handle / invite hint):** `p383_54249`
- **Logo URL:** [https://raw.githubusercontent.com/Datura-ai/lium-logos/refs/heads/main/Celium_Icon_FullColor.png](https://raw.githubusercontent.com/Datura-ai/lium-logos/refs/heads/main/Celium_Icon_FullColor.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.064019567 |
| 8104292 | 0.064024677 |
| 8104340 | 0.06402783 |
| 8104388 | 0.064048907 |
| 8104436 | 0.064051885 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

