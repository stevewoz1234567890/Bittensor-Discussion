# NetUID 33 — ReadyAI (`ט`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**ReadyAI** (NetUID **33**) (`ט`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `20`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ17,139.913222095. **Alpha liquidity in pool (`alpha_in`)** = ‎2,500,952.904783360ט‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,835,033.550210785ט‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.006877702`** *(also **moving-average price** `0.006936060730367899` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎824,612.808221623ט‎`. **Owner hotkey / coldkey (chain):** `5HinUfk5SqBUAbkMtgdNoum3VJvwrLgdvwW5sbXA1UPYZ8uB` / `5HinUfk5SqBUAbkMtgdNoum3VJvwrLgdvwW5sbXA1UPYZ8uB`.
- **Subnet registered at block:** `2943950` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎14.935794915ט‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ט‎` · α-in `‎0.000000000ט‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104415`
- **Liquidity constant `k`:** `42866115760533209635540339200`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `ReadyAI` |
| Symbol (API) | `ט` |
| Rank | `40` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.006877753` |
| Market cap | `27050392621367.798896169` |
| Market cap Δ 1d | `-0.566449061666474246` |
| Liquidity | `34340849565417` |
| Total τ | `17139977740543` |
| Total α | `4335753714755679` |
| α in pool | `2500943523978611` |
| α staked | `1432084111844862` |
| Price Δ 1h | `-0.550117282199393331` |
| Price Δ 1d | `-0.680173184878699248` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `33` |
| Owner SS58 (API) | `5HinUfk5SqBUAbkMtgdNoum3VJvwrLgdvwW5sbXA1UPYZ8uB` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `2943950` |
| Registration wall time | `2024-05-12T23:17:24Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `14` |
| Active miners | `236` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `14` |
| Max validators (API) | `64` |
| Neuron reg. cost | `1053795` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# **ReadyAI** <!-- omit in toc -->
[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---
- [Conversation Genome Project](#conversation-genome-project-overview)
  - [Key Features](#key-features)
  - [Benefits](#Benefits)
  - [System Design](#System-Design)
  - [Rewards and Incentives](#reward-mechanism)
- [Getting Started](#Getting-Started)
  - [Installation & Compute Requirements](#installation--compute-requirements)
  - [Configuration](#configuration)
  - [LLM Selection](#LLM-Selection)
  - [Quickstart - Running the tests](#running-the-tests)
  - [Registration](#Registration)
  - [Get Running Quickly with the Docker Image!](#Running-a-Miner-or-a-Validator-with-Docker)
  - [Get a miner Running on Runpod](#Running-a-Miner-on-Runpod)
- [Subnet Roles](#subnet-roles)
  - [Mining](#mining)
  - [Validating](#validating)
- [Helpful Guides](#helpful-guides)
  - [Runpod](#Runpod)
  - [Managing Processes](#managing-processes)
  - [Making sure your port is open](#making-sure-your-port-is-open)
- [llms.txt Reference MCP](#llmstxt-reference-mcp)
- [License](#license)

---

# Introduction to ReadyAI

ReadyAI is an open-source initiative aimed at provide a low-cost resource-minimal data structuring and semantic tagging pipeline for any individual or business. AI runs on Structured Data. ReadyAI is a low-cost, structured data pipeline to turn your raw data into structured data for your vector databases and AI applications.

If you are new to Bittensor, please checkout the [Bittensor Website](https://bittensor.com/) before proceeding to the setup section.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** ReadyAI (readyai.ai) enables structured data processing at scale, democratizing access to the valuable digital commodity of structured data – the key ingredient for high quality fine tuned models a...

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
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 7200 |
| Registration recycle cost snapshot (`burn`) | τ0.001059907 |
| Owner SS58 (`owner_ss58`) | `5HinUfk5SqBUAbkMtgdNoum3VJvwrLgdvwW5sbXA1UPYZ8uB` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `7200` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
| `commit_reveal_period` | `11` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Installation & Compute Requirements

This repository requires Python version greater than 3.8 and up to 3.11. To get started, clone the repository and install the required dependencies:

```console
git clone https://github.com/afterpartyai/bittensor-conversation-genome-project.git cgp-subnet
cd cgp-subnet
pip install -r requirements.txt
```

Miners & Validators using an OpenAI API Key will need a CPU with at least 8GB of Ram and 20GB of Disk Space.

---

# For Validators. Read from api.conversations.xyz

#export CGP_API_READ_HOST=https://api.conversations.xyz
#export CGP_API_READ_PORT=443

---

# For Validators. Write to db.conversations.xyz

#export CGP_API_WRITE_HOST=https://db.conversations.xyz
#export CGP_API_WRITE_PORT=443

---

## Mining

You can launch your miners on testnet using the following command.

To run with pm2 please see instructions [here](#Running-a-Miner-with-PM2)

If you are running on runpod, please read instructions [here](#Using-Runpod).

To setup and run a miner with Docker, see instructions [here](#Running-a-Miner-or-a-Validator-with-Docker).

```
python3 -m neurons.miner --subtensor.network test --netuid 138 --wallet.name <coldkey name> --wallet.hotkey <hotkey name> --logging.debug --axon.port <port>
```

Once you've registered on on mainnet SN33, you can start your miner with this command:

```
python3 -m neurons.miner --netuid 33 --wallet.name <wallet name> --wallet.hotkey <hotkey name> --axon.port <port>
```

---

#### Using the Prebuilt Docker Image

This section shows you how to quickly run the API server using a prebuilt Docker image—**no build step required**!

The image comes preloaded with a `conversations.sqlite` database containing **4,888 podcast conversations** ready for training or testing.

**Steps**

1. **Create Your `.env` File**

   Copy the example environment file and create your own configuration:  
   ```
   cp env.example .env
   ```

2. **Configure the Environment**

   Open the `.env` file and set the `TYPE` variable to `api`:  
   ```
   TYPE=api
   ```
   You will also need to adjust the endpoints for your needs as explained [here](#for-testing-with-a-local-api)

   > [!IMPORTANT]  
   > **If you are a validator** and you want to use the local api and test dataset to send conversations to miners, you have to set `TYPE=validator` and `START_LOCAL_CGP_API=true` instead


3. **Start the Server**

   Run the following script to launch the server:  
   ```
   mot/up
   ```

   This will:
   - Download the Docker image if not already present
   - Start the API using Docker Compose

   **To build the image yourself** instead of using the prebuilt one:  
   ```
   docker compose build  
   docker compose up
   ```

**Verifying the Server**

If the server starts correctly, your logs should show something like:  
```
cgp_miner-1  | INFO:     Started server process [7]  
cgp_miner-1  | INFO:     Waiting for application startup.  
cgp_miner-1  | INFO:     Application startup complete.  
cgp_miner-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**Test the API**

