# NetUID 89 — InfiniteHash (`ᛒ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**InfiniteHash** (NetUID **89**) (`ᛒ`).

BTC Pool + Lightning Network



#### SubnetIdentity `additional` *(chain)*



The Last Bitcoin Mining Pool, made by Bittensor

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `76`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,560.420085262. **Alpha liquidity in pool (`alpha_in`)** = ‎1,796,229.708470931ᛒ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,048,980.807419371ᛒ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003772056`** *(also **moving-average price** `0.0037744638975709677` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎160,061.085308996ᛒ‎`. **Owner hotkey / coldkey (chain):** `5FCN4P1KqFtsgBk29ABeDZuAnhrcHP2iTN2fG1kBefJBhBLd` / `5Dc5NmEUptDeMLrxDSvg8kfCToxJkiF47apAYSVTycAVvDN4`.
- **Subnet registered at block:** `5313364` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎56.185491720ᛒ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ᛒ‎` · α-in `‎0.000000000ᛒ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104359`
- **Liquidity constant `k`:** `11784021457197002554668518922`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `InfiniteHash`
- **Symbol (API):** `ᛒ`
- **Rank:** `85`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003772099`
- **Market cap:** `13267445377965.699970806`
- **Market cap Δ 1d:** `-0.700523044943587912`
- **Liquidity:** `13335976371940`
- **Total τ:** `6560459597470`
- **Total α:** `3844977515890302`
- **α in pool:** `1796219233501147`
- **α staked:** `1721038764755447`
- **Price Δ 1h:** `-0.015877231625749`
- **Price Δ 1d:** `-0.821722522658959781`
#### Subnet activity (TAOStats)

- **NetUID (API):** `89`
- **Owner SS58 (API):** `5Dc5NmEUptDeMLrxDSvg8kfCToxJkiF47apAYSVTycAVvDN4`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `5313364`
- **Registration wall time:** `2025-04-09T11:46:24Z`
- **Registration cost snapshot:** `286399608951`
- **Active keys:** `256`
- **Active validators:** `10`
- **Active miners:** `3`
- **Active dual-role:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `10`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

# InfiniteHash Subnet (SN89)

# Decentralized Bitcoin Mining & Lightning Infrastructure

Track [Pool Metrics](https://infinitehash.xyz)

# What is InfiniteHash?

InfiniteHash Subnet (SN89) is revolutionizing Bitcoin mining by combining decentralized mining operations with cutting-edge Lightning Network infrastructure. We're building a truly decentralized and more democratic Bitcoin mining pool AND in parallel the foundation for Bitcoin to become the preferred payment layer for the emerging AI agent economy via our enterprise quality Lightning network.

# How It Works

Phase 1 (launch): Market Discovery
- Miners contribute hashrate and earn Alpha tokens proportional to contribution
- All mined Bitcoin is converted to Alpha and burned, creating continuous buying pressure
- Market discovers sustainable Alpha-to-hashrate conversion rates

Phase 2: Sustainable Economics
- Minimum hashrate threshold for base rewards - no incentive for overcommitting hash
- Alpha denominated hashprice designed to exceed BTC hashprice available in market, after pool fees. Min hashrate threshold adjusted routinely
- Miners also run Lightning nodes and compete (creating uid curve) on quality for incremental rewards beyond hashrate

# Getting Started

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

# Validators

- - -

For a detailed description of the auction-based incentive mechanism and validator responsibilities, see `docs/subnet_auction_incentive_system.md`.

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

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

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

---

## AWS

<details>
Initiate the infrastructure with Terraform:
TODO

To push a new version of the application to AWS, just push to a branch named `deploy-$(ENVIRONMENT_NAME)`.
Typical values for `$(ENVIRONMENT_NAME)` are `prod` and `staging`.
For this to work, GitHub actions needs to be provided with credentials for an account that has the following policies enabled:

- AutoScalingFullAccess
- AmazonEC2ContainerRegistryFullAccess
- AmazonS3FullAccess

See `.github/workflows/cd.yml` to find out the secret names.

For more details see [README_AWS.md](README_AWS.md)
</details>

---

## B2 cloud storage

> In these examples we assume that backups will be stored inside `folder`. If you want to store backups in the root folder, just use empty string instead of `folder`.

First, create a Backblaze B2 account and a bucket for backups (with [lifecycle rules](https://www.backblaze.com/docs/cloud-storage-configure-and-manage-lifecycle-rules)):

```sh
b2 bucket create --lifecycle-rule '{"daysFromHidingToDeleting": 30, "daysFromUploadingToHiding": 30, "fileNamePrefix": "folder/"}' "infinite-hashes-backups" allPrivate
```

> If you want to add backups to already existing bucket, use `b2 bucket update` command and don't forget to list all previous lifecycle rules as well as adding the new one.

Create an application key with restricted access to a single bucket:

```sh
b2 key create --bucket "infinite-hashes-backups" --namePrefix "folder/" "infinite-hashes-backups-key" listBuckets,listFiles,readFiles,writeFiles
```

Fill in `.env` file:
- `BACKUP_B2_BUCKET=infinite-hashes-backups`
- `BACKUP_B2_FOLDER=folder`
- `BACKUP_B2_APPLICATION_KEY_ID=0012345abcdefgh0000000000`
- `BACKUP_B2_APPLICATION_KEY=A001bcdefgHIJKLMNOPQRSTUxx11x22`

---

## Restoring system from backup after a catastrophical failure

1. Follow the instructions above to set up a new production environment
2. Restore the database using one of
```sh
docker compose run --rm backups ./restore-db.sh /var/backups/{backup-name}.dump.zstd

docker compose run --rm backups ./restore-db.sh b2://{bucket-name}/{backup-name}.dump.zstd
docker compose run --rm backups ./restore-db.sh b2id://{ID}
```
3. See if everything works
4. Make sure everything is filled up in `.env`, error reporting integration, email accounts etc

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/backend-developers-ltd/InfiniteHash/master/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://infinitehash.xyz](https://infinitehash.xyz)
- **GitHub:** [https://github.com/backend-developers-ltd/InfiniteHash](https://github.com/backend-developers-ltd/InfiniteHash)
- **Logo URL:** [https://raw.githubusercontent.com/DeltaCompute24/RheftheChef/main/thechef.jpg](https://raw.githubusercontent.com/DeltaCompute24/RheftheChef/main/thechef.jpg)
- **Contact:** btc@infinitehash.xyz

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.003772085 |
| 8104292 | 0.003772076 |
| 8104340 | 0.003772061 |
| 8104388 | 0.00377206 |
| 8104436 | 0.003772055 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

