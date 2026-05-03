# NetUID 47 — EvolAI (`צ`)

## Overview

**EvolAI** (NetUID **47**) (`צ`).

A subnet focused on the research, development, and evaluation of evolving AI systems

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `237`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,054.038973655. **Alpha liquidity in pool (`alpha_in`)** = ‎194,713.281266936צ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎709,345.010705084צ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005413042`** *(also **moving-average price** `0.005127015057951212` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎12,140.141883315צ‎`. **Owner hotkey / coldkey (chain):** `5GjN9n3ndtbRTir5HCRsaaFjxfoQpffnYsAc5VG9iWMfdEWj` / `5DDKR8DVDQ4UaAprFR5gfc6WXFgk3cG6WmBpdKZ8Eah4Z6Mu`.
- **Subnet registered at block:** `7340355` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎144.735853509צ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002706544` · α-out `‎1.000000000צ‎` · α-in `‎0.500000000צ‎`.

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
| 8104085 | 0.005413591 |
| 8104133 | 0.005413551 |
| 8104181 | 0.005413602 |
| 8104229 | 0.005413272 |
| 8104277 | 0.005413042 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

