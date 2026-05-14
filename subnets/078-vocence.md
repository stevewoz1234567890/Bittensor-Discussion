# NetUID 78 — Vocence (`و`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Vocence** (NetUID **78**) (`و`).

The voice layer for decentralized intelligence

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `65`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ257.287202897. **Alpha liquidity in pool (`alpha_in`)** = ‎22,449.055208165و‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎142,700.240678784و‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.011461166`** *(also **moving-average price** `0.009336754214018583` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎5,502.302954396و‎`. **Owner hotkey / coldkey (chain):** `5Fk765B4CRBekwErwE5VxvveWhHztHSfsnsLt8cbDayDWsuk` / `5FnQCJW2Rm1BijNBUJzPetcpZx43RWutYiyaxA8j88fy9i9L`.
- **Subnet registered at block:** `7966145` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎30.622372940و‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.003310494` · α-out `‎1.000000000و‎` · α-in `‎0.288844412و‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104370`
- **Liquidity constant `k`:** `5775854622189102926054005`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Vocence` |
| Symbol (API) | `و` |
| Rank | `126` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.011354306` |
| Market cap | `1470093591851.876156866` |
| Market cap Δ 1d | `54.436652696324515774` |
| Liquidity | `510637978399` |
| Total τ | `255316497148` |
| Total α | `164848934005761` |
| α in pool | `22486753593907` |
| α staked | `106987790411854` |
| Price Δ 1h | `-4.267251918566121604` |
| Price Δ 1d | `43.056449581772121022` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `78` |
| Owner SS58 (API) | `5FnQCJW2Rm1BijNBUJzPetcpZx43RWutYiyaxA8j88fy9i9L` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `7966145` |
| Registration wall time | `2026-04-14T11:12:24Z` |
| Registration cost snapshot | `534835676993` |
| Active keys | `142` |
| Active validators | `9` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `3305848` |
| Max neurons | `256` |
| Validator slots (metadata) | `9` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <img src="docs/vocence.png" alt="Vocence" width="640">
</p>

# <a href="https://vocence.ai" style="color: #DFFF00;">Vocence</a>

**Open, incentivized voice intelligence on Bittensor.**

Vocence is a Bittensor subnet focused on the development and evaluation of voice intelligence models, including Prompt-based Text-to-Speech (PromptTTS), Speech-to-Text (STT), Speech-to-Speech (STS), voice cloning, and other multimodal voice capabilities.

The network incentivizes miners to train and deploy models that follow natural-language prompts describing both content and voice traits such as gender, tone, emotion, pitch, speaking speed, age group, accent, and recording environment.

Validators evaluate how well models produce high-quality audio that matches both the requested content and the described voice characteristics.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Generate speech from prompts, clone any voice, design custom voices, and create music — powered by a decentralized network on Bittensor.

**Fetched document title:** Vocence — Decentralized Voice AI

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 142 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5FnQCJW2Rm1BijNBUJzPetcpZx43RWutYiyaxA8j88fy9i9L` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
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

## Validator quick start

**To run a validator you must contact the Vocence team.** They will:

- Grant **Chutes permission** so your validator can access miners' chutes.
- Provide the **owner API endpoint** (`API_URL`) for miner list, blocklist, and evaluation submission (dashboard integration).
- Provide the **Hippius sub-bucket keys**

Then:

1. **Clone, env, and run with Docker (recommended)**

   ```bash
   git clone https://github.com/Vocence-bt/vocence
   cd vocence
   cp env.example .env
   # Edit .env: NETWORK, NETUID (78), WALLET_NAME, HOTKEY_NAME,
   # CHUTES_API_KEY, API_URL, Hippius keys, VALIDATOR_NAME, etc.
   # Edit VALIDATOR_BUCKETS_JSON with readonly access for active validator sample buckets.
   docker-compose up -d
   ```

   The stack runs the published validator image and **Watchtower**; when the team pushes a new image, your validator auto-updates. See **[docs/validator-setup.md](docs/validator-setup.md)** for details and **[docs/cicd-pipeline.md](docs/cicd-pipeline.md)** for how the image is built and published.

