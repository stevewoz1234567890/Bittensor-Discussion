# NetUID 70 — NexisGen (`غ`)

## Overview

**NexisGen** (NetUID **70**) (`غ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `260`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ814.012800354. **Alpha liquidity in pool (`alpha_in`)** = ‎96,549.814522117غ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎302,514.902744672غ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008431229`** *(also **moving-average price** `0.007921961136162281` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎13,741.393829717غ‎`. **Owner hotkey / coldkey (chain):** `5EJGfSvRcEGVQtqDuU7YYwuZRHmaktf6JEZDeFPyeXksiHrm` / `5HisJVRY5s72aGFqcvemjk2AzdQnPhbTcMjWDecWZKtoCqj9`.
- **Subnet registered at block:** `7787562` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎138.296155154غ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004215723` · α-out `‎1.000000000غ‎` · α-in `‎0.500000000غ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.00844147`
- **Market cap:** `2525663692828.58086773`
- **Liquidity:** `1628401613290`
- **Total τ:** `814190330764`
- **Total α:** `398955881354359`
- **α in pool:** `96453731699141`
- **α staked:** `202743409655218`
- **Price Δ 1h:** `1.702803629097599015`
- **Price Δ 1d:** `8.537899360200785863`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `180`
- **Active validators:** `8`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `4220771`
- **Max neurons:** `256`
- **Validators (metadata):** `8`
- **Neuron reg. cost:** `50000000`

### On-chain declared purpose *(SubnetIdentity)*

Enterprise dataset delivery

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 180
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.050000000
- **Owner SS58 (`owner_ss58`):** `5HisJVRY5s72aGFqcvemjk2AzdQnPhbTcMjWDecWZKtoCqj9`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.050000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
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

## Miner / validator hardware (CPU/GPU/RAM)

*No GitHub URL on-chain; hardware notes not fetched automatically.*

## On-chain identity — description


Enterprise dataset delivery

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Logo URL:** [https://www.nexisgen.ai/logo.png](https://www.nexisgen.ai/logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.008336066 |
| 8104133 | 0.008378821 |
| 8104181 | 0.008402525 |
| 8104229 | 0.008439704 |
| 8104277 | 0.008431229 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

