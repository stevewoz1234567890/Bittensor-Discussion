# NetUID 93 — Bitcast (`ᚃ`)

## Overview

**Bitcast** (NetUID **93**) (`ᚃ`).

The Decentralized Creators Economy

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `283`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ20,145.028048495. **Alpha liquidity in pool (`alpha_in`)** = ‎1,325,624.666124129ᚃ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,720,373.376589050ᚃ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.015196685`** *(also **moving-average price** `0.01481353654526174` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎810,537.860796142ᚃ‎`. **Owner hotkey / coldkey (chain):** `5DAoDtMxVqtMu2Nd5E7QhPEGXDMgrySvE1b3rRT5ARDhfNNK` / `5FLfN276taTF6Ud62soChQhPNbtF2EPK4dr3pJB9oTsTpUvr`.
- **Subnet registered at block:** `5370681` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎210.135618308ᚃ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ᚃ‎` · α-in `‎0.000000000ᚃ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.015196797`
- **Market cap:** `49084607871830.900218311`
- **Liquidity:** `40290276997444`
- **Total τ:** `20145102500971`
- **Total α:** `4045923042713179`
- **α in pool:** `1325619766880728`
- **α staked:** `1904311373992635`
- **Price Δ 1h:** `0.680718606385867702`
- **Price Δ 1d:** `6.58027122821639738`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `9`
- **Active miners:** `7`
- **Active dual:** `1`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `9`
- **Neuron reg. cost:** `5000000`

### On-chain declared purpose *(SubnetIdentity)*

The Decentralized Creators Economy

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <a href="https://www.bitcast.network/">
    <img src="assets/lockup_gradient.svg" alt="Bitcast Logo" width="800" />
  </a>
</p>

# Bitcast — The Decentralized Creator Economy

Bitcast is a decentralized platform that incentivizes content creators to connect brands with audiences. Creators publish YouTube videos to satisfy defined briefs and earn rewards based on engagement metrics.

---

### Supplementary site crawl *(marketing HTML)*

**Fetched document title:** bitcast

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
- **`immunity_period` (blocks):** 50400
- **Registration recycle cost snapshot (`burn`):** τ0.005000000
- **Owner SS58 (`owner_ss58`):** `5FLfN276taTF6Ud62soChQhPNbtF2EPK4dr3pJB9oTsTpUvr`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.005000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
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

### For Miners

1. **Review Requirements**  
   Ensure your YouTube account and videos meet the [minimum requirements](bitcast/miner/README.md).

2. **Publish Content**  
   Create videos targeting one or more active briefs.

3. **Earn Rewards**  
   Videos that satisfy briefs are rewarded based on **YouTube Premium revenue** stats.

4. **Agency Operations**  
   Run a single miner with up to 5 YouTube accounts to operate as a content agency, aggregating multiple creators under one mining operation.

See the [Miner Setup Guide](bitcast/miner/README.md) for:
- Installation and configuration  
- OAuth and account integration  
- Miner registration on the network  
- Reward tracking and monitoring

---

### For Validators

Validators maintain the integrity of the network by:
- Retrieving analytics data via OAuth  
- Verifying content engagement  
- Disbursing on-chain rewards to Miners

Refer to the [Validator Setup Guide](bitcast/validator/README.md) for detailed instructions.

---

---

## 📊 Scoring & Rewards System

Bitcast employs a dynamic, multi-layered scoring and rewards mechanism to fairly distribute emissions and incentivize high-quality participation. The system is designed to prioritize genuine engagement and prevent manipulation.

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/bitcast-network/bitcast/main/README.md`*

## On-chain identity — description


