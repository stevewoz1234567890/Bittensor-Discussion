# NetUID 97 — distil (`ა`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**distil** (NetUID **97**) (`ა`).

Distillation

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `84`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ4,507.582223665. **Alpha liquidity in pool (`alpha_in`)** = ‎95,225.136979750ა‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎346,649.640530138ა‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.047320072`** *(also **moving-average price** `0.04762440640479326` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎165,992.268634269ა‎`. **Owner hotkey / coldkey (chain):** `5EvHrbHz8rT8DrWazxFhzfMsmscFtPE3qhRDeY4ggKZrBcxZ` / `5EUXD91ADceyH7nRWXCqG1wbaCEhsqosT4rjGhwaZDRR4ib6`.
- **Subnet registered at block:** `7735450` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎45.430991235ა‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.022209760` · α-out `‎1.000000000ა‎` · α-in `‎0.469351749ა‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104351`
- **Liquidity constant `k`:** `429235134695985727075783750`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `distil`
- **Symbol (API):** `ა`
- **Rank:** `59`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.047416683`
- **Market cap:** `19294493707628.046973767`
- **Market cap Δ 1d:** `1.632392701886412875`
- **Liquidity:** `9012456724385`
- **Total τ:** `4506991002206`
- **Total α:** `441545277086471`
- **α in pool:** `95018576524622`
- **α staked:** `311895034611527`
- **Price Δ 1h:** `-0.334418023790884375`
- **Price Δ 1d:** `-0.957814539578590929`
#### Subnet activity (TAOStats)

- **NetUID (API):** `97`
- **Owner SS58 (API):** `5EUXD91ADceyH7nRWXCqG1wbaCEhsqosT4rjGhwaZDRR4ib6`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `7735450`
- **Registration wall time:** `2026-03-13T09:19:36.001Z`
- **Registration cost snapshot:** `560765039232`
- **Active keys:** `256`
- **Active validators:** `1`
- **Active miners:** `5`
- **Active dual-role:** `0`
- **Emission:** `22270404`
- **Max neurons:** `256`
- **Validator slots (metadata):** `1`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `659684863`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `7200`

### Repository README excerpt *(everything before first `##` heading)*

# Distil — SN97

A Bittensor subnet for competitive model distillation of **Qwen/Qwen3.6-35B-A3B** (35B total, ~3B active MoE).

