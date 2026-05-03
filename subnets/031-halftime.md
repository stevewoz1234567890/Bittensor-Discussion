# NetUID 31 — Halftime (`ז`)

## Overview

**Halftime** (NetUID **31**) (`ז`).

Halftime is a Bittensor subnet for decentralized multimodal intelligence project, focused on context-aware analysis for media and advertising.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `159`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,345.931016426. **Alpha liquidity in pool (`alpha_in`)** = ‎254,308.689394338ז‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎882,143.616728173ז‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005292469`** *(also **moving-average price** `0.005303943995386362` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎15,154.599959899ז‎`. **Owner hotkey / coldkey (chain):** `5CDZ527X1CiStK1ViGkbC4EjVoouwiGW4ijRKRFfrLpQfftn` / `5H3mfhC8DS853nezGzh73rRnrFqPaPXtaCR8jDtgkSCHrfvb`.
- **Subnet registered at block:** `7173591` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎100.822314180ז‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002646234` · α-out `‎1.000000000ז‎` · α-in `‎0.500000000ז‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005292443`
- **Market cap:** `4105523999389.630005786`
- **Liquidity:** `2691776457586`
- **Total τ:** `1345893157019`
- **Total α:** `1136433618216302`
- **α in pool:** `254302842858584`
- **α staked:** `521430405357718`
- **Price Δ 1h:** `0.003835804876574003`
- **Price Δ 1d:** `0.294281847306967671`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `16`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `2646223`
- **Max neurons:** `256`
- **Validators (metadata):** `16`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Halftime is a Bittensor subnet for decentralized multimodal intelligence project, focused on context-aware analysis for media and advertising. Planned go-live Q2 2026.

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

## On-chain identity — description


Halftime is a Bittensor subnet for decentralized multimodal intelligence project, focused on context-aware analysis for media and advertising. Planned go-live Q2 2026.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Logo URL:** [https://x.ai/images/noise.png](https://x.ai/images/noise.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8103976 | 0.005292308 |
| 8104024 | 0.005292361 |
| 8104072 | 0.005292384 |
| 8104120 | 0.005292385 |
| 8104168 | 0.005292412 |
| 8104216 | 0.005292469 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

