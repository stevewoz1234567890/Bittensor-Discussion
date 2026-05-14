# NetUID 50 — Synth (`ש`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Synth** (NetUID **50**) (`ש`).

Predictive intelligence for financial markets and beyond

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `37`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ14,886.695405125. **Alpha liquidity in pool (`alpha_in`)** = ‎1,596,994.294261352ש‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,117,399.489652251ש‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.009347237`** *(also **moving-average price** `0.00949745811522007` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,081,297.219622956ש‎`. **Owner hotkey / coldkey (chain):** `5DxyiWpGqN5xXiczXcEGph51BcgTqcYKD5GKZqoACuc2sJkD` / `5DxyiWpGqN5xXiczXcEGph51BcgTqcYKD5GKZqoACuc2sJkD`.
- **Subnet registered at block:** `4763204` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎27.812411020ש‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ש‎` · α-in `‎0.000000000ש‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104398`
- **Liquidity constant `k`:** `23773967622391310974270229000`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Synth` |
| Symbol (API) | `ש` |
| Rank | `26` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.009346622` |
| Market cap | `41201064743262.905420608` |
| Market cap Δ 1d | `0.224203636735901888` |
| Liquidity | `29813197393241` |
| Total τ | `14886199173860` |
| Total α | `4714160783913603` |
| α in pool | `1597047384539695` |
| α staked | `2811076186014769` |
| Price Δ 1h | `1.140432357936690692` |
| Price Δ 1d | `0.095612471344638194` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `50` |
| Owner SS58 (API) | `5DxyiWpGqN5xXiczXcEGph51BcgTqcYKD5GKZqoACuc2sJkD` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4763204` |
| Registration wall time | `2025-01-22T21:56:00Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `13` |
| Active miners | `238` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `13` |
| Max validators (API) | `64` |
| Neuron reg. cost | `800000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">
  <a href="https://www.synthdata.co/">
    <img alt="Synth banner logo" src="https://github.com/synthdataco/synth-subnet/blob/main/docs/images/logo.png" height="134" />
  </a>
</div>

<h1 align="center">
    Synth Subnet
</h1>

<div align="center">
    <a href="https://www.synthdata.co" target="_blank">
        <b>Website</b>
    </a>
·
    <a href="https://github.com/synthdataco/synth-subnet/blob/main/Synth%20Whitepaper%20v1.pdf" target="_blank">
        <b>Whitepaper</b>
    </a>
·
    <a href="https://discord.gg/gnt8sFMdg6" target="_blank">
        <b>Discord</b>
    </a>
·
    <a href="https://api.synthdata.co/docs" target="_blank">
        <b>API Documentation</b>
    </a>
</div>

---

<div align="center">

