# NetUID 52 — Dojo (`ا`)

## Overview

**Dojo** (NetUID **52**) (`ا`).

### Chain & market snapshot *(from `DynamicInfo`)*

- **Tempo / epoch pacing:** `360` blocks between steps; **blocks since last step:** `180`. **Emission allocation field:** `τ0.000000000` *(protocol snapshot at block 8104216)*.
- **TAO routed into swap pool reserves:** **`tao_in`** = τ19,000.141044834. **Alpha liquidity in pool (`alpha_in`)** = ‎2,629,748.808410370ا‎; **`alpha_out`** (off-pool bonded/staked tally) = ‎2,323,079.294657043ا‎.
- **Implied Alpha spot:** **`price`** τ per α unit ≈ **`τ0.007225183`** *(also **moving-average price** `0.007247202331200242` used in some dashboards)*.
- **Outstanding subnet volume accumulator:** `‎742,695.525254938ا‎`. **Owner hotkey / coldkey (chain):** `5EgfUiH6A99dhihMzp7eMM8UDkvmFjCWgM5gnpBN8UgLrVuz` / `5Fv1ZvNPsEvUN6jfia6Mv3ZoefZ6KdoowGMjkPMX61QwRLXx`.
- **Subnet registered at block:** `3989825` (see explorers for approximate wall-clock age). **Is dynamic liquidity subnet:** `True`.
- **Pending emissions cues:** pending α emission `‎135.800472973ا‎`; pending root emission `τ0.000000000`.
- **Per-flow emission splits:** τ-in `τ0.000000000` · α-out `‎1.000000000ا‎` · α-in `‎0.000000000ا‎`.

### TAOStats snapshot *(off-chain index)*

