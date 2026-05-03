# NetUID 51 — lium.io (`ת`)

## Overview

**lium.io** (NetUID **51**) (`ת`).

revolutionizing the democratization of compute

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `241`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ125,547.747001302. **Alpha liquidity in pool (`alpha_in`)** = ‎1,960,904.896755307ת‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,926,637.532345324ת‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.064023114`** *(also **moving-average price** `0.06366990529932082` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,581,867.859435499ת‎`. **Owner hotkey / coldkey (chain):** `5FTVrwEpjvpNeKwczFtYjs62GHKKLHLCdqCThtj2unZouKg1` / `5FqACMtcegZxxopgu1g7TgyrnyD8skurr9QDPLPhxNQzsThe`.
- **Subnet registered at block:** `3966206` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎181.644817283ת‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.032011529` · α-out `‎1.000000000ת‎` · α-in `‎0.500000000ת‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.06403018`
- **Market cap:** `247794939697704.58226628`
- **Liquidity:** `251100038054316`
- **Total τ:** `125552279938008`
- **Total α:** `4887512691930109`
- **α in pool:** `1960759100104184`
- **α staked:** `1909211899472962`
- **Price Δ 1h:** `0.284829729508470552`
- **Price Δ 1d:** `2.52318077346229111`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `38`
- **Active dual:** `0`
- **Emission:** `32014949`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `5000000`

### On-chain declared purpose *(SubnetIdentity)*

revolutionizing the democratization of compute

### Repository README excerpt *(everything before first `##` heading)*

# lium.io

**[Lium Subnet Documentation](https://docs.lium.io/bittensor-subnet/overview)**

<img width="469" height="468" alt="image" src="https://github.com/user-attachments/assets/69550b83-91a9-492a-bd7a-09d35c6106d3" />

Welcome to **Lium.io powered by Bittensor Subnet 51**! This project enables a decentralized, peer-to-peer GPU rental marketplace, connecting miners who contribute GPU resources with users who need computational power. Our frontend interface is available at [lium.io](https://lium.io), where you can easily rent machines from the subnet.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to Datura-ai/lium-io development by creating an account on GitHub.

**Fetched document title:** GitHub - Datura-ai/lium-io · GitHub

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.005000000
- **Owner SS58 (`owner_ss58`):** `5FqACMtcegZxxopgu1g7TgyrnyD8skurr9QDPLPhxNQzsThe`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.005000000 / τ0.100000001
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `12000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `500000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

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

## On-chain identity — description


revolutionizing the democratization of compute

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/Datura-ai/lium-io](https://github.com/Datura-ai/lium-io)
- **Discord (handle / invite hint):** `p383_54249`
- **Logo URL:** [https://raw.githubusercontent.com/Datura-ai/lium-logos/refs/heads/main/Celium_Icon_FullColor.png](https://raw.githubusercontent.com/Datura-ai/lium-logos/refs/heads/main/Celium_Icon_FullColor.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.064010359 |
| 8104133 | 0.064013316 |
| 8104181 | 0.064027671 |
| 8104229 | 0.064031985 |
| 8104277 | 0.064023114 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.041228878 |
| 2026-03-10T23:59:48Z | 7718257 | 0.041172595 |
| 2026-03-11T23:59:48Z | 7725455 | 0.040949206 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.040825763 |
| 2026-03-13T23:59:48Z | 7739841 | 0.040755555 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.040737211 |
| 2026-03-15T23:59:48Z | 7754226 | 0.04066029 |
| 2026-03-16T23:59:48Z | 7761426 | 0.040511211 |
| 2026-03-17T23:59:48Z | 7768619 | 0.040532986 |
| 2026-03-18T23:59:48Z | 7775819 | 0.040557154 |
| 2026-03-19T23:59:48Z | 7783014 | 0.04037553507857072219 |
| 2026-03-20T23:59:48Z | 7790201 | 0.040557844 |
| 2026-03-21T23:59:48Z | 7797398 | 0.04060882 |
| 2026-03-22T23:59:48Z | 7804598 | 0.041116561 |
| 2026-03-23T23:59:48Z | 7811798 | 0.040853495 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.04095063939710854866 |
| 2026-03-25T23:59:48Z | 7826196 | 0.040879473 |
| 2026-03-26T23:59:48Z | 7833396 | 0.041623121 |
| 2026-03-27T23:59:48Z | 7840596 | 0.041459497 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.041356452 |
| 2026-03-29T23:59:48Z | 7854902 | 0.041393568 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.041135499 |
| 2026-03-31T23:59:48Z | 7869291 | 0.04081986 |
| 2026-04-01T23:59:48Z | 7876474 | 0.040878433 |
| 2026-04-02T23:59:48Z | 7883622 | 0.040874687 |
| 2026-04-03T23:59:48Z | 7890794 | 0.040729665 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.040954817 |
| 2026-04-05T23:59:48Z | 7905188 | 0.048161949 |
| 2026-04-06T23:59:48Z | 7912388 | 0.047277773 |
| 2026-04-07T23:59:48Z | 7919588 | 0.046487893 |
| 2026-04-08T23:59:48Z | 7926788 | 0.046726326 |
| 2026-04-09T23:59:48Z | 7933987 | 0.047248717 |
| 2026-04-10T23:59:48Z | 7941184 | 0.047782313 |
| 2026-04-11T23:59:48Z | 7948384 | 0.049099304 |
| 2026-04-12T23:59:48Z | 7955584 | 0.04998057 |
| 2026-04-13T23:59:48Z | 7962784 | 0.049516663 |
| 2026-04-14T23:59:48Z | 7969979 | 0.04990304 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.050354292 |
| 2026-04-16T23:59:48Z | 7984379 | 0.050143003 |
| 2026-04-17T23:59:48Z | 7991579 | 0.051765532 |
| 2026-04-18T23:59:48Z | 7998779 | 0.052930748 |
| 2026-04-19T23:59:48Z | 8005979 | 0.053065169 |
| 2026-04-20T23:59:48Z | 8013179 | 0.053270942 |
| 2026-04-21T23:59:48Z | 8020376 | 0.054361159 |
| 2026-04-22T23:59:48Z | 8027562 | 0.054552222 |
| 2026-04-23T23:59:48Z | 8034762 | 0.05492458 |
| 2026-04-24T23:59:48Z | 8041962 | 0.05599553 |
| 2026-04-25T23:59:48Z | 8049151 | 0.057588306 |
| 2026-04-26T23:59:48Z | 8056274 | 0.057920416 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.058133133 |
| 2026-04-28T23:59:48Z | 8070646 | 0.058492038 |
| 2026-04-29T23:59:48Z | 8077790 | 0.060390149 |
| 2026-04-30T23:59:48Z | 8084984 | 0.061111903 |
| 2026-05-01T23:59:48Z | 8092168 | 0.062299329 |
| 2026-05-02T23:59:48Z | 8099357 | 0.063776521 |
| 2026-05-03T16:10:00Z | 8104202 | 0.06403018 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

