# NetUID 117 — Unknown (`Ⲁ`)

## Overview

**Unknown** (NetUID **117**) (`Ⲁ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `307`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,110.418336419. **Alpha liquidity in pool (`alpha_in`)** = ‎750,550.732477299Ⲁ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,261,819.253428423Ⲁ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004144017`** *(also **moving-average price** `0.004074668977409601` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎96,875.064610944Ⲁ‎`. **Owner hotkey / coldkey (chain):** `5CyXUidjedyVBR2UsuafJ128DMhWsxzaAxB1Zi7Uyf7jjKVG` / `5D9j5tWvXahPCbHnkhNAhB6Dg4cgGFuDiz4KNHBBxPRTSAYX`.
- **Subnet registered at block:** `5710859` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎211.585998394Ⲁ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002072007` · α-out `‎1.000000000Ⲁ‎` · α-in `‎0.500000000Ⲁ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004160487`
- **Market cap:** `7232177306298.767133318`
- **Liquidity:** `6232750953798`
- **Total τ:** `3116465219579`
- **Total α:** `2012271968567872`
- **α in pool:** `749019461956985`
- **α staked:** `989281200032529`
- **Price Δ 1h:** `-0.111784877494002007`
- **Price Δ 1d:** `2.971187777166732914`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `70`
- **Active validators:** `1`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `2080241`
- **Max neurons:** `256`
- **Validators (metadata):** `1`
- **Neuron reg. cost:** `10000000`

### On-chain declared purpose *(SubnetIdentity)*

~

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <img src="voibes.jpeg" alt="voibes">
</p>

# Chi: A Vibe-Codable Bittensor Subnet Template.

1. Clone this repo into Cursor
2. Ask your agent: "How do I make: [your subnet idea]? @knowledge"

Made by Const <3

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Vibe-codable Bittensor Subnet Template. Contribute to helionlink/Chi development by creating an account on GitHub.

**Fetched document title:** GitHub - helionlink/Chi: Vibe-codable Bittensor Subnet Template · GitHub

### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 70
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 21600
- **Registration recycle cost snapshot (`burn`):** τ0.010000000
- **Owner SS58 (`owner_ss58`):** `5D9j5tWvXahPCbHnkhNAhB6Dg4cgGFuDiz4KNHBBxPRTSAYX`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.010000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `21600` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `720` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `True`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `52429`, `3277`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/helionlink/Chi/main/README.md`*

## On-chain identity — description


~

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/helionlink/Chi](https://github.com/helionlink/Chi)
- **Discord (handle / invite hint):** `~`
- **Logo:** `~`
- **Contact:** hello@helionlink.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.00414198 |
| 8104133 | 0.004160366 |
| 8104181 | 0.004160454 |
| 8104229 | 0.00414398 |
| 8104277 | 0.004144017 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004178445 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004229601 |
| 2026-03-11T23:59:48Z | 7725455 | 0.004351688 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.004421962 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004144207 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004112438 |
| 2026-03-15T23:59:48Z | 7754226 | 0.003966145 |
| 2026-03-16T23:59:48Z | 7761426 | 0.004051597 |
| 2026-03-17T23:59:48Z | 7768619 | 0.003949432 |
| 2026-03-18T23:59:48Z | 7775819 | 0.003991039 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00393684275187659097 |
| 2026-03-20T23:59:48Z | 7790201 | 0.003851095 |
| 2026-03-21T23:59:48Z | 7797398 | 0.003824928 |
| 2026-03-22T23:59:48Z | 7804598 | 0.00385888 |
| 2026-03-23T23:59:48Z | 7811798 | 0.003819704 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00369899004525199093 |
| 2026-03-25T23:59:48Z | 7826196 | 0.003680661 |
| 2026-03-26T23:59:48Z | 7833396 | 0.003520132 |
| 2026-03-27T23:59:48Z | 7840596 | 0.00349776 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.003540677 |
| 2026-03-29T23:59:48Z | 7854902 | 0.003574047 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.003594268 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003638486 |
| 2026-04-01T23:59:48Z | 7876474 | 0.003628413 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003526194 |
| 2026-04-03T23:59:48Z | 7890794 | 0.003518142 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.00354014 |
| 2026-04-05T23:59:48Z | 7905188 | 0.003568476 |
| 2026-04-06T23:59:48Z | 7912388 | 0.003565718 |
| 2026-04-07T23:59:48Z | 7919588 | 0.003637812 |
| 2026-04-08T23:59:48Z | 7926788 | 0.003653332 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003481502 |
| 2026-04-10T23:59:48Z | 7941184 | 0.003545223 |
| 2026-04-11T23:59:48Z | 7948384 | 0.003478696 |
| 2026-04-12T23:59:48Z | 7955584 | 0.003431696 |
| 2026-04-13T23:59:48Z | 7962784 | 0.003425961 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003468969 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.003448259 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003398468 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003369407 |
| 2026-04-18T23:59:48Z | 7998779 | 0.003395812 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003362554 |
| 2026-04-20T23:59:48Z | 8013179 | 0.003333926 |
| 2026-04-21T23:59:48Z | 8020376 | 0.003309941 |
| 2026-04-22T23:59:48Z | 8027562 | 0.003191397 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003132148 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003273293 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003313235 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003431829 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.003490544 |
| 2026-04-28T23:59:48Z | 8070646 | 0.003506214 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004104141 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004018547 |
| 2026-05-01T23:59:48Z | 8092168 | 0.003972518 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004035145 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004160487 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

