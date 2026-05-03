# NetUID 23 — Trishool (`ψ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Trishool** (NetUID **23**) (`ψ`).

Trishool is the AI alignment protocol built on Bittensor

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `10`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ6,881.839272681. **Alpha liquidity in pool (`alpha_in`)** = ‎1,689,884.985241153ψ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,249,159.732924780ψ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004072242`** *(also **moving-average price** `0.003940909635275602` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎351,814.079599984ψ‎`. **Owner hotkey / coldkey (chain):** `5HKsvivbcTKKTJEWQpsQD5Fur8CdyibHwZb8xQzrJw5rM28H` / `5CqTRwoFmme25YAbbwovR9rEic1UY7hYBLHxSk1PSfZ2jpmN`.
- **Subnet registered at block:** `2063528` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎7.542965854ψ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ψ‎` · α-in `‎0.000000000ψ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104425`
- **Liquidity constant `k`:** `11629516857746518780909841193`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Trishool`
- **Symbol (API):** `ψ`
- **Rank:** `69`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004070134`
- **Market cap:** `16499505161286.094756602`
- **Market cap Δ 1d:** `6.170061761736476332`
- **Liquidity:** `13759897142841`
- **Total τ:** `6880047087046`
- **Total α:** `4938811718165933`
- **α in pool:** `1690325197105533`
- **α staked:** `2363473808353770`
- **Price Δ 1h:** `0.096059542160449439`
- **Price Δ 1d:** `6.032310394028623613`
#### Subnet activity (TAOStats)

- **NetUID (API):** `23`
- **Owner SS58 (API):** `5CqTRwoFmme25YAbbwovR9rEic1UY7hYBLHxSk1PSfZ2jpmN`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `2063528`
- **Registration wall time:** `2024-01-02T19:38:12Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual-role:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `12`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `100000000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

# **Trishool Subnet Phase 2**

[Discord](https://discord.com/channels/799672011265015819/1437447445176127618) • [Dashboard](https://trishool.ai/dashboard) • [Website](https://trishool.ai/) • [Twitter](https://x.com/trishoolai/) •
[Network](https://taostats.io/subnets/23/chart)
</div>

A Bittensor subnet building the SOTA AI guard model. Miners submit adversarial prompts that validators evaluate via agents (OpenClaw + Judge); scores are aggregated and written as on-chain weights.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** A decentralized defense grid for humanity.

**Fetched document title:** Trishool

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

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/TrishoolAI/trishool-phase2/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://trishool.ai](https://trishool.ai)
- **GitHub:** [https://github.com/TrishoolAI/trishool-phase2](https://github.com/TrishoolAI/trishool-phase2)
- **Discord:** [https://discord.com/channels/799672011265015819/1437447445176127618](https://discord.com/channels/799672011265015819/1437447445176127618)
- **Logo URL:** [https://trishool.ai/_next/image?url=%2Ftrishool-logo-small.png&w=96&q=75](https://trishool.ai/_next/image?url=%2Ftrishool-logo-small.png&w=96&q=75)
- **Contact:** nav@astroware.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.004070135 |
| 8104244 | 0.004072472 |
| 8104292 | 0.004072463 |
| 8104340 | 0.004072449 |
| 8104388 | 0.004072245 |
| 8104436 | 0.004072242 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

