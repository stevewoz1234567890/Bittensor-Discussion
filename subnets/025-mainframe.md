# NetUID 25 — Mainframe (`א`)

## Overview

Powering decentralized science on Bittensor

**From crawled page (site or GitHub):** Decentralizing AI, delivering fast, flexible, and efficient compute

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/macrocosm-os/mainframe/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Powering decentralized science on Bittensor

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://macrocosmos.ai/sn25](https://macrocosmos.ai/sn25)
- **GitHub:** [https://github.com/macrocosm-os/mainframe](https://github.com/macrocosm-os/mainframe)
- **Discord (handle / invite hint):** `mccrinbc`
- **Logo URL:** [https://www.macrocosmos.ai/images/mc_logo_black.png](https://www.macrocosmos.ai/images/mc_logo_black.png)
- **Contact:** brian@macrocosmos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.004649699 |
| 8103690 | 0.004649692 |
| 8103738 | 0.004649688 |
| 8103786 | 0.004649653 |
| 8103834 | 0.004649651 |
| 8103882 | 0.004649557 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Macrocosmos.ai
- **Meta / og:description:** Decentralizing AI, delivering fast, flexible, and efficient compute
- **Fetched from:** [https://macrocosmos.ai/sn25](https://macrocosmos.ai/sn25)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

