# NetUID 62 — Ridges (`ز`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Ridges** (NetUID **62**) (`ز`).

Software Engineering Agents

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `49`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ40,758.365070172. **Alpha liquidity in pool (`alpha_in`)** = ‎1,973,973.925941923ز‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,720,147.052846762ز‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.020882541`** *(also **moving-average price** `0.022098089335486293` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎4,169,711.862428218ز‎`. **Owner hotkey / coldkey (chain):** `5EsNzkZ3DwDqCsYmSJDeGXX51dQJd5broUCH6dbDjvkTcicD` / `5DhsVYewpCdQQUenHU52k5Cys1WsTWTt5V5m84D3n4L8FWDS`.
- **Subnet registered at block:** `4474225` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎36.820611657ز‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ز‎` · α-in `‎0.000000000ز‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104386`
- **Liquidity constant `k`:** `80455949912541564767091620756`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Ridges`
- **Symbol (API):** `ز`
- **Rank:** `11`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.020111036`
- **Market cap:** `91469634788315.787451272`
- **Market cap Δ 1d:** `-20.001294545732862069`
- **Liquidity:** `80442577664380`
- **Total τ:** `39983516771030`
- **Total α:** `4694035989614697`
- **α in pool:** `2011784022133468`
- **α staked:** `2536446849131234`
- **Price Δ 1h:** `1.009962203326145471`
- **Price Δ 1d:** `-20.07586797865312957`
#### Subnet activity (TAOStats)

- **NetUID (API):** `62`
- **Owner SS58 (API):** `5DhsVYewpCdQQUenHU52k5Cys1WsTWTt5V5m84D3n4L8FWDS`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `4474225`
- **Registration wall time:** `2024-12-13T18:33:36Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `13`
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

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


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
| 8104244 | 0.020048762 |
| 8104292 | 0.020270114 |
| 8104340 | 0.021049435 |
| 8104388 | 0.021016627 |
| 8104436 | 0.020902636 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

