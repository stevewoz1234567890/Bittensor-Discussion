# NetUID 51 — lium.io (`ת`)

## Overview

revolutionizing the democratization of compute

**From crawled page (site or GitHub):** Contribute to Datura-ai/lium-io development by creating an account on GitHub.

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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/Datura-ai/lium-io/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


revolutionizing the democratization of compute

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/Datura-ai/lium-io](https://github.com/Datura-ai/lium-io)
- **Discord (handle / invite hint):** `p383_54249`
- **Logo URL:** [https://raw.githubusercontent.com/Datura-ai/lium-logos/refs/heads/main/Celium_Icon_FullColor.png](https://raw.githubusercontent.com/Datura-ai/lium-logos/refs/heads/main/Celium_Icon_FullColor.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.063768602 |
| 8103690 | 0.063783907 |
| 8103738 | 0.063831029 |
| 8103786 | 0.063840223 |
| 8103834 | 0.063843413 |
| 8103882 | 0.063846935 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** GitHub - Datura-ai/lium-io · GitHub
- **Meta / og:description:** Contribute to Datura-ai/lium-io development by creating an account on GitHub.
- **Fetched from:** [https://github.com/Datura-ai/lium-io](https://github.com/Datura-ai/lium-io)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

