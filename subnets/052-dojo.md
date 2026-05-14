# NetUID 52 — Dojo (`ا`)

## Overview

### Subnet narrative *(full `SubnetIdentity` text)*

**Dojo** (NetUID **52**) (`ا`).

*No **`description`** field on-chain.* Use the README excerpt (below), TAOStats snapshots, **Topology / hyperparameters** further down this page, and outbound links.

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `39`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104436)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ19,000.079901019. **Alpha liquidity in pool (`alpha_in`)** = ‎2,629,757.271057091ا‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,323,290.832010322ا‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007225137`** *(also **moving-average price** `0.007245828630402684` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎742,695.586398753ا‎`. **Owner hotkey / coldkey (chain):** `5EgfUiH6A99dhihMzp7eMM8UDkvmFjCWgM5gnpBN8UgLrVuz` / `5Fv1ZvNPsEvUN6jfia6Mv3ZoefZ6KdoowGMjkPMX61QwRLXx`.
- **Subnet registered at block:** `3989825` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎29.423637289ا‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ا‎` · α-in `‎0.000000000ا‎`.

#### Further numeric `DynamicInfo` fields

- **`last_step` (block):** `8104396`
- **Liquidity constant `k`:** `49965598270370409120778075729`

*Values are pallet **`DynamicInfo`** at head block **8104436**. **`last_step`** anchors the most recent epoch advance. On-chain swap math also exposes callables on this object in Python (e.g. `tao_to_alpha`); see Bittensor `DynamicInfo` docs. **`tempo`** / **`blocks_since_last_step`** describe pacing; **`tao_in`** / **`alpha_in`** / **`alpha_out`** split liquidity; **`price`** reflects τ-per-α (see **`moving_price`**).*

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)


| Field | Value |
| --- | --- |
| Subnet name (API) | `Dojo` |
| Symbol (API) | `ا` |
| Rank | `34` |
| Block (API) | `8104202` |
| Time (API) | `2026-05-03T16:10:00Z` |
| Price τ/α | `0.007225184` |
| Market cap | `30227342236862.657366048` |
| Market cap Δ 1d | `-3.066642785140106367` |
| Liquidity | `38000560059371` |
| Total τ | `19000141433397` |
| Total α | `4952815103067413` |
| α in pool | `2629748754630281` |
| α staked | `1553859889365866` |
| Price Δ 1h | `-0.00192378942782212` |
| Price Δ 1d | `-3.165658498300449809` |

#### Subnet activity (TAOStats)


| Field | Value |
| --- | --- |
| NetUID (API) | `52` |
| Owner SS58 (API) | `5Fv1ZvNPsEvUN6jfia6Mv3ZoefZ6KdoowGMjkPMX61QwRLXx` |
| Block (API) | `8104199` |
| Time (API) | `2026-05-03T16:09:24.001Z` |
| Registration block | `3989825` |
| Registration wall time | `2024-10-07T08:39:00Z` |
| Registration cost snapshot | `0` |
| Active keys | `256` |
| Active validators | `12` |
| Active miners | `1` |
| Active dual-role | `0` |
| Emission | `0` |
| Max neurons | `256` |
| Validator slots (metadata) | `12` |
| Max validators (API) | `64` |
| Neuron reg. cost | `999999999` |
| Tempo (API) | `360` |
| Min allowed weights (API) | `1` |
| Max weights limit (API) | `65535` |
| Activity cutoff | `5000` |

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to tensorplex-labs/dojo development by creating an account on GitHub.

**Fetched document title:** GitHub - tensorplex-labs/dojo · GitHub

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
| `immunity_period` (blocks) | 10800 |
| Registration recycle cost snapshot (`burn`) | τ0.999999999 |
| Owner SS58 (`owner_ss58`) | `5Fv1ZvNPsEvUN6jfia6Mv3ZoefZ6KdoowGMjkPMX61QwRLXx` |


### Consensus hyperparameters (`SubnetHyperparameters` snapshot)


| Field | Value |
| --- | --- |
| Registration allowed | `True` |
| `min_burn` / `max_burn` (RAO envelope) | τ0.999999999 / τ100.000000000 |
| PoW `difficulty` + bounds | `10000000` (min `10000000`, max `18446744073709551615`) |
| `target_regs_per_interval` | `1` |
| `immunity_period` | `10800` blocks |
| `max_regs_per_block` | `1` |
| `serving_rate_limit` | `50` |
| `weights_rate_limit` | `100` |
| `activity_cutoff` | `5000` blocks |
| `commit_reveal_weights_enabled` | `False` |
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

## Miner

Miners do not need to spin up any server or code level things to mine! You just need to register to the network, and load your hotkey wallet onto a browser wallet e.g. Talisman and wait to receive tasks.
Start mining at [Testnet](https://testnet.dojo.network) | [Mainnet](https://dojo.network)

```bash

---

## Validator

Please refer the [setup guide](docs/validator.md).

---

### Git hooks (required)

This repo uses lefthook to enforce quality gates:

- pre-commit: make fmt, make vet, make lint
- pre-push: go test ./...
  Install and keep it current:
- make preflight
- lefthook install -f # force reinstall if hooks don’t run
- git config --get core.hooksPath (should be unset for default)

---

#### CPU / GPU / RAM lines (automatic grep)

*No sizing lines matched the scrape heuristics — see `docs/`, repo guides, Discord, or homepage.*


*Primary README URL used: `https://raw.githubusercontent.com/tensorplex-labs/dojo/main/README.md`*

## SubnetIdentity links *(from chain)*


*Full **`description`** / **`additional`** text is under **Overview → Subnet narrative**.*


- **GitHub:** [https://github.com/tensorplex-labs/dojo](https://github.com/tensorplex-labs/dojo)
- **Contact:** jarvis@tensorplex.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104244 | 0.007225169 |
| 8104292 | 0.007225159 |
| 8104340 | 0.007225143 |
| 8104388 | 0.007225142 |
| 8104436 | 0.007225137 |

### Extended history — TAOStats pool price (daily)

*TAOStats fetch failed:* `HTTP 429: {"status_code":429,"message":"Rate Limited. Try Again Later."}`


---

*Subtensor `finney`, block **8104436**, 2026-05-03 16:56 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

