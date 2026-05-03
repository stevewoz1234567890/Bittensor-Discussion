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

- **Subnet name (API):** `BitAds`
- **Symbol (API):** `π`
- **Rank:** `60`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004686429`
- **Market cap:** `19078669664018.670027927`
- **Market cap Δ 1d:** `0.35885413103041216`
- **Liquidity:** `17052082489374`
- **Total τ:** `8525707821782`
- **Total α:** `4850619519377699`
- **α in pool:** `1819375620028060`
- **α staked:** `2251670727632103`
- **Price Δ 1h:** `-0.000490776391180364`
- **Price Δ 1d:** `0.254335185922037249`
#### Subnet activity (TAOStats)

- **NetUID (API):** `16`
- **Owner SS58 (API):** `5CqRkhQUEgkQ4nBB4SCKnc9AzKPs9VLYv28erjeXPqQYVt9V`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `2765446`
- **Registration wall time:** `2024-04-15T10:46:00Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `15`
- **Active miners:** `1`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `15`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

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

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.005413 |
| 2026-03-10T23:59:48Z | 7718257 | 0.005326224 |
| 2026-03-11T23:59:48Z | 7725455 | 0.005357516 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.005287908 |
| 2026-03-13T23:59:48Z | 7739841 | 0.005196321 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.005285167 |
| 2026-03-15T23:59:48Z | 7754226 | 0.005177829 |
| 2026-03-16T23:59:48Z | 7761426 | 0.005470077 |
| 2026-03-17T23:59:48Z | 7768619 | 0.005462637 |
| 2026-03-18T23:59:48Z | 7775819 | 0.00501762 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00500185828439039218 |
| 2026-03-20T23:59:48Z | 7790201 | 0.005000151 |
| 2026-03-21T23:59:48Z | 7797398 | 0.004995832 |
| 2026-03-22T23:59:48Z | 7804598 | 0.005025805 |
| 2026-03-23T23:59:48Z | 7811798 | 0.005039735 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00505952754620248907 |
| 2026-03-25T23:59:48Z | 7826196 | 0.005010238 |
| 2026-03-26T23:59:48Z | 7833396 | 0.004957642 |
| 2026-03-27T23:59:48Z | 7840596 | 0.004943464 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.004940996 |
| 2026-03-29T23:59:48Z | 7854902 | 0.004944664 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.004962506 |
| 2026-03-31T23:59:48Z | 7869291 | 0.005032776 |
| 2026-04-01T23:59:48Z | 7876474 | 0.005001342 |
| 2026-04-02T23:59:48Z | 7883622 | 0.005020229 |
| 2026-04-03T23:59:48Z | 7890794 | 0.005034223 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.005034172 |
| 2026-04-05T23:59:48Z | 7905188 | 0.005024304 |
| 2026-04-06T23:59:48Z | 7912388 | 0.005081429 |
| 2026-04-07T23:59:48Z | 7919588 | 0.004989348 |
| 2026-04-08T23:59:48Z | 7926788 | 0.005067768 |
| 2026-04-09T23:59:48Z | 7933987 | 0.004985602 |
| 2026-04-10T23:59:48Z | 7941184 | 0.004975125 |
| 2026-04-11T23:59:48Z | 7948384 | 0.004984129 |
| 2026-04-12T23:59:48Z | 7955584 | 0.004943079 |
| 2026-04-13T23:59:48Z | 7962784 | 0.004789527 |
| 2026-04-14T23:59:48Z | 7969979 | 0.00478166 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.004759383 |
| 2026-04-16T23:59:48Z | 7984379 | 0.004718666 |
| 2026-04-17T23:59:48Z | 7991579 | 0.004705145 |
| 2026-04-18T23:59:48Z | 7998779 | 0.004718356 |
| 2026-04-19T23:59:48Z | 8005979 | 0.00470898 |
| 2026-04-20T23:59:48Z | 8013179 | 0.004679722 |
| 2026-04-21T23:59:48Z | 8020376 | 0.004683453 |
| 2026-04-22T23:59:48Z | 8027562 | 0.00468353 |
| 2026-04-23T23:59:48Z | 8034762 | 0.004717933 |
| 2026-04-24T23:59:48Z | 8041962 | 0.004710451 |
| 2026-04-25T23:59:48Z | 8049151 | 0.004700618 |
| 2026-04-26T23:59:48Z | 8056274 | 0.004699555 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.004675381 |
| 2026-04-28T23:59:48Z | 8070646 | 0.00470749 |
| 2026-04-29T23:59:48Z | 8077790 | 0.004690174 |
| 2026-04-30T23:59:48Z | 8084984 | 0.004686294 |
| 2026-05-01T23:59:48Z | 8092168 | 0.00467959 |
| 2026-05-02T23:59:48Z | 8099357 | 0.004695183 |
| 2026-05-03T16:10:00Z | 8104202 | 0.004686429 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

