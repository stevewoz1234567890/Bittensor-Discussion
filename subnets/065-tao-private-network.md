# NetUID 65 — TAO Private Network (`ص`)

## Overview

**TAO Private Network** (NetUID **65**) (`ص`).

Developer-friendly Decentralised VPN infrastructure.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `193`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,665.214837107. **Alpha liquidity in pool (`alpha_in`)** = ‎1,904,699.625701946ص‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,008,302.691886448ص‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004024152`** *(also **moving-average price** `0.004010349046438932` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎191,818.793574729ص‎`. **Owner hotkey / coldkey (chain):** `5DAmVrUgpTX9xmRyZ7R3UUFNSzh7ZNY6qYxv9N4VeCq6mHHL` / `5GxEEHxLWpvcAGghL8LG7xNjrxZk4SEPW1VT43hGPZ2TP9mZ`.
- **Subnet registered at block:** `4950813` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎145.522227046ص‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ص‎` · α-in `‎0.000000000ص‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004024152`
- **Market cap:** `17124253251100.178286312`
- **Liquidity:** `15330015645266`
- **Total τ:** `7665215054566`
- **Total α:** `4912989317588394`
- **α in pool:** `1904699571661334`
- **α staked:** `2350669820722497`
- **Price Δ 1h:** `0.130956590241730986`
- **Price Δ 1d:** `0.562619607270822598`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `13`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Developer-friendly Decentralised VPN infrastructure.



**Additional commentary (on-chain)**


-

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

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.004018882 |
| 8104072 | 0.004018879 |
| 8104120 | 0.004024115 |
| 8104168 | 0.004024154 |
| 8104216 | 0.004024151 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.004974256 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005019556 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005082045 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005557001 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005244476 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005064923 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004875599 |
| 2026-03-16T23:59:48Z | 7761426 | 0.004764901 |
| 2026-03-17T23:59:48Z | 7768619 | 0.004636518 |
| 2026-03-18T23:59:48Z | 7775819 | 0.004711172 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00465412373289286079 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004647952 |
| 2026-03-21T23:59:48Z | 7797398 | 0.004665608 |
| 2026-03-22T23:59:48Z | 7804598 | 0.004721464 |
| 2026-03-23T23:59:48Z | 7811798 | 0.004879413 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00455197861179456992 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004561839 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004458484 |
| 2026-03-27T23:59:48Z | 7840596 | 0.00447987 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004741256 |
| 2026-03-29T23:59:48Z | 7854902 | 0.00467397 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.005061171 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005134429 |
| 2026-04-01T23:59:48Z | 7876474 | 0.005090359 |
| 2026-04-02T23:59:48Z | 7883622 | 0.005077119 |
| 2026-04-03T23:59:48Z | 7890794 | 0.005276549 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.005183205 |
| 2026-04-05T23:59:48Z | 7905188 | 0.005112961 |
| 2026-04-06T23:59:48Z | 7912388 | 0.005220925 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004932919 |
| 2026-04-08T23:59:48Z | 7926788 | 0.00492447 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004670623 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004190404 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004256218 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004285606 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004202662 |
| 2026-04-14T23:59:48Z | 7969979 | 0.0042951 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.00421331 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004212247 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004194362 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004193438 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004253144 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004278815 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004243177 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004266505 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004266927 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004160568 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004145536 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004137262 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004003193 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004072832 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004097907 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004073048 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004014513 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004002806 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004024152 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

