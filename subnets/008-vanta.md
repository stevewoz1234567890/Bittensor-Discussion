# NetUID 8 — Vanta (`θ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Vanta** (NetUID **8**) (`θ`).

The first decentralized & trustless liquidity and execution engine for prop firms and traders



#### SubnetIdentity `additional` *(chain)*



Vanta Network is the first decentralized, trustless liquidity and execution engine for prop firms and traders. It live-trades top-performing miners who deposit alpha for funding, rewards them based on verifiable performance, and uses profits to buy back alpha, creating a transparent, risk-adjusted, and incentive-aligned trading ecosystem.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `356`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ87,403.824881311. **Alpha liquidity in pool (`alpha_in`)** = ‎2,472,921.452214913θ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,525,861.620235384θ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.035346098`** *(also **moving-average price** `0.03516483888961375` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,299,814.679774004θ‎`. **Owner hotkey / coldkey (chain):** `5F6tnxzAAxbhaWRmeUmB63JEM3VXBNSmqb3AwYJVDStQjw8y` / `5F6tnxzAAxbhaWRmeUmB63JEM3VXBNSmqb3AwYJVDStQjw8y`.
- **Subnet registered at block:** `1477264` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎268.763174216θ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000θ‎` · α-in `‎0.000000000θ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104079`
- **Liquidity constant `k`:** `216142793554629544000289190943`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Vanta`
- **Symbol (API):** `θ`
- **Rank:** `6`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.03534313`
- **Market cap:** `158070530820905.68075191`
- **Market cap Δ 1d:** `0.793277816029892197`
- **Liquidity:** `174804609092404`
- **Total τ:** `87400154240097`
- **Total α:** `4998550072450297`
- **α in pool:** `2473025305124579`
- **α staked:** `1999428912170428`
- **Price Δ 1h:** `0.001689182832481192`
- **Price Δ 1d:** `0.690357307719032915`
#### Subnet activity (TAOStats)

- **NetUID (API):** `8`
- **Owner SS58 (API):** `5F6tnxzAAxbhaWRmeUmB63JEM3VXBNSmqb3AwYJVDStQjw8y`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `1477264`
- **Registration wall time:** `2023-10-12T21:19:48Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `17`
- **Active miners:** `42`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `17`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

> Proprietary Trading Network is now Vanta Network!

<p align="center">
  <a href="https://taoshi.io">
    <img width="385" alt="taoshi - ptn repo logo" src="https://www.taoshi.io/white-black.png">
  </a>
</p>

<div align='center'>

[![Discord Chat](https://img.shields.io/discord/1163496128499683389.svg)](https://discord.gg/2XSw62p9Fj)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

</div>

<p align="center">
  <a href="https://taoshi.io">Website</a>
  ·
  <a href="#installation">Installation</a>
  ·
  <a href="https://dashboard.taoshi.io/">Dashboard</a>
  ·
  <a href="https://twitter.com/taoshiio">Twitter</a>
    ·
  <a href="https://twitter.com/taoshiio">Bittensor</a>
</p>

---

<details>
  <summary>Table of contents</summary>
  <ol>
    <li><a href="#vanta-network">Vanta Network</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#how-does-it-work">How does it work?</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#building-a-model">Building A Model</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#faq">FAQ</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>

  </ol>
</details>

---

<details id='bittensor'>
  <summary>What is Bittensor?</summary>

Bittensor is a mining network, similar to Bitcoin, that includes built-in incentives designed to encourage computers to provide access to machine learning models in an efficient and censorship-resistant manner. Bittensor is comprised of Subnets, Miners, and Validators.

> Explain Like I'm Five

Bittensor is an API that connects machine learning models and incentivizes correctness through the power of the blockchain.

### Subnets

Subnets are decentralized networks of machines that collaborate to train and serve machine learning models.

### Miners

Miners run machine learning models. They send signals to the Validators.

### Validators

Validators recieve trade signals from Miners. Validators ensure trades are valid, store them, and track portfolio returns.

</details>

<br />
<br />

# Vanta Network

This repository contains the code for the Vanta Network developed by Taoshi.

Vanta receives signals from quant and deep learning machine learning trading systems to deliver the world's
most complete trading signals across a variety of asset classes.

# Features

🛠️&nbsp;Open Source Strategy Building Techniques (In Our Taoshi Community)<br>
🫰&nbsp;Signals From a <a href="https://github.com/taoshidev/vanta-network/blob/main/vali_objects/vali_config.py#L19"> Variety of Asset Classes</a> - Forex, Crypto, and Equities<br>
📈&nbsp;<a href="https://taomarketcap.com/subnet/8?subpage=miners&metagraph_type=miners">Millions of $ Payouts</a> to Top Traders<br>
💪&nbsp;Innovative Trader Performance Metrics that Identify the Best Traders<br>
🔎&nbsp;<a href="https://dashboard.taoshi.io/">Trading + Metrics Visualization Dashboard</a>

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
- **`immunity_period` (blocks):** 1200
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5F6tnxzAAxbhaWRmeUmB63JEM3VXBNSmqb3AwYJVDStQjw8y`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `1200` blocks
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
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Miners

Miners run machine learning models. They send signals to the Validators.

---

### Validators

Validators recieve trade signals from Miners. Validators ensure trades are valid, store them, and track portfolio returns. 

</details>

<br />
<br />

---

### Validator Installation

Please see our [Validator Installation](https://github.com/taoshidev/vanta-network/blob/main/docs/validator.md) guide.

---

### Miner Installation

Please see our [Miner Installation](https://github.com/taoshidev/vanta-network/blob/main/docs/miner.md) guide.

---

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- `| NVDA   | NVIDIA                  | Technology             |`
- `| AMD    | Advanced Micro Devices  | Technology             |`
- - 2 vCPU + 8 GB memory
- - Run the miner using CPU

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- - **Hardware**: 4 vCPU + 16 GB memory with 1 TB balanced persistent disk

---

##### Extra scrape: `miner.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- `| NVDA   | NVIDIA                  | Technology             |`
- `| AMD    | Advanced Micro Devices  | Technology             |`
- - 2 vCPU + 8 GB memory
- - Run the miner using CPU

---

##### Extra scrape: `validator.md` (grep only)

#### CPU / GPU / RAM lines (automatic grep)

- - **Hardware**: 4 vCPU + 16 GB memory with 1 TB balanced persistent disk


*Primary README URL used: `https://raw.githubusercontent.com/taoshidev/vanta-network/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.vantanetwork.io/](https://www.vantanetwork.io/)
- **GitHub:** [https://github.com/taoshidev/vanta-network](https://github.com/taoshidev/vanta-network)
- **Discord (handle / invite hint):** `tl_arrash`
- **Logo URL:** [https://website-git-ken-vanta-taoshi.vercel.app/black-white.png](https://website-git-ken-vanta-taoshi.vercel.app/black-white.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.035343135 |
| 8104244 | 0.035343051 |
| 8104292 | 0.035343064 |
| 8104340 | 0.035343041 |
| 8104388 | 0.035346053 |
| 8104436 | 0.035346098 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

