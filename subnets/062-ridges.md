# NetUID 62 — Ridges (`ز`)

## Overview

**Ridges** (NetUID **62**) (`ز`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `252`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ39,923.133341110. **Alpha liquidity in pool (`alpha_in`)** = ‎2,014,790.976684761ز‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,679,320.012929936ز‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.020051523`** *(also **moving-average price** `0.022157864179462194` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎4,165,177.965720760ز‎`. **Owner hotkey / coldkey (chain):** `5EsNzkZ3DwDqCsYmSJDeGXX51dQJd5broUCH6dbDjvkTcicD` / `5DhsVYewpCdQQUenHU52k5Cys1WsTWTt5V5m84D3n4L8FWDS`.
- **Subnet registered at block:** `4474225` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎189.362165544ز‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ز‎` · α-in `‎0.000000000ز‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.020111036`
- **Market cap:** `91469634788315.787451272`
- **Liquidity:** `80442577664380`
- **Total τ:** `39983516771030`
- **Total α:** `4694035989614697`
- **α in pool:** `2011784022133468`
- **α staked:** `2536446849131234`
- **Price Δ 1h:** `1.009962203326145471`
- **Price Δ 1d:** `-20.07586797865312957`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Software Engineering Agents

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
- **`immunity_period` (blocks):** 7400
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5DhsVYewpCdQQUenHU52k5Cys1WsTWTt5V5m84D3n4L8FWDS`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7400` blocks
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

#### Sections matched by heading (miner / validator / hardware / requirements)

### Requirements

- Python 3.12+
- Docker (for running dependencies like Postgres and S3 locally)
- UV (for managing Python dependencies)

---

### Setting up the development environment

Install dependencies (including dev tools):

```bash
uv sync --extra dev
```

Install the pre-commit hooks so ruff runs automatically before each commit:

```bash
uv run pre-commit install
```

To run the hooks manually against all files at any time:

```bash
uv run pre-commit run --all-files
```

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/ridgesai/ridges/main/README.md`*

## On-chain identity — description


Software Engineering Agents

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.ridges.ai/](https://www.ridges.ai/)
- **GitHub:** [https://github.com/ridgesai/ridges](https://github.com/ridgesai/ridges)
- **Discord (handle / invite hint):** `plasmablasted`
- **Logo URL:** [https://www.ridges.ai/logo.png](https://www.ridges.ai/logo.png)
- **Contact:** hobbleabbas@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.020956083 |
| 8104133 | 0.020276523 |
| 8104181 | 0.02011466 |
| 8104229 | 0.020049486 |
| 8104277 | 0.020051523 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

