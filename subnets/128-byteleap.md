# NetUID 128 — ByteLeap (`න`)

## Overview

**ByteLeap** (NetUID **128**) (`න`).

Pioneering the Future of Cloud & Blockchain

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `318`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,006.202978404. **Alpha liquidity in pool (`alpha_in`)** = ‎1,207,180.036916299න‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,093,299.882223897න‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003304085`** *(also **moving-average price** `0.0033066037576645613` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎74,002.162723071න‎`. **Owner hotkey / coldkey (chain):** `5FpsgU3JFa8S2GnngH92J9vtHHi4PYgZzxGXnwdFNwEwt9h8` / `5GgMeLFN4YssT6f9i9pZpRmczt8GYDsCZ1nYPiGRcTPWn3AA`.
- **Subnet registered at block:** `5856038` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎231.795104423න‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000න‎` · α-in `‎0.000000000න‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003304118`
- **Market cap:** `10343739933201.364912248`
- **Liquidity:** `7994868267471`
- **Total τ:** `4006223337268`
- **Total α:** `3300404919140196`
- **α in pool:** `1207173875207727`
- **α staked:** `1923386211690309`
- **Price Δ 1h:** `0.048478175888269462`
- **Price Δ 1d:** `-0.147899131221041205`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `13`
- **Active miners:** `41`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Pioneering the Future of Cloud & Blockchain

### Repository README excerpt *(everything before first `##` heading)*

# ByteLeap Miner - Bittensor SN128 Compute Network

ByteLeap Miner is the resource aggregation component of the ByteLeap distributed compute platform. Miners connect to the Bittensor network (SN128), aggregate worker resources, and earn rewards through active compute leases and computational challenges.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to byteleapai/byteleap-Miner development by creating an account on GitHub.

**Fetched document title:** GitHub - byteleapai/byteleap-Miner · GitHub

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
- **Owner SS58 (`owner_ss58`):** `5GgMeLFN4YssT6f9i9pZpRmczt8GYDsCZ1nYPiGRcTPWn3AA`

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

#### Sections matched by heading (miner / validator / hardware / requirements)

# ByteLeap Miner - Bittensor SN128 Compute Network

ByteLeap Miner is the resource aggregation component of the ByteLeap distributed compute platform. Miners connect to the Bittensor network (SN128), aggregate worker resources, and earn rewards through active compute leases and computational challenges.

---

## Scoring System

Miners earn rewards through two main factors:

---

### Prerequisites

- Python 3.8+
- Bittensor wallet with registered hotkey

---

### Installation

```bash

---

# Setup environment

python3 -m venv venv
source ./venv/bin/activate

---

# Install dependencies

pip install -r requirements.txt
```

---

### Running the Miner

**Start Miner** (aggregates workers, communicates with Bittensor):
```bash
python scripts/run_miner.py --config config/miner_config.yaml
```

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/byteleapai/byteleap-Miner/main/README.md`*

## On-chain identity — description


Pioneering the Future of Cloud & Blockchain

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/byteleapai/byteleap-Miner](https://github.com/byteleapai/byteleap-Miner)
- **Discord:** [https://discord.com/channels/799672011265015819/1387438124132733110](https://discord.com/channels/799672011265015819/1387438124132733110)
- **Logo URL:** [https://avatars.githubusercontent.com/u/217718200](https://avatars.githubusercontent.com/u/217718200)
- **Contact:** byteleap.ai@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104133 | 0.003304126 |
| 8104181 | 0.003304121 |
| 8104229 | 0.003304101 |
| 8104277 | 0.003304085 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.003778133 |
| 2026-03-10T23:59:48Z | 7718257 | 0.003729261 |
| 2026-03-11T23:59:48Z | 7725455 | 0.003748368 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.003737538 |
| 2026-03-13T23:59:48Z | 7739841 | 0.003596596 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.003720709 |
| 2026-03-15T23:59:48Z | 7754226 | 0.003554782 |
| 2026-03-16T23:59:48Z | 7761426 | 0.003555709 |
| 2026-03-17T23:59:48Z | 7768619 | 0.003551613 |
| 2026-03-18T23:59:48Z | 7775819 | 0.00357841 |
| 2026-03-19T23:59:48Z | 7783014 | 0.003638763034288994 |
| 2026-03-20T23:59:48Z | 7790201 | 0.00369698 |
| 2026-03-21T23:59:48Z | 7797398 | 0.003644133 |
| 2026-03-22T23:59:48Z | 7804598 | 0.003629737 |
| 2026-03-23T23:59:48Z | 7811798 | 0.003792318 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00361712277628454546 |
| 2026-03-25T23:59:48Z | 7826196 | 0.003579704 |
| 2026-03-26T23:59:48Z | 7833396 | 0.003643616 |
| 2026-03-27T23:59:48Z | 7840596 | 0.00364794 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.00364938 |
| 2026-03-29T23:59:48Z | 7854902 | 0.003578554 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.003630225 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003665121 |
| 2026-04-01T23:59:48Z | 7876474 | 0.003729465 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003987799 |
| 2026-04-03T23:59:48Z | 7890794 | 0.003857525 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.003885666 |
| 2026-04-05T23:59:48Z | 7905188 | 0.003950535 |
| 2026-04-06T23:59:48Z | 7912388 | 0.003948929 |
| 2026-04-07T23:59:48Z | 7919588 | 0.003858658 |
| 2026-04-08T23:59:48Z | 7926788 | 0.003709563 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003480005 |
| 2026-04-10T23:59:48Z | 7941184 | 0.003551686 |
| 2026-04-11T23:59:48Z | 7948384 | 0.003563905 |
| 2026-04-12T23:59:48Z | 7955584 | 0.003516075 |
| 2026-04-13T23:59:48Z | 7962784 | 0.003439112 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003507974 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.00343377 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003379046 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003383817 |
| 2026-04-18T23:59:48Z | 7998779 | 0.003375152 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003375012 |
| 2026-04-20T23:59:48Z | 8013179 | 0.003380131 |
| 2026-04-21T23:59:48Z | 8020376 | 0.003402733 |
| 2026-04-22T23:59:48Z | 8027562 | 0.003328042 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003331278 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003331605 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003402883 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003383164 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.003397319 |
| 2026-04-28T23:59:48Z | 8070646 | 0.003383044 |
| 2026-04-29T23:59:48Z | 8077790 | 0.003296998 |
| 2026-04-30T23:59:48Z | 8084984 | 0.003258766 |
| 2026-05-01T23:59:48Z | 8092168 | 0.003297143 |
| 2026-05-02T23:59:48Z | 8099357 | 0.003310554 |
| 2026-05-03T16:10:00Z | 8104202 | 0.003304118 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

