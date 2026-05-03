# NetUID 106 — VoidAI (`Դ`)

## Overview

Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP

**From crawled page (site or GitHub):** Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP - v0idai/SN106

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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/v0idai/SN106/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/v0idai/SN106](https://github.com/v0idai/SN106)
- **Discord:** [https://discord.gg/Qu8gGDJETB](https://discord.gg/Qu8gGDJETB)
- **Contact:** voidai7777@gmail.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.004119518 |
| 8103738 | 0.004119512 |
| 8103786 | 0.004119463 |
| 8103834 | 0.00411946 |
| 8103882 | 0.004121102 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** GitHub - v0idai/SN106: Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP · GitHub
- **Meta / og:description:** Multi-chain liquidity protocol enabling interoperability for Bittensor by leveraging Chainlink CCIP - v0idai/SN106
- **Fetched from:** [https://github.com/v0idai/SN106](https://github.com/v0idai/SN106)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

