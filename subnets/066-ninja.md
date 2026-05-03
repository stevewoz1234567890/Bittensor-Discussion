# NetUID 66 — ninja (`ض`)

## Overview

**ninja** (NetUID **66**) (`ض`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `194`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ14,109.826388381. **Alpha liquidity in pool (`alpha_in`)** = ‎966,472.959189225ض‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,883,230.867756480ض‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.014168925`** *(also **moving-average price** `0.01378167630173266` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎995,570.880679678ض‎`. **Owner hotkey / coldkey (chain):** `5DRPoRiBSPNvgSvRsehaUhtXqPgXYrds8VS42vdzT5MzcpZV` / `5DRtWRDDrcKfgwPBkjADBVPSFzpLSGXejzNXXRtfSCpkFKHP`.
- **Subnet registered at block:** `4958013` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎146.136233413ض‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.007084457` · α-out `‎1.000000000ض‎` · α-in `‎0.500000000ض‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.014168821`
- **Market cap:** `57936897289888.934113238`
- **Liquidity:** `27803424553321`
- **Total τ:** `14109684347993`
- **Total α:** `4849687919151558`
- **α in pool:** `966469984011287`
- **α staked:** `3122571531149991`
- **Price Δ 1h:** `-0.993307722682447937`
- **Price Δ 1d:** `0.394212929257286715`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `6`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `7084400`
- **Max neurons:** `256`
- **Validators (metadata):** `6`
- **Neuron reg. cost:** `10080643`

### On-chain declared purpose *(SubnetIdentity)*

Distilling software agents

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
- **`immunity_period` (blocks):** 6080
- **Registration recycle cost snapshot (`burn`):** τ0.012292581
- **Owner SS58 (`owner_ss58`):** `5DRtWRDDrcKfgwPBkjADBVPSFzpLSGXejzNXXRtfSCpkFKHP`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `6080` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `3`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

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

## On-chain identity — description


Distilling software agents

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/unarbos/tau](https://github.com/unarbos/tau)
- **Discord (handle / invite hint):** `arbos`
- **Logo:** `🥷`
- **Contact:** tau@arbos.life

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.014167083 |
| 8104072 | 0.014079811 |
| 8104120 | 0.013923418 |
| 8104168 | 0.014175518 |
| 8104216 | 0.014168925 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004066763 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004052818 |
| 2026-03-11T23:59:48Z | 7725455 | 0.004110381 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.004141991 |
| 2026-03-13T23:59:48Z | 7739841 | 0.003780386 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.003773223 |
| 2026-03-15T23:59:48Z | 7754226 | 0.003579388 |
| 2026-03-16T23:59:48Z | 7761426 | 0.00530743 |
| 2026-03-17T23:59:48Z | 7768619 | 0.007060962 |
| 2026-03-18T23:59:48Z | 7775819 | 0.0071642 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00696976938266179549 |
| 2026-03-20T23:59:48Z | 7790201 | 0.006992559 |
| 2026-03-21T23:59:48Z | 7797398 | 0.007314765 |
| 2026-03-22T23:59:48Z | 7804598 | 0.00695725 |
| 2026-03-23T23:59:48Z | 7811798 | 0.007006862 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00579828147355004597 |
| 2026-03-25T23:59:48Z | 7826196 | 0.007438128 |
| 2026-03-26T23:59:48Z | 7833396 | 0.007290541 |
| 2026-03-27T23:59:48Z | 7840596 | 0.007445686 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.007169142 |
| 2026-03-29T23:59:48Z | 7854902 | 0.006729046 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.007197252 |
| 2026-03-31T23:59:48Z | 7869291 | 0.007863886 |
| 2026-04-01T23:59:48Z | 7876474 | 0.009031637 |
| 2026-04-02T23:59:48Z | 7883622 | 0.009144855 |
| 2026-04-03T23:59:48Z | 7890794 | 0.009437919 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.00905912 |
| 2026-04-05T23:59:48Z | 7905188 | 0.009088383 |
| 2026-04-06T23:59:48Z | 7912388 | 0.009054654 |
| 2026-04-07T23:59:48Z | 7919588 | 0.009323681 |
| 2026-04-08T23:59:48Z | 7926788 | 0.009907636 |
| 2026-04-09T23:59:48Z | 7933987 | 0.008949624 |
| 2026-04-10T23:59:48Z | 7941184 | 0.009485057 |
| 2026-04-11T23:59:48Z | 7948384 | 0.010613908 |
| 2026-04-12T23:59:48Z | 7955584 | 0.014470211 |
| 2026-04-13T23:59:48Z | 7962784 | 0.017303561 |
| 2026-04-14T23:59:48Z | 7969979 | 0.016019534 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.016846194 |
| 2026-04-16T23:59:48Z | 7984379 | 0.016049614 |
| 2026-04-17T23:59:48Z | 7991579 | 0.016069342 |
| 2026-04-18T23:59:48Z | 7998779 | 0.014640732 |
| 2026-04-19T23:59:48Z | 8005979 | 0.015191184 |
| 2026-04-20T23:59:48Z | 8013179 | 0.013982861 |
| 2026-04-21T23:59:48Z | 8020376 | 0.013478256 |
| 2026-04-22T23:59:48Z | 8027562 | 0.012888491 |
| 2026-04-23T23:59:48Z | 8034762 | 0.013942772 |
| 2026-04-24T23:59:48Z | 8041962 | 0.014463833 |
| 2026-04-25T23:59:48Z | 8049151 | 0.014586987 |
| 2026-04-26T23:59:48Z | 8056274 | 0.013627798 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.013452891 |
| 2026-04-28T23:59:48Z | 8070646 | 0.012655453 |
| 2026-04-29T23:59:48Z | 8077790 | 0.013069776 |
| 2026-04-30T23:59:48Z | 8084984 | 0.013197353 |
| 2026-05-01T23:59:48Z | 8092168 | 0.012380219 |
| 2026-05-02T23:59:48Z | 8099357 | 0.013358822 |
| 2026-05-03T16:10:00Z | 8104202 | 0.014168821 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

