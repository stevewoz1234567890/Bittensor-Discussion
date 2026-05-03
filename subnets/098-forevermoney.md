# NetUID 98 — ForeverMoney (`ბ`)

## Overview

**ForeverMoney** (NetUID **98**) (`ბ`).

Decentralized intelligence for advanced liquidity management.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `288`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,258.167161014. **Alpha liquidity in pool (`alpha_in`)** = ‎1,526,143.370259256ბ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,341,154.886899284ბ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004101973`** *(also **moving-average price** `0.004097687778994441` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎177,201.366320226ბ‎`. **Owner hotkey / coldkey (chain):** `5EJ2354xmxG8AoYoRuefW2kpLiZ8f3g68MSaFiVDAGUWRmR2` / `5Dd9Q6yueRkH1fLTHa2xdEEPoMQiqenWKRMUtZKPTuvjRL3w`.
- **Subnet registered at block:** `5445992` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎213.019252662ბ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ბ‎` · α-in `‎0.000000000ბ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004102`
- **Market cap:** `11783389026464.33108`
- **Liquidity:** `12518407265695`
- **Total τ:** `6258188141478`
- **Total α:** `3867223257158540`
- **α in pool:** `1526138255538253`
- **α staked:** `1346457801620287`
- **Price Δ 1h:** `0.016043529166794674`
- **Price Δ 1d:** `0.243080918062400463`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Decentralized intelligence for advanced liquidity management.  Alpha-gated TG https://t.me/+3MN77q0y9lwyMDVk



**Additional commentary (on-chain)**


Making liquidity intelligent.

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Decentralized Liquidity Intelligence

**Fetched document title:** ForeverMoney 九八 - SN98

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
- **Owner SS58 (`owner_ss58`):** `5Dd9Q6yueRkH1fLTHa2xdEEPoMQiqenWKRMUtZKPTuvjRL3w`

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

### 1. Prerequisites

- **Python 3.10+**
- **Git**

---

### 2. Installation

Clone the repository and set up the virtual environment:

```bash

---

# Create a virtual environment

python3 -m venv .venv

---

# Install dependencies

pip install -r requirements.txt
```

---

## ⛏️ Running a Miner

**Getting Started:** Implement a `rebalance_query_handler` that responds to `RebalanceQuery` requests from validators. Accept/refuse jobs and return desired positions (rebalance or keep current). Build reputation through consistent participation for 7 days to become eligible for live execution.

1.  **Register your miner** (if not already registered):
    See [MINER_REGISTRATION_GUIDE.md](./MINER_REGISTRATION_GUIDE.md) for detailed instructions.

2.  **Run the miner**:
    ```bash
    # Using python directly
    python -m miner.miner \
        --wallet.name <your_wallet> \
        --wallet.hotkey <your_hotkey> \
        --netuid 98

    # Using PM2 (Recommended for production)
    pm2 start miner/miner.py --name sn98-miner -- \
        --wallet.name <your_wallet> \
        --wallet.hotkey <your_hotkey> \
        --netuid 98
    ```

For a complete implementation guide and scoring details, see **[MINER_GUIDE.md](./MINER_GUIDE.md)**.

---

---

## 🛡️ Running a Validator

Validators evaluate miner strategies and execute winning strategies on-chain.

1.  **Database Setup**:
    Validators require a PostgreSQL database to store job history and scores. Ensure you have PostgreSQL installed and configured, then update your `.env` file with the credentials (`JOBS_POSTGRES_*`).

2.  **Run the validator**:
    ```bash
    # Using python directly
    python validator/validator.py \
        --wallet.name <your_wallet> \
        --wallet.hotkey <your_hotkey> \
        --netuid 98

    # Using PM2 (Recommended for production)
    pm2 start validator/validator.py --name sn98-validator -- \
        --wallet.name <your_wallet> \
        --wallet.hotkey <your_hotkey> \
        --netuid 98
    ```

3.  **Auto-Update (optional)**  
    By default the validator runs an auto-update task every **1 hour**: it executes `scripts/update_to_latest.sh` to fetch the latest release from the repo, install dependencies, and (if you use PM2) restart processes so new code is loaded.

    - **Enable (default):** `--auto-update true` — runs the update script every 3600 seconds.
    - **Disable:** `--auto-update false` — no automatic updates.

    ```bash
    # Disable auto-update
    python validator/validator.py \
        --wallet.name <your_wallet> \
        --wallet.hotkey <your_hotkey> \
        --netuid 98 \
        --auto-update false
    ```

    You can also run the update script manually from the repo root:
    ```bash
    chmod +x scripts/update_to_latest.sh
    ./scripts/update_to_latest.sh              # update to latest release tag
    ./scripts/update_to_latest.sh main         # update to branch main instead
    ./scripts/update_to_latest.sh --no-restart # skip pm2 restart
    ```

For detailed system architecture, see **[ARCHITECTURE.md](./ARCHITECTURE.md)**.

---

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/SN98-ForeverMoney/forever-money/main/README.md`*

## On-chain identity — description


Decentralized intelligence for advanced liquidity management.  Alpha-gated TG https://t.me/+3MN77q0y9lwyMDVk

## On-chain identity — additional field


Making liquidity intelligent.

## Registered contact & links


- **Website:** [https://forevermoney.ai](https://forevermoney.ai)
- **GitHub:** [https://github.com/SN98-ForeverMoney/forever-money](https://github.com/SN98-ForeverMoney/forever-money)
- **Discord:** [https://discord.gg/8XuGcpY2w4](https://discord.gg/8XuGcpY2w4)
- **Logo URL:** [https://sn98.s3.eu-north-1.amazonaws.com/sn98.png](https://sn98.s3.eu-north-1.amazonaws.com/sn98.png)
- **Contact:** gm@forevermoney.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.004102015 |
| 8104133 | 0.004102007 |
| 8104181 | 0.004102003 |
| 8104229 | 0.004101986 |
| 8104277 | 0.004101973 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004855353 |
| 2026-03-10T23:59:48Z | 7718257 | 0.004845768 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005168308 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005168604 |
| 2026-03-13T23:59:48Z | 7739841 | 0.004839907 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.00488859 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004692037 |
| 2026-03-16T23:59:48Z | 7761426 | 0.004585354 |
| 2026-03-17T23:59:48Z | 7768619 | 0.004447311 |
| 2026-03-18T23:59:48Z | 7775819 | 0.00443633 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00447493467956393473 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004447522 |
| 2026-03-21T23:59:48Z | 7797398 | 0.00449678 |
| 2026-03-22T23:59:48Z | 7804598 | 0.004584173 |
| 2026-03-23T23:59:48Z | 7811798 | 0.004590051 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00450072711987568333 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004484835 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004424381 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004446737 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004424432 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004459888 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.0045942 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004533116 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004539356 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004528673 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004525545 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004433343 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004418532 |
| 2026-04-06T23:59:48Z | 7912388 | 0.00428281 |
| 2026-04-07T23:59:48Z | 7919588 | 0.00434151 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004176384 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004185931 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004191445 |
| 2026-04-11T23:59:48Z | 7948384 | 0.00419123 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004087016 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004045323 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004078029 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.00397639 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003983157 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004041336 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004029723 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004034098 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004029713 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004021481 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004179238 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004271882 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004235898 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004198866 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004182892 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004037114 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004068572 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004085578 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004142775 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004112201 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004089799 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004102 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

