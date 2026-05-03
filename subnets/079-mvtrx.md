# NetUID 79 — MVTRX (`ي`)

## Overview

Building a SOTA Exchange for dTAO and Beyond

Powered by TAOS Matrix of Simulations Sandbox

**From crawled page (site or GitHub):** Simulation of Automated Trading in Intelligent Markets (a.k.a. Sn-79)

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
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.002076310
- **Owner SS58 (`owner_ss58`):** `5Fxp7QBG81X7PLdMkAe1RLCvqqfQSw9rJC5ppEQs9FP8qez9`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
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

## Miner / validator compute notes (README excerpts)

### Validator Role <span id="mechanism-validator"><span>

Validators in the subnet are responsible primarily for maintaining the state of the simulation, and rewarding agents (miners) which achieve the best results over all realizations of the simulated market.  They deploy two components:
- The C++ simulator, which handles all the computation necessary to simulate asset markets
- The Python validator, which receives state updates from the simulator, forwards these to miners, submits instructions received in response back to the simulator, and calculates miner scores based on their performance throughout the simulation.

---

### Miner Role <span id="mechanism-miner"><span>

Miners in the subnet function as trading agents in the distributed simulation; their role is to develop and host trading strategies which maximize their average risk-adjusted performance measures over all simulated market realizations, while also maintaining a sufficient level of trading activity.  There are no strict limitations on what strategies are able to be applied, but the simulation parameters and performance evaluation metrics will be continually reviewed, selected and adjusted with the intention of maximizing the utility of the output data, and promoting the use of intelligent, risk-averse and budget-constrained trading logic.

---
<div style="page-break-after: always;"></div>

---

### Validator <span id="technical-validator"><span>

The validator functions in a sense as a "proxy" which allows the C++ simulator to communicate with participants in the subnet, and handles all the Bittensor-network-related tasks involved in validator operation - authenticating and distributing requests, validating and processing responses, calculating miner scores, setting weights and, ultimately, providing access to the subnet computational resources for external queries.

---

### Miner <span id="technical-miner"><span>

Miners receive state updates from validators, and respond with instructions as to how they would like to modify their positions in the simulated orderbook realizations by placing and cancelling orders.  In this first version of the subnet, state updates are published at a parameterized interval throughout the simulation and miners are only able to submit instructions at each state publishing event - a planned future implementation will allow continuous bidirectional communication of state and instructions, in line with real exchange operation.  The state update includes all L3 messages processed since the last update, so that strategies analysing the most detailed information are still possible to apply, being limited only in the time-scale at which the algorithm is able to act.

While awaiting the validator to request and receive responses from miners, the simulation is paused such that no events are processed during this time; in order to reward efficient computation as well as agent performance, the response time of miners is used to determine the "delay" or "latency" with which their instructions will be processed by the simulator.  Longer response times thus imply more events that may take place before execution of their instructions, requiring realistic effects like price slippage to be accounted for.   This incentivizes miners to be both fast and intelligent in their trading strategy, while also carefully managing their risk across all market state realizations.  

Miner agents are otherwise treated in the simulator on the same footing as the background agents; their instructions are processed as if they would be submitted to a real exchange, with orders being traded or opened on the book in accordance with standard matching rules.  Every agent's orders will interact with those of the background agents and miners - this ensures a proper and full accounting of the performance of the miner, including their market impact.  Since agents actions directly affect the market structure, this must also be considered when making trading decisions.

---
<div style="page-break-after: always;"></div>

---

## Requirements <span id="requirements"><span>

Requirements are subject to change as the subnet matures and evolves; this section describes the recommended resources to be available for the initial simulation conditions.  We currently manage 40 orderbooks in a simulation, each having around 1000 background agents, while the aim in the near- to mid-term is to reach 1,000+ simulated orderbooks in order to achieve a meaningful level of statistical significance in the evaluation of results.

---

### Validator <span id="requirements-validator"><span>

Validators need to host the C++ simulator as well as the Python validator.  In the early days of the subnet, the number of orderbooks simulated as well as the count and type of background agents will be reduced so as to limit the requirements before the subnet matures and sufficient emissions are gained to justify the expense of hosting more powerful machinery.  Basic requirements:

- 32GB RAM
- 16 CORE CPU
- Ubuntu >= 22.04
- g++ 14.

We hope to increase both major parameters significantly so that validators may wish to prepare a larger machine for easier expansion.  It should be noted however that increasing the CPU resources available will result in a faster progression of simulations due to multi-threaded processing of the orderbook realizations.  This should not inherently be a problem, but may cause divergences in scoring if there is a major discrepancy in resources with…


*README source used for excerpts: `https://raw.githubusercontent.com/taos-im/sn-79/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Building a SOTA Exchange for dTAO and Beyond

## On-chain identity — additional field


Powered by TAOS Matrix of Simulations Sandbox

## Registered contact & links


- **Website:** [https://taos.im](https://taos.im)
- **GitHub:** [https://github.com/taos-im/sn-79](https://github.com/taos-im/sn-79)
- **Logo URL:** [https://assets.mvtrx.fi/logo.png](https://assets.mvtrx.fi/logo.png)
- **Contact:** to@mvtrx.fi

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.009392993 |
| 8103690 | 0.009379832 |
| 8103738 | 0.009293103 |
| 8103786 | 0.009205706 |
| 8103834 | 0.009201882 |
| 8103882 | 0.009210235 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** TAOS – Simulation of Automated Trading in Intelligent Markets (a.k.a. Sn-79)
- **Meta / og:description:** Simulation of Automated Trading in Intelligent Markets (a.k.a. Sn-79)
- **Fetched from:** [https://taos.im](https://taos.im)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

