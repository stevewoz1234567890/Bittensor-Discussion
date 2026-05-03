# NetUID 33 — ReadyAI (`ט`)

## Overview

**ReadyAI** (NetUID 33) does not currently expose a long on-chain description. Use the registered links and any website excerpt below; confirm the subnet’s purpose on official channels and explorers.

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.001146975
- **Owner SS58 (`owner_ss58`):** `5HinUfk5SqBUAbkMtgdNoum3VJvwrLgdvwW5sbXA1UPYZ8uB`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7200` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `11`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

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

Lines caught by patterns such as **\d+ GB/TB**, **CUDA / VRAM**, **RTX / H100 / A100**, **vCPU / cores**, etc. *(Heuristic — confirm on the subnet’s official repo / docs.)*

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

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


*Empty — no description bytes set in `SubnetIdentity`.*

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/afterpartyai/bittensor-conversation-genome-project](https://github.com/afterpartyai/bittensor-conversation-genome-project)
- **Contact:** david@readyai.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.006915814 |
| 8103843 | 0.006915804 |
| 8103891 | 0.006915801 |
| 8103939 | 0.006915643 |
| 8103987 | 0.006877773 |
| 8104035 | 0.006877771 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

