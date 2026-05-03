# NetUID 7 — Allways (`η`)

## Overview

**Allways** (NetUID **7**) (`η`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `197`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,663.503124306. **Alpha liquidity in pool (`alpha_in`)** = ‎1,602,845.881289076η‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,927,735.131157058η‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004770612`** *(also **moving-average price** `0.004767643520608544` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎293,989.658636504η‎`. **Owner hotkey / coldkey (chain):** `5ChTwrqwqeHpX8rLw73oDWXRjTfz83U4p3kRuKgvEfAEt8EE` / `5CAc19iETJmWD2rYVX1ht58ghCpyHq86MoBNdx5TzLfinzcx`.
- **Subnet registered at block:** `2627691` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎147.629475083η‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002385305` · α-out `‎1.000000000η‎` · α-in `‎0.500000000η‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004770467`
- **Market cap:** `21584064601379.995169273`
- **Liquidity:** `15309468717543`
- **Total τ:** `7663207629417`
- **Total α:** `4530497453722356`
- **α in pool:** `1602832822892747`
- **α staked:** `2921685343018472`
- **Price Δ 1h:** `-0.86018747851661458`
- **Price Δ 1d:** `0.633719416778154537`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `14`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `2385229`
- **Max neurons:** `256`
- **Validators (metadata):** `14`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

universal transaction layer

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Allways

**Fetched document title:** Allways

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
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CAc19iETJmWD2rYVX1ht58ghCpyHq86MoBNdx5TzLfinzcx`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `100`
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

#### Sections matched by heading (miner / validator / hardware / requirements)

### Requirements

- Python 3.10+
- Bittensor wallet
- Docker & Docker Compose

---

### Running with Docker

**Miner:**

```bash
docker compose -f docker-compose.miner.yml up -d
```

**Validator:**

```bash
docker compose -f docker-compose.vali.yml up -d
```

Both require a `.env` file with `PORT` and `WALLET_PATH` configured.

---

# activate the uv virtual environment

source .venv/bin/activate

alw --help
```

---

## Validator Storage Layout

Validator state lives in `~/.allways/validator/state.db` (SQLite, WAL mode).
Tables: `pending_confirms`, `rate_events`, `swap_outcomes`. Collateral /
active / min_collateral state is held in memory and rebuilt from contract
events each startup; only `swap_outcomes` (the all-time credibility ledger)
needs to persist across restarts.

---

## Miner Environment Variables

- `MINER_TIMEOUT_CUSHION_BLOCKS` — defaults to 5. Miner skips fulfilling a
  swap when fewer than this many blocks remain before its timeout, trading
  a skipped swap for avoided slashes on slow dest-chain inclusion.
- `BTC_MODE`, `BTC_PRIVATE_KEY`, `BTC_RPC_URL`, etc. — see `.env.example`.

---

## Running a Local Subtensor Lite Node (Validators)

Validators read miner rate commitments every ~3 minutes AND stream contract
events every block via the same connection. Pointing at the public `finney`
entrypoint works but adds latency and RPC pressure — every validator on the
network should run its own lite node for this.

```bash

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/entrius/allways/main/README.md`*

## On-chain identity — description


universal transaction layer

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://all-ways.io/](https://all-ways.io/)
- **GitHub:** [https://github.com/entrius/allways](https://github.com/entrius/allways)
- **Logo URL:** [https://allways-905418005698-us-east-2-an.s3.us-east-2.amazonaws.com/sn7-light.png](https://allways-905418005698-us-east-2-an.s3.us-east-2.amazonaws.com/sn7-light.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104037 | 0.00478087 |
| 8104085 | 0.004782564 |
| 8104133 | 0.004775711 |
| 8104181 | 0.004770421 |
| 8104229 | 0.004770515 |
| 8104277 | 0.004770612 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004584992 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004639462 |
| 2026-03-11T23:59:48Z | 7725455 | 0.004464817 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.004498171 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004393975 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.004331319 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004173215 |
| 2026-03-16T23:59:48Z | 7761426 | 0.004320136 |
| 2026-03-17T23:59:48Z | 7768619 | 0.004312839 |
| 2026-03-18T23:59:48Z | 7775819 | 0.004356456 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00493785483230372574 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005135276 |
| 2026-03-21T23:59:48Z | 7797398 | 0.004913637 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005492205 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005438019 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00513665757244976028 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005507247 |
| 2026-03-26T23:59:48Z | 7833396 | 0.003413467 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004033165 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.003898689 |
| 2026-03-29T23:59:48Z | 7854902 | 0.003851622 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.003845445 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003657604 |
| 2026-04-01T23:59:48Z | 7876474 | 0.003664139 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003664755 |
| 2026-04-03T23:59:48Z | 7890794 | 0.003584566 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.003689736 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004111119 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004126469 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004159406 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004237201 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003975081 |
| 2026-04-10T23:59:48Z | 7941184 | 0.00402502 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004029786 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004002474 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004048478 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004264502 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004220131 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004167967 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004259737 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004293664 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004295713 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004754108 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004941212 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004475155 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004435877 |
| 2026-04-24T23:59:48Z | 8041962 | 0.00451305 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004279627 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004271563 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004469391 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004362826 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004358496 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004327329 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004556317 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004807702 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004770467 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

