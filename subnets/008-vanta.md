# NetUID 8 — Vanta (`θ`)

## Overview

The first decentralized & trustless liquidity and execution engine for prop firms and traders

Vanta Network is the first decentralized, trustless liquidity and execution engine for prop firms and traders. It live-trades top-performing miners who deposit alpha for funding, rewards them based on verifiable performance, and uses profits to buy back alpha, creating a transparent, risk-adjusted, and incentive-aligned trading ecosystem.

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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/taoshidev/vanta-network/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


The first decentralized & trustless liquidity and execution engine for prop firms and traders

## On-chain identity — additional field


Vanta Network is the first decentralized, trustless liquidity and execution engine for prop firms and traders. It live-trades top-performing miners who deposit alpha for funding, rewards them based on verifiable performance, and uses profits to buy back alpha, creating a transparent, risk-adjusted, and incentive-aligned trading ecosystem.

## Registered contact & links


- **Website:** [https://www.vantanetwork.io/](https://www.vantanetwork.io/)
- **GitHub:** [https://github.com/taoshidev/vanta-network](https://github.com/taoshidev/vanta-network)
- **Discord (handle / invite hint):** `tl_arrash`
- **Logo URL:** [https://website-git-ken-vanta-taoshi.vercel.app/black-white.png](https://website-git-ken-vanta-taoshi.vercel.app/black-white.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.035309888 |
| 8103690 | 0.035309458 |
| 8103738 | 0.035309427 |
| 8103786 | 0.035325081 |
| 8103834 | 0.035325464 |
| 8103882 | 0.035341576 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