[![License: MIT](https://img.shields.io/github/license/synthdataco/synth-subnet)][license]

</div>

---

### Table of contents

- [1. Overview](#-1-overview)
  - [1.1. Introduction](#11-introduction)
  - [1.2. Task Presented to the Miners](#12-task-presented-to-the-miners)
  - [1.3. Validator's Scoring Methodology](#13-validators-scoring-methodology)
  - [1.4. Calculation of Leaderboard Score](#14-calculation-of-leaderboard-score)
  - [1.5. Overall Purpose](#15-overall-purpose)
- [2. Usage](#-2-usage)
  - [2.1. Miners](#21-miners)
    - [2.1.1. Tutorial](#211-tutorial)
    - [2.1.2. Reference](#212-reference)
  - [2.2. Validators](#22-validators)
  - [2.3. Develop](#23-develop)
- [3. License](#-3-license)

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
| `immunity_period` (blocks) | 65535 |
| Registration recycle cost snapshot (`burn`) | τ0.800000000 |
| Owner SS58 (`owner_ss58`) | `5DxyiWpGqN5xXiczXcEGph51BcgTqcYKD5GKZqoACuc2sJkD` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.800000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `65535` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
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

### 1.2. Task Presented to the Miners

```mermaid
sequenceDiagram
    participant Miner
    participant Validator
    participant Storage

    loop Every Hour
        Validator->>Miner: Request with input prompts
        note left of Validator: asset='BTC', start_time='2025-02-10T14:59:00', time_increment=300, etc.

        Miner-->>Validator: Prediction results
        note right of Miner: result: price prediction <br/> [[{"time": "2025-02-10T14:59:00+00:00", "price": 97352.60591372}, ...], ...]

        Validator->>Validator: Run "prediction results" validation function

        alt Validation error
            Validator->>Storage: Save error
        else No errors
            Validator->>Storage: Save prediction results
        end
    end
```

Miners are tasked with providing probabilistic forecasts of an asset's future price movements. Specifically, each miner is required to generate multiple simulated price paths for an asset, from the current time over specified time increments and time horizon. Initially, all checking prompts were to produce 100 simulated paths for the future price of bitcoin at 5-minute time increments for the next 24 hours. As of November 13, 2025, the network has been upgraded to request that miners produce 1000 simulated paths for the future price of BTC, ETH, SOL, and XAU for the next 24 hours. This upgrade reflects Synth’s commitment to developing high frequency trading capabilities. January 2026, further assets were added to Synth predictions. 5 tokenized equity assets, SPYX, NVDAX, TSLAX, AAPLX, and GOOGLX are now included in the 24-Hour predictions. In March 2026, 3 new assets were launched on the 24-Hour horizon: XRP, HYPE, and WTIOIL. HYPE was also added to the 1-Hour horizon.

Whereas other subnets ask miners to predict single values for future prices, we’re interested in the miners correctly quantifying uncertainty. We want their price paths to represent their view of the probability distribution of the future price, and we want their paths to encapsulate realistic price dynamics, such as volatility clustering and skewed fat tailed price change distributions. As the network matures, modelling the correlations between asset prices will be essential.

If the miners do a good job, the Synth Subnet will become the world-leading source of realistic synthetic price data for training AI agents. And it will be the go-to location for asking questions on future price probability distributions - a valuable resource for options trading and portfolio management.

The checking prompts sent to the miners will have the format:
(start_time, asset, time_increment, time_horizon, num_simulations)

The 24-Hour prompt parameters have the following values:

- **Start Time ($t_0$)**: 1 minute from the time of the request.
- **Asset**: BTC, ETH, XAU, SOL, SPYX, NVDAX, TSLAX, AAPLX, GOOGLX, XRP, HYPE, WTIOIL.
- **Time Increment ($\Delta t$)**: 5 minutes.
- **Time Horizon ($T$)**: 24 hours.
- **Number of Simulations ($N_{\text{sim}}$)**: 1000.

The 1-Hour prompt parameters have the following values:

- **Start Time ($t_0$)**: 1 minute from the time of the request.
- **Asset**: BTC, ETH, SOL, XAU, HYPE.
- **Time Increment ($\Delta t$)**: 1 minute.
- **Time Horizon ($T$)**: 1 hour.
- **Number of Simulations ($N_{\text{sim}}$)**: 1000.

**Asset Weights**

| Asset  | Weight             |
| ------ | ------------------ |
| BTC    | 1.0                |
| ETH    | 0.7064366394033871 |
| XAU    | 1.7370922597118699 |
| SOL    | 0.6310037175639559 |
| SPYX   | 3.437935601155441  |
| NVDAX  | 1.6028217601617174 |
| TSLAX  | 1.6068755936957768 |
| AAPLX  | 2.0916380815843123 |
| GOOGLX | 1.6827392777257926 |
| XRP    | 0.5658394110809131 |
| HYPE   | 0.4784547133706857 |
| WTIOIL | 0.8475062847978935 |

Validators cycle through the assets, sending out prediction requests at regular intervals. The miner has until the start time to return ($N_{\text{sim}}$) paths, each containing price predictions at times given by:

$$
t_i = t_0 + i \times \Delta t, \quad \text{for }\, i = 0, 1, 2, \dots, N
$$

where:

- $N = \dfrac{T}{\Delta t}$ is the total number of increments.

We recommend the miner sends a request to the Pyth Oracle to acquire the price of the asset at the start_time.

If they fail to return predictions by the start_time or the predictions are in the wrong format, they will be scored 0 for that prompt.

**Emissions Split**

24-Hour Predictions: 50% of total emissions
1-Hour HFT Predictions: 50% of total emissions

<sup>[Back to top ^][table-of-contents]</sup>

---

### 1.3. Validator's Scoring Methodology

Th…

---





#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/mode-network/synth-subnet/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://synthdata.co](https://synthdata.co)
- **GitHub:** [https://github.com/mode-network/synth-subnet](https://github.com/mode-network/synth-subnet)
- **Logo URL:** [https://taostats.io/images/subnets/50.webp?w=96&q=75](https://taostats.io/images/subnets/50.webp?w=96&q=75)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.009346589 |
| 8104292 | 0.009346567 |
| 8104340 | 0.00934653 |
| 8104388 | 0.009346504 |
| 8104436 | 0.009347236 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

