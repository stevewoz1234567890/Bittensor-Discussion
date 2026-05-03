# NetUID 94 — Bitsota (`ᚄ`)

## Overview

**Bitsota** (NetUID **94**) (`ᚄ`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `222`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ1,934.235316237. **Alpha liquidity in pool (`alpha_in`)** = ‎383,019.734667997ᚄ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎970,039.409110400ᚄ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.005051339`** *(also **moving-average price** `0.004893454490229487` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎24,031.630512500ᚄ‎`. **Owner hotkey / coldkey (chain):** `5Ef5EsPQoMVmJ8rYectQ26BEvscvATEGm365bcQjo1Y6bxGr` / `5EZRCK9op9piMhQvHqrEL1SNQU8ENU8s9aqGnRKNsUxmPYP2`.
- **Subnet registered at block:** `6962737` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎144.664623533ᚄ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002525664` · α-out `‎1.000000000ᚄ‎` · α-in `‎0.500000000ᚄ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.005051256`
- **Market cap:** `4874480190357.248198784`
- **Liquidity:** `3868900382399`
- **Total τ:** `1934187249804`
- **Total α:** `1353042789043181`
- **α in pool:** `383016250333740`
- **α staked:** `581987342902724`
- **Price Δ 1h:** `-0.894785850588067717`
- **Price Δ 1d:** `6.016659995924095835`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `11`
- **Active miners:** `1`
- **Active dual:** `1`
- **Emission:** `2525619`
- **Max neurons:** `256`
- **Validators (metadata):** `11`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Decentralized SoTA Research



**Additional commentary (on-chain)**


https://discord.gg/jkJWJtPuw7

### Repository README excerpt *(everything before first `##` heading)*

# BitSota

**Decentralized Research Network on Bittensor**

BitSota is a decentralized research network that evolves machine learning algorithms through competitive optimization. We're a problem agnostic platform and enable the optimization of different categories of problems, with a focus on self-improving and self-generating AI.
Currently, Miners develop ML algorithms using genetic programming, while validators evaluate performance and distribute rewards through smart contract voting on the Bittensor network.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** BitSota main repository. Contribute to AlveusLabs/SN94-BitSota development by creating an account on GitHub.

**Fetched document title:** GitHub - AlveusLabs/SN94-BitSota: BitSota main repository · GitHub

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
- **Owner SS58 (`owner_ss58`):** `5EZRCK9op9piMhQvHqrEL1SNQU8ENU8s9aqGnRKNsUxmPYP2`

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

### Direct Mining

Individual miners evolve algorithms locally and submit breakthroughs to validators. Requires higher compute but offers larger individual rewards.

**Best for:** Experienced miners with dedicated hardware

**[→ Direct Mining Guide](docs/mining.md)**

---

### Pool Mining

Collaborative mining where participants handle smaller evolution and evaluation tasks. Pool aggregates results and submits to validators on behalf of all participants.

**Best for:** New miners or those with limited compute resources

**[→ Pool Mining Guide](docs/pool-mining.md)**

---

### Direct Mining Flow

```
Miner → Evolve Locally → Beat SOTA → Submit to Relay → Validators Verify → Relay Consensus → Weight Update → Emissions
```

1. Miner runs genetic programming engine for up to 150 generations
2. When algorithm beats State-of-the-Art threshold, submits to relay
3. Validators download submission and independently re-evaluate
4. Validators choose weight setting mode:
   - Relay mode: Vote on relay, wait for consensus, then set weights
   - Local mode: Set weights immediately based on own evaluation
5. Validators set on-chain weights: 90% burn, 10% winner
6. Network emissions flow to winner via Yuma consensus

---

### Pool Mining Flow

```
Pool → Assigns Tasks → Miners Execute → Pool Consensus → Submit to Validators → Epoch Rewards
```

1. Pool distributes evolution and evaluation tasks to participants
2. Multiple miners evaluate each algorithm (3+ required)
3. Pool computes median consensus with 10% tolerance
4. Rewards distributed based on reputation at epoch boundaries
5. Pool submits best algorithms to validators on behalf of participants

**[→ Detailed Rewards Guide](docs/rewards.md)**

---

### For Miners

**Desktop GUI (Recommended):**
1. Download from [bitsota.ai](https://bitsota.ai)
2. Install for your platform
3. Import your Bittensor hotkey
4. Choose mining mode (Direct or Pool)
5. Start mining

See detailed setup guides:
- [Direct Mining Setup](docs/mining.md#setup)
- [Pool Mining Setup](docs/pool-mining.md#setup)

---

### For Validators

```bash
git clone https://github.com/AlveusLabs/BitSota.git
cd BitSota
pip install -r requirements.txt
pip install -e .

cp validator_config.yaml.example validator_config.yaml

---

# Edit validator_config.yaml with your wallet and burn_hotkey

python neurons/validator_node.py
```

**[→ Full Validator Setup](docs/validation.md#setup)**

---

## Requirements

**Minimum:**
- Python 3.10+
- 4GB RAM
- 2GB storage
- Stable internet connection

**For Validation:**
- 16GB RAM
- 8+ CPU cores

---

#### CPU / GPU / RAM lines (automatic grep)

- - 2GB storage
- - 16GB RAM
- - 8+ CPU cores


*Primary README URL used: `https://raw.githubusercontent.com/AlveusLabs/SN94-BitSota/main/README.md`*

## On-chain identity — description


Decentralized SoTA Research

## On-chain identity — additional field


https://discord.gg/jkJWJtPuw7

## Registered contact & links


- **GitHub:** [https://github.com/AlveusLabs/SN94-BitSota](https://github.com/AlveusLabs/SN94-BitSota)
- **Discord (handle / invite hint):** `dev.alveuslabs`
- **Logo URL:** [https://bitsota.ai/logo.png](https://bitsota.ai/logo.png)
- **Contact:** info@bitsota.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.005066504 |
| 8104072 | 0.005066753 |
| 8104120 | 0.005066992 |
| 8104168 | 0.005051069 |
| 8104216 | 0.005051339 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.00517454 |
| 2026-03-10T23:59:48Z | 7718257 | 0.00566154 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005994666 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005901503 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005299371 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005459002 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005517145 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005575684 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005264658 |
| 2026-03-18T23:59:48Z | 7775819 | 0.00560901 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00562818508446807784 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005587722 |
| 2026-03-21T23:59:48Z | 7797398 | 0.00557646 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005910722 |
| 2026-03-23T23:59:48Z | 7811798 | 0.00582123 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00551324287826278022 |
| 2026-03-25T23:59:48Z | 7826196 | 0.004782011 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004555003 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004716633 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004837941 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004474121 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004102921 |
| 2026-03-31T23:59:48Z | 7869291 | 0.003950631 |
| 2026-04-01T23:59:48Z | 7876474 | 0.003949316 |
| 2026-04-02T23:59:48Z | 7883622 | 0.003923558 |
| 2026-04-03T23:59:48Z | 7890794 | 0.004096633 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004226617 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004346317 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004232048 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004244558 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004229573 |
| 2026-04-09T23:59:48Z | 7933987 | 0.003544461 |
| 2026-04-10T23:59:48Z | 7941184 | 0.003879977 |
| 2026-04-11T23:59:48Z | 7948384 | 0.003890286 |
| 2026-04-12T23:59:48Z | 7955584 | 0.003815359 |
| 2026-04-13T23:59:48Z | 7962784 | 0.003847064 |
| 2026-04-14T23:59:48Z | 7969979 | 0.003789897 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.003680854 |
| 2026-04-16T23:59:48Z | 7984379 | 0.003707255 |
| 2026-04-17T23:59:48Z | 7991579 | 0.003734088 |
| 2026-04-18T23:59:48Z | 7998779 | 0.00366182 |
| 2026-04-19T23:59:48Z | 8005979 | 0.003499051 |
| 2026-04-20T23:59:48Z | 8013179 | 0.003611132 |
| 2026-04-21T23:59:48Z | 8020376 | 0.00359776 |
| 2026-04-22T23:59:48Z | 8027562 | 0.003626941 |
| 2026-04-23T23:59:48Z | 8034762 | 0.003632555 |
| 2026-04-24T23:59:48Z | 8041962 | 0.003620207 |
| 2026-04-25T23:59:48Z | 8049151 | 0.003653944 |
| 2026-04-26T23:59:48Z | 8056274 | 0.003836345 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004210434 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004411787 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004503037 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004567943 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004550181 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004898348 |
| 2026-05-03T16:10:00Z | 8104202 | 0.005051256 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

