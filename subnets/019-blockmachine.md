# NetUID 19 — blockmachine (`t`)

## Overview

**blockmachine** (NetUID **19**) (`t`).

Harnessing Bittensor's incentive layer to forge self-optimizing infrastructure.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `147`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ37,644.040219984. **Alpha liquidity in pool (`alpha_in`)** = ‎2,664,835.686191816t‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,287,617.366524083t‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.014128891`** *(also **moving-average price** `0.014199528377503157` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,594,134.594053425t‎`. **Owner hotkey / coldkey (chain):** `5CK49hDJcseEk1V7iB1dmmztdw4igafhxLsVN82VtUVAQRfC` / `5FWh37LfVV5LE9dZA91STzbtebh6vxYa3MH71c621sYafo1L`.
- **Subnet registered at block:** `1956072` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎110.903097011t‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000t‎` · α-in `‎0.000000000t‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.014128891`
- **Market cap:** `59894670470417.628066886`
- **Liquidity:** `75295213163090`
- **Total τ:** `37644040965839`
- **Total α:** `4952440052715899`
- **α in pool:** `2664835633401922`
- **α staked:** `1574327261295024`
- **Price Δ 1h:** `-0.010148386537464637`
- **Price Δ 1d:** `-1.335345514707494647`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `10`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `100000000`

### On-chain declared purpose *(SubnetIdentity)*

Harnessing Bittensor's incentive layer to forge self-optimizing infrastructure.

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to taostat/blockmachine development by creating an account on GitHub.

**Fetched document title:** GitHub - taostat/blockmachine · GitHub

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
- **`immunity_period` (blocks):** 3600
- **Registration recycle cost snapshot (`burn`):** τ0.100000000
- **Owner SS58 (`owner_ss58`):** `5FWh37LfVV5LE9dZA91STzbtebh6vxYa3MH71c621sYafo1L`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.100000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `3600` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `360` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `True` / `0`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Miners

https://github.com/taostat/blockmachine-miner

---

## Validators

https://github.com/taostat/blockmachine-validator

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/taostat/blockmachine/main/README.md`*

## On-chain identity — description


Harnessing Bittensor's incentive layer to forge self-optimizing infrastructure.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/taostat/blockmachine/](https://github.com/taostat/blockmachine/)
- **Logo URL:** [https://blockmachine.io/logo.svg](https://blockmachine.io/logo.svg)
- **Contact:** team@blockmachine.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8103976 | 0.014130315 |
| 8104024 | 0.014130311 |
| 8104072 | 0.014128916 |
| 8104120 | 0.014128905 |
| 8104168 | 0.014128897 |
| 8104216 | 0.014128891 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

