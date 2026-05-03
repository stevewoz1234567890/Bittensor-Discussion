# NetUID 31 — Halftime (`ז`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Halftime** (NetUID **31**) (`ז`).

Halftime is a Bittensor subnet for decentralized multimodal intelligence project, focused on context-aware analysis for media and advertising. Planned go-live Q2 2026.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `18`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,346.450713051. **Alpha liquidity in pool (`alpha_in`)** = ‎254,430.485791418ז‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎882,338.479325180ז‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005291980`** *(also **moving-average price** `0.005303265061229467` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎15,154.803591541ז‎`. **Owner hotkey / coldkey (chain):** `5CDZ527X1CiStK1ViGkbC4EjVoouwiGW4ijRKRFfrLpQfftn` / `5H3mfhC8DS853nezGzh73rRnrFqPaPXtaCR8jDtgkSCHrfvb`.
- **Subnet registered at block:** `7173591` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎11.414599362ז‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002645988` · α-out `‎1.000000000ז‎` · α-in `‎0.500000000ז‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104417`
- **Liquidity constant `k`:** `342578109015767090156396318`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Halftime`
- **Symbol (API):** `ז`
- **Rank:** `116`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005292443`
- **Market cap:** `4105523999389.630005786`
- **Market cap Δ 1d:** `1.23200111394651236`
- **Liquidity:** `2691776457586`
- **Total τ:** `1345893157019`
- **Total α:** `1136433618216302`
- **α in pool:** `254302842858584`
- **α staked:** `521430405357718`
- **Price Δ 1h:** `0.003835804876574003`
- **Price Δ 1d:** `0.294281847306967671`
#### Subnet activity (TAOStats)

- **NetUID (API):** `31`
- **Owner SS58 (API):** `5H3mfhC8DS853nezGzh73rRnrFqPaPXtaCR8jDtgkSCHrfvb`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `7173591`
- **Registration wall time:** `2025-12-25T05:41:12Z`
- **Registration cost snapshot:** `273045257585`
- **Active keys:** `256`
- **Active validators:** `16`
- **Active miners:** `1`
- **Active dual-role:** `1`
- **Emission:** `2646223`
- **Max neurons:** `256`
- **Validator slots (metadata):** `16`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

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
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5H3mfhC8DS853nezGzh73rRnrFqPaPXtaCR8jDtgkSCHrfvb`

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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Logo URL:** [https://x.ai/images/noise.png](https://x.ai/images/noise.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.005292449 |
| 8104244 | 0.005292212 |
| 8104292 | 0.005292118 |
| 8104340 | 0.005291869 |
| 8104388 | 0.005291967 |
| 8104436 | 0.005291982 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.005143391 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005304719 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005735686 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005597351 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005249017 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005250816 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005144509 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005474855 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005376101 |
| 2026-03-18T23:59:48Z | 7775819 | 0.00518946 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00533498195448066731 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005216601 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005036575 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005299215 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005063551 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00504905514878476208 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004697761 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004156091 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004528585 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004451356 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004563102 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004387419 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004234961 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004262821 |
| 2026-04-02T23:59:48Z | 7883622 | 0.00406474 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004239836 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004521854 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004371702 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004310359 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004335929 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004185214 |
| 2026-04-09T23:59:48Z | 7933987 | 0.00388066 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004176992 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004308673 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004134655 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004193777 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004306787 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004036037 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004510557 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004460028 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004591604 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004296656 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004415847 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004490074 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004850907 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004774247 |
| 2026-04-24T23:59:48Z | 8041962 | 0.00473774 |
| 2026-04-25T23:59:48Z | 8049151 | 0.00478553 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004958651 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004971644 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004988296 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004940245 |
| 2026-04-30T23:59:48Z | 8084984 | 0.005210063 |
| 2026-05-01T23:59:48Z | 8092168 | 0.005266849 |
| 2026-05-02T23:59:48Z | 8099357 | 0.005314896 |
| 2026-05-03T16:10:00Z | 8104202 | 0.005292443 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

