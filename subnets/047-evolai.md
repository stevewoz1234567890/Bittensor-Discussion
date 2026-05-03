# NetUID 47 — EvolAI (`צ`)

## Overview

**EvolAI** (NetUID **47**) (`צ`).

A subnet focused on the research, development, and evaluation of evolving AI systems

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `175`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,053.930048038. **Alpha liquidity in pool (`alpha_in`)** = ‎194,671.403383208צ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎709,297.997047422צ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005413643`** *(also **moving-average price** `0.00512284878641367` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎12,140.038517233צ‎`. **Owner hotkey / coldkey (chain):** `5GjN9n3ndtbRTir5HCRsaaFjxfoQpffnYsAc5VG9iWMfdEWj` / `5DDKR8DVDQ4UaAprFR5gfc6WXFgk3cG6WmBpdKZ8Eah4Z6Mu`.
- **Subnet registered at block:** `7340355` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎106.871744693צ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002706822` · α-out `‎1.000000000צ‎` · α-in `‎0.500000000צ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005413609`
- **Market cap:** `3313045404257.663278468`
- **Liquidity:** `2107734532381`
- **Total τ:** `1053891178401`
- **Total α:** `903950773306331`
- **α in pool:** `194665583343812`
- **α staked:** `417319028817440`
- **Price Δ 1h:** `-0.080288536698044411`
- **Price Δ 1d:** `7.386307395769340403`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `60`
- **Active validators:** `13`
- **Active miners:** `23`
- **Active dual:** `0`
- **Emission:** `2706808`
- **Max neurons:** `256`
- **Validators (metadata):** `13`
- **Neuron reg. cost:** `50000000`

### On-chain declared purpose *(SubnetIdentity)*

A subnet focused on the research, development, and evaluation of evolving AI systems

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to openevolai/evolai development by creating an account on GitHub.

**Fetched document title:** GitHub - openevolai/evolai · GitHub

## Operational parameters — registration, limits, economics (chain)


### Topology & economics (`SubnetInfo` snapshot)

- **`max_n` (max registered UIDs):** 256
- **`subnetwork_n`:** 60
- **Max validators allowed (`max_allowed_validators`):** 64
- **Min weights per neuron (`min_allowed_weights`):** 1
- **`max_weights_limit` (consensus-encoded cap):** 65535
- **`tempo` (blocks between epoch advances):** 360
- **`scaling_law_power`:** 50
- **`modality` ID:** `0`
- **`emission_value` (display field):** 0
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.050000000
- **Owner SS58 (`owner_ss58`):** `5DDKR8DVDQ4UaAprFR5gfc6WXFgk3cG6WmBpdKZ8Eah4Z6Mu`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.050000000 / τ100.000000000
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

## Installation

Install [uv](https://github.com/astral-sh/uv), then:

```bash
git clone https://github.com/evolai-subnet/evolai.git
uv pip install -e .
```

Or with pip:

```bash
pip install -e .
```

Verify:

```bash
evolcli --help
```

---

## Mining

Requirements:

- Model name must contain `evolai`
- Model must be public on HuggingFace
- Supported tracks: `transformer`, `mamba2`

Check eligibility:

```bash
evolcli miner check --model username/evolai-0.4b --track transformer
evolcli miner check --model username/evolai-mamba2-0.4b --track mamba2
```

Get your challenge:

```bash
evolcli miner get-challenge <validator-uid>
```

Register your model:

```bash
evolcli miner register --wallet-name miner1 --hotkey my-hotkey --track transformer
evolcli miner register --wallet-name miner1 --hotkey my-hotkey --track mamba2
```

Re-register after you publish a new model version.

---

#### CPU / GPU / RAM lines (automatic grep)

- A GPU 80 GB is required to run validator evaluations.


*Primary README URL used: `https://raw.githubusercontent.com/openevolai/evolai/main/README.md`*

## On-chain identity — description


A subnet focused on the research, development, and evaluation of evolving AI systems

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/openevolai/evolai.git](https://github.com/openevolai/evolai.git)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.005414648 |
| 8104072 | 0.005413565 |
| 8104120 | 0.005413549 |
| 8104168 | 0.005413574 |
| 8104216 | 0.005413643 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.006394427 |
| 2026-03-10T23:59:48Z | 7718257 | 0.006357688 |
| 2026-03-11T23:59:48Z | 7725455 | 0.007165034 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.006358142 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005050114 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005993796 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005596769 |
| 2026-03-16T23:59:48Z | 7761426 | 0.006155368 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005781696 |
| 2026-03-18T23:59:48Z | 7775819 | 0.005567737 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00559987189491214786 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004664243 |
| 2026-03-21T23:59:48Z | 7797398 | 0.00508443 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005499717 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005236733 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00523985301704723376 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005011728 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004547474 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004768256 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004899643 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004788779 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004615324 |
| 2026-03-31T23:59:48Z | 7869291 | 0.00445047 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004339323 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004312433 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004775648 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004785473 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004861369 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004890095 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004530277 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004638877 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004087359 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004424665 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004371538 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004194216 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004232045 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004744104 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004471427 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004605288 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004751828 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004720308 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004425966 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004487512 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004361721 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004450767 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004634645 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004885585 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004893674 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004947584 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.005076577 |
| 2026-04-28T23:59:48Z | 8070646 | 0.005017478 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004804881 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004950865 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004904557 |
| 2026-05-02T23:59:48Z | 8099357 | 0.00496418 |
| 2026-05-03T16:10:00Z | 8104202 | 0.005413609 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

