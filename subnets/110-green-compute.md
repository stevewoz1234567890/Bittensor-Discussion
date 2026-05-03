# NetUID 110 — Green Compute (`Ѐ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Green Compute** (NetUID **110**) (`Ѐ`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `97`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ3,751.724634547. **Alpha liquidity in pool (`alpha_in`)** = ‎649,894.658093139Ѐ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,789,686.655813180Ѐ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005761625`** *(also **moving-average price** `0.005773381795734167` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎110,233.265668621Ѐ‎`. **Owner hotkey / coldkey (chain):** `5CCf21ieTFDMkVMs9BHe2Tb6ysVDGVHqbgKjU21CURLPq32d` / `5D53sX6AwAzXUB24G85Ch35hYr5rCpXjYFWpFTe4uzBb75sL`.
- **Subnet registered at block:** `5606062` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎68.456140081Ѐ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002880812` · α-out `‎1.000000000Ѐ‎` · α-in `‎0.500000000Ѐ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104338`
- **Liquidity constant `k`:** `2438225798628529430663073033`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Green Compute`
- **Symbol (API):** `Ѐ`
- **Rank:** `94`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005761703`
- **Market cap:** `10379525923044.146803413`
- **Market cap Δ 1d:** `2.809732844250101254`
- **Liquidity:** `7494882167562`
- **Total τ:** `3751079127157`
- **Total α:** `2439243496657571`
- **α in pool:** `649773693716227`
- **α staked:** `1151694712941344`
- **Price Δ 1h:** `-1.082109686401076238`
- **Price Δ 1d:** `2.231410472286620409`
#### Subnet activity (TAOStats)

- **NetUID (API):** `110`
- **Owner SS58 (API):** `5D53sX6AwAzXUB24G85Ch35hYr5rCpXjYFWpFTe4uzBb75sL`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `5606062`
- **Registration wall time:** `2025-05-20T03:26:00Z`
- **Registration cost snapshot:** `186420726696`
- **Active keys:** `256`
- **Active validators:** `14`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `2880852`
- **Max neurons:** `256`
- **Validator slots (metadata):** `14`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Rent 4090s and 5090s by the hour, run OpenAI-compatible inference, or earn rewards as a miner. Bittensor subnet 110, powered by verified green energy.

**Fetched document title:** Decentralized GPU compute on Bittensor

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
- **Owner SS58 (`owner_ss58`):** `5D53sX6AwAzXUB24G85Ch35hYr5rCpXjYFWpFTe4uzBb75sL`

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
- **`commit_reveal_weights_enabled`:** `False`
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


- **Website:** [https://www.green-compute.com/](https://www.green-compute.com/)
- **Logo URL:** [https://www.green-compute.com/green.png](https://www.green-compute.com/green.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.005761648 |
| 8104292 | 0.005761631 |
| 8104340 | 0.005761576 |
| 8104388 | 0.005761613 |
| 8104436 | 0.005761625 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004367783 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004263551 |
| 2026-03-11T23:59:48Z | 7725455 | 0.00424502 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.00436112 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004283294 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004085905 |
| 2026-03-15T23:59:48Z | 7754226 | 0.003572765 |
| 2026-03-16T23:59:48Z | 7761426 | 0.003835506 |
| 2026-03-17T23:59:48Z | 7768619 | 0.003591766 |
| 2026-03-18T23:59:48Z | 7775819 | 0.003927356 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00361832214215156777 |
| 2026-03-20T23:59:48Z | 7790201 | 0.003753931 |
| 2026-03-21T23:59:48Z | 7797398 | 0.003711958 |
| 2026-03-22T23:59:48Z | 7804598 | 0.003672885 |
| 2026-03-23T23:59:48Z | 7811798 | 0.003791346 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00383898430159971012 |
| 2026-03-25T23:59:48Z | 7826196 | 0.003628577 |
| 2026-03-26T23:59:48Z | 7833396 | 0.003366506 |
| 2026-03-27T23:59:48Z | 7840596 | 0.003420295 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.003470436 |
| 2026-03-29T23:59:48Z | 7854902 | 0.003362466 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.003467889 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003434792 |
| 2026-04-01T23:59:48Z | 7876474 | 0.003437998 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003403758 |
| 2026-04-03T23:59:48Z | 7890794 | 0.003468117 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.003612613 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004088789 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004005189 |
| 2026-04-07T23:59:48Z | 7919588 | 0.003972696 |
| 2026-04-08T23:59:48Z | 7926788 | 0.003939452 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003930419 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004084783 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004174633 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004156627 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004332659 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004758605 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.005174485 |
| 2026-04-16T23:59:48Z | 7984379 | 0.005502801 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004990239 |
| 2026-04-18T23:59:48Z | 7998779 | 0.005196967 |
| 2026-04-19T23:59:48Z | 8005979 | 0.005875537 |
| 2026-04-20T23:59:48Z | 8013179 | 0.005445518 |
| 2026-04-21T23:59:48Z | 8020376 | 0.006247334 |
| 2026-04-22T23:59:48Z | 8027562 | 0.006273696 |
| 2026-04-23T23:59:48Z | 8034762 | 0.006577492 |
| 2026-04-24T23:59:48Z | 8041962 | 0.005986947 |
| 2026-04-25T23:59:48Z | 8049151 | 0.005887603 |
| 2026-04-26T23:59:48Z | 8056274 | 0.006681772 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.005959506 |
| 2026-04-28T23:59:48Z | 8070646 | 0.00565586 |
| 2026-04-29T23:59:48Z | 8077790 | 0.005727632 |
| 2026-04-30T23:59:48Z | 8084984 | 0.005731258 |
| 2026-05-01T23:59:48Z | 8092168 | 0.005624965 |
| 2026-05-02T23:59:48Z | 8099357 | 0.005810064 |
| 2026-05-03T16:10:00Z | 8104202 | 0.005761703 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

