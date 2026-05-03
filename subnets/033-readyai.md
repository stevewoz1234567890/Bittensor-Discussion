# NetUID 33 — ReadyAI (`ט`)

## Overview

**From crawled page (site or GitHub):** ReadyAI (readyai.ai) enables structured data processing at scale, democratizing access to the valuable digital commodity of structured data – the key ingredient for high quality fine tuned models a...

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 7200
- **Registration recycle cost snapshot (`burn`):** τ0.001222226
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

## Miner / validator compute notes (README excerpts)

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

### pm2 Installation

To install Pm2 on your Ubuntu Device, use

```
apt install nodejs npm
npm install -g pm2
```

The basic command structure to run a process in pm2 is below:

```
pm2 start "<your neuron start command here>" --name "<your process name here>"
```

---

### Running a Miner with PM2

To run a miner with PM2, you can use the following template:

```
pm2 start "python3 -m neurons.miner --netuid 33 --wallet.name default --wallet.hotkey default --logging.debug --axon.port <port>" --name "miner"
```

---

### Running a Validator with PM2

To run a validator with PM2, you can use the following template:

```
pm2 start "python3 -m neurons.validator --netuid 33 --wallet.name <wallet name> --wallet.hotkey <hotkey name> --axon.port <port>" --name "validator"
```

---

### Requirements

- An [OpenAI API Key](https://platform.openai.com/api-keys)
- A [Bittensor wallet](https://docs.bittensor.com/working-with-keys#creating-a-wallet-with-btcli)
- [Registering](https://docs.bittensor.com/miners/#miner-registration) the hotkey on the subnet 33 
  - or 138 if you want to run on the test network

---

# --- For Validators ---

export WANDB_API_KEY=        # Your WandB API Key
export WAND_ENABLED=0        # Enable or disable WandB (Validators NEED to set this to 1)
```

- Do not forget to set your OpenAI API Key
- Set `TYPE=miner` to run a miner, or `TYPE=validator` to run a validator.
- Set `NETWORK=finney` to run on the main net, or `NETWORK=test` to run on the test net.
- Don't forget the port you chose has to be open and be able to receive HTTP requests. To validate follow the steps [here](#making-sure-your-port-is-open).
- ***If you are a validator:***
  - Do not forget to set your `WANDB_API_KEY` and to set `WAND_ENABLED` to 1
  - **On Finney**, do not forget to setup your ReadyAI API key by following the steps [here](https://github.com/afterpartyai/bittensor-conversation-genome-project/blob/main/docs/generate-validator-api-key.md) and make sure you have a file called `readyai_api_data.json` containing your API key.
  - **On Test net**, rename the provided API key in the root of the repository from `testnet_readyai_api_data.json` to `readyai_api_data.json` using `cp testnet_readyai_api_data.json readyai_api_data.json`. It will be pre-loaded in the Docker automaticaly.

---

## How to Run a Bittensor Miner on Subnet 33 Using Runpod

This guide walks you through the process of deploying a Bittensor miner on Subnet 33 using [Runpod](https://runpod.io). In a few simple steps, you’ll go from zero to mining on the testnet or mainnet.

---

---

## ✅ Requirements

- A [Runpod.io](https://runpod.io) account  
- An OpenAI API key

---

---

## 🌍 Make Sure Your Miner is Reachable

Validators need to be able to reach your miner's Axon port.

1. Click **Connect** on your pod.
    ![Miner Connect Button](docs/deploy-miner-on-runpod/runpod-miner-connect-button.png)
2. Note the **Direct TCP** port (not port 22). This is your Axon port and **must** be publicly accessible.
    ![Miner Axon Port](docs/deploy-miner-on-runpod/runpod-miner-axon-port.png)

To test if it's reachable:

```
curl <YOUR_POD_IP>:<AXON_PORT>
```

You should:
- Get a JSON-like response in your terminal
    ![Axon reachable curl](docs/deploy-miner-on-runpod/runpod-miner-reachable-curl.png)
- See logs in your miner indicating it received a connection
    ![Axon reached in miner](docs/deploy-miner-on-runpod/runpod-miner-axon-reached.png)

---

---

## 🔑 Registering your miner

You will need:
- Enough Tao to pay the registration fee

You can register by following these steps:
1. Connect via SSH into your miner as explained [here](#Connect-via-SSH)
2. Run the following command and complete the prompts:
```
btcli s register --netuid 138 --wallet.name default --wallet.hotkey default --network test --wallet.path /workspace/wallets
```

You can change the `--netuid` to `33` and the `--network` to `finney` if you want to register on the main Bittensor network

---

---

## 🎉 Your Miner Is Live!

You should now see logs indicating that the miner is running and active. When it actually handles validator requests, you will see logs like this:
![Miner is working](docs/deploy-miner-on-runpod/runpod-miner-is-working.png)
> It can take up to 1 hour before validators send requests to your miner.

---


*README source used for excerpts: `https://raw.githubusercontent.com/afterpartyai/bittensor-conversation-genome-project/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

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
| 8103642 | 0.006949432 |
| 8103690 | 0.006915876 |
| 8103738 | 0.00691587 |
| 8103786 | 0.006915815 |
| 8103834 | 0.00691581 |
| 8103882 | 0.006915801 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Meta / og:description:** ReadyAI (readyai.ai) enables structured data processing at scale, democratizing access to the valuable digital commodity of structured data – the key ingredient for high quality fine tuned models a...
- **Fetched from:** [https://github.com/afterpartyai/bittensor-conversation-genome-project](https://github.com/afterpartyai/bittensor-conversation-genome-project)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

