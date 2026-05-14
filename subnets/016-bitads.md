# NetUID 16 — BitAds (`π`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**BitAds** (NetUID **16**) (`π`).

BitAds is a decentralized, Proof of Sale marketing network where merchandisers stake or rent ALPHA to own marketing bandwidth, and miners earn on verified sales.



#### SubnetIdentity `additional` *(chain)*



https://x.com/bitads_ai

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `3`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ8,525.668112283. **Alpha liquidity in pool (`alpha_in`)** = ‎1,819,384.093400071π‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎3,031,468.425977628π‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004686385`** *(also **moving-average price** `0.004689555848017335` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎304,463.801440165π‎`. **Owner hotkey / coldkey (chain):** `5FRfiDbLxWAiac97ig4c5mgkb5yxSUVJDijmwJxw5RE5Ew9g` / `5CqRkhQUEgkQ4nBB4SCKnc9AzKPs9VLYv28erjeXPqQYVt9V`.
- **Subnet registered at block:** `2765446` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎2.259889497π‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000π‎` · α-in `‎0.000000000π‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104432`
- **Liquidity constant `k`:** `15511464949095900681668172093`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `BitAds` |
| Symbol (API) | `π` |
| Rank | `60` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004686429` |
| Market cap | `19078669664018.670027927` |
| Market cap Δ 1d | `0.35885413103041216` |
| Liquidity | `17052082489374` |
| Total τ | `8525707821782` |
| Total α | `4850619519377699` |
| α in pool | `1819375620028060` |
| α staked | `2251670727632103` |
| Price Δ 1h | `-0.000490776391180364` |
| Price Δ 1d | `0.254335185922037249` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `16` |
| Owner SS58 (API) | `5CqRkhQUEgkQ4nBB4SCKnc9AzKPs9VLYv28erjeXPqQYVt9V` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `2765446` |
| Registration wall time | `2024-04-15T10:46:00Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `15` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `15` |
| Max validators (API) | `64` |
| Neuron reg. cost | `500000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

<div align="center">

<img src="https://raw.githubusercontent.com/FirstTensorLabs/BitAds-Assets/refs/heads/main/Logo-white-green.png" width="30%" alt="BitAds Logo" />

# BitAds | Subnet 16

BitAds is a decentralized, proof of sale marketing network where merchandisers stake or rent ALPHA to own marketing bandwidth,<br> and miners earn on verified sales.

**Website**: [bitads.ai](https://bitads.ai)<br>
**Discord:** [SN16](https://discord.gg/qasY3HA9F9)<br>
**X**: [bitads_ai](https://x.com/bitads_ai)

</div>

*(README prelude often echoes the subnet tagline — miner/validator runbooks typically live further down in-repo.)*


### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** BitAds is a decentralized performance marketing network where brands pay only for verified sales. Connect Pixel + Stripe, stake ALPHA for marketing bandwidth, and eliminate wasted ad spend forever.

**Fetched document title:** BitAds – Decentralized Marketing Network

### Topology & economics (`SubnetInfo` snapshot)


| Field | Value |
| --- | --- |
| `max_n` (max registered UIDs) | 256 |
| `subnetwork_n` | 256 |
| Max validators allowed (`max_allowed_validators`) | 64 |
| Min weights per neuron (`min_allowed_weights`) | 1 |
| `max_weights_limit` (consensus-encoded cap) | 65535 |
| `tempo` (blocks between epoch advances) | 360 |
| `scaling_law_power` | 50 |
| `modality` ID | `0` |
| `emission_value` (display field) | 0 |
| `difficulty` (PoW field on info view) | 10000000 |
| `immunity_period` (blocks) | 50400 |
| Registration recycle cost snapshot (`burn`) | τ0.000500000 |
| Owner SS58 (`owner_ss58`) | `5CqRkhQUEgkQ4nBB4SCKnc9AzKPs9VLYv28erjeXPqQYVt9V` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.000500000 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `50400` blocks |
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

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/FirstTensorLabs/BitAds/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://bitads.ai](https://bitads.ai)
- **GitHub:** [https://github.com/FirstTensorLabs/BitAds](https://github.com/FirstTensorLabs/BitAds)
- **Discord:** [https://discord.gg/qasY3HA9F9](https://discord.gg/qasY3HA9F9)
- **Logo URL:** [https://raw.githubusercontent.com/FirstTensorLabs/BitAds-Assets/refs/heads/main/Logo-white-green-black.png](https://raw.githubusercontent.com/FirstTensorLabs/BitAds-Assets/refs/heads/main/Logo-white-green-black.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.004686429 |
| 8104244 | 0.004686414 |
| 8104292 | 0.004686405 |
| 8104340 | 0.00468639 |
| 8104388 | 0.004686389 |
| 8104436 | 0.004686385 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

```mermaid
xychart-beta
    title "TAOStats daily pool price (τ per α)"
    x-axis ["2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12", "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17", "2026-03-18", "2026-03-19", "2026-03-20", "2026-03-21", "2026-03-22", "2026-03-23", "2026-03-24", "2026-03-25", "2026-03-26", "2026-03-27", "2026-03-28", "2026-03-29", "2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05", "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10", "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17", "2026-04-18", "2026-04-19", "2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23", "2026-04-24", "2026-04-25", "2026-04-26", "2026-04-27", "2026-04-28", "2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02", "2026-05-03"]
    y-axis "Price" in 0.004611805 --> 0.005533653
    line [0.005413, 0.005326224, 0.005357516, 0.005287908, 0.005196321, 0.005285167, 0.005177829, 0.005470077, 0.005462637, 0.00501762, 0.00500185828439, 0.005000151, 0.004995832, 0.005025805, 0.005039735, 0.0050595275462, 0.005010238, 0.004957642, 0.004943464, 0.004940996, 0.004944664, 0.004962506, 0.005032776, 0.005001342, 0.005020229, 0.005034223, 0.005034172, 0.005024304, 0.005081429, 0.004989348, 0.005067768, 0.004985602, 0.004975125, 0.004984129, 0.004943079, 0.004789527, 0.00478166, 0.004759383, 0.004718666, 0.004705145, 0.004718356, 0.00470898, 0.004679722, 0.004683453, 0.00468353, 0.004717933, 0.004710451, 0.004700618, 0.004699555, 0.004675381, 0.00470749, 0.004690174, 0.004686294, 0.00467959, 0.004695183, 0.004686429]
```



---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

