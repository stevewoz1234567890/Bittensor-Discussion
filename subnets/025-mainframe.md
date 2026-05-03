# NetUID 25 — Mainframe (`א`)

## Overview

**Mainframe** (NetUID **25**) (`א`).

Powering decentralized science on Bittensor

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `153`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ10,901.769443110. **Alpha liquidity in pool (`alpha_in`)** = ‎2,344,983.412465104א‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,617,465.083674610א‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004649537`** *(also **moving-average price** `0.004660719074308872` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎404,079.377470174א‎`. **Owner hotkey / coldkey (chain):** `5F6aRdsBHajN2NhZHBTB6ibBFu7YuZZEWruWzB8x6B6GiZ4D` / `5F6aRdsBHajN2NhZHBTB6ibBFu7YuZZEWruWzB8x6B6GiZ4D`.
- **Subnet registered at block:** `2998801` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎115.446736542א‎`; pending root emission `τ0.000000000`.
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
| 8103976 | 0.004649552 |
| 8104024 | 0.00464955 |
| 8104072 | 0.004649546 |
| 8104120 | 0.004649542 |
| 8104168 | 0.004649539 |
| 8104216 | 0.004649537 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.00572984 |
| 2026-03-10T23:59:48Z | 7718257 | 0.00556628 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005553626 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005596661 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005265075 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005285914 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005135098 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005093337 |
| 2026-03-17T23:59:48Z | 7768619 | 0.004909771 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005111273 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00504636825097816742 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005020874 |
| 2026-03-21T23:59:48Z | 7797398 | 0.004955577 |
| 2026-03-22T23:59:48Z | 7804598 | 0.004972931 |
| 2026-03-23T23:59:48Z | 7811798 | 0.004992892 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00516771600140668403 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005177074 |
| 2026-03-26T23:59:48Z | 7833396 | 0.00487797 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004715387 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004701788 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004720373 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004725232 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004770379 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004829654 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004842767 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004870667 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004966587 |
| 2026-04-05T23:59:48Z | 7905188 | 0.005030836 |
| 2026-04-06T23:59:48Z | 7912388 | 0.005065682 |
| 2026-04-07T23:59:48Z | 7919588 | 0.005119279 |
| 2026-04-08T23:59:48Z | 7926788 | 0.005096496 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004738891 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004817607 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004816521 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004778441 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004897487 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004724628 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004767052 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004750254 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004769579 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004790607 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004917179 |
| 2026-04-20T23:59:48Z | 8013179 | 0.005027552 |
| 2026-04-21T23:59:48Z | 8020376 | 0.00498748 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004872269 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004872594 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004856358 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004823309 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004759109 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004734224 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004635471 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004653862 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004706979 |
| 2026-05-01T23:59:48Z | 8092168 | 0.00467523 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004682274 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004649537 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

