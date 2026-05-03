# NetUID 4 — Targon (`δ`)

## Overview

**Targon** (NetUID **4**) (`δ`).

Incentivized Compute Marketplace powered by the Targon Virtual Machine (TVM).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `194`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ132,430.336928233. **Alpha liquidity in pool (`alpha_in`)** = ‎2,311,840.640343520δ‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,799,367.164963178δ‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.057285210`** *(also **moving-average price** `0.05783221940509975` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎1,983,114.519547265δ‎`. **Owner hotkey / coldkey (chain):** `5Hp18g9P8hLGKp9W3ZDr4bvJwba6b6bY3P2u3VdYf8yMR8FM` / `5CXGPMnq9RCCLUEvp9G2iUuabw69TSFM155UVS1S4Zmusaxv`.
- **Subnet registered at block:** `1411451` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎146.695220296δ‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.017842212` · α-out `‎1.000000000δ‎` · α-in `‎0.311462741δ‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.057221392`
- **Market cap:** `264658685461101.924572128`
- **Liquidity:** `264714449340654`
- **Total τ:** `132355261157812`
- **Total α:** `5111110210761540`
- **α in pool:** `2313106751804326`
- **α staked:** `2312063594647608`
- **Price Δ 1h:** `-0.45622540267843479`
- **Price Δ 1d:** `0.176965079092971994`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `5`
- **Active miners:** `6`
- **Active dual:** `1`
- **Emission:** `17140816`
- **Max neurons:** `256`
- **Validators (metadata):** `5`
- **Neuron reg. cost:** `500000`

### On-chain declared purpose *(SubnetIdentity)*

Incentivized Compute Marketplace powered by the Targon Virtual Machine (TVM).

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

## On-chain identity — description


Incentivized Compute Marketplace powered by the Targon Virtual Machine (TVM).

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **Website:** [https://targon.com](https://targon.com)
- **GitHub:** [https://github.com/manifold-inc/targon](https://github.com/manifold-inc/targon)
- **Logo URL:** [https://www.manifold.inc/favicon.svg](https://www.manifold.inc/favicon.svg)
- **Contact:** devs@manifold.inc

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104037 | 0.057441032 |
| 8104085 | 0.057214199 |
| 8104133 | 0.057218319 |
| 8104181 | 0.057222265 |
| 8104229 | 0.057221398 |
| 8104277 | 0.05728521 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

