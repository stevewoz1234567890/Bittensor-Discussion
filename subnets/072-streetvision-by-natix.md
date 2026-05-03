# NetUID 72 — StreetVision by NATIX (`ق`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**StreetVision by NATIX** (NetUID **72**) (`ق`).

Powered by NATIX’s Internet of Cameras, StreetVision is advancing autonomous driving, Physical AI, and map-making.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `59`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,765.323298098. **Alpha liquidity in pool (`alpha_in`)** = ‎2,316,174.529734059ق‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,103,230.019542807ق‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.003353336`** *(also **moving-average price** `0.003364197677001357` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎194,580.989060985ق‎`. **Owner hotkey / coldkey (chain):** `5Fmvr2VJs9EpyR5NbNpLTKgEXS8fRnQA6F349xqswsz6VL88` / `5HTYVBxrF2WbVN8RBtFxAkBGuHJxjgLd9Sze5gxH4KC6GLCv`.
- **Subnet registered at block:** `5064327` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎44.127733970ق‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ق‎` · α-in `‎0.000000000ق‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104376`
- **Liquidity constant `k`:** `17985844038205067200720519782`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `StreetVision by NATIX`
- **Symbol (API):** `ق`
- **Rank:** `78`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.003353437`
- **Market cap:** `14575034916702.493549613`
- **Market cap Δ 1d:** `0.414772960040458228`
- **Liquidity:** `15532468662632`
- **Total τ:** `7765441003030`
- **Total α:** `4419223572646096`
- **α in pool:** `2316139429368430`
- **α staked:** `2030158090669219`
- **Price Δ 1h:** `0.391484750146690776`
- **Price Δ 1d:** `0.284516120736033695`
#### Subnet activity (TAOStats)

- **NetUID (API):** `72`
- **Owner SS58 (API):** `5HTYVBxrF2WbVN8RBtFxAkBGuHJxjgLd9Sze5gxH4KC6GLCv`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `5064327`
- **Registration wall time:** `2025-03-05T21:39:00Z`
- **Registration cost snapshot:** `191341473067`
- **Active keys:** `256`
- **Active validators:** `6`
- **Active miners:** `244`
- **Active dual-role:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validator slots (metadata):** `6`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `89115719`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

<p align="center">
  <img src="static/natix-network-logo.svg" alt="NATIX Network Logo" width="150"/>
</p>
<h1 align="center"> StreetVision  <br/> <small>Bittensor Subnet for Image Classification and Object Detection</small></h1>

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This network is a decentralized subnet designed to inference images to extract information such as construction sites. Built on Bittensor, this subnet incentivizes miners to develop and deploy models that accurately detect features, starting with construction sites.

<table style="border: none !important; width: 100% !important; border-collapse: collapse !important; margin: 0 auto !important;">
  <tbody>
    <tr>
      <td><b>Docs</b></td>
      <td><b>Resources</b></td>
    </tr>
    <tr style="vertical-align: top !important">
      <td>
        ⛏️ <a href="docs/Mining.md">Mining Guide</a><br>
        🔧 <a href="docs/Validating.md">Validator Guide</a><br>
        🏗️ <a href="#subnet-architecture">Architecture Diagrams</a><br>
        📈 <a href="docs/Incentive.md">Incentive Mechanism</a><br>
        🤝 <a href="docs/Contributor_Guide.md">Contributor Guide</a></td>
      <td>
        🚀 <a href="https://www.natix.network">NATIX Network</a><br>
        🤗 <a href="https://huggingface.co/natix-network-org">NATIX Network Hugging Face</a><br>
        📊 <a href="https://wandb.ai/natix_network/natix-testnet">W&B</a><br>
      </td>
    </tr>
  </tbody>
</table>

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** NATIX rewards tokens to network users for collecting geospatial data with the app. Download the app, mount your phone, drive, and start earning

**Fetched document title:** NATIX Network | Smartphone DePIN with IoT, Web3 & AI

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
- **`immunity_period` (blocks):** 21600
- **Registration recycle cost snapshot (`burn`):** τ0.089643086
- **Owner SS58 (`owner_ss58`):** `5HTYVBxrF2WbVN8RBtFxAkBGuHJxjgLd9Sze5gxH4KC6GLCv`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `21600` blocks
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

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/natixnetwork/streetvision-subnet/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://www.natix.network/?utm_source=bittensor](https://www.natix.network/?utm_source=bittensor)
- **GitHub:** [https://github.com/natixnetwork/streetvision-subnet](https://github.com/natixnetwork/streetvision-subnet)
- **Discord:** [https://discord.com/channels/799672011265015819/1349122541754515538](https://discord.com/channels/799672011265015819/1349122541754515538)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.003353502 |
| 8104292 | 0.003353497 |
| 8104340 | 0.003353339 |
| 8104388 | 0.003353338 |
| 8104436 | 0.003353336 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

