# NetUID 89 — InfiniteHash (`ᛒ`)

## Overview

BTC Pool + Lightning Network

The Last Bitcoin Mining Pool, made by Bittensor

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

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
- **Owner SS58 (`owner_ss58`):** `5Dc5NmEUptDeMLrxDSvg8kfCToxJkiF47apAYSVTycAVvDN4`

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
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `0`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

# Decentralized Bitcoin Mining & Lightning Infrastructure

Track [Pool Metrics](https://infinitehash.xyz)

---

# For Miners

Requirements / Getting Started (V1)

- Bitcoin ASIC miners
- Bittensor baseminer - no SN specific configurations. Validators score your hash contribution based on your hotkey in the ASIC workerID
- Point Your ASICs to Our Pool


Pool URL: stratum+tcp://btc.global.luxor.tech:700 (or choose a specific regional stratum if desired).

Configure Worker Names
  - Format: `infinite.YOUR_HOTKEY.your_workerID`
  - YOUR_HOTKEY: Your Bittensor wallet hotkey
  - your_workerID: Any identifier you choose for your ASIC fleet

Examples:
```
infinite.5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY.1
infinite.5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY.warehouse_a
```

---

# Validators

- - -

For a detailed description of the auction-based incentive mechanism and validator responsibilities, see `docs/subnet_auction_incentive_system.md`.

---

# Base requirements

- docker with [compose plugin](https://docs.docker.com/compose/install/linux/)
- python 3.11
- [uv](https://docs.astral.sh/uv/)
- [nox](https://nox.thea.codes)

---

# Setup development environment

```sh
./setup-dev.sh
docker compose up -d
cd app/src
uv run manage.py wait_for_database --timeout 10
uv run manage.py migrate
uv run manage.py runserver
```

---

# Setup production environment (git deployment)

<details>

This sets up "deployment by pushing to git storage on remote", so that:

- `git push origin ...` just pushes code to Github / other storage without any consequences;
- `git push production master` pushes code to a remote server running the app and triggers a git hook to redeploy the application.

```
Local .git ------------> Origin .git
                \
                 ------> Production .git (redeploy on push)
```

- - -

Use `ssh-keygen` to generate a key pair for the server, then add read-only access to repository in "deployment keys" section (`ssh -A` is easy to use, but not safe).

```sh


*README source used for excerpts: `https://raw.githubusercontent.com/backend-developers-ltd/InfiniteHash/master/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


BTC Pool + Lightning Network

## On-chain identity — additional field


The Last Bitcoin Mining Pool, made by Bittensor

## Registered contact & links


- **Website:** [https://infinitehash.xyz](https://infinitehash.xyz)
- **GitHub:** [https://github.com/backend-developers-ltd/InfiniteHash](https://github.com/backend-developers-ltd/InfiniteHash)
- **Logo URL:** [https://raw.githubusercontent.com/DeltaCompute24/RheftheChef/main/thechef.jpg](https://raw.githubusercontent.com/DeltaCompute24/RheftheChef/main/thechef.jpg)
- **Contact:** btc@infinitehash.xyz

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.003772761 |
| 8103738 | 0.003772756 |
| 8103786 | 0.003772713 |
| 8103834 | 0.003772709 |
| 8103882 | 0.0037727 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