2. **Optional: run from source**

   ```bash
   uv sync
   uv run vocence serve
   ```

   For all validator CLI options (e.g. split generator vs weight setter), see [docs/CLI.md](docs/CLI.md#validator-commands).

---

---

## Validator scoring

Sample generation is still local to each validator: each validator downloads source audio, queries miners, evaluates results, uploads artifacts to its own Hippius bucket, and submits evaluation metadata to the owner API.

Weight setting is now **global and deterministic**:

- Validators fetch the current **valid miner list** from the owner API.
- Validators fetch the current **active validator list** from the owner API. A validator is considered active when it submitted evaluation data recently (default window: 24 hours).
- Validators load local readonly bucket credentials from `VALIDATOR_BUCKETS_JSON` in `.env`.
- For each active validator that also exists in `VALIDATOR_BUCKETS_JSON`, validators read the most recent scoring window from that validator's bucket (default: 50 evaluations).
- Miner win rates are aggregated across active validators using **stake-weighted scoring**, where each validator's influence is weighted by `sqrt(stake)` from the current metagraph.
- A miner is globally eligible only if it has more than **40 evaluations** in at least **3 active validator buckets**.
- The winner must still beat earlier eligible miners, including the owner base model when present, by `THRESHOLD_MARGIN`.
- If there are too few active validators, too few readable validator buckets, or no miner satisfies the consensus + margin rules, validators burn by setting weight `1.0` on UID `0`.

This makes honest validators converge on the same leader from the same cross-validator evidence instead of relying on a single validator's local bucket.

---

---

## Miner quick start

See the **miner_sample/** directory for the full flow (HF repo + Chutes wrapper). You can also use the [CLI](docs/CLI.md#miner-commands) to deploy and commit:

- **vocence miner push** — Deploy your model to Chutes (`--model-name`, `--model-revision`).
- **vocence miner commit** — Commit model + Chute ID to chain (`--chute-id`, wallet).

miner_sample contains:

- **MINER_GUIDE.md** — Repo layout, engine contract, approved variables, render/build/deploy, and owner-side wrapper integrity.
- **chute_template/** — Canonical Jinja2 template; render with your four variables.
- **example_repo/** — Example HF repo layout (mock miner.py, chute_config.yml, vocence_config.yaml).

Use **uv** for local tooling (e.g. `uv run vocence`); Chutes builds run in their own environment.

---

---





#### CPU / GPU / RAM lines (automatic grep)

- `| **Miners** | Train PromptTTS models, publish them on Hugging Face, and deploy on [Chutes](https://chutes.ai) using the canonical Vocence wrapper. They expose a single `/speak` API (text + instruction → WAV). You can run miner workflows via the [CLI](docs/CLI.md#miner-commands) (`vocence miner push`, `vocence miner commit`) or follow [miner_sample](miner_sample/MINER_GUIDE.md) for the Chutes deploy. Rewards come from validator scores. |`


*Primary README URL used: `https://raw.githubusercontent.com/vocence-78/vocence/master/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.vocence.ai](https://www.vocence.ai)
- **GitHub:** [https://github.com/vocence-78/vocence](https://github.com/vocence-78/vocence)
- **Discord:** [https://discord.gg/TWmfwJAtXG](https://discord.gg/TWmfwJAtXG)
- **Logo URL:** [https://www.vocence.ai/tab_logo.png](https://www.vocence.ai/tab_logo.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.011424125 |
| 8104292 | 0.011520564 |
| 8104340 | 0.011505001 |
| 8104388 | 0.011468563 |
| 8104436 | 0.011461166 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.001357598 --> 0.01440338
    line [0.004109643, 0.004183468, 0.00420842, 0.00419243, 0.004065513, 0.003901809, 0.002757296, 0.002941471, 0.003195247, 0.003371019, 0.00341816412882, 0.00328893, 0.003012039, 0.003823171, 0.003741991, 0.00340150626733, 0.003525956, 0.003252291, 0.00319308, 0.003167857, 0.003343762, 0.003775555, 0.003959418, 0.003862442, 0.003383689, 0.00327571, 0.002626907, 0.002604933, 0.002589182, 0.002358755, 0.002457724, 0.002424766, 0.002350458, 0.002261615, 0.002261384, 0.002257307, 0.013503673, 0.009877673, 0.007742507, 0.007106113, 0.006910053, 0.00626176, 0.007208875, 0.00748281, 0.010822676, 0.009631142, 0.008424677, 0.007325858, 0.007334336, 0.00732589, 0.007236427, 0.007896605, 0.008596101, 0.007602709, 0.008845081, 0.011354306]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