The Decentralized Creators Economy

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://www.bitcast.network/](https://www.bitcast.network/)
- **GitHub:** [https://github.com/bitcast-network/bitcast](https://github.com/bitcast-network/bitcast)
- **Logo URL:** [https://bitcast-logo.s3.us-west-2.amazonaws.com/Bitcast+logo+multi+white.webp](https://bitcast-logo.s3.us-west-2.amazonaws.com/Bitcast+logo+multi+white.webp)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.01515994 |
| 8104133 | 0.015160208 |
| 8104181 | 0.015174454 |
| 8104229 | 0.015196739 |
| 8104277 | 0.015196685 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.014681327 |
| 2026-03-10T23:59:48Z | 7718257 | 0.015452756 |
| 2026-03-11T23:59:48Z | 7725455 | 0.015542639 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.015039283 |
| 2026-03-13T23:59:48Z | 7739841 | 0.01537258 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.017112115 |
| 2026-03-15T23:59:48Z | 7754226 | 0.017628603 |
| 2026-03-16T23:59:48Z | 7761426 | 0.017727804 |
| 2026-03-17T23:59:48Z | 7768619 | 0.017487896 |
| 2026-03-18T23:59:48Z | 7775819 | 0.017305098 |
| 2026-03-19T23:59:48Z | 7783014 | 0.01666838737571929605 |
| 2026-03-20T23:59:48Z | 7790201 | 0.016273718 |
| 2026-03-21T23:59:48Z | 7797398 | 0.016851925 |
| 2026-03-22T23:59:48Z | 7804598 | 0.01630232 |
| 2026-03-23T23:59:48Z | 7811798 | 0.017154247 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.01675519014827303122 |
| 2026-03-25T23:59:48Z | 7826196 | 0.016541456 |
| 2026-03-26T23:59:48Z | 7833396 | 0.015357557 |
| 2026-03-27T23:59:48Z | 7840596 | 0.01500895 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.014960884 |
| 2026-03-29T23:59:48Z | 7854902 | 0.015654304 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.015239573 |
| 2026-03-31T23:59:48Z | 7869291 | 0.015759797 |
| 2026-04-01T23:59:48Z | 7876474 | 0.01658201 |
| 2026-04-02T23:59:48Z | 7883622 | 0.017431599 |
| 2026-04-03T23:59:48Z | 7890794 | 0.017071177 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.017836104 |
| 2026-04-05T23:59:48Z | 7905188 | 0.018532904 |
| 2026-04-06T23:59:48Z | 7912388 | 0.018826392 |
| 2026-04-07T23:59:48Z | 7919588 | 0.019588773 |
| 2026-04-08T23:59:48Z | 7926788 | 0.017897013 |
| 2026-04-09T23:59:48Z | 7933987 | 0.019309276 |
| 2026-04-10T23:59:48Z | 7941184 | 0.018716664 |
| 2026-04-11T23:59:48Z | 7948384 | 0.01857412 |
| 2026-04-12T23:59:48Z | 7955584 | 0.018798972 |
| 2026-04-13T23:59:48Z | 7962784 | 0.019517525 |
| 2026-04-14T23:59:48Z | 7969979 | 0.018271891 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.018159473 |
| 2026-04-16T23:59:48Z | 7984379 | 0.017296797 |
| 2026-04-17T23:59:48Z | 7991579 | 0.016741414 |
| 2026-04-18T23:59:48Z | 7998779 | 0.015352218 |
| 2026-04-19T23:59:48Z | 8005979 | 0.015563486 |
| 2026-04-20T23:59:48Z | 8013179 | 0.015522951 |
| 2026-04-21T23:59:48Z | 8020376 | 0.015257377 |
| 2026-04-22T23:59:48Z | 8027562 | 0.0146232 |
| 2026-04-23T23:59:48Z | 8034762 | 0.015102341 |
| 2026-04-24T23:59:48Z | 8041962 | 0.014587818 |
| 2026-04-25T23:59:48Z | 8049151 | 0.015449286 |
| 2026-04-26T23:59:48Z | 8056274 | 0.015308365 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.014951104 |
| 2026-04-28T23:59:48Z | 8070646 | 0.015256595 |
| 2026-04-29T23:59:48Z | 8077790 | 0.01541044 |
| 2026-04-30T23:59:48Z | 8084984 | 0.014999507 |
| 2026-05-01T23:59:48Z | 8092168 | 0.014197495 |
| 2026-05-02T23:59:48Z | 8099357 | 0.014860874 |
| 2026-05-03T16:10:00Z | 8104202 | 0.015196797 |


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