Make a test request to verify it’s running:  
```
curl -X POST localhost:8000/api/v1/conversation/reserve
```

Expected output:  
```
{"guid":11388,"lines":[[1,"Welcome to the Sell or Die podcast."],[1,"I...
```

---

## Using Runpod

Runpod is a very helpful resource for easily launching and managing cloud GPU and CPU instances, however, there are several configuration settings that must be implemented both on Runpod and in your start command for the subnet.

---

### Choosing an Instance

To run the subnet code for ReadyAI, you'll need either a GPU or a CPU, depending on your subnet role and configuration.

Miners & Validators using an OpenAI API Key, you will need a CPU with at least 8GB of Ram and 20GB of Disk Space. Runpod provides basic CPU units of different processing powers.

---

### Configuring Your Instance

Runpod Instances are dockerized. As a result, there are specific ports configurations needed to be able to run processes over the network.

When you are launching your pod, and have selected your instance, click "Edit Template."

With the editing window open, you adjust your container disk space and/or volume diskspace to match the needs of your neuron, and you can expose additional ports. You will need to expose symmetrical TCP Ports, which requires you to specify non-standard ports >=70000 in the "Expose TCP ports" field. Add however many ports you will need (we recommend at least 2, or more if you want to run additional miners).

Now, you can deploy your instan…

---





#### CPU / GPU / RAM lines (automatic grep)

- Miners & Validators using an OpenAI API Key will need a CPU with at least 8GB of Ram and 20GB of Disk Space.
- - `readyai_conversation_data_importer.py` -- An example processor that reads [ReadyAi/5000-podcast-conversations-with-metadata-and-embedding-dataset](https://huggingface.co/datasets/ReadyAi/5000-podcast-conversations-with-metadata-and-embedding-dataset) and processes a subset of it and inserts it into the `conversations.sqlite` data store
- - `facebook_conversation_data_importer.py` -- An example processor that reads the subset of the Facebook conversation data and processes it into the `conversations.sqlite` data store
- Runpod is a very helpful resource for easily launching and managing cloud GPU and CPU instances, however, there are several configuration settings that must be implemented both on Runpod and in your start command for the subnet.
- To run the subnet code for ReadyAI, you'll need either a GPU or a CPU, depending on your subnet role and configuration.
- Miners & Validators using an OpenAI API Key, you will need a CPU with at least 8GB of Ram and 20GB of Disk Space. Runpod provides basic CPU units of different processing powers.
- - Choose a data center with available CPU instances.
- - Set a volume name and allocate 10 GB (enough for typical usage).
- - Select the cheapest available CPU option — it’s sufficient for this subnet.


*Primary README URL used: `https://raw.githubusercontent.com/afterpartyai/bittensor-conversation-genome-project/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/afterpartyai/bittensor-conversation-genome-project](https://github.com/afterpartyai/bittensor-conversation-genome-project)
- **Contact:** david@readyai.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.006877754 |
| 8104244 | 0.006877736 |
| 8104292 | 0.006877725 |
| 8104340 | 0.006877707 |
| 8104388 | 0.006877707 |
| 8104436 | 0.006877702 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

