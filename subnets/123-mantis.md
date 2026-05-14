# NetUID 123 — MANTIS (`𑀀`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**MANTIS** (NetUID **123**) (`𑀀`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `110`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ7,841.630801646. **Alpha liquidity in pool (`alpha_in`)** = ‎1,584,146.272787410𑀀‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎1,784,147.928533353𑀀‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.004971643`** *(also **moving-average price** `0.004885409725829959` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎460,879.179416735𑀀‎`. **Owner hotkey / coldkey (chain):** `5GxsywPcZyWVYYJ7iuJpfmtujaA695M4FMCiqNRRcqNba82o` / `5HVuEdEGMYisecwjkWC7dKDPEzgs9cECdsdCQagfPRVf6FxZ`.
- **Subnet registered at block:** `5794330` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎80.338628562𑀀‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.002125616` · α-out `‎1.000000000𑀀‎` · α-in `‎0.427548176𑀀‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104325`
- **Liquidity constant `k`:** `12422290207002460873236076860`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `MANTIS` |
| Symbol (API) | `𑀀` |
| Rank | `70` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.004971773` |
| Market cap | `16293875436874.392123057` |
| Market cap Δ 1d | `6.540692303545573308` |
| Liquidity | `15716654161401` |
| Total τ | `7841238852322` |
| Total α | `3367961406654623` |
| α in pool | `1584025519483549` |
| α staked | `1693251105349160` |
| Price Δ 1h | `0.251770062914285864` |
| Price Δ 1d | `6.279770970745007754` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `123` |
| Owner SS58 (API) | `5HVuEdEGMYisecwjkWC7dKDPEzgs9cECdsdCQagfPRVf6FxZ` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `5794330` |
| Registration wall time | `2025-06-16T15:03:24Z` |
| Registration cost snapshot | `118034291488` |
| Active keys | `256` |
| Active validators | `7` |
| Active miners | `236` |
| Active dual-role | `1` |
| Emission | `2134773` |
| Max neurons | `256` |
| Validator slots (metadata) | `7` |
| Max validators (API) | `64` |
| Neuron reg. cost | `300000000` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to Barbariandev/MANTIS development by creating an account on GitHub.

**Fetched document title:** GitHub - Barbariandev/MANTIS · GitHub

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
| `difficulty` (PoW field on info view) | 18446744073709551615 |
| `immunity_period` (blocks) | 5000 |
| Registration recycle cost snapshot (`burn`) | τ0.300000000 |
| Owner SS58 (`owner_ss58`) | `5HVuEdEGMYisecwjkWC7dKDPEzgs9cECdsdCQagfPRVf6FxZ` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.300000000 / τ100.000000000 |
| PoW `difficulty` + bounds | `18446744073709551615` (min `18446744073709551615`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `5000` blocks |
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

## Dependencies

Declared in `pyproject.toml`. Core: `bittensor`, `torch`, `scikit-learn`, `numpy`, `requests`, `aiohttp`, `tqdm`, `boto3`.

See `MINER_GUIDE.md` for submission details per challenge type.

---

---

#### CPU / GPU / RAM lines (automatic grep)

- - Size: ≤ 25 MB


*Primary README URL used: `https://raw.githubusercontent.com/Barbariandev/MANTIS/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/Barbariandev/MANTIS](https://github.com/Barbariandev/MANTIS)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.004971755 |
| 8104292 | 0.004971741 |
| 8104340 | 0.004971652 |
| 8104388 | 0.00497165 |
| 8104436 | 0.004971643 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | — | 0.004871176 |
| 2026-03-10T23:59:48Z | — | 0.004815896 |
| 2026-03-11T23:59:48Z | — | 0.00502642 |
| 2026-03-12T23:59:48Z | — | 0.005029492 |
| 2026-03-13T23:59:48Z | — | 0.004945437 |
| 2026-03-14T23:59:48Z | — | 0.005028234 |
| 2026-03-15T23:59:48Z | — | 0.00492177 |
| 2026-03-16T23:59:48Z | — | 0.004864958 |
| 2026-03-17T23:59:48Z | — | 0.004597918 |
| 2026-03-18T23:59:48Z | — | 0.004885275 |
| 2026-03-19T23:59:48Z | — | 0.00454175683386 |
| 2026-03-20T23:59:48Z | — | 0.004488695 |
| 2026-03-21T23:59:48Z | — | 0.005241565 |
| 2026-03-22T23:59:48Z | — | 0.005031189 |
| 2026-03-23T23:59:48Z | — | 0.004775827 |
| 2026-03-24T23:59:48Z | — | 0.00496339384621 |
| 2026-03-25T23:59:48Z | — | 0.004747673 |
| 2026-03-26T23:59:48Z | — | 0.004617756 |
| 2026-03-27T23:59:48Z | — | 0.00461154 |
| 2026-03-28T23:59:48Z | — | 0.004525578 |
| 2026-03-29T23:59:48Z | — | 0.005005021 |
| 2026-03-30T23:59:48Z | — | 0.004800516 |
| 2026-03-31T23:59:48Z | — | 0.004873085 |
| 2026-04-01T23:59:48Z | — | 0.004811138 |
| 2026-04-02T23:59:48Z | — | 0.004689486 |
| 2026-04-03T23:59:48Z | — | 0.004665923 |
| 2026-04-04T23:59:48Z | — | 0.004684159 |
| 2026-04-05T23:59:48Z | — | 0.004650271 |
| 2026-04-06T23:59:48Z | — | 0.004617368 |
| 2026-04-07T23:59:48Z | — | 0.004607446 |
| 2026-04-08T23:59:48Z | — | 0.004450717 |
| 2026-04-09T23:59:48Z | — | 0.004514787 |
| 2026-04-10T23:59:48Z | — | 0.004784873 |
| 2026-04-11T23:59:48Z | — | 0.004697064 |
| 2026-04-12T23:59:48Z | — | 0.004758921 |
| 2026-04-13T23:59:48Z | — | 0.004686275 |
| 2026-04-14T23:59:48Z | — | 0.004603364 |
| 2026-04-15T23:59:48Z | — | 0.00443163 |
| 2026-04-16T23:59:48Z | — | 0.004422382 |
| 2026-04-17T23:59:48Z | — | 0.004343803 |
| 2026-04-18T23:59:48Z | — | 0.004552728 |
| 2026-04-19T23:59:48Z | — | 0.004577636 |
| 2026-04-20T23:59:48Z | — | 0.004453452 |
| 2026-04-21T23:59:48Z | — | 0.004474875 |
| 2026-04-22T23:59:48Z | — | 0.004777635 |
| 2026-04-23T23:59:48Z | — | 0.004542108 |
| 2026-04-24T23:59:48Z | — | 0.004483966 |
| 2026-04-25T23:59:48Z | — | 0.004521812 |
| 2026-04-26T23:59:48Z | — | 0.004560312 |
| 2026-04-27T23:59:48Z | — | 0.004508147 |
| 2026-04-28T23:59:48Z | — | 0.004649058 |
| 2026-04-29T23:59:48Z | — | 0.004662264 |
| 2026-04-30T23:59:48Z | — | 0.004648693 |
| 2026-05-01T23:59:48Z | — | 0.004614356 |
| 2026-05-02T23:59:48Z | — | 0.004741734 |
| 2026-05-03T23:59:48Z | — | 0.004971773 |

---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