Sources: [subnet latest](https://docs.taostats.io/reference/get-subnets-1), [pool latest](https://docs.taostats.io/reference/get-subnet-pools).
#### Liquidity pool (TAOStats)

- **Block (API):** `8104202`
- **Time (API):** `2026-05-03T16:10:00Z`
- **Price τ/α:** `0.007225184`
- **Market cap:** `30227342236862.657366048`
- **Liquidity:** `38000560059371`
- **Total τ:** `19000141433397`
- **Total α:** `4952815103067413`
- **α in pool:** `2629748754630281`
- **α staked:** `1553859889365866`
- **Price Δ 1h:** `-0.00192378942782212`
- **Price Δ 1d:** `-3.165658498300449809`
#### Subnet activity (TAOStats)

- **Block (API):** `8104199`
- **Time (API):** `2026-05-03T16:09:24.001Z`
- **Active keys:** `256`
- **Active validators:** `12`
- **Active miners:** `1`
- **Active dual:** `0`
- **Emission:** `0`
- **Max neurons:** `256`
- **Validators (metadata):** `12`
- **Neuron reg. cost:** `999999999`

### On-chain declared purpose *(SubnetIdentity)*

*SubnetIdentity **description** is empty on-chain; see README, links below, or off-chain docs.*

### Repository README excerpt *(everything before first `##` heading)*

*README text unavailable for extraction (no compatible GitHub link or Markdown too short).*

### Supplementary site crawl *(marketing HTML)*

**Landing meta / crawler:** Contribute to tensorplex-labs/dojo development by creating an account on GitHub.

**Fetched document title:** GitHub - tensorplex-labs/dojo · GitHub

## Operational parameters — registration, limits, economics (chain)


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
- **Registration recycle cost snapshot (`burn`):** τ0.999999999
- **Owner SS58 (`owner_ss58`):** `5Fv1ZvNPsEvUN6jfia6Mv3ZoefZ6KdoowGMjkPMX61QwRLXx`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.999999999 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `10800` blocks
- **`max_regs_per_block`:** `1`
- **`serving_rate_limit`:** `50`
- **`weights_rate_limit`:** `100`
- **`activity_cutoff`:** `5000` blocks
- **`commit_reveal_weights_enabled`:** `False`
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

## On-chain identity — description


*Unset in `SubnetIdentity`.*

## On-chain identity — additional field


*Unset.*

## Registered contact & links


- **GitHub:** [https://github.com/tensorplex-labs/dojo](https://github.com/tensorplex-labs/dojo)
- **Contact:** jarvis@tensorplex.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

*Probes every **48** blocks, lookback ≈ **576** blocks (bounded by typical public RPC history depth).*
| Block | α price (TAO) |
|------:|----------------:|
| 8104024 | 0.007225315 |
| 8104072 | 0.007225311 |
| 8104120 | 0.007225305 |
| 8104168 | 0.007225186 |
| 8104216 | 0.007225183 |

### Extended history — TAOStats pool price (daily)

[TAOStats](https://docs.taostats.io/reference/get-historical-subnet-pools) daily pool **`price`** (TAO per α), **120** rows in this snapshot.

| Timestamp (UTC) | Block | Pool price |
|-----------------|------:|-----------:|
| 2026-03-09T23:59:48Z | 7711060 | 0.008467911 |
| 2026-03-10T23:59:48Z | 7718257 | 0.008369303 |
| 2026-03-11T23:59:48Z | 7725455 | 0.008350783 |
| 2026-03-12T23:59:48.001Z | 7732653 | 0.00834742 |
| 2026-03-13T23:59:48Z | 7739841 | 0.007304328 |
| 2026-03-14T23:59:48.001Z | 7747036 | 0.007432864 |
| 2026-03-15T23:59:48Z | 7754226 | 0.007281606 |
| 2026-03-16T23:59:48Z | 7761426 | 0.007163811 |
| 2026-03-17T23:59:48Z | 7768619 | 0.006930582 |
| 2026-03-18T23:59:48Z | 7775819 | 0.007121404 |
| 2026-03-19T23:59:48Z | 7783014 | 0.00716854220757642154 |
| 2026-03-20T23:59:48Z | 7790201 | 0.006930637 |
| 2026-03-21T23:59:48Z | 7797398 | 0.006923277 |
| 2026-03-22T23:59:48Z | 7804598 | 0.006939209 |
| 2026-03-23T23:59:48Z | 7811798 | 0.006947596 |
| 2026-03-24T23:59:48.001Z | 7818996 | 0.00698861303952297978 |
| 2026-03-25T23:59:48Z | 7826196 | 0.006975721 |
| 2026-03-26T23:59:48Z | 7833396 | 0.007027653 |
| 2026-03-27T23:59:48Z | 7840596 | 0.007027523 |
| 2026-03-28T23:59:48.001Z | 7847743 | 0.007053246 |
| 2026-03-29T23:59:48Z | 7854902 | 0.007051001 |
| 2026-03-30T23:59:48.001Z | 7862095 | 0.00711649 |
| 2026-03-31T23:59:48Z | 7869291 | 0.007172853 |
| 2026-04-01T23:59:48Z | 7876474 | 0.007228082 |
| 2026-04-02T23:59:48Z | 7883622 | 0.007209636 |
| 2026-04-03T23:59:48Z | 7890794 | 0.007201373 |
| 2026-04-04T23:59:48.001Z | 7897988 | 0.007102141 |
| 2026-04-05T23:59:48Z | 7905188 | 0.007098693 |
| 2026-04-06T23:59:48Z | 7912388 | 0.007092407 |
| 2026-04-07T23:59:48Z | 7919588 | 0.007076258 |
| 2026-04-08T23:59:48Z | 7926788 | 0.007071842 |
| 2026-04-09T23:59:48Z | 7933987 | 0.007051831 |
| 2026-04-10T23:59:48Z | 7941184 | 0.007089542 |
| 2026-04-11T23:59:48Z | 7948384 | 0.007112514 |
| 2026-04-12T23:59:48Z | 7955584 | 0.007133586 |
| 2026-04-13T23:59:48Z | 7962784 | 0.007167387 |
| 2026-04-14T23:59:48Z | 7969979 | 0.00722896 |
| 2026-04-15T23:59:48.001Z | 7977179 | 0.007240976 |
| 2026-04-16T23:59:48Z | 7984379 | 0.007243785 |
| 2026-04-17T23:59:48Z | 7991579 | 0.007326508 |
| 2026-04-18T23:59:48Z | 7998779 | 0.007309283 |
| 2026-04-19T23:59:48Z | 8005979 | 0.00732773 |
| 2026-04-20T23:59:48Z | 8013179 | 0.007312588 |
| 2026-04-21T23:59:48Z | 8020376 | 0.007270079 |
| 2026-04-22T23:59:48Z | 8027562 | 0.007268947 |
| 2026-04-23T23:59:48Z | 8034762 | 0.007273155 |
| 2026-04-24T23:59:48Z | 8041962 | 0.007285815 |
| 2026-04-25T23:59:48Z | 8049151 | 0.007282559 |
| 2026-04-26T23:59:48Z | 8056274 | 0.007281935 |
| 2026-04-27T23:59:48.001Z | 8063454 | 0.007271578 |
| 2026-04-28T23:59:48Z | 8070646 | 0.007305443 |
| 2026-04-29T23:59:48Z | 8077790 | 0.007265691 |
| 2026-04-30T23:59:48Z | 8084984 | 0.007260285 |
| 2026-05-01T23:59:48Z | 8092168 | 0.007241175 |
| 2026-05-02T23:59:48Z | 8099357 | 0.007307313 |
| 2026-05-03T16:10:00Z | 8104202 | 0.007225184 |


---

*Subtensor `finney`, block **8104216**, 2026-05-03 16:12 UTC. Regenerate: `scripts/generate_subnet_pages.py`.*

