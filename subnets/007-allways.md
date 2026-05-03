# NetUID 7 — Allways (`η`)

## Overview

universal transaction layer

**From crawled page (site or GitHub):** Allways

## Operational parameters — registration, limits, economics (chain)


**What is on-chain here:** consensus / registration economics (burns, immunity, capacities, tempo, weight rules). These are **not** GPU SKU requirements—those live in subnet code and READMEs (see the next section when GitHub excerpts are available).

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
- **`immunity_period` (blocks):** 10800
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5CAc19iETJmWD2rYVX1ht58ghCpyHq86MoBNdx5TzLfinzcx`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `100`
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

## Miner / validator compute notes (README excerpts)

### Requirements

- Python 3.10+
- Bittensor wallet
- Docker & Docker Compose

---

## Validator Storage Layout

Validator state lives in `~/.allways/validator/state.db` (SQLite, WAL mode).
Tables: `pending_confirms`, `rate_events`, `swap_outcomes`. Collateral /
active / min_collateral state is held in memory and rebuilt from contract
events each startup; only `swap_outcomes` (the all-time credibility ledger)
needs to persist across restarts.

---

## Miner Environment Variables

- `MINER_TIMEOUT_CUSHION_BLOCKS` — defaults to 5. Miner skips fulfilling a
  swap when fewer than this many blocks remain before its timeout, trading
  a skipped swap for avoided slashes on slow dest-chain inclusion.
- `BTC_MODE`, `BTC_PRIVATE_KEY`, `BTC_RPC_URL`, etc. — see `.env.example`.

---

## Running a Local Subtensor Lite Node (Validators)

Validators read miner rate commitments every ~3 minutes AND stream contract
events every block via the same connection. Pointing at the public `finney`
entrypoint works but adds latency and RPC pressure — every validator on the
network should run its own lite node for this.

```bash


*README source used for excerpts: `https://raw.githubusercontent.com/entrius/allways/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


universal transaction layer

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **Website:** [https://all-ways.io/](https://all-ways.io/)
- **GitHub:** [https://github.com/entrius/allways](https://github.com/entrius/allways)
- **Logo URL:** [https://allways-905418005698-us-east-2-an.s3.us-east-2.amazonaws.com/sn7-light.png](https://allways-905418005698-us-east-2-an.s3.us-east-2.amazonaws.com/sn7-light.png)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.004813142 |
| 8103690 | 0.004822649 |
| 8103738 | 0.004805362 |
| 8103786 | 0.004816396 |
| 8103834 | 0.004816524 |
| 8103882 | 0.004811807 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** Allways
- **Meta / og:description:** Allways
- **Fetched from:** [https://all-ways.io/](https://all-ways.io/)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

