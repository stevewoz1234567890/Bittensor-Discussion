# NetUID 66 — ninja (`ض`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**ninja** (NetUID **66**) (`ض`).

Distilling software agents

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `53`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ14,120.221579489. **Alpha liquidity in pool (`alpha_in`)** = ‎965,959.807747063ض‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,884,023.816956961ض‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.014186512`** *(also **moving-average price** `0.013805747032165527` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎995,593.103520936ض‎`. **Owner hotkey / coldkey (chain):** `5DRPoRiBSPNvgSvRsehaUhtXqPgXYrds8VS42vdzT5MzcpZV` / `5DRtWRDDrcKfgwPBkjADBVPSFzpLSGXejzNXXRtfSCpkFKHP`.
- **Subnet registered at block:** `4958013` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎39.924136755ض‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.007093253` · α-out `‎1.000000000ض‎` · α-in `‎0.500000000ض‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104382`
- **Liquidity constant `k`:** `13639566522269124692460790807`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `ninja` |
| Symbol (API) | `ض` |
| Rank | `20` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.014168821` |
| Market cap | `57936897289888.934113238` |
| Market cap Δ 1d | `0.559022155487541821` |
| Liquidity | `27803424553321` |
| Total τ | `14109684347993` |
| Total α | `4849687919151558` |
| α in pool | `966469984011287` |
| α staked | `3122571531149991` |
| Price Δ 1h | `-0.993307722682447937` |
| Price Δ 1d | `0.394212929257286715` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `66` |
| Owner SS58 (API) | `5DRtWRDDrcKfgwPBkjADBVPSFzpLSGXejzNXXRtfSCpkFKHP` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4958013` |
| Registration wall time | `2025-02-19T03:15:12Z` |
| Registration cost snapshot | `65230444016` |
| Active keys | `256` |
| Active validators | `6` |
| Active miners | `1` |
| Active dual-role | `1` |
| Emission | `7084400` |
| Max neurons | `256` |
| Validator slots (metadata) | `6` |
| Max validators (API) | `64` |
| Neuron reg. cost | `10080643` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# tau

`tau` is a small CLI for running a staged SWE workflow:

1. `generate` mines a commit and creates a task.
2. `solve` runs a solver against that task.
3. `compare` scores two saved solutions by changed-line similarity.
4. `eval` compares multiple solutions with an LLM judge.
5. `delete` removes saved task artifacts.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to unarbos/tau development by creating an account on GitHub.

**Fetched document title:** GitHub - unarbos/tau · GitHub

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 256 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 6080 |
| Registration recycle cost snapshot (`burn`) | τ0.010140203 |
| Owner SS58 (`owner_ss58`) | `5DRtWRDDrcKfgwPBkjADBVPSFzpLSGXejzNXXRtfSCpkFKHP` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `6080` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `3` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Prerequisites

- Python 3.11+
- `uv`
- Docker
- A GitHub token for task generation
- An OpenRouter API key for Docker PI solves and evaluation
- A Cursor API key for Cursor solves

---

## Setup

From the `tau/` directory:

```bash
source .venv/bin/activate
uv pip install -e .
```

Create a `.env` file in `tau/` if you do not already have one:

```bash
GITHUB_TOKEN=your_github_token
OPENROUTER_API_KEY=your_openrouter_api_key
CURSOR_API_KEY=your_cursor_api_key
```

`tau` loads `.env` automatically from the project root.

---

## Cursor Agent In Docker

When you pass `--agent cursor`, tau builds a Docker image, runs the Cursor CLI inside it, and collects the resulting diff.

---

### Docker options

| Flag | Purpose |
|------|---------|
| `--solver-model <model>` | Override the model used by Cursor |
| `--agent-timeout <seconds>` | Time limit for the solve |
| `--docker-solver-memory 2g` | Container memory limit |
| `--docker-solver-cpus 2` | Container CPU limit |
| `--docker-solver-no-cache` | Force rebuild the Docker image |
| `--debug` | Enable debug logging |

---









#### CPU / GPU / RAM lines (automatic grep)

- 2. A container starts with resource limits (memory, CPU, pids, tmpfs).
- `| `--docker-solver-memory 2g` | Container memory limit |`
- `| `--docker-solver-cpus 2` | Container CPU limit |`


*Primary README URL used: `https://raw.githubusercontent.com/unarbos/tau/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/unarbos/tau](https://github.com/unarbos/tau)
- **Discord (handle / invite hint):** `arbos`
- **Logo:** `🥷`
- **Contact:** tau@arbos.life

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.014169003 |
| 8104292 | 0.014195985 |
| 8104340 | 0.014184297 |
| 8104388 | 0.014185468 |
| 8104436 | 0.014186518 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

