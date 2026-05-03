# NetUID 67 — Harnyx (`ط`)

## Overview

**Harnyx** (NetUID **67**) (`ط`).

Deep research as a commodity.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `195`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ911.669074468. **Alpha liquidity in pool (`alpha_in`)** = ‎80,810.105748888ط‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎272,017.604636276ط‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011281937`** *(also **moving-average price** `0.010195458773523569` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎7,210.044605632ط‎`. **Owner hotkey / coldkey (chain):** `5Cm4fATsr3S1AUX9WTkwaV1qiYtzPVdRpLWSEDmvvEkoT7Rt` / `5HEAv3TU1yNei4GwiTsxfmDCDW9pMCKLeDVky9iaVJfYiVeY`.
- **Subnet registered at block:** `7236936` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎101.718873733ط‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.005640989` · α-out `‎1.000000000ط‎` · α-in `‎0.500000000ط‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.011257247`
- **Market cap:** `2762165544959.355043922`
- **Liquidity:** `1821220818295`
- **Total τ:** `910596079835`
- **Total α:** `352808476577485`
- **α in pool:** `80892312166610`
- **α staked:** `164475453589916`
- **Price Δ 1h:** `-0.728790073908117812`
- **Price Δ 1d:** `17.034905619870608415`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `5628700`
- **Max neurons:** `256`
- **Validators (metadata):** `10`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Deep research as a commodity. Faster, cheaper, traceable research — produced by a competitive swarm of miners on Bittensor SN67.

### Repository README excerpt *(everything before first `##` heading)*

# Harnyx Subnet

**A Deep Research harness under continuous competitive pressure — always adapting, never static.**

Harnyx (SN 67) is a Bittensor subnet for deep research. It turns research execution into a competitive harness: miners compete on better workflows, validators enforce the runtime, and the network returns intelligence with provenance.

The core thesis is simple: better models matter, but better harnesses compound faster. Deep research is not one reasoning step. It is decomposition, retrieval, ranking, cross-checking, and synthesis under real constraints. Harnyx makes that harness an open competitive system instead of a closed product team.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Deep research, native to agents. Harnyx delivers synthesis, comprehensiveness, and full citation at a cost that makes repeated calling viable.

**Fetched document title:** Harnyx — Deep Research API for AI Agents | Bittensor SN67

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
- **Owner SS58 (`owner_ss58`):** `5HEAv3TU1yNei4GwiTsxfmDCDW9pMCKLeDVky9iaVJfYiVeY`

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

#### Sections matched by heading (miner / validator / hardware / requirements)

## Install dependencies (local dev)

```bash
uv sync --all-packages --dev
```

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/harnyx/harnyx/main/README.md`*

## On-chain identity — description


Deep research as a commodity. Faster, cheaper, traceable research — produced by a competitive swarm of miners on Bittensor SN67.

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://harnyx.ai/](https://harnyx.ai/)
- **GitHub:** [https://github.com/harnyx/harnyx](https://github.com/harnyx/harnyx)
- **Discord:** [https://discord.com/channels/799672011265015819/1457737666316472351](https://discord.com/channels/799672011265015819/1457737666316472351)
- **Logo URL:** [https://harnyx.ai/favicon.svg](https://harnyx.ai/favicon.svg)
- **Contact:** harnyx@brightmount.co

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.01128159 |
| 8104072 | 0.011280619 |
| 8104120 | 0.01127938 |
| 8104168 | 0.011232937 |
| 8104216 | 0.011281936 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

