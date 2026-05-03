# NetUID 96 — Verathos (`᚛`)

## Overview

Verified AI inference and training subnet.

**From crawled page (site or GitHub):** Cryptographically verified AI inference and training on Bittensor. Trust the math, not the server.

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
- **Registration recycle cost snapshot (`burn`):** τ0.010000000
- **Owner SS58 (`owner_ss58`):** `5CGq1JQhmZmR8w3pXFqycUgX9mcLt8bPwMZ8YDJbEmELpw7X`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.010000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `True`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `900000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `3`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator compute notes (README excerpts)

### As a Miner

Requires NVIDIA GPU with 24 GB+ VRAM (RTX 4090, A100, H100, etc.).

**Quick start** (guided wizard handles wallet, registration, funding, HTTPS, PM2):
```bash
curl -fsSL https://verathos.ai/install.sh | bash   # or: git clone ... && cd verathos && bash scripts/setup_miner.sh
verathos setup                                       # interactive setup wizard
verathos start                                       # start mining
```

**Manual step-by-step:**
```bash
git clone https://github.com/verathos-ai/verathos && cd verathos
bash scripts/setup_miner.sh          # creates venv, installs deps, builds CUDA ext
```

Then create a wallet, register on subnet, fund your EVM address, and start:

```bash
python -m neurons.miner \
    --wallet miner --hotkey default \
    --model-id auto \
    --netuid 96 \
    --subtensor-network finney \
    --endpoint https://YOUR-PUBLIC-IP-OR-DOMAIN
```

`--model-id auto` detects your GPU and picks the optimal model. See the [Setup Guide](docs/setup.md) for wallet creation, EVM funding, model selection, and production deployment with PM2.

---

### As a Validator

No GPU required.

**Quick start:**
```bash
curl -fsSL https://verathos.ai/install.sh | bash -s – --validator   # or: git clone ... && bash scripts/setup_validator.sh
verathos setup validator                                              # interactive setup wizard
verathos start validator                                              # start validating
```

**Manual step-by-step:**
```bash
git clone https://github.com/verathos-ai/verathos && cd verathos
bash scripts/setup_validator.sh

python -m neurons.validator \
    --wallet validator --hotkey default \
    --netuid 96 \
    --subtensor-network finney
```

See the [Setup Guide](docs/setup.md) for wallet creation, EVM funding, auto-update, and running the gateway proxy.


*README source used for excerpts: `https://raw.githubusercontent.com/verathos-ai/verathos/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Verified AI inference and training subnet.

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://verathos.ai](https://verathos.ai)
- **GitHub:** [https://github.com/verathos-ai/verathos](https://github.com/verathos-ai/verathos)
- **Logo URL:** [https://raw.githubusercontent.com/verathos-ai/verathos/main/assets/logo.png](https://raw.githubusercontent.com/verathos-ai/verathos/main/assets/logo.png)
- **Contact:** info@verathos.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.024590279 |
| 8103738 | 0.024960995 |
| 8103786 | 0.024070642 |
| 8103834 | 0.024052009 |
| 8103882 | 0.023941147 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Verathos — Verified Intelligence for Everyone
- **Meta / og:description:** Cryptographically verified AI inference and training on Bittensor. Trust the math, not the server.
- **Fetched from:** [https://verathos.ai](https://verathos.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

