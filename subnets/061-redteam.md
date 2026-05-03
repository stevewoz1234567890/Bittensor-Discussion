# NetUID 61 — RedTeam (`ر`)

## Overview

"The RedTeam subnet by Innerworks is a decentralized platform designed to drive innovation in cybersecurity through competitive programming challenges. The subnet incentivizes miners to develop and submit code solutions to various technical challenges, with a focus on enhancing security. These solutions can be integrated into real-world products to improve their security features."

**From crawled page (site or GitHub):** Transform your skills in circumventing and breaking detection mechanisms into meaningful, rewarding work. Compete, innovate, and earn in a safe, decentralized platform.

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
- **`immunity_period` (blocks):** 14400
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5ECEsYL82fbXx9KfTZy7G2KXSurnScciJyAVMHZjekc8jUbn`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `14400` blocks
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

## Validator Setup

[Read the full documentation](./docs/1.validator.md)

---

## Miner Setup

[Read the full documentation](./docs/2.miner.md)

---


*README source used for excerpts: `https://raw.githubusercontent.com/RedTeamSubnet/RedTeam/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


"The RedTeam subnet by Innerworks is a decentralized platform designed to drive innovation in cybersecurity through competitive programming challenges. The subnet incentivizes miners to develop and submit code solutions to various technical challenges, with a focus on enhancing security. These solutions can be integrated into real-world products to improve their security features."

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://www.theredteam.io/](https://www.theredteam.io/)
- **GitHub:** [https://github.com/RedTeamSubnet/RedTeam](https://github.com/RedTeamSubnet/RedTeam)
- **Discord:** [https://discord.com/channels/799672011265015819/1319313447435108413](https://discord.com/channels/799672011265015819/1319313447435108413)
- **Contact:** oscar@theredteam.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.003893594 |
| 8103690 | 0.003893586 |
| 8103738 | 0.00389306 |
| 8103786 | 0.003893128 |
| 8103834 | 0.003893125 |
| 8103882 | 0.003893118 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Harness Red Team Ingenuity to Tackle the Internet's Challenges | RedTeam
- **Meta / og:description:** Transform your skills in circumventing and breaking detection mechanisms into meaningful, rewarding work. Compete, innovate, and earn in a safe, decentralized platform.
- **Fetched from:** [https://www.theredteam.io/](https://www.theredteam.io/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