**Dashboard**: [distil.arbos.life](https://distil.arbos.life)
**API**: [api.arbos.life](https://api.arbos.life)
**Chat with the King**: [chat.arbos.life](https://chat.arbos.life) — try the current best distilled model
**Subnet**: Finney netuid 97

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
- **Registration recycle cost snapshot (`burn`):** τ0.752524871
- **Owner SS58 (`owner_ss58`):** `5EUXD91ADceyH7nRWXCqG1wbaCEhsqosT4rjGhwaZDRR4ib6`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.500000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `7200` blocks
- **`commit_reveal_weights_enabled`:** `False`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `500000`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

### Requirements

- Bittensor wallet registered on subnet 97
- HuggingFace account for model hosting
- Training infrastructure (your choice)

---

### Model Requirements

Your model must:
- Use **same tokenizer** as Qwen3.5-35B-A3B (vocab_size=248,320)
- Have ≤ **5.25B total parameters** (15% of teacher's 35B)
- Be in **safetensors** format (bf16/fp16)
- Use **`Qwen3_5ForConditionalGeneration`** architecture (model_type=`qwen3_5`) — required for vLLM compatibility
- Be loadable via `AutoModelForCausalLM.from_pretrained()`
- Stay **public and unchanged** on HuggingFace — making a repo private or pushing new commits = DQ
- **No quantized models** (GPTQ/AWQ/GGUF rejected)
- **Unique weights** — Cannot be identical to any previously committed model

---

### Pre-Submission Check (Recommended)

Before committing, run the validation tools to verify your model passes ALL validator checks:

```bash
pip install click huggingface_hub transformers safetensors

---

# Recommended: test_miner.py runs all 15 validator checks locally

python test_miner.py --model-repo your-username/your-model

---

# Alternative: check_model.py (quick pre-GPU checks)

python check_model.py --model-repo your-username/your-model

---

# Full eval with KL scoring (requires GPU):

python check_model.py --model-repo your-username/your-model --eval

---

# Commit (PERMANENT — interactive confirmation required):

python miner.py \
    --network finney \
    --netuid 97 \
    --wallet-name my_wallet \
    --hotkey-name my_hotkey \
    --model-repo your-username/your-distilled-model
```

The miner script includes `--dry-run`/`--test-only` flags, interactive confirmation before committing, and post-commit verification. To change models, register a new hotkey.

---

### GPU Requirements

- **Full teacher (Qwen3.5-35B-A3B unquantized):** 2× A100 80GB+ recommended (one for teacher, one for student)
- **Local dev with smaller models:** 2× 24GB GPUs (e.g. RTX 3090/4090)

---

### Requirements

- **GPU**: 1x B200 192GB recommended (~100GB minimum VRAM: teacher 67GB + student 8GB + teacher logits cache 17GB + king model 8GB). A100 80GB is insufficient for the vLLM pipeline.
- **Bittensor wallet** registered as validator on subnet 97
- **Python 3.10+**

---

# Or with PM2 (recommended):

pm2 start scripts/run_validator.sh --name distil-validator
pm2 save
```

If `pip install .` fails:

```bash
pip install "bittensor>=8.0.0" "bittensor-wallet>=2.0.0" "click>=8.0.0" \
    "transformers>=4.45.0" "huggingface-hub>=0.20.0" "numpy>=1.26.0" \
    "torch>=2.1.0" "safetensors>=0.4.0"
```

---

### Split Validator Architecture

The validator now runs as a split architecture across two trust boundaries:

- **Dedicated `distil` host** (secure): Wallet keys, chain access, weight setting, validator orchestration, API, dashboard, and persistent state all live on one Distil-only Hetzner machine.
- **Lium GPU pod** (remote): Teacher/student forward passes, KL computation, vLLM inference. This machine has the GPU but **no chain access** — it cannot set weights or read wallet keys.
- **Optional external helpers**: Benchmark sync and chat inference can remain remote, but they do not hold wallet keys or perform weight setting.

Wallet keys never leave the `distil` host. The GPU pod receives evaluation tasks and returns scores. This separation ensures that even a compromised GPU pod cannot steal funds or manipulate weights directly.

---

#### CPU / GPU / RAM lines (automatic grep)

- 1. **Pre-checks (no GPU)** — Every epoch (~10 min), all committed models are verified:
- - Models that fail pre-checks are **never sent to GPU** — no wasted compute
- 6. **vLLM-accelerated evaluation** — vLLM generates teacher continuations 5–10× faster than pure HuggingFace inference. Teacher logits are precomputed and cached on GPU. Multi-GPU pod scaffolding (`DISTIL_TP_SIZE`, `DISTIL_STUDENT_PARALLELISM`) supports 4× / 8× H100 migration for Kimi K2.6 / batched student forward (v30.4).
- - **Top-128 sparse KL**: Teacher returns top-128 logprobs per position (`--max-logprobs 128` on vLLM). Student softmaxes over the full 248,320-token vocab, then gathers + renormalizes to the same 128 positions for a proper KL on the shared support. Full-vocab dense path exists in `compute_kl_from_precomputed` for reference; disabled in prod for bandwidth (~150GB/round at full vocab).
- - **Full teacher (Qwen3.5-35B-A3B unquantized):** 2× A100 80GB+ recommended (one for teacher, one for student)
- - **Local dev with smaller models:** 2× 24GB GPUs (e.g. RTX 3090/4090)
- **Local dev with smaller models (e.g. 2× 24GB GPUs):**
- - **GPU**: 1x B200 192GB recommended (~100GB minimum VRAM: teacher 67GB + student 8GB + teacher logits cache 17GB + king model 8GB). A100 80GB is insufficient for the vLLM pipeline.
- 1. Loads the teacher model (Qwen3.5-35B-A3B) via vLLM for fast generation (~67GB VRAM)
- 5. Teacher logits are precomputed and cached on GPU for fast scoring
- `| `GET /api/scores` | Current KL scores, disqualification reasons, last eval details |`
- ├── check_model.py            # Pre-submission checker (13 pre-GPU + 4 GPU checks)
- │   ├── kl_divergence.py      # Sparse top-128 KL on GPU (dense path available for offline replays)
- │   ├── pod_eval_vllm.py      # GPU eval runner: vLLM teacher generation + HF logit extraction,
- │   │                         #   GPU-resident teacher logits, early stopping, king-in-VRAM
- │   ├── remote_validator.py   # King-of-the-hill validator (Hetzner + Lium GPU)
- - **Lium GPU pod** (remote): Teacher/student forward passes, KL computation, vLLM inference. This machine has the GPU but **no chain access** — it cannot set weights or read wallet keys.
- Wallet keys never leave the `distil` host. The GPU pod receives evaluation tasks and returns scores. This separation ensures that even a compromised GPU pod cannot steal funds or manipulate weights directly.


*Primary README URL used: `https://raw.githubusercontent.com/unarbos/distil/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://distill.arbos.life](https://distill.arbos.life)
- **GitHub:** [https://github.com/unarbos/distil](https://github.com/unarbos/distil)
- **Discord (handle / invite hint):** `@Arbos`
- **Logo URL:** [https://pub-0821b4e0d60149b79bad17376722bc75.r2.dev/assets/droplet.png](https://pub-0821b4e0d60149b79bad17376722bc75.r2.dev/assets/droplet.png)
- **Contact:** arbos@bittensor.com

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.047428688 |
| 8104292 | 0.04752195 |
| 8104340 | 0.04729595 |
| 8104388 | 0.047019938 |
| 8104436 | 0.047320071 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.003340688 |
| 2026-03-10T23:59:48Z | 7718257 | 0.002457403 |
| 2026-03-11T23:59:48Z | 7725455 | 0.002833465 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.00266213 |
| 2026-03-13T23:59:48Z | 7739841 | 0.003537339 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.01350265 |
| 2026-03-15T23:59:48Z | 7754226 | 0.058176127 |
| 2026-03-16T23:59:48Z | 7761426 | 0.04183495 |
| 2026-03-17T23:59:48Z | 7768619 | 0.025481645 |
| 2026-03-18T23:59:48Z | 7775819 | 0.023874272 |
| 2026-03-19T23:59:48Z | 7783014 | 0.0304054247764384575 |
| 2026-03-20T23:59:48Z | 7790201 | 0.026880337 |
| 2026-03-21T23:59:48Z | 7797398 | 0.034027002 |
| 2026-03-22T23:59:48Z | 7804598 | 0.044824748 |
| 2026-03-23T23:59:48Z | 7811798 | 0.037528298 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.0362597222606328946 |
| 2026-03-25T23:59:48Z | 7826196 | 0.067875769 |
| 2026-03-26T23:59:48Z | 7833396 | 0.063004975 |
| 2026-03-27T23:59:48Z | 7840596 | 0.05901166 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.060491711 |
| 2026-03-29T23:59:48Z | 7854902 | 0.05224509 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.058897907 |
| 2026-03-31T23:59:48Z | 7869291 | 0.045831769 |
| 2026-04-01T23:59:48Z | 7876474 | 0.043434207 |
| 2026-04-02T23:59:48Z | 7883622 | 0.037824752 |
| 2026-04-03T23:59:48Z | 7890794 | 0.035846827 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.033041389 |
| 2026-04-05T23:59:48Z | 7905188 | 0.037512425 |
| 2026-04-06T23:59:48Z | 7912388 | 0.032505603 |
| 2026-04-07T23:59:48Z | 7919588 | 0.03250282 |
| 2026-04-08T23:59:48Z | 7926788 | 0.032379647 |
| 2026-04-09T23:59:48Z | 7933987 | 0.024714601 |
| 2026-04-10T23:59:48Z | 7941184 | 0.060424091 |
| 2026-04-11T23:59:48Z | 7948384 | 0.05682897 |
| 2026-04-12T23:59:48Z | 7955584 | 0.070282306 |
| 2026-04-13T23:59:48Z | 7962784 | 0.082574145 |
| 2026-04-14T23:59:48Z | 7969979 | 0.068488072 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.064561522 |
| 2026-04-16T23:59:48Z | 7984379 | 0.048374309 |
| 2026-04-17T23:59:48Z | 7991579 | 0.049956384 |
| 2026-04-18T23:59:48Z | 7998779 | 0.043828038 |
| 2026-04-19T23:59:48Z | 8005979 | 0.051646821 |
| 2026-04-20T23:59:48Z | 8013179 | 0.047267019 |
| 2026-04-21T23:59:48Z | 8020376 | 0.048763485 |
| 2026-04-22T23:59:48Z | 8027562 | 0.044646923 |
| 2026-04-23T23:59:48Z | 8034762 | 0.046794588 |
| 2026-04-24T23:59:48Z | 8041962 | 0.047018743 |
| 2026-04-25T23:59:48Z | 8049151 | 0.049959433 |
| 2026-04-26T23:59:48Z | 8056274 | 0.048674396 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.047571374 |
| 2026-04-28T23:59:48Z | 8070646 | 0.046354647 |
| 2026-04-29T23:59:48Z | 8077790 | 0.047812225 |
| 2026-04-30T23:59:48Z | 8084984 | 0.048105933 |
| 2026-05-01T23:59:48Z | 8092168 | 0.047731699 |
| 2026-05-02T23:59:48Z | 8099357 | 0.047812864 |
| 2026-05-03T16:10:00Z | 8104202 | 0.047416683 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

