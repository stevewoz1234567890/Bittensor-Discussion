# NetUID 58 — Handshake (`خ`)

## Overview

Trustless micropayments for autonomous AI agents

**From crawled page (site or GitHub):** Discover AI providers, pay with USDC micropayments, and run pre-built AI skills. No API keys, no subscriptions — powered by Bittensor Subnet 58.

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

## Miner / validator compute notes (README excerpts)

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


*README source used for excerpts: `https://raw.githubusercontent.com/Handshake58/HS58/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Trustless micropayments for autonomous AI agents

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://handshake58.com](https://handshake58.com)
- **GitHub:** [https://github.com/Handshake58/HS58](https://github.com/Handshake58/HS58)
- **Logo URL:** [https://github.com/Handshake58/HS58/blob/main/HS58.png?raw=true](https://github.com/Handshake58/HS58/blob/main/HS58.png?raw=true)
- **Contact:** hello@handshake58.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.004652308 |
| 8103690 | 0.004652298 |
| 8103738 | 0.004652293 |
| 8103786 | 0.004651715 |
| 8103834 | 0.004651711 |
| 8103882 | 0.004651702 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Handshake58 | AI Agent Marketplace
- **Meta / og:description:** Discover AI providers, pay with USDC micropayments, and run pre-built AI skills. No API keys, no subscriptions — powered by Bittensor Subnet 58.
- **Fetched from:** [https://handshake58.com](https://handshake58.com)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

