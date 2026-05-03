# NetUID 0 — root (`Τ`)

## Overview

The **root network** (NetUID 0) is Bittensor’s top-level coordination layer. TAO holders delegate stake to root validators, who set **weights** on other subnets. Those weights help determine how network **emissions** are allocated across subnets. Root is not an application or “task” subnet like higher netuids; it is the mechanism through which the protocol routes incentive and security across the rest of the network.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 64
- **`subnetwork_n`:** 64
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 0
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 100
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 4611686018427387903
- **`immunity_period` (blocks):** 4096
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5C4hrfjw9DjXZTzV3MwzrrAr9P1MJhSrvWGWqi1eSuyUpnhM`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `4611686018427387903` (min `4611686018427387903`, max `4611686018427387903`)
- **`target_regs_per_interval`:** `64`
- **`immunity_period`:** `4096` blocks
- **`max_regs_per_block`:** `64`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `18446744073709551615`
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

No GitHub URL is registered on-chain for this subnet, so README-based hardware notes were not fetched. Use the website or community links above when available.

## On-chain identity — description


*Empty — no description bytes set in `SubnetIdentity`.*

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


*No `SubnetIdentity` registered on-chain.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Root uses TAO directly; protocol surfaces **1 τ per root weight unit** for pricing helpers.

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103306 | 1 |
| 8103354 | 1 |
| 8103402 | 1 |
| 8103450 | 1 |
| 8103498 | 1 |
| 8103546 | 1 |
| 8103594 | 1 |
| 8103642 | 1 |
| 8103690 | 1 |
| 8103738 | 1 |
| 8103786 | 1 |
| 8103834 | 1 |
| 8103882 | 1 |


---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

