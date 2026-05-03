# NetUID 102 — ConnitoAI (`ვ`)

## Overview

**ConnitoAI** (NetUID **102**) (`ვ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `230`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ959.530875090. **Alpha liquidity in pool (`alpha_in`)** = ‎48,034.317471222ვ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎223,666.096486848ვ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.019976401`** *(also **moving-average price** `0.01625258894637227` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎7,926.529789332ვ‎`. **Owner hotkey / coldkey (chain):** `5EEinUEy3cfBCUyhbvCcYfWU713QCsDoVXqbbRLKFtEqKkC9` / `5HidKLutq4YQgmBPWtLRYzh2cGYgWJRaC4owcz756W87puTL`.
- **Subnet registered at block:** `7840965` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎115.389823476ვ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.008269685` · α-out `‎1.000000000ვ‎` · α-in `‎0.413969081ვ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.019976853`
- **Market cap:** `4590584934844.152957687`
- **Liquidity:** `1918890274404`
- **Total τ:** `959430411495`
- **Total α:** `271682030217179`
- **α in pool:** `48028579021391`
- **α staked:** `181766621195788`
- **Price Δ 1h:** `1.053034289286458247`
- **Price Δ 1d:** `47.479911002007017252`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `4`
- **Active miners:** `3`
- **Active dual:** `0`
- **Emission:** `8266953`
- **Max neurons:** `256`
- **Validators (metadata):** `4`
- **Neuron reg. cost:** `2224407`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

## Operational parameters — registration, limits, economics (chain)


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
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.002152769
- **Owner SS58 (`owner_ss58`):** `5HidKLutq4YQgmBPWtLRYzh2cGYgWJRaC4owcz756W87puTL`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
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


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


*No links or contacts in chain identity.*

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.020104216 |
| 8104072 | 0.020098844 |
| 8104120 | 0.020126734 |
| 8104168 | 0.020006574 |
| 8104216 | 0.019976401 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

