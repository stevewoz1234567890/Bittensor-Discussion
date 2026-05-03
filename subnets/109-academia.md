# NetUID 109 — Academia (`՞`)

## Overview

**Academia** (NetUID **109**) (`՞`).

Academia: where builders become subnet owners.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `237`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,276.191128074. **Alpha liquidity in pool (`alpha_in`)** = ‎201,933.122377267՞‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎812,866.819869836՞‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006318840`** *(also **moving-average price** `0.006166824838146567` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎22,441.597020118՞‎`. **Owner hotkey / coldkey (chain):** `5DyQkk4x6CwDtjtxe1NG2aMgQVXe9ZpZdT14SdYYwEVd3XUk` / `5EZcsP7SqGLNfXujcX6ZRJ3epRQ2yCDXURjr8XcaEY45eZdm`.
- **Subnet registered at block:** `7257480` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎147.542931821՞‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003159416` · α-out `‎1.000000000՞‎` · α-in `‎0.500000000՞‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.006293581`
- **Market cap:** `4331695648721.370937791`
- **Liquidity:** `2546986598515`
- **Total τ:** `1273595072902`
- **Total α:** `1014782070596411`
- **α in pool:** `202331792601679`
- **α staked:** `485940217994732`
- **Price Δ 1h:** `-0.12723754716858372`
- **Price Δ 1d:** `5.213743227271131499`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `14`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `3146787`
- **Max neurons:** `256`
- **Validators (metadata):** `14`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Academia: where builders become subnet owners.

### Repository README excerpt *(everything before first `##` heading)*

# Academia

We're building a Bittensor subnet incubation academy - modeled after La Masia, where promising subnet ideas are developed in-house on mainnet and graduated into dedicated subnets. **Where builders become subnet owners.**

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Academia: where builders become subnet owners. Contribute to fx-integral/academia development by creating an account on GitHub.

**Fetched document title:** GitHub - fx-integral/academia: Academia: where builders become subnet owners · GitHub

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
- **Owner SS58 (`owner_ss58`):** `5EZcsP7SqGLNfXujcX6ZRJ3epRQ2yCDXURjr8XcaEY45eZdm`

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

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/fx-integral/academia/main/README.md`*

## On-chain identity — description


Academia: where builders become subnet owners.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/fx-integral/academia](https://github.com/fx-integral/academia)
- **Discord:** [https://discord.gg/invite/m9J8QTf5JT](https://discord.gg/invite/m9J8QTf5JT)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.006361671 |
| 8104072 | 0.006361883 |
| 8104120 | 0.006362062 |
| 8104168 | 0.006293402 |
| 8104216 | 0.006318839 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.005444255 |
| 2026-03-10T23:59:48Z | 7718257 | 0.00582279 |
| 2026-03-11T23:59:48Z | 7725455 | 0.006325859 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.006260366 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005479152 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005424277 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004997211 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005554659 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005357092 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005340715 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00549599161518261034 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004809065 |
| 2026-03-21T23:59:48Z | 7797398 | 0.005273815 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005291331 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005567665 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00556818991070534814 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005005712 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004653155 |
| 2026-03-27T23:59:48Z | 7840596 | 0.005358103 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.005196593 |
| 2026-03-29T23:59:48Z | 7854902 | 0.005003365 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004789178 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004059036 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004185373 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003841246 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004396687 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004443732 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004220321 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004063718 |
| 2026-04-07T23:59:48Z | 7919588 | 0.00450898 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004538798 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003523778 |
| 2026-04-10T23:59:48Z | 7941184 | 0.003857334 |
| 2026-04-11T23:59:48Z | 7948384 | 0.003849834 |
| 2026-04-12T23:59:48Z | 7955584 | 0.003848416 |
| 2026-04-13T23:59:48Z | 7962784 | 0.003824067 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003861723 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.0037833 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003839551 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004167851 |
| 2026-04-18T23:59:48Z | 7998779 | 0.003819032 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003748993 |
| 2026-04-20T23:59:48Z | 8013179 | 0.003775083 |
| 2026-04-21T23:59:48Z | 8020376 | 0.003745978 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004283187 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004161711 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004155237 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004065936 |
| 2026-04-26T23:59:48Z | 8056274 | 0.005115292 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.005007397 |
| 2026-04-28T23:59:48Z | 8070646 | 0.006067876 |
| 2026-04-29T23:59:48Z | 8077790 | 0.005951418 |
| 2026-04-30T23:59:48Z | 8084984 | 0.005889088 |
| 2026-05-01T23:59:48Z | 8092168 | 0.005614954 |
| 2026-05-02T23:59:48Z | 8099357 | 0.006133129 |
| 2026-05-03T16:10:00Z | 8104202 | 0.006293581 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

