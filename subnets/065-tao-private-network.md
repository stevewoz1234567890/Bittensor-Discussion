# NetUID 65 — TAO Private Network (`ص`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**TAO Private Network** (NetUID **65**) (`ص`).

Developer-friendly Decentralised VPN infrastructure.



#### SubnetIdentity `additional` *(chain)*



-

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `52`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,659.170107383. **Alpha liquidity in pool (`alpha_in`)** = ‎1,906,202.922682122ص‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,007,019.394906272ص‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004017814`** *(also **moving-average price** `0.004010861739516258` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎191,824.838304453ص‎`. **Owner hotkey / coldkey (chain):** `5DAmVrUgpTX9xmRyZ7R3UUFNSzh7ZNY6qYxv9N4VeCq6mHHL` / `5GxEEHxLWpvcAGghL8LG7xNjrxZk4SEPW1VT43hGPZ2TP9mZ`.
- **Subnet registered at block:** `4950813` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎39.208325314ص‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ص‎` · α-in `‎0.000000000ص‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104383`
- **Liquidity constant `k`:** `14599932444013016805114306726`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `TAO Private Network` |
| Symbol (API) | `ص` |
| Rank | `64` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004024152` |
| Market cap | `17124253251100.178286312` |
| Market cap Δ 1d | `0.676446155735899312` |
| Liquidity | `15330015645266` |
| Total τ | `7665215054566` |
| Total α | `4912989317588394` |
| α in pool | `1904699571661334` |
| α staked | `2350669820722497` |
| Price Δ 1h | `0.130956590241730986` |
| Price Δ 1d | `0.562619607270822598` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `65` |
| Owner SS58 (API) | `5GxEEHxLWpvcAGghL8LG7xNjrxZk4SEPW1VT43hGPZ2TP9mZ` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4950813` |
| Registration wall time | `2025-02-18T03:15:12Z` |
| Registration cost snapshot | `37274536408` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `13` |
| Active dual-role | `1` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `12` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

# TPN - Tao Private Network

The TPN subnet coordinates miners that offer VPN connections in a wide variety of geographic locations.

In the TPN subnet, there are three kinds of nodes:

- **Workers**: These are easy to run nodes that provide VPN connections and get rewarded by mining pools. They are simple to set up machines with no Bittensor neuron at all.
- **Miners**: These nodes offer the VPN connections that workers provide and are given subnet emissions, they are responsible for distributing those rewards to workers however they see fit. Profitability depends on how you decide to pay the workers that sign up to your pool
- **Validators**: These nodes validate the work of miners and act as an interface to end users

Want to know more? Please read the [FAQ](#faq).

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** TAO Private Network

**Fetched document title:** TPN

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
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5GxEEHxLWpvcAGghL8LG7xNjrxZk4SEPW1VT43hGPZ2TP9mZ` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `True` |
| `commit_reveal_period` | `1` |
| `liquid_alpha_enabled` | `False` |
| `user_liquidity_enabled` (subnet pool) | `False` |
| `bonds_reset_enabled` / `bonds_moving_avg` | `False` / `900000` |
| `subnet_is_active` | `True` |
| `yuma_version` | `2` |
| `alpha_sigmoid_steepness` / `alpha_high` / `alpha_low` | 1000.0, `58982`, `45875` |

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

## Preparing your machine

Before starting your server, please prepare your machine by setting up the required enrivonment.

---

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

# Add the current user to docker for rootless docker running

if [ -z "$USER" ]; then
    USER=$(whoami)
fi
sudo groupadd docker &> /dev/null
sudo usermod -aG docker $USER
newgrp docker << EOF
    sudo service docker start
EOF
```

For miners and validators, you also need to install python and Bittensor components:

> [!CAUTION]
> Workers: ignore the setup steps below, you do NOT need them.

```bash

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

### 2: Configure your environment

You need so set some settings so make sure your server operates how you want. This influences things like on what address you get paid and so forth.

```bash
cd tpn-subnet/federated-container

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

You will now need to register your key with Bittensor. The registration costs for this can be found on our [Taostats subnet page](https://taostats.io/subnets/65/registration), as well as the amount of available registration s…

---





#### CPU / GPU / RAM lines (automatic grep)

- - [ ] Have a Debian/Ubuntu machine with 2 cores and 2GiB+ RAM ready
- 3. While speed and bandwidth size will matter soon, at this stage what matters most is that your workers and mining pool respond with reasonable speed. What matters most there is having a decent CPU and not being stingy on RAM
- - 2 CPU cores
- - 1-2GB RAM for a worker, 4-8GB RAM for a mining pool, 8-16GB RAM for a validator
- - 10-20 GB disk space for a worker, 50GB disk space for a mining pool or validator


*Primary README URL used: `https://raw.githubusercontent.com/taofu-labs/tpn-subnet/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://tpn.taofu.xyz/](https://tpn.taofu.xyz/)
- **GitHub:** [https://github.com/taofu-labs/tpn-subnet](https://github.com/taofu-labs/tpn-subnet)
- **Discord:** [https://discord.gg/GRVZyPYd6G](https://discord.gg/GRVZyPYd6G)
- **Logo URL:** [https://tpn.taofu.xyz/img/logo.jpg](https://tpn.taofu.xyz/img/logo.jpg)
- **Contact:** contact@taoprivatenetwork.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.00402414 |
| 8104292 | 0.004018831 |
| 8104340 | 0.004017818 |
| 8104388 | 0.004017817 |
| 8104436 | 0.004017813 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

