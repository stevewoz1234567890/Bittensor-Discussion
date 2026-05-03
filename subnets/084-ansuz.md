# NetUID 84 — ansuz (`ᚨ`)

## Overview

**ansuz** (NetUID **84**) (`ᚨ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `274`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,548.924371783. **Alpha liquidity in pool (`alpha_in`)** = ‎134,407.500665151ᚨ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎228,374.978295573ᚨ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011524109`** *(also **moving-average price** `0.0024061582516878843` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎2,158.797498515ᚨ‎`. **Owner hotkey / coldkey (chain):** `5EjbqZDoEAMzk3AzCExmBT6toYC2iEKyyymQojsm8NkLpVAF` / `5G1hDNpPA8pRZUMJRBcELthCaHVPQcHZb1X3jbeyQ9zUtbbd`.
- **Subnet registered at block:** `8085297` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎143.549084410ᚨ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003698686` · α-out `‎1.000000000ᚨ‎` · α-in `‎0.320944760ᚨ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.01150642`
- **Market cap:** `4086330910848.3735368`
- **Liquidity:** `3094917653565`
- **Total τ:** `1547457722745`
- **Total α:** `362683372525551`
- **α in pool:** `134486654478157`
- **α staked:** `220648210305883`
- **Price Δ 1h:** `3.636914038452341054`
- **Price Δ 1d:** `7.777321410757949645`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `28`
- **Active validators:** `5`
- **Active miners:** `2`
- **Active dual:** `1`
- **Emission:** `3697230`
- **Max neurons:** `256`
- **Validators (metadata):** `5`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 28
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5G1hDNpPA8pRZUMJRBcELthCaHVPQcHZb1X3jbeyQ9zUtbbd`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `4611686018427387903`)
- **`target_regs_per_interval`:** `2`
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
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No GitHub URL on-chain; hardware notes not fetched automatically.*

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


*No `SubnetIdentity` registered on-chain.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.011283639 |
| 8104133 | 0.011648989 |
| 8104181 | 0.011662116 |
| 8104229 | 0.011510726 |
| 8104277 | 0.011524108 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

