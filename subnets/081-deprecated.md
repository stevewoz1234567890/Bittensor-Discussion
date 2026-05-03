# NetUID 81 — deprecated (`ᚠ`)

## Overview

**deprecated** (NetUID **81**) (`ᚠ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `209`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ20,595.351128103. **Alpha liquidity in pool (`alpha_in`)** = ‎2,369,538.105420420ᚠ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,002,437.660023069ᚠ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.008696841`** *(also **moving-average price** `0.008882277878001332` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎767,235.613961110ᚠ‎`. **Owner hotkey / coldkey (chain):** `5F9uEDDovurwEJihzZSpKypipVy84EEAPHTt3EfepTjcQfij` / `5DUELqJMeY6tA7652ooUUvU9TgUCi5hnv9o66nC8Zjw7BtW5`.
- **Subnet registered at block:** `5203057` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎156.181904774ᚠ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ᚠ‎` · α-in `‎0.000000000ᚠ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.008696842`
- **Market cap:** `31035372958706.372534278`
- **Liquidity:** `41202849643913`
- **Total τ:** `20595351666002`
- **Total α:** `4371962765443489`
- **α in pool:** `2369538043569365`
- **α staked:** `1199041557934994`
- **Price Δ 1h:** `-0.000747392147576144`
- **Price Δ 1d:** `-2.458971346844344032`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `7`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `7`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

deprecated

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
- **`immunity_period` (blocks):** 10799
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5DUELqJMeY6tA7652ooUUvU9TgUCi5hnv9o66nC8Zjw7BtW5`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10799` blocks
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

*No miner/validator sections auto-matched.* Open [https://github.com/deprecated/deprecated](https://github.com/deprecated/deprecated) for requirements.

## On-chain identity — description


deprecated

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/deprecated/deprecated](https://github.com/deprecated/deprecated)
- **Discord (handle / invite hint):** `deprecated`
- **Logo URL:** [https://deprecated.png](https://deprecated.png)
- **Contact:** deprecated@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.008696896 |
| 8104072 | 0.008696888 |
| 8104120 | 0.00869688 |
| 8104168 | 0.008696846 |
| 8104216 | 0.008696841 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

