# NetUID 106 — VoidAI (`Դ`)

## Overview

**VoidAI** (NetUID **106**) (`Դ`).

Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `234`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,610.200634691. **Alpha liquidity in pool (`alpha_in`)** = ‎1,853,333.130034810Դ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,972,389.104670705Դ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004122417`** *(also **moving-average price** `0.00411937409080565` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎294,788.554342339Դ‎`. **Owner hotkey / coldkey (chain):** `5D7FVSM1fJM56zHJuMBuQ5LH32mkLni52JonoeppFrezvyHy` / `5E5Ctr2D9SjvLwNn45UNhBpjuQ7QWuinMqpAXY1ueRfJr5PT`.
- **Subnet registered at block:** `5558480` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎172.914425667Դ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000Դ‎` · α-in `‎0.000000000Դ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004122417`
- **Market cap:** `13284750341513.167188945`
- **Liquidity:** `15250412636598`
- **Total τ:** `7610200884574`
- **Total α:** `3825709234705515`
- **α in pool:** `1853333069416388`
- **α staked:** `1369230378559197`
- **Price Δ 1h:** `0.031957487078692582`
- **Price Δ 1d:** `0.089882402642571773`
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

Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP - v0idai/SN106

**Fetched document title:** GitHub - v0idai/SN106: Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP · GitHub

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
- **Owner SS58 (`owner_ss58`):** `5E5Ctr2D9SjvLwNn45UNhBpjuQ7QWuinMqpAXY1ueRfJr5PT`

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
- **`commit_reveal_weights_enabled`:** `False`
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

#### Minimum Specifications

- **CPU**: 4 cores 
- **RAM**: 8GB RAM
- **Storage**: 50GB+ SSD storage
- **Network**: Stable internet connection (50+ Mbps)
- **OS**: Linux (Ubuntu 20.04+ recommended), macOS, or Windows

---

#### Recommended Specifications

- **CPU**: 8 cores 
- **RAM**: 16GB RAM
- **Storage**: 100GB+  SSD
- **Network**: High-speed internet (100+ Mbps)
- **OS**: Linux (Ubuntu 22.04 LTS)

---

#### Required Software

- **Node.js**: v18.0.0 or higher
- **npm**: v8.0.0 or higher
- **Git**: Latest version

---

#### 2. Install Dependencies

```bash
npm install
```

---

#### 3. Configure Environment

```bash

---

# Copy environment template

cp .env.example .env

---

# Edit environment variables

nano .env
```

---

#### 4. Required Environment Variables

```bash

---

#### 5. Run the Validator

```bash

---

# Start the validator

npm run validator

```

---

### What the Validator Does

1. **Data Collection**: Fetches NFT liquidity positions from enabled chains
2. **Performance Analysis**: Calculates current tick data and position quality (only in-range positions get rewards)
3. **Weight Calculation**: Determines miner weights based on position quality and subnet performance
4. **Weight Submission**: Submits calculated weights to the BitTensor network every 20 minutes
5. **Distribution Policy**: Burn disabled (0%). 100% of weight is allocated to miners; UID 0 receives 0 units.

---

#### CPU / GPU / RAM lines (automatic grep)

- - **CPU**: 4 cores
- - **RAM**: 8GB RAM
- - **Storage**: 50GB+ SSD storage
- - **CPU**: 8 cores
- - **RAM**: 16GB RAM
- - **Storage**: 100GB+  SSD


*Primary README URL used: `https://raw.githubusercontent.com/v0idai/SN106/main/README.md`*

## On-chain identity — description


Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/v0idai/SN106](https://github.com/v0idai/SN106)
- **Discord:** [https://discord.gg/Qu8gGDJETB](https://discord.gg/Qu8gGDJETB)
- **Contact:** voidai7777@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.004121092 |
| 8104072 | 0.004122429 |
| 8104120 | 0.004122423 |
| 8104168 | 0.004122419 |
| 8104216 | 0.004122417 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.005324814 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005208443 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005157412 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.00519933 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005028496 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005053658 |
| 2026-03-15T23:59:48Z | 7754226 | 0.004912185 |
| 2026-03-16T23:59:48Z | 7761426 | 0.004791066 |
| 2026-03-17T23:59:48Z | 7768619 | 0.004585323 |
| 2026-03-18T23:59:48Z | 7775819 | 0.004626883 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00468844016989360114 |
| 2026-03-20T23:59:48Z | 7790201 | 0.004547435 |
| 2026-03-21T23:59:48Z | 7797398 | 0.004433012 |
| 2026-03-22T23:59:48Z | 7804598 | 0.004441814 |
| 2026-03-23T23:59:48Z | 7811798 | 0.00452222 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00414820714468631473 |
| 2026-03-25T23:59:48Z | 7826196 | 0.003993367 |
| 2026-03-26T23:59:48Z | 7833396 | 0.003932354 |
| 2026-03-27T23:59:48Z | 7840596 | 0.003926484 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.003981641 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004149082 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004155111 |
| 2026-03-31T23:59:48Z | 7869291 | 0.004144059 |
| 2026-04-01T23:59:48Z | 7876474 | 0.004176214 |
| 2026-04-02T23:59:48Z | 7883622 | 0.004199454 |
| 2026-04-03T23:59:48Z | 7890794 | 0.00420171 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.004188564 |
| 2026-04-05T23:59:48Z | 7905188 | 0.004154436 |
| 2026-04-06T23:59:48Z | 7912388 | 0.004101197 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004141594 |
| 2026-04-08T23:59:48Z | 7926788 | 0.004316964 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004302392 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004060561 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004041235 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004054232 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004153124 |
| 2026-04-14T23:59:48Z | 7969979 | 0.004223767 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.00426092 |
| 2026-04-16T23:59:48Z | 7984379 | 0.00414333 |
| 2026-04-17T23:59:48Z | 7991579 | 0.0040509 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004072984 |
| 2026-04-19T23:59:48Z | 8005979 | 0.004162113 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004178277 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004125596 |
| 2026-04-22T23:59:48Z | 8027562 | 0.004179497 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004186834 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004204024 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004149973 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004172046 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.00414629 |
| 2026-04-28T23:59:48Z | 8070646 | 0.004224488 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004146222 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004120289 |
| 2026-05-01T23:59:48Z | 8092168 | 0.004107945 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004118311 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004122417 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

