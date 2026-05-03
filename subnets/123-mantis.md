# NetUID 123 — MANTIS (`𑀀`)

## Overview

**MANTIS** (NetUID **123**) (`𑀀`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `313`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104277)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,841.375144931. **Alpha liquidity in pool (`alpha_in`)** = ‎1,584,062.474475997𑀀‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,784,006.116348188𑀀‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004971744`** *(also **moving-average price** `0.004881599685177207` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎460,879.098936003𑀀‎`. **Owner hotkey / coldkey (chain):** `5GxsywPcZyWVYYJ7iuJpfmtujaA695M4FMCiqNRRcqNba82o` / `5HVuEdEGMYisecwjkWC7dKDPEzgs9cECdsdCQagfPRVf6FxZ`.
- **Subnet registered at block:** `5794330` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎228.597152464𑀀‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002127947` · α-out `‎1.000000000𑀀‎` · α-in `‎0.428008151𑀀‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.004971773`
- **Market cap:** `16293875436874.392123057`
- **Liquidity:** `15716654161401`
- **Total τ:** `7841238852322`
- **Total α:** `3367961406654623`
- **α in pool:** `1584025519483549`
- **α staked:** `1693251105349160`
- **Price Δ 1h:** `0.251770062914285864`
- **Price Δ 1d:** `6.279770970745007754`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `7`
- **Active miners:** `236`
- **Active dual:** `1`
- **Emission:** `2134773`
- **Max neurons:** `256`
- **Validators (metadata):** `7`
- **Neuron reg. cost:** `300000000`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to Barbariandev/MANTIS development by creating an account on GitHub.

**Fetched document title:** GitHub - Barbariandev/MANTIS · GitHub

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
- **Registration recycle cost snapshot (`burn`):** τ0.300000000
- **Owner SS58 (`owner_ss58`):** `5HVuEdEGMYisecwjkWC7dKDPEzgs9cECdsdCQagfPRVf6FxZ`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.300000000 / τ100.000000000
- **PoW `difficulty` + bounds:** `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `5000` blocks
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

## Dependencies

Declared in `pyproject.toml`. Core: `bittensor`, `torch`, `scikit-learn`, `numpy`, `requests`, `aiohttp`, `tqdm`, `boto3`.

See `MINER_GUIDE.md` for submission details per challenge type.

---

---

#### CPU / GPU / RAM lines (automatic grep)

- - Size: ≤ 25 MB


*Primary README URL used: `https://raw.githubusercontent.com/Barbariandev/MANTIS/main/README.md`*

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/Barbariandev/MANTIS](https://github.com/Barbariandev/MANTIS)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104085 | 0.004975456 |
| 8104133 | 0.004975446 |
| 8104181 | 0.004971648 |
| 8104229 | 0.00497176 |
| 8104277 | 0.004971744 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104277**, 2026-05-03 16:25 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

