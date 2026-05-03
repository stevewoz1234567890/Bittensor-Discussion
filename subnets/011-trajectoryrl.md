# NetUID 11 — TrajectoryRL (`λ`)

## Overview

Agentic RL as a Service, Optimize agent trajectories to make agents cheaper, safer, and more reliable.

**From crawled page (site or GitHub):** The open factory for AI agent skills. Open-source skills, vetted by continuous competition, that work with any agent harness. TrajectoryRL runs a 24/7 competition on Bittensor Subnet 11 to produce the best skills. The winners surface automatically and anyone can use them.

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
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.200000000
- **Owner SS58 (`owner_ss58`):** `5D2Jhtbnm7iAdKfjRk6DisXBnr1MEsYat8kXqaPNrVqJP3uE`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.200000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `10`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `100000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

### For Validators

Validators run in Docker, auto-updated by Watchtower. The validator pulls the latest TrajRL-Bench image before each eval cycle — new scenarios are picked up automatically.

```bash

---

### For Miners

Mining means writing a **SKILL.md** — instructions and strategies that teach an AI agent how to handle operational scenarios. The testee agent SSHes into an isolated sandbox (shell + mock services + scenario files), reads your SKILL.md, solves the task. A judge agent then SSHes in, grounds its evaluation in the sandbox state, and scores the work. No GPU, no server, no uptime required.

---

#### 1. Prerequisites (one-time)

```bash
pip install bittensor-cli

btcli wallet create --wallet-name my-miner
btcli subnets register --wallet-name my-miner --hotkey default --netuid 11
```

---

# Upload to S3-compatible storage (configure S3_BUCKET, AWS_* in .env.miner)

trajectoryrl-miner upload pack.json


*README source used for excerpts: `https://raw.githubusercontent.com/trajectoryRL/trajectoryRL/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Agentic RL as a Service, Optimize agent trajectories to make agents cheaper, safer, and more reliable.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://trajrl.com](https://trajrl.com)
- **GitHub:** [https://github.com/trajectoryRL/trajectoryRL](https://github.com/trajectoryRL/trajectoryRL)
- **Logo URL:** [https://pbs.twimg.com/profile_images/2018928039716089856/2PZ-Bhm2_400x400.jpg](https://pbs.twimg.com/profile_images/2018928039716089856/2PZ-Bhm2_400x400.jpg)
- **Contact:** trajectoryrl@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.011318871 |
| 8103690 | 0.011318849 |
| 8103738 | 0.01131866 |
| 8103786 | 0.011316364 |
| 8103834 | 0.011316356 |
| 8103882 | 0.011310858 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** TrajectoryRL | Bittensor Subnet 11
- **Meta / og:description:** The open factory for AI agent skills. Open-source skills, vetted by continuous competition, that work with any agent harness. TrajectoryRL runs a 24/7 competition on Bittensor Subnet 11 to produce the best skills. The winners surface automatically and anyone can use them.
- **Fetched from:** [https://trajrl.com](https://trajrl.com)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

