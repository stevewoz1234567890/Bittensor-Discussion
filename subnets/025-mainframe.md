# NetUID 25 — Mainframe (`א`)

## Overview

**Mainframe** (NetUID **25**) (`א`).

Powering decentralized science on Bittensor

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `215`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ10,901.750240956. **Alpha liquidity in pool (`alpha_in`)** = ‎2,344,987.542387744א‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,617,522.953751970א‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004649521`** *(also **moving-average price** `0.004660516977310181` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎404,079.396672328א‎`. **Owner hotkey / coldkey (chain):** `5F6aRdsBHajN2NhZHBTB6ibBFu7YuZZEWruWzB8x6B6GiZ4D` / `5F6aRdsBHajN2NhZHBTB6ibBFu7YuZZEWruWzB8x6B6GiZ4D`.
- **Subnet registered at block:** `2998801` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎162.229041897א‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000א‎` · α-in `‎0.000000000א‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004649537`
- **Market cap:** `20485610704200.579203526`
- **Liquidity:** `21804856583744`
- **Total τ:** `10901769690931`
- **Total α:** `4962435496139714`
- **α in pool:** `2344983359163256`
- **α staked:** `2060963018766542`
- **Price Δ 1h:** `-0.000408641169178304`
- **Price Δ 1d:** `-0.734763991013573364`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `14`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `14`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Powering decentralized science on Bittensor

### Repository README excerpt *(everything before first `##` heading)*

<!-- <div align="center">
    <img src="./assets/macrocosmos-black.png" alt="Alt generative-folding-tao">
</div> -->

<picture>
    <source srcset="./assets/macrocosmos-white.png"  media="(prefers-color-scheme: dark)">
    <img src="macrocosmos-white.png">
</picture>

<picture>
    <source srcset="./assets/macrocosmos-black.png"  media="(prefers-color-scheme: light)">
    <img src="macrocosmos-black.png">
</picture>

<div align="center">

</div>


<div align="center">
    <img src="./assets/mainframe_official.png" alt="mainframe-official">
</div>

*inspiration from [owl_posting](https://x.com/owl_posting)*

<div align="center">

# Mainframe

</div>

Subnet 25, Mainframe (formerly known as Protein-Folding) is the first decentralized science subnet on Bittensor. Its focus is on creating DeSci technology for pharmaceutical companies, researchers, and academics. Presently, its focus is on using global computing power to simulate protein molecular dynamics via OpenMM, and protein-ligand docking using DiffDock; both processes essential in most drug discovery pipelines. However, this subnet is designed to be adaptive to a wide array of computing-based problems in the life sciences, utilizing Bittensor’s tokenomics and incentive structure to offer affordable solutions.

Mainframe asks a simple question: can a decentralized, incentivized pool of people be used for generalized scientific compute? At Macrocosmos, we believe it is possible. Not only that, we believe that decentralized and accessible in-silico experimentation is imperative to accelerate science.

"Rational simulation-guided design of atomic systems has been a dream of researchers across the chemical sciences for decades. Enabling rapid and performant experimentation to experts would unlock massive potential to accelerate chemical science" [Mann et al. 2025](https://rowansci.com/publications/egret-1-pretrained-neural-network-potentials)

Mainframe attempts to tackle this very important challenge.



<div align="center">

<a href="https://app.macrocosmos.ai/mainframe">
  <img src="./assets/mainframe-link.png" alt="mainframe" width="300"/>
</a>

👆🏼 enter the mainframe app 👆🏼

</div>

<div align="center">

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Decentralizing AI, delivering fast, flexible, and efficient compute

**Fetched document title:** Macrocosmos.ai

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
- **`immunity_period` (blocks):** 21600
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5F6aRdsBHajN2NhZHBTB6ibBFu7YuZZEWruWzB8x6B6GiZ4D`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `21600` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `5`
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

# Mainframe

</div>

Subnet 25, Mainframe (formerly known as Protein-Folding) is the first decentralized science subnet on Bittensor. Its focus is on creating DeSci technology for pharmaceutical companies, researchers, and academics. Presently, its focus is on using global computing power to simulate protein molecular dynamics via OpenMM, and protein-ligand docking using DiffDock; both processes essential in most drug discovery pipelines. However, this subnet is designed to be adaptive to a wide array of computing-based problems in the life sciences, utilizing Bittensor’s tokenomics and incentive structure to offer affordable solutions.

Mainframe asks a simple question: can a decentralized, incentivized pool of people be used for generalized scientific compute? At Macrocosmos, we believe it is possible. Not only that, we believe that decentralized and accessible in-silico experimentation is imperative to accelerate science.

"Rational simulation-guided design of atomic systems has been a dream of researchers across the chemical sciences for decades. Enabling rapid and performant experimentation to experts would unlock massive potential to accelerate chemical science" [Mann et al. 2025](https://rowansci.com/publications/egret-1-pretrained-neural-network-potentials)

Mainframe attempts to tackle this very important challenge. 



<div align="center">

<a href="https://app.macrocosmos.ai/mainframe">
  <img src="./assets/mainframe-link.png" alt="mainframe" width="300"/>
</a>

👆🏼 enter the mainframe app 👆🏼

</div>

<div align="center">

---

### 🧑🏻‍💻 Mainframe App:

https://app.macrocosmos.ai/mainframe

---

### 📖 Mainframe Documentation:

https://docs.macrocosmos.ai/subnets/subnet-25-mainframe

---

### 👾 Mainframe’s API:

https://docs.macrocosmos.ai/developers/api-documentation/sn25-mainframe

---

### 🧮 Mainframe's Protein Folding Dashboard:

https://www.macrocosmos.ai/sn25/dashboard


<div align="center">

---

# Mainframe Incentive Architecture

</div>

As Mainframe is meant to be a collection of different scientific computation tasks happening in parallel, the result is that there are a collection of incentive mechanisms that must be managed. The sections below outline our current tasks: 

<div align="center">

---

# Dashboards, Tools, and Additional Resources

</div>

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/macrocosm-os/mainframe/main/README.md`*

## On-chain identity — description


Powering decentralized science on Bittensor

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://macrocosmos.ai/sn25](https://macrocosmos.ai/sn25)
- **GitHub:** [https://github.com/macrocosm-os/mainframe](https://github.com/macrocosm-os/mainframe)
- **Discord (handle / invite hint):** `mccrinbc`
- **Logo URL:** [https://www.macrocosmos.ai/images/mc_logo_black.png](https://www.macrocosmos.ai/images/mc_logo_black.png)
- **Contact:** brian@macrocosmos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104037 | 0.004649548 |
| 8104085 | 0.004649546 |
| 8104133 | 0.004649542 |
| 8104181 | 0.004649539 |
| 8104229 | 0.004649529 |
| 8104277 | 0.004649521 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

