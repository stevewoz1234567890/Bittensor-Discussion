# NetUID 4 — Targon (`δ`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Targon** (NetUID **4**) (`δ`).

Incentivized Compute Marketplace powered by the Targon Virtual Machine (TVM).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `352`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ132,433.964824490. **Alpha liquidity in pool (`alpha_in`)** = ‎2,311,875.678530524δ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,799,539.311407608δ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.057285911`** *(also **moving-average price** `0.0578084378503263` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,983,143.205161180δ‎`. **Owner hotkey / coldkey (chain):** `5Hp18g9P8hLGKp9W3ZDr4bvJwba6b6bY3P2u3VdYf8yMR8FM` / `5CXGPMnq9RCCLUEvp9G2iUuabw69TSFM155UVS1S4Zmusaxv`.
- **Subnet registered at block:** `1411451` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎266.169181074δ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.017837652` · α-out `‎1.000000000δ‎` · α-in `‎0.311379394δ‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104083`
- **Liquidity constant `k`:** `306170862289105366508767732760`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Subnet name (API):** `Targon`
- **Symbol (API):** `δ`
- **Rank:** `2`
- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.057221392`
- **Market cap:** `264658685461101.924572128`
- **Market cap Δ 1d:** `0.356628249092294066`
- **Liquidity:** `264714449340654`
- **Total τ:** `132355261157812`
- **Total α:** `5111110210761540`
- **α in pool:** `2313106751804326`
- **α staked:** `2312063594647608`
- **Price Δ 1h:** `-0.45622540267843479`
- **Price Δ 1d:** `0.176965079092971994`
#### Subnet activity (TAOStats)

- **NetUID (API):** `4`
- **Owner SS58 (API):** `5CXGPMnq9RCCLUEvp9G2iUuabw69TSFM155UVS1S4Zmusaxv`
- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Registration block:** `1411451`
- **Registration wall time:** `2023-10-03T17:56:12.003Z`
- **Registration cost snapshot:** `0`
- **Active keys:** `256`
- **Active validators:** `5`
- **Active miners:** `6`
- **Active dual-role:** `1`
- **Emission:** `17140816`
- **Max neurons:** `256`
- **Validator slots (metadata):** `5`
- **Max validators (API):** `64`
- **Neuron reg. cost:** `500000`
- **Tempo (API):** `360`
- **Min allowed weights (API):** `1`
- **Max weights limit (API):** `65535`
- **Activity cutoff:** `5000`

### Repository README excerpt *(everything before first `##` heading)*

# Targon: The Confidential Decentralized AI Cloud

Targon is a next-generation AI infrastructure platform that leverages
Confidential Compute (CC) and Protected pcie (PPCIE) technology to secure the
entire stack. By providing a secure execution environment from hardware to
application layers, Targon enables verifiable and trustworthy operations across
the entire infrastructure in a decentralized fashion.

NOTICE: Using this software, you must agree to the Terms and Agreements provided
in the terms and conditions document. By downloading and running this software,
you implicitly agree to these terms and conditions.

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Scale with Secure GPU & CPU Rentals on a Lightning-Fast Cloud for Training and Deployment

