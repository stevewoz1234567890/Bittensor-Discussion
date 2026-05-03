# NetUID 27 — Nodexo (`ג`)

## Overview

**Nodexo** (NetUID **27**) (`ג`).

Decentralized AI compute platfrom

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `155`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,738.474595757. **Alpha liquidity in pool (`alpha_in`)** = ‎1,843,171.198682931ג‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,220,075.702777776ג‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004727634`** *(also **moving-average price** `0.004702158272266388` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎608,233.848058674ג‎`. **Owner hotkey / coldkey (chain):** `5Cyfk5Jjee6uCafjZyUUjtKd7Q4qh1yJ48Ts7bkT9xXaDqe1` / `5CopvHeTZHNy6RMztuRFvViwwZbsZaVkJPA9zmRRnPAna73M`.
- **Subnet registered at block:** `1727132` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎117.126093265ג‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002363815` · α-out `‎1.000000000ג‎` · α-in `‎0.500000000ג‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004727609`
- **Market cap:** `19749618960333.004475377`
- **Liquidity:** `17452205884142`
- **Total τ:** `8738421918729`
- **Total α:** `5063232098171489`
- **α in pool:** `1843169341079829`
- **α staked:** `2334337504417124`
- **Price Δ 1h:** `0.146800915715726488`
- **Price Δ 1d:** `2.406913124981858527`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `17`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `2363801`
- **Max neurons:** `256`
- **Validators (metadata):** `17`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Decentralized AI compute platfrom

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CopvHeTZHNy6RMztuRFvViwwZbsZaVkJPA9zmRRnPAna73M`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `2`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

*No miner/validator sections auto-matched.* Open [https://github.com/neuralinternet/compute-subnet](https://github.com/neuralinternet/compute-subnet) for requirements.

## On-chain identity — description


Decentralized AI compute platfrom

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/neuralinternet/compute-subnet](https://github.com/neuralinternet/compute-subnet)
- **Discord:** [https://discord.com/invite/nodexo](https://discord.com/invite/nodexo)
- **Logo URL:** [https://console.nodexo.ai/assets/images/logo/logo-dark.svg](https://console.nodexo.ai/assets/images/logo/logo-dark.svg)
- **Contact:** neuralinternet@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8103976 | 0.004722104 |
| 8104024 | 0.00472314 |
| 8104072 | 0.004724165 |
| 8104120 | 0.004727465 |
| 8104168 | 0.004727549 |
| 8104216 | 0.004727634 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004849407 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004671013 |
| 2026-03-11T23:59:48Z | 7725455 | 0.004753401 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.004605123 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004568423 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004453422 |
| 2026-03-15T23:59:48Z | 7754226 | 0.00405837 |
| 2026-03-16T23:59:48Z | 7761426 | 0.003829837 |
| 2026-03-17T23:59:48Z | 7768619 | 0.003868935 |
| 2026-03-18T23:59:48Z | 7775819 | 0.003890099 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00421013766692158611 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004136861 |
| 2026-03-21T23:59:48Z | 7797398 | 0.004357792 |
| 2026-03-22T23:59:48Z | 7804598 | 0.004269505 |
| 2026-03-23T23:59:48Z | 7811798 | 0.00421508 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00401139063810840301 |
| 2026-03-25T23:59:48Z | 7826196 | 0.003984546 |
| 2026-03-26T23:59:48Z | 7833396 | 0.003885721 |
| 2026-03-27T23:59:48Z | 7840596 | 0.003937246 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.003941515 |
| 2026-03-29T23:59:48Z | 7854902 | 0.003984391 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.003829273 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003768773 |
| 2026-04-01T23:59:48Z | 7876474 | 0.003793159 |
| 2026-04-02T23:59:48Z | 7883622 | 0.0036804 |
| 2026-04-03T23:59:48Z | 7890794 | 0.003705141 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004020162 |
| 2026-04-05T23:59:48Z | 7905188 | 0.003980974 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004070842 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004144014 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004439043 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003780858 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004154932 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004339949 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004346618 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004598838 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004545115 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004357265 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004342725 |
| 2026-04-17T23:59:48Z | 7991579 | 0.00424128 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004325465 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004814555 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004999118 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004488769 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004348144 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004357293 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004289813 |
| 2026-04-25T23:59:48Z | 8049151 | 0.00452718 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004680418 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004562446 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004319474 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004672087 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004619783 |
| 2026-05-01T23:59:48Z | 8092168 | 0.00477625 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004706712 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004727609 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

