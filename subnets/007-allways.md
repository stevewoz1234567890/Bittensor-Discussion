# NetUID 7 — Allways (`η`)

## Overview

**Allways** (NetUID **7**) (`η`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `135`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,663.262359208. **Alpha liquidity in pool (`alpha_in`)** = ‎1,602,834.350301281η‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,927,677.571399249η‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004770499`** *(also **moving-average price** `0.004767600214108825` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎293,989.523393838η‎`. **Owner hotkey / coldkey (chain):** `5ChTwrqwqeHpX8rLw73oDWXRjTfz83U4p3kRuKgvEfAEt8EE` / `5CAc19iETJmWD2rYVX1ht58ghCpyHq86MoBNdx5TzLfinzcx`.
- **Subnet registered at block:** `2627691` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎101.167415069η‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002385247` · α-out `‎1.000000000η‎` · α-in `‎0.500000000η‎`.

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
| 8103976 | 0.004794129 |
| 8104024 | 0.004790584 |
| 8104072 | 0.00478204 |
| 8104120 | 0.004782643 |
| 8104168 | 0.004770393 |
| 8104216 | 0.004770499 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

