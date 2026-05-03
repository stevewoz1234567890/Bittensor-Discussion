# NetUID 16 — BitAds (`π`)

## Overview

BitAds is a decentralized, Proof of Sale marketing network where merchandisers stake or rent ALPHA to own marketing bandwidth, and miners earn on verified sales.

https://x.com/bitads_ai

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
- **`immunity_period` (blocks):** 50400
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CqRkhQUEgkQ4nBB4SCKnc9AzKPs9VLYv28erjeXPqQYVt9V`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `50400` blocks
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

## For Miners

Miners drive traffic and conversions to BitAds campaigns and are rewarded based on:
- **Verified sales:** Number of successful sales
- **Revenue contributions:** Total revenue generated in USD
- **Low refund ratios**
- **Overall contribution to campaign success**

See [Mining Guide](docs/mining.md) for details.

---

## For Validators

Validators collect miner performance data, calculate scores, and submit weights to the Bittensor network. The scoring algorithm evaluates miners using:

1. **Refund Rate**: $\text{ref}_i = \min(1, \frac{{\text{refund}\_\text{orders}}_i}{\max(1, \text{sales}_i)})$
2. **Sales Normalization**: Square root normalization against P95 percentile
3. **Revenue Normalization**: Logarithmic normalization against P95 percentile
4. **Base Score**: $15$% sales + $85$% revenue
5. **Final Score**: $\text{score}_i = \text{base}_i \times (1 - \text{ref}_i)$

See [Validating Guide](docs/validating.md) for setup instructions.

---

### BitAds Miner Score

**Purpose**: Compute a bounded score in $[0,1]$ per miner for the last 30 days, combining:
- Sales volume (weight 15%)
- Revenue in USD (weight 85%)
- Refund rate as a multiplicative penalty

This is outlier-resistant, easy to implement, and aligned with merchant value.

---

### Inputs (per miner i, last 30 days)

- `sales_i` (integer ≥ 0): number of verified orders (post-webhook truth)
- `rev_i` (float ≥ 0): sum of verified revenue in USD
- `refund_orders_i` (integer ≥ 0): number of refunded orders among the verified ones

**Derived**:
- $\text{ref}_i = \frac{{\text{refund}\_\text{orders}}_i}{\max(1, \text{sales}_i)}$ (refund rate in $[0,1]$)

> **Note**: If `sales_i = 0`, the score will be 0 regardless of refunds, which is intended.

---

#### Example 2: Burn Required

- **Emissions**: $15,000 USD
- **Sales**: $10,000 USD
- **Target ratio**: 1.0 (1:1)

$$\text{burn} = \frac{15,000 - 10,000 \times 1.0}{15,000} \times 100 \approx 33.3\%$$

Approximately 33% of emissions need to be burned to maintain the 1:1 ratio.

---

#### CPU / GPU / RAM lines (automatic grep)

*Nothing in this README excerpt matched GPU/VRAM/CPU sizing patterns (`\d+ GB/TB`, `CUDA`, `H100/RTX/…`, `vCPU/cores`). Check **`docs/`**, miner/validator guides linked here, Discord, or the subnet’s homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/FirstTensorLabs/BitAds/main/README.md`*

*Markdown includes **matched headings** plus a **hardware grep** (GB/VRAM/GPU/CUDA/cpu/cores).* Always verify against the subnet’s current repository branch.*

## On-chain identity — description


BitAds is a decentralized, Proof of Sale marketing network where merchandisers stake or rent ALPHA to own marketing bandwidth, and miners earn on verified sales.

## On-chain identity — additional field


https://x.com/bitads_ai

## Registered contact & links


- **Website:** [https://bitads.ai](https://bitads.ai)
- **GitHub:** [https://github.com/FirstTensorLabs/BitAds](https://github.com/FirstTensorLabs/BitAds)
- **Discord:** [https://discord.gg/qasY3HA9F9](https://discord.gg/qasY3HA9F9)
- **Logo URL:** [https://raw.githubusercontent.com/FirstTensorLabs/BitAds-Assets/refs/heads/main/Logo-white-green-black.png](https://raw.githubusercontent.com/FirstTensorLabs/BitAds-Assets/refs/heads/main/Logo-white-green-black.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103795 | 0.004686467 |
| 8103843 | 0.004686458 |
| 8103891 | 0.004686455 |
| 8103939 | 0.004686451 |
| 8103987 | 0.004686447 |
| 8104035 | 0.004686444 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


---

*Snapshot: Subtensor `finney`, head block **8104035**, 2026-05-03 15:36 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

