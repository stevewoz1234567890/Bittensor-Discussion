# NetUID 58 — Handshake (`خ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Handshake** (NetUID **58**) (`خ`).

Trustless micropayments for autonomous AI agents

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `45`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,327.661631135. **Alpha liquidity in pool (`alpha_in`)** = ‎1,699,677.649704724خ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,262,041.301441240خ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004904863`** *(also **moving-average price** `0.004678783239796758` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎353,194.104526630خ‎`. **Owner hotkey / coldkey (chain):** `5HHaedKuMkEr4UHk4D1x1QmdXtmg1FJH4PP2G3FUzLzUAyR2` / `5CigXk8XsnSqi8unxvYma6n8wYD35obs1XCS9eibjFF4vYEN`.
- **Subnet registered at block:** `4367003` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎33.954684852خ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000خ‎` · α-in `‎0.000000000خ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104390`
- **Liquidity constant `k`:** `14154340348743745016954981740`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Handshake` |
| Symbol (API) | `خ` |
| Rank | `63` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004648204` |
| Market cap | `17938671589098.210551216` |
| Market cap Δ 1d | `0.41794035191850751` |
| Liquidity | `16222230553996` |
| Total τ | `8105921179712` |
| Total α | `4961485951145964` |
| α in pool | `1746117290524264` |
| α staked | `2113152136785340` |
| Price Δ 1h | `-0.075155319560590752` |
| Price Δ 1d | `0.307642640789236306` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `58` |
| Owner SS58 (API) | `5CigXk8XsnSqi8unxvYma6n8wYD35obs1XCS9eibjFF4vYEN` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `4367003` |
| Registration wall time | `2024-11-28T21:05:00Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `16` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `16` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <img src="HS58.png" width="120" />
</p>

<h1 align="center">Handshake58</h1>

<p align="center">
  <strong>AI Provider Directory  DRAIN & MPP Protocols  Bittensor Subnet 58</strong>
</p>

<p align="center">
  <a href="https://handshake58.com">Live Marketplace</a>
  <a href="docs/thesis.html">Thesis</a>
  <a href="https://github.com/kimbo128/DRAIN">DRAIN Protocol</a>
</p>

---

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Discover AI providers, pay with USDC micropayments, and run pre-built AI skills. No API keys, no subscriptions — powered by Bittensor Subnet 58.

**Fetched document title:** Handshake58 | AI Agent Marketplace

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
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5CigXk8XsnSqi8unxvYma6n8wYD35obs1XCS9eibjFF4vYEN` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
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

### Prerequisites

- **Node.js** >= 18 and npm
- **Polygon wallet**  You need a private key to receive USDC payments (see [Wallet Setup](#wallet-setup) below)
- **API key** for your chosen backend (e.g. OpenAI, Anthropic)  not needed for self-hosted like Ollama
- **Alchemy account** (free)  for reliable Polygon RPC ([sign up here](https://www.alchemy.com/))

---

### Step 1: Clone & Install

```bash
git clone https://github.com/Handshake58/HS58.git
cd HS58/providers/hs58-openai  # or hs58-claude, hs58-grok, hs58-custom, etc.

npm install
cp env.example .env
```

---

# Required

OPENAI_API_KEY=sk-...                 # Your backend API key
PROVIDER_PRIVATE_KEY=0x...            # Polygon wallet private key (receives USDC)

---

# Recommended  use Alchemy for reliable claiming (free tier is fine)

POLYGON_RPC_URL=https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY

---

### Bittensor Wallet (for Miners/Validators)

See the [HS58-subnet README](https://github.com/Handshake58/HS58-subnet) for Bittensor wallet setup with `btcli`.

---

---

## For Miners (Bittensor Subnet 58)

Run a provider + register as a Bittensor miner to earn TAO incentives.

---

### 10 Minute Setup

1. **Deploy a provider**  Pick a template above, deploy on Railway (see [Quick Start](#quick-start--deploy-a-provider))
2. **Install btcli**  `pip install bittensor` (Python >= 3.9)
3. **Create wallet**  `btcli wallet new_coldkey` + `btcli wallet new_hotkey`
4. **Fund with TAO**  Send ~0.1 TAO to your coldkey for registration
5. **Register**  `btcli subnet register --netuid 58`
6. **Deploy miner neuron**  Fork [HS58-subnet](https://github.com/Handshake58/HS58-subnet), set `NEURON_TYPE=miner`
7. **Done**  Miner auto-registers on handshake58.com, validator scores you

See the full guide in the [HS58-subnet README](https://github.com/Handshake58/HS58-subnet).

---

## For Validators

Run a validator to score providers on Subnet 58.

1. **Install btcli**  `pip install bittensor`
2. **Create wallet + stake TAO**  Need enough stake for weight-setting permission
3. Fork [HS58-subnet](https://github.com/Handshake58/HS58-subnet), set `NEURON_TYPE=validator`
4. Deploy on Railway as worker service
5. See the [HS58-subnet README](https://github.com/Handshake58/HS58-subnet) for full setup

---

---





#### CPU / GPU / RAM lines (automatic grep)

- `| [DRAIN Protocol](https://github.com/kimbo128/DRAIN) | Core protocol, smart contracts, SDK |`


*Primary README URL used: `https://raw.githubusercontent.com/Handshake58/HS58/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://handshake58.com](https://handshake58.com)
- **GitHub:** [https://github.com/Handshake58/HS58](https://github.com/Handshake58/HS58)
- **Logo URL:** [https://github.com/Handshake58/HS58/blob/main/HS58.png?raw=true](https://github.com/Handshake58/HS58/blob/main/HS58.png?raw=true)
- **Contact:** hello@handshake58.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004650472 |
| 8104292 | 0.004775608 |
| 8104340 | 0.004769024 |
| 8104388 | 0.00476913 |
| 8104436 | 0.004904863 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.00426374 --> 0.007351702
    line [0.007099956, 0.007138739, 0.007110328, 0.006689298, 0.00640185, 0.006050204, 0.005447796, 0.005542638, 0.005727418, 0.005691967, 0.00496350570984, 0.004844691, 0.00535211, 0.005556428, 0.00574178, 0.00540282870466, 0.004476703, 0.004717631, 0.00553481, 0.005814922, 0.006446389, 0.006911185, 0.006527374, 0.006069353, 0.005809448, 0.005424334, 0.005615323, 0.005606346, 0.005492216, 0.005700211, 0.005746594, 0.005083317, 0.005315773, 0.005198255, 0.005229468, 0.005181071, 0.005219085, 0.005030982, 0.005028389, 0.005055798, 0.005108455, 0.005180073, 0.005156482, 0.004991696, 0.004848212, 0.004952905, 0.004804605, 0.004806663, 0.004894965, 0.004804817, 0.004779558, 0.004778958, 0.00474815, 0.004743704, 0.00468795, 0.004648204]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

