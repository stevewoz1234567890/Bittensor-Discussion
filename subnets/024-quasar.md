# NetUID 24 — Quasar (`ω`)

## Overview

**Quasar** (NetUID **24**) (`ω`).

Bittensor subnet built to crush the long-context barrier.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `152`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ16,078.026481599. **Alpha liquidity in pool (`alpha_in`)** = ‎1,088,005.987752441ω‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,802,931.231559627ω‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.014641783`** *(also **moving-average price** `0.014582769013941288` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,066,166.684866813ω‎`. **Owner hotkey / coldkey (chain):** `5GE25P2qGpGmjzGipqezZckMvyR2mpcsJS387bbcpitNSfm5` / `5EjSHN7ZH4y21tgf8ACe5WtRQYvoWdLS6xsYvBktEycbmKYi`.
- **Subnet registered at block:** `2538424` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎114.570187218ω‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.004408906` · α-out `‎1.000000000ω‎` · α-in `‎0.301118083ω‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.014641786`
- **Market cap:** `65515900616305.44320969`
- **Liquidity:** `32008262642941`
- **Total τ:** `16077969843000`
- **Total α:** `4890920303189939`
- **α in pool:** `1088002023792852`
- **α staked:** `3386581924934813`
- **Price Δ 1h:** `0.741113708532612196`
- **Price Δ 1d:** `-2.101590374283352708`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `4407449`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Bittensor subnet built to crush the long-context barrier.



**Additional commentary (on-chain)**


-

### Repository README excerpt *(everything before first `##` heading)*

# Quasar Subnet

**Bittensor subnet built to crush the long-context barrier | SN24 |**

Quasar is SILX Labs' competitive small-model subnet on Bittensor. Miners train
Quasar-compatible language models, publish them as public Hugging Face
repositories, and commit the pinned model revision on-chain. Validators verify
each valid commitment, score it with the production composite evaluator, and set
weights to the current king.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Building the next generation of long-context foundation models. Open weights, novel architectures, real benchmarks.

**Fetched document title:** SILX AI

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
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5EjSHN7ZH4y21tgf8ACe5WtRQYvoWdLS6xsYvBktEycbmKYi`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
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

## Model Requirements

Submissions must match the official Quasar base interface. The canonical config
is the `config.json` in
[`silx-ai/Quasar-3B-A1B-Preview`](https://huggingface.co/silx-ai/Quasar-3B-A1B-Preview).

A valid model must:

- Use the Quasar architecture and tokenizer.
- Keep `vocab_size=248320`.
- Stay within the current subnet parameter cap.
- Provide public safetensors weights.
- Include the expected Quasar custom code files.
- Be loadable with `AutoModelForCausalLM.from_pretrained(..., trust_remote_code=True)`.
- Stay public and unchanged after the committed revision.
- Avoid quantized formats such as GPTQ, AWQ, GGUF, and FP8.
- Use unique weights that are not identical to an earlier committed model.

---

## Mining Guide

Requirements:

- Bittensor wallet registered on subnet 24.
- Hugging Face account for model hosting.
- Training infrastructure of your choice.

Install the miner dependencies:

```bash
python -m pip install -r requirements-miner.txt
```

Check your model before committing:

```bash
python miner/check_model.py --model-repo your-username/your-model
python miner/test_miner.py --model-repo your-username/your-model
```

Submit a dry run first:

```bash
python miner/miner.py \
  --network finney \
  --netuid 24 \
  --wallet-name my_wallet \
  --hotkey-name my_hotkey \
  --model-repo your-username/your-model \
  --dry-run
```

Remove `--dry-run` only after the checks pass and you are ready to commit that
repo revision on-chain.

---

## Validator Guide

Requirements:

- Bittensor wallet registered as a validator on subnet 24.
- Python 3.10+.
- GPU capacity for the current evaluator.
- Local wallet keys kept on the validator host.

Quick start:

```bash
python -m pip install -r requirements-validator.txt
bash scripts/run_validator.sh
```

Common validator settings:

```bash
QUASAR_NETWORK=finney
QUASAR_NETUID=24
QUASAR_WALLET_NAME=validator
QUASAR_HOTKEY_NAME=validator
QUASAR_WALLET_PATH=/path/to/wallets
QUASAR_STATE_DIR=/path/to/state
```

Keep wallet files, provider keys, Hugging Face tokens, and state credentials out
of git. Use a private environment file or your process manager's secret store.

---

#### CPU / GPU / RAM lines (automatic grep)

- - Pre-checks run before GPU evaluation: architecture compliance, tokenizer
- - GPU capacity for the current evaluator.


*Primary README URL used: `https://raw.githubusercontent.com/SILX-LABS/QUASAR-SUBNET/main/README.md`*

## On-chain identity — description


Bittensor subnet built to crush the long-context barrier.

## On-chain identity — additional field


-

## Registered contact & links


- **Website:** [https://silxinc.com/](https://silxinc.com/)
- **GitHub:** [https://github.com/SILX-LABS/QUASAR-SUBNET/](https://github.com/SILX-LABS/QUASAR-SUBNET/)
- **Discord:** [https://discordapp.com/channels/799672011265015819/1214246819886931988](https://discordapp.com/channels/799672011265015819/1214246819886931988)
- **Logo URL:** [https://silxinc.com/_next/image?url=%2Flogo-white.png&w=640&q=75](https://silxinc.com/_next/image?url=%2Flogo-white.png&w=640&q=75)
- **Contact:** -

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8103976 | 0.014802216 |
| 8104024 | 0.014549214 |
| 8104072 | 0.014469004 |
| 8104120 | 0.014640507 |
| 8104168 | 0.014641801 |
| 8104216 | 0.014641783 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