**Fetched document title:** Targon

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
- **`immunity_period` (blocks):** 7520
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CXGPMnq9RCCLUEvp9G2iUuabw69TSFM155UVS1S4Zmusaxv`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `100000000000000`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `7520` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `True`
- **`commit_reveal_period`:** `1`
- **`liquid_alpha_enabled`:** `False`
- **`user_liquidity_enabled` (subnet pool):** `False`
- **`bonds_reset_enabled` / `bonds_moving_avg`:** `False` / `1`
- **`subnet_is_active`:** `True`
- **`yuma_version`:** `2`
- **`alpha_sigmoid_steepness` / `alpha_high` / `alpha_low`:** 1000.0, `58982`, `45875`

- **Docs:** [Subnet hyperparameters (Learn Bittensor)](https://learnbittensor.org/explore/concept/subnet-hyperparameters)

## Miner / validator hardware (CPU/GPU/RAM)

#### Sections matched by heading (miner / validator / hardware / requirements)

# Targon: The Confidential Decentralized AI Cloud

Targon is a next-generation AI infrastructure platform that leverages
Confidential Compute (CC) and Protected pcie (PPCIE) technology to secure the
entire stack. By providing a secure execution environment from hardware to
application layers, Targon enables verifiable and trustworthy operations across
the entire infrastructure in a decentralized fashion.

NOTICE: Using this software, you must agree to the Terms and Agreements provided
in the terms and conditions document. By downloading and running this software,
you implicitly agree to these terms and conditions.

---

### AI Infrastructure Capabilities

- End-to-end secure model inference pipeline
- Hardware-level attestation and verification
- Protected model execution with CC or PPCIE isolation
- Verifiable computation through remote attestation
- Secure memory management for AI workloads
- Isolated execution environment for sensitive operations

---

#### CPU / GPU / RAM lines (automatic grep)

- - GPU TEE (Trusted Execution Environment) for isolated execution
- - NVIDIA Confidential Compute integration OR
- - NVIDIA PPCIE
- - AMD SEV-SNP integration


*Primary README URL used: `https://raw.githubusercontent.com/manifold-inc/targon/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **Website:** [https://targon.com](https://targon.com)
- **GitHub:** [https://github.com/manifold-inc/targon](https://github.com/manifold-inc/targon)
- **Logo URL:** [https://www.manifold.inc/favicon.svg](https://www.manifold.inc/favicon.svg)
- **Contact:** devs@manifold.inc

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104196 | 0.057221401 |
| 8104244 | 0.057223037 |
| 8104292 | 0.057285193 |
| 8104340 | 0.057285718 |
| 8104388 | 0.057282509 |
| 8104436 | 0.057285911 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.046600613 |
| 2026-03-10T23:59:48Z | 7718257 | 0.044671352 |
| 2026-03-11T23:59:48Z | 7725455 | 0.044992059 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.045044181 |
| 2026-03-13T23:59:48Z | 7739841 | 0.044617073 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.044974878 |
| 2026-03-15T23:59:48Z | 7754226 | 0.048140667 |
| 2026-03-16T23:59:48Z | 7761426 | 0.050329983 |
| 2026-03-17T23:59:48Z | 7768619 | 0.048695883 |
| 2026-03-18T23:59:48Z | 7775819 | 0.048080551 |
| 2026-03-19T23:59:48Z | 7783014 | 0.04836100149019909583 |
| 2026-03-20T23:59:48Z | 7790201 | 0.049109114 |
| 2026-03-21T23:59:48Z | 7797398 | 0.049968164 |
| 2026-03-22T23:59:48Z | 7804598 | 0.05165981 |
| 2026-03-23T23:59:48Z | 7811798 | 0.061013414 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.06184430854535391113 |
| 2026-03-25T23:59:48Z | 7826196 | 0.066822963 |
| 2026-03-26T23:59:48Z | 7833396 | 0.060947965 |
| 2026-03-27T23:59:48Z | 7840596 | 0.061895334 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.063063153 |
| 2026-03-29T23:59:48Z | 7854902 | 0.065204757 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.064037034 |
| 2026-03-31T23:59:48Z | 7869291 | 0.062491315 |
| 2026-04-01T23:59:48Z | 7876474 | 0.063967724 |
| 2026-04-02T23:59:48Z | 7883622 | 0.062467608 |
| 2026-04-03T23:59:48Z | 7890794 | 0.062987777 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.062974174 |
| 2026-04-05T23:59:48Z | 7905188 | 0.062341489 |
| 2026-04-06T23:59:48Z | 7912388 | 0.062265633 |
| 2026-04-07T23:59:48Z | 7919588 | 0.061441453 |
| 2026-04-08T23:59:48Z | 7926788 | 0.059118644 |
| 2026-04-09T23:59:48Z | 7933987 | 0.054508584 |
| 2026-04-10T23:59:48Z | 7941184 | 0.053899182 |
| 2026-04-11T23:59:48Z | 7948384 | 0.054216944 |
| 2026-04-12T23:59:48Z | 7955584 | 0.053167615 |
| 2026-04-13T23:59:48Z | 7962784 | 0.05393021 |
| 2026-04-14T23:59:48Z | 7969979 | 0.052268678 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.052176297 |
| 2026-04-16T23:59:48Z | 7984379 | 0.053980353 |
| 2026-04-17T23:59:48Z | 7991579 | 0.055863978 |
| 2026-04-18T23:59:48Z | 7998779 | 0.056493406 |
| 2026-04-19T23:59:48Z | 8005979 | 0.056178061 |
| 2026-04-20T23:59:48Z | 8013179 | 0.057823106 |
| 2026-04-21T23:59:48Z | 8020376 | 0.059238895 |
| 2026-04-22T23:59:48Z | 8027562 | 0.059936151 |
| 2026-04-23T23:59:48Z | 8034762 | 0.05899197 |
| 2026-04-24T23:59:48Z | 8041962 | 0.058073284 |
| 2026-04-25T23:59:48Z | 8049151 | 0.059177521 |
| 2026-04-26T23:59:48Z | 8056274 | 0.059106068 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.059256637 |
| 2026-04-28T23:59:48Z | 8070646 | 0.058311586 |
| 2026-04-29T23:59:48Z | 8077790 | 0.058234294 |
| 2026-04-30T23:59:48Z | 8084984 | 0.057661247 |
| 2026-05-01T23:59:48Z | 8092168 | 0.057040686 |
| 2026-05-02T23:59:48Z | 8099357 | 0.057896253 |
| 2026-05-03T16:10:00Z | 8104202 | 0.057221392 |


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

