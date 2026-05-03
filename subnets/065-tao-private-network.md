# NetUID 65 — TAO Private Network (`ص`)

## Overview

Developer-friendly Decentralised VPN infrastructure.

-

**From crawled page (site or GitHub):** TAO Private Network

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
- **Owner SS58 (`owner_ss58`):** `5GxEEHxLWpvcAGghL8LG7xNjrxZk4SEPW1VT43hGPZ2TP9mZ`

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

## Miner / validator compute notes (README excerpts)

### 1: Installing dependencies

Requirements:

- Linux OS (Ubuntu LTS recommended)
- 2 CPU cores
- 1-2GB RAM for a worker, 4-8GB RAM for a mining pool, 8-16GB RAM for a validator
- 10-20 GB disk space for a worker, 50GB disk space for a mining pool or validator
- Publically accessible IP address

All servers share some of the same dependencies. No matter which you choose to run, please install the dependencies by executing the following commands:

```bash

---

# Install the required system dependencies

sudo apt update
sudo apt install -y git jq netcat-openbsd
sudo apt upgrade -y # OPTIONAL, this updated system packages

---

# Install docker

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

---

# Install wireguard and wireguard-tools, these are commonly preinstalled on Ubuntu

sudo apt install -y wireguard wireguard-tools
sudo modprobe wireguard

---

# Clone the TPN repository, it contains all the required code

cd ~
git clone https://github.com/taofu-labs/tpn-subnet.git

---

# Install python, node and pm2

sudo apt install -y nodejs npm python3 python3-venv python3-pip
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
RC_PATH="$HOME/.${SHELL##*/}rc"
echo "Using rc path $RC_PATH"
echo 'export PATH=~/.npm-global/bin:$PATH' >> "$RC_PATH"
source "$RC_PATH"
npm install -g pm2

---

# Install the required python dependencies

cd ~/tpn-subnet
python3 -m venv venv
source venv/bin/activate
TPN_CACHE="$HOME/.tpn_cache"
mkdir -p $TPN_CACHE
export TMPDIR=$TPN_CACHE
export WANDB_CACHE_DIR=$TPN_CACHE
pip3 install -r requirements.txt
export PYTHONPATH=.
```

---

# Edit .env with your specific configuration

nano .env
```

Take note of the mandatory and optional sections. For miners and validators, you need to get these two external API keys:

- Make an account at https://lite.ip2location.com/. Set it as the `IP2LOCATION_DOWNLOAD_TOKEN` environment variable in the docker compose file. Add this in the specified location in the `.env` file you copied above.
- Make an account at https://www.maxmind.com and generate a license key in account settings. Add this in the specified location in the `.env` file you copied above.

---

### 3: Configure keys (mining pool/validator only)

> [!CAUTION]
> Workers: ignore this section

The next step is to configure the Bittensor keys for your miner and/or validator. Note that these keys are stored in the `~/.bittensor` directory. You have 2 options:

1. Copy existing cold and hotkeys to `~/.bittensor`
2. Generate a new coldkey and hotkey

If you have existing keys that you are deploying, copy them in the following structure:

```bash
~/.bittensor/
├── tpn_coldkey # This directory name is how btcli knows the name of your coldkey
│   ├── coldkeypub.txt # This file contains your public coldkey, NOT THE PRIVATE KEY, the miner machine does not need the private key
|   └── hotkeys # This directory contains the private keys of your hotkeys
|       ├── tpn_hotkey # This file contains the private key of your hotkey in json format
```

If you want to generate new keys, execute the following commands:

```bash
btcli w new_coldkey --wallet.name tpn_coldkey
btcli w new_hotkey --wallet.name tpn_coldkey --wallet.hotkey tpn_hotkey
``` 

Note that the above will generate a private key for your coldkey as well. This is a key with security implications and should be stored securely. Ideally you delete it from your miner server after backing it up safely. This can be done by running `rm ~/.bittensor/wallets/tpn_coldkey/coldkey`, only do this AFTER YOU SECURELY BACKED UP YOUR KEY AND SEED PHRASE.

You will now need to register your key with Bittensor. The registration costs for this can be found on our [Taostats subnet page](https://taostats.io/subnets/65/registration), as well as the amount of available registration slots. The slots become available every 72 minutes, so if there are none available you should wait.

To register:

1. Get your cold key public key by runing: `cat ~/.bittensor/wallets/tpn_coldkey/coldkeypub.txt | jq -r '.ss58Address'`
2. Send TAO to your public key, we recommend sending the registration cost and some extra for gas fees
3. Verify that you have a balance on your wallet using `btcli wallet balance --ss58 YOUR_ss58_ADDRESS`
4. Register by running `btcli s register --wallet.name tpn_coldkey --hotkey tpn_hotkey --netuid 65`, this commamnd will ask for the colekey password you created previously

You may now continue with the rest of the setup. Your registration is immune to being deregistered for 5000 blocks which is about 16 hours. Make sure you finish your setup within this window.

---

### Updating your miner

The miner automatically updates some components periodically, but not all. You should regularly run the following commands to keep your miner up to date:

```bash

---

## Running a validator

Validators are the interface between end users and miners. They send work requests to miners, which the miners complete and submit to the validator. Running a validator is more complicated than a miner and requires more setup than a miner.

---

### Step 1: Configure the validator settings

The validator neuron needs you to supply a WanDB API key. You can get one by signing up at [WanDB](https://wandb.ai/site). Once you have the key, add it to your environment by running the code below:

```bash

---

### Step 2: Start the validator

The validator also consists out of two components:

1. A validator neuron that is managed through `pm2`…


*README source used for excerpts: `https://raw.githubusercontent.com/taofu-labs/tpn-subnet/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Developer-friendly Decentralised VPN infrastructure.

## On-chain identity — additional field


-

## Registered contact & links


- **Website:** [https://tpn.taofu.xyz/](https://tpn.taofu.xyz/)
- **GitHub:** [https://github.com/taofu-labs/tpn-subnet](https://github.com/taofu-labs/tpn-subnet)
- **Discord:** [https://discord.gg/GRVZyPYd6G](https://discord.gg/GRVZyPYd6G)
- **Logo URL:** [https://tpn.taofu.xyz/img/logo.jpg](https://tpn.taofu.xyz/img/logo.jpg)
- **Contact:** contact@taoprivatenetwork.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.003998093 |
| 8103690 | 0.004029497 |
| 8103738 | 0.004029493 |
| 8103786 | 0.004029453 |
| 8103834 | 0.00402945 |
| 8103882 | 0.004018891 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** TPN
- **Meta / og:description:** TAO Private Network
- **Fetched from:** [https://tpn.taofu.xyz/](https://tpn.taofu.xyz/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

