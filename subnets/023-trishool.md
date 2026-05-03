# NetUID 23 — Trishool (`ψ`)

## Overview

Trishool is the AI alignment protocol built on Bittensor

**From crawled page (site or GitHub):** A decentralized defense grid for humanity.

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

## Miner / validator compute notes (README excerpts)

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

## Running the Validator

```bash
pm2 start validator.config.js
```

Useful PM2 commands:

```bash
pm2 logs trishool-subnet          # live logs
pm2 status                        # process table
pm2 restart trishool-subnet       # restart
pm2 stop trishool-subnet          # stop without removing
```

---

## Miners

```bash
python -m alignet.cli.miner upload \
  --submission-file your_submission.json \
  --surface-area 1 \
  --coldkey coldkey_name \
  --hotkey hotkey_name \
  --network finney \
  --netuid 23 \
  --api-url https://api.trishool.ai
```

**Submission file format** (keys Q1–Qn must match the active challenge's `question_count`):

| Surface Area | Format |
|---|---|
| 1 | `{"Q1": "prompt", "Q2": "prompt", ...}` |
| 2 | `{"Q1": {"prompt": "...", "url": "..."}, ...}` |
| 3 | `{"Q1": {"prompt": "...", "endpoint": "..."}, ...}` |
| 4 | `{"Q1": {"conversation": [...]}, ...}` |
| 5 | `{"Q1": {"session1": [...], "session2": [...]}, ...}` |

---


*README source used for excerpts: `https://raw.githubusercontent.com/TrishoolAI/trishool-phase2/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

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
| 8103642 | 0.004067935 |
| 8103690 | 0.00406613 |
| 8103738 | 0.004066125 |
| 8103786 | 0.004066082 |
| 8103834 | 0.004065843 |
| 8103882 | 0.00406623 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Trishool
- **Meta / og:description:** A decentralized defense grid for humanity.
- **Fetched from:** [https://trishool.ai](https://trishool.ai)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

