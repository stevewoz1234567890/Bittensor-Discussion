# NetUID 120 — Affine (`ⴷ`)

## Overview

**Affine** (NetUID **120**) (`ⴷ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `248`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ84,499.856559737. **Alpha liquidity in pool (`alpha_in`)** = ‎1,254,406.979626642ⲃ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,941,624.654601604ⲃ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.067101088`** *(also **moving-average price** `0.06717911059968174` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎958,574.320396245ⲃ‎`. **Owner hotkey / coldkey (chain):** `5Fn7rj78bfSrNcFQCHShC7aoVSneGLbiPD7xFHu3zhwFrQhs` / `5Fc3ZZQAYB3SPXKcFnd1WJeyQvArSZZeB6LU1rb7zvQ6XvDh`.
- **Subnet registered at block:** `5749344` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎180.201224319ⲃ‎`; pending root emission `τ0.000000000`.
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
| 8104024 | 0.067068378 |
| 8104072 | 0.067068256 |
| 8104120 | 0.067088376 |
| 8104168 | 0.067101189 |
| 8104216 | 0.067101088 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.081091598 |
| 2026-03-10T23:59:48Z | 7718257 | 0.080957445 |
| 2026-03-11T23:59:48Z | 7725455 | 0.079465589 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.079843437 |
| 2026-03-13T23:59:48Z | 7739841 | 0.082226237 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.078840973 |
| 2026-03-15T23:59:48Z | 7754226 | 0.077660935 |
| 2026-03-16T23:59:48Z | 7761426 | 0.078815898 |
| 2026-03-17T23:59:48Z | 7768619 | 0.077683399 |
| 2026-03-18T23:59:48Z | 7775819 | 0.076398778 |
| 2026-03-19T23:59:48Z | 7783014 | 0.07612364746791819334 |
| 2026-03-20T23:59:48Z | 7790201 | 0.07676534 |
| 2026-03-21T23:59:48Z | 7797398 | 0.077468528 |
| 2026-03-22T23:59:48Z | 7804598 | 0.076546976 |
| 2026-03-23T23:59:48Z | 7811798 | 0.074625152 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.08054129733424494616 |
| 2026-03-25T23:59:48Z | 7826196 | 0.082784291 |
| 2026-03-26T23:59:48Z | 7833396 | 0.083777851 |
| 2026-03-27T23:59:48Z | 7840596 | 0.084587264 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.081606531 |
| 2026-03-29T23:59:48Z | 7854902 | 0.080097977 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.078596674 |
| 2026-03-31T23:59:48Z | 7869291 | 0.076895582 |
| 2026-04-01T23:59:48Z | 7876474 | 0.077424993 |
| 2026-04-02T23:59:48Z | 7883622 | 0.07605462 |
| 2026-04-03T23:59:48Z | 7890794 | 0.074686745 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.074123129 |
| 2026-04-05T23:59:48Z | 7905188 | 0.074251143 |
| 2026-04-06T23:59:48Z | 7912388 | 0.074520619 |
| 2026-04-07T23:59:48Z | 7919588 | 0.07310012 |
| 2026-04-08T23:59:48Z | 7926788 | 0.075322627 |
| 2026-04-09T23:59:48Z | 7933987 | 0.077224997 |
| 2026-04-10T23:59:48Z | 7941184 | 0.079774911 |
| 2026-04-11T23:59:48Z | 7948384 | 0.077961469 |
| 2026-04-12T23:59:48Z | 7955584 | 0.077980188 |
| 2026-04-13T23:59:48Z | 7962784 | 0.079320062 |
| 2026-04-14T23:59:48Z | 7969979 | 0.078427227 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.076662086 |
| 2026-04-16T23:59:48Z | 7984379 | 0.076413786 |
| 2026-04-17T23:59:48Z | 7991579 | 0.075912431 |
| 2026-04-18T23:59:48Z | 7998779 | 0.075586581 |
| 2026-04-19T23:59:48Z | 8005979 | 0.076683597 |
| 2026-04-20T23:59:48Z | 8013179 | 0.07398891 |
| 2026-04-21T23:59:48Z | 8020376 | 0.072726335 |
| 2026-04-22T23:59:48Z | 8027562 | 0.0724072 |
| 2026-04-23T23:59:48Z | 8034762 | 0.071717015 |
| 2026-04-24T23:59:48Z | 8041962 | 0.071198776 |
| 2026-04-25T23:59:48Z | 8049151 | 0.070948354 |
| 2026-04-26T23:59:48Z | 8056274 | 0.070516153 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.069883062 |
| 2026-04-28T23:59:48Z | 8070646 | 0.069672906 |
| 2026-04-29T23:59:48Z | 8077790 | 0.069677541 |
| 2026-04-30T23:59:48Z | 8084984 | 0.069442753 |
| 2026-05-01T23:59:48Z | 8092168 | 0.067221269 |
| 2026-05-02T23:59:48Z | 8099357 | 0.066795188 |
| 2026-05-03T16:10:00Z | 8104202 | 0.067101102 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

