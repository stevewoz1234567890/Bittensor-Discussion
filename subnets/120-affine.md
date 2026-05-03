# NetUID 120 — Affine (`ⴷ`)

## Overview

**Affine** (NetUID **120**) (`ⴷ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `310`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ84,499.440983625. **Alpha liquidity in pool (`alpha_in`)** = ‎1,254,413.172941338ⲃ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,941,680.461286908ⲃ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.067100438`** *(also **moving-average price** `0.06717778113670647` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎958,574.735972357ⲃ‎`. **Owner hotkey / coldkey (chain):** `5Fn7rj78bfSrNcFQCHShC7aoVSneGLbiPD7xFHu3zhwFrQhs` / `5Fc3ZZQAYB3SPXKcFnd1WJeyQvArSZZeB6LU1rb7zvQ6XvDh`.
- **Subnet registered at block:** `5749344` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎225.251582290ⲃ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ⲃ‎` · α-in `‎0.000000000ⲃ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.067101102`
- **Market cap:** `204312276156669.302747358`
- **Liquidity:** `168671947249165`
- **Total τ:** `84499861658075`
- **Total α:** `3196018634228246`
- **α in pool:** `1254406903646541`
- **α staked:** `1790435432276188`
- **Price Δ 1h:** `0.099866997656135215`
- **Price Δ 1d:** `0.468473353615653492`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Reason Mining

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Affine: Reason Mining

**Fetched document title:** Affine

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
- **Owner SS58 (`owner_ss58`):** `5Fc3ZZQAYB3SPXKcFnd1WJeyQvArSZZeB6LU1rb7zvQ6XvDh`

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

## Installation

```bash

---

# Install uv package manager

curl -LsSf https://astral.sh/uv/install.sh | sh

---

# Clone and install Affine

git clone https://github.com/AffineFoundation/affine.git
cd affine
uv venv && source .venv/bin/activate && uv pip install -e .

---

# Verify installation

af
```

---

### For Miners

📖 **[Complete Miner Guide →](docs/MINER.md)**

Learn how to:
- Set up your environment and configure API keys
- Pull models from the network
- Improve models with reinforcement learning
- Deploy to Chutes and commit on-chain
- Use CLI commands to query your mining status

---

### For Validators

📖 **[Complete Validator Guide →](docs/VALIDATOR.md)**

Learn how to:
- Set up and configure your validator
- Run with Docker (recommended) or locally
- Monitor validator performance
- Troubleshoot common issues
- Set weights on-chain

---

### Additional Resources

- 📚 **[FAQ](docs/FAQ.md)** - Frequently asked questions

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/AffineFoundation/affine/main/README.md`*

## On-chain identity — description


Reason Mining

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.affine.io](https://www.affine.io)
- **GitHub:** [https://github.com/AffineFoundation/affine](https://github.com/AffineFoundation/affine)
- **Discord (handle / invite hint):** `consttt`
- **Logo URL:** [https://raw.githubusercontent.com/AffineFoundation/affine/main/affine.png](https://raw.githubusercontent.com/AffineFoundation/affine/main/affine.png)
- **Contact:** hello@affine.io

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.067083834 |
| 8104133 | 0.067101256 |
| 8104181 | 0.067101157 |
| 8104229 | 0.067100773 |
| 8104277 | 0.067100438 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

