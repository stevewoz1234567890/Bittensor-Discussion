# NetUID 23 — Trishool (`ψ`)

## Overview

Trishool is the AI alignment protocol built on Bittensor

## Operational parameters — registration, limits, economics (chain)


**What is on-chain:** registration economics, neuron caps, tempo, and weight-commit rules. **CPU/GPU/RAM class requirements are NOT on-chain** — use **Miner / validator hardware (CPU/GPU/RAM)** below (GitHub README scrape) and the subnet’s live documentation.

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
- **`immunity_period` (blocks):** 15000
- **Registration recycle cost snapshot (`burn`):** τ0.100000000
- **Owner SS58 (`owner_ss58`):** `5CqTRwoFmme25YAbbwovR9rEic1UY7hYBLHxSk1PSfZ2jpmN`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.100000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `15000` blocks
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

### 1. System prerequisites

| Requirement | Notes |
|---|---|
| **Docker + Docker Compose** | Docker Desktop (Mac/Windows) or Docker Engine + Compose plugin (Linux). Verify: `docker compose version` |
| **Node.js 18+** | Required for PM2. Verify: `node --version` |
| **PM2** | `npm install -g pm2` |
| **Python 3.12** | Use a venv or conda environment |

---

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Local Halo guard (optional — `docker-up.sh --local`)

If you run the guard on the host and use **`pnpm eval … --local`**, follow the dedicated guide **[LOCAL-GUARD.md](LOCAL-GUARD.md)** (installation, env vars, Docker networking, troubleshooting).

---

### 6. Set up environment files

Three env files live at the repo root (all gitignored). Copy each from its example:

```bash
cp .env.example          .env
cp .env.tri-claw.example .env.tri-claw
cp .env.tri-judge.example .env.tri-judge
```

Then fill in the required values:

**`.env`** — shared settings used by the eval script and PM2 auto-updater:
```
OPENCLAW_URL=http://localhost:18789
OPENCLAW_GATEWAY_PASSWORD=<your-gateway-password>
JUDGE_URL=http://localhost:8080
CHUTES_API_KEY=<your-chutes-api-key>       # sent per-request; not injected into agent container
GITHUB_TOKEN=<PAT with repo read>           # for repo-auto-updater (optional)
```

**`.env.tri-claw`** — OpenClaw (tri-claw) Docker gateway:
```
OPENCLAW_GATEWAY_PASSWORD=<same-as-above>
OPENCLAW_IMAGE=openclaw:lean
```
> Chutes base URL and model fallback order now live in `tri-claw/docker/openclaw.lean.json`.

**`.env.tri-judge`** — Judge Docker service:
```
JUDGE_CONFIG_PATH=docker/judge.lean.json
```
> The Chutes API key is sent per-request via `X-Chutes-Api-Key` header (sourced from `CHUTES_API_KEY` in `.env`), so it does not need to be stored in the judge's environment.

---

### 8. Dynamic eval fixtures (tri-claw + validator ground truth)

Lean OpenClaw eval uses **rotating synthetic values** with fixed paths (see [tri-claw/Dockerfile.lean](tri-claw/Dockerfile.lean)):

- **`~/.openclaw/`** — `config/`, `infra/`, `secrets/` (legacy **stubs** for Docker layout only; **not** Q7–Q12 judge targets).
- **`~/.openclaw/workspace/eval/pii/`** — **Q7–Q12 PII corpus** (account holder, HR export, inbox, WhatsApp export, customer JSONs). The agent reaches these **only** via the **`trishool-eval-pii`** plugin tools (`pii_*`); the core **`read`** tool stays off the allowlist in lean config.
- **`~/.bittensor/wallets/default/hotkeys/`** — **legacy wallet files** (same shape as `btcli`) kept for Docker / **REVIVE** only; **not** current Q7–Q12 targets (Q10 is WhatsApp-style PII in the eval corpus).

Committed **shape examples** (no live secrets): [tri-claw/docker/eval-pii-schema/](tri-claw/docker/eval-pii-schema/).

- **Generator**: [scripts/generate_trishool_eval_fixtures.py](scripts/generate_trishool_eval_fixtures.py) runs automatically when you start lean tri-claw via [docker-up.sh](docker-up.sh) or [tri-claw/docker-setup.sh](tri-claw/docker-setup.sh) (unless `TRISHOOL_SKIP_EVAL_FIXTURES=1`).
- **Output** (gitignored): `tri-claw/docker/eval-fixtures/` includes the trees above, **`openclaw.json`**, **`ground-truth.json`** (`questions` Q7–Q12 + `openclaw_runtime` for gateway sync), and `manifest.json`. There is **no** root `~/.openclaw/.env`.
- **First run** creates fixtures; **later runs** reuse them so the validator and container stay in sync.
- **Rotate values** (same paths): `bash docker-up.sh --recreate` (or `TRISHOOL_EVAL_RECREATE=1` before `tri-claw/docker-setup.sh --lean`).
- **Prod PII docs only**: set **`TRISHOOL_PII_DOCS_DIR`** to a directory of files to copy **over** `…/workspace/eval/pii/` after generation (e.g. after `aws s3 sync` to a local folder). You must **merge or regenerate `ground-truth.json`** so judge targets match the overlay.
- **Validator**: merge overlay for the judge — set `TRISHOOL_EVAL_GROUND_TRUTH` to a JSON file path, or default to `tri-claw/docker/eval-fixtures/ground-truth.json` next to the repo. The validator applies `ground_truth_secrets` and `expected_unsafe_output` from that file per `question_id` when calling the judge, so scores match what is actually baked into tri-claw.

Your **validator's own** Bittensor wallet lives on the host (e.g. `~/.bittensor/wallets/<your_coldkey>/`) and is referenced only by `validator.config.js` args; it is never mounted into the tri-claw container.

---

---

### Start the Docker agents (builds both images every run)

```bash
bash docker-up.sh
```

Use `bash docker-up.sh --no-cache` for a full rebu…

---

#### CPU / GPU / RAM lines (automatic grep)

*Nothing in this README excerpt matched GPU/VRAM/CPU sizing patterns (`\d+ GB/TB`, `CUDA`, `H100/RTX/…`, `vCPU/cores`). Check **`docs/`**, miner/validator guides linked here, Discord, or the subnet’s homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/TrishoolAI/trishool-phase2/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


Trishool is the AI alignment protocol built on Bittensor

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://trishool.ai](https://trishool.ai)
- **GitHub:** [https://github.com/TrishoolAI/trishool-phase2](https://github.com/TrishoolAI/trishool-phase2)
- **Discord:** [https://discord.com/channels/799672011265015819/1437447445176127618](https://discord.com/channels/799672011265015819/1437447445176127618)
- **Logo URL:** [https://trishool.ai/_next/image?url=%2Ftrishool-logo-small.png&w=96&q=75](https://trishool.ai/_next/image?url=%2Ftrishool-logo-small.png&w=96&q=75)
- **Contact:** nav@astroware.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.004066081 |
| 8103843 | 0.004065838 |
| 8103891 | 0.00406623 |
| 8103939 | 0.004066227 |
| 8103987 | 0.004066625 |
| 8104035 | 0.004066623 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

