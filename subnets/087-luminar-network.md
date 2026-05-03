# NetUID 87 — Luminar Network (`Ы`)

## Overview

**Luminar Network** (NetUID **87**) (`Ы`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `215`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,187.580813536. **Alpha liquidity in pool (`alpha_in`)** = ‎230,878.709850886Ы‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎852,684.530250103Ы‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005144822`** *(also **moving-average price** `0.004713969537988305` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎17,277.874386037Ы‎`. **Owner hotkey / coldkey (chain):** `5Do9743TzawQr4TKapjkxEnvNeaZC6Ldk1GephdJai7cQsN5` / `5GquyFXCVX4dAB1GFNSfZemYZm43H8KWa1BSTjV9UKeSYt2x`.
- **Subnet registered at block:** `7208725` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎135.288173500Ы‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002572407` · α-out `‎1.000000000Ы‎` · α-in `‎0.500000000Ы‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005144742`
- **Market cap:** `3794999837658.419150406`
- **Liquidity:** `2375325327052`
- **Total τ:** `1187538285252`
- **Total α:** `1083545657735793`
- **α in pool:** `230873976148888`
- **α staked:** `506772311586905`
- **Price Δ 1h:** `0.198615495358497269`
- **Price Δ 1d:** `16.865450114690621537`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `2572366`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `1000000`

### On-chain declared purpose *(SubnetIdentity)*

Video Surveillance Agents

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Intelligent Video Infrastructure Built with AI Systems

**Fetched document title:** Luminar Network | Intelligent Video Infrastructure

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
- **Registration recycle cost snapshot (`burn`):** τ0.001000000
- **Owner SS58 (`owner_ss58`):** `5GquyFXCVX4dAB1GFNSfZemYZm43H8KWa1BSTjV9UKeSYt2x`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.001000000 / τ100.000000000
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


Video Surveillance Agents

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://luminar.network/](https://luminar.network/)
- **Discord:** [https://x.com/LuminarNetwork](https://x.com/LuminarNetwork)
- **Logo URL:** [https://i.ibb.co/8nXxKTVf/5-Mc-VFISU-400x400-1-modified.png](https://i.ibb.co/8nXxKTVf/5-Mc-VFISU-400x400-1-modified.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.005138672 |
| 8104072 | 0.005138865 |
| 8104120 | 0.005139037 |
| 8104168 | 0.005144575 |
| 8104216 | 0.005144822 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

