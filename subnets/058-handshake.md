# NetUID 58 — Handshake (`خ`)

## Overview

**Handshake** (NetUID **58**) (`خ`).

Trustless micropayments for autonomous AI agents

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `186`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,105.920933288. **Alpha liquidity in pool (`alpha_in`)** = ‎1,746,117.343541936خ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,215,381.607604028خ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004648203`** *(also **moving-average price** `0.004673666320741177` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎351,629.166976476خ‎`. **Owner hotkey / coldkey (chain):** `5HHaedKuMkEr4UHk4D1x1QmdXtmg1FJH4PP2G3FUzLzUAyR2` / `5CigXk8XsnSqi8unxvYma6n8wYD35obs1XCS9eibjFF4vYEN`.
- **Subnet registered at block:** `4367003` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎140.345062928خ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000خ‎` · α-in `‎0.000000000خ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004648204`
- **Market cap:** `17938671589098.210551216`
- **Liquidity:** `16222230553996`
- **Total τ:** `8105921179712`
- **Total α:** `4961485951145964`
- **α in pool:** `1746117290524264`
- **α staked:** `2113152136785340`
- **Price Δ 1h:** `-0.075155319560590752`
- **Price Δ 1d:** `0.307642640789236306`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `16`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `16`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Trustless micropayments for autonomous AI agents

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
- **`difficulty` (PoW field on info view):** 10000000
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CigXk8XsnSqi8unxvYma6n8wYD35obs1XCS9eibjFF4vYEN`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
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

## On-chain identity — description


Trustless micropayments for autonomous AI agents

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://handshake58.com](https://handshake58.com)
- **GitHub:** [https://github.com/Handshake58/HS58](https://github.com/Handshake58/HS58)
- **Logo URL:** [https://github.com/Handshake58/HS58/blob/main/HS58.png?raw=true](https://github.com/Handshake58/HS58/blob/main/HS58.png?raw=true)
- **Contact:** hello@handshake58.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.004651692 |
| 8104072 | 0.004651688 |
| 8104120 | 0.004651682 |
| 8104168 | 0.004651678 |
| 8104216 | 0.004648203 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

