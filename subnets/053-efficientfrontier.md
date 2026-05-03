# NetUID 53 — EfficientFrontier (`ب`)

## Overview

**From crawled page (site or GitHub):** Contribute to EfficientFrontier-SignalPlus/EfficientFrontier development by creating an account on GitHub.

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
- **`immunity_period` (blocks):** 1
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5Fv2Qm2w9tnotv9xpGq9EVKaSjRtFzGdas5RBsUswpdsE5Sh`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
- **PoW `difficulty` + bounds:** `10000000` (min `10000000`, max `18446744073709551615`)
- **`target_regs_per_interval`:** `1`
- **`immunity_period`:** `1` blocks
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

## Miner / validator compute notes (README excerpts)

### 2. Professional Trading Infrastructure

SignalPlus is a professionally recognized and trusted partner with most of crypto's largest exchanges, offering a comprehensive suite of trading tools and risk management features available to every user. Traders can utilize the SignalPlus platform to execute complex and algorithmic trades in a systematic way, freeing up their focus to refine trading frameworks and higher cognitive functions that ultimately generate true alpha.

Some of SignalPlus's advanced trading functions include:
- **Stop Loss/Take Profit**
- **Iceberg Orders**
- **Balance Trade**
- **TWAP (Time-Weighted Average Price)**
- **DDH (Dynamic Delta Hedging)**

In a nutshell, the **SignalPlus platform dramatically lowers the barriers to entry**, and directly expands the group of participating subnet miners into the Bittensor network.  **SignalPlus is the critical link** that ensures the authenticity of trading data and provides traders with the tools they need to succeed.

Without such a platform, it would be impossible to securely validate trades or to provide the professional trading infrastructure to promote a high quality data environment. By removing unwanted technical complexities, SignalPlus allows traders to focus on what really matters — their strategy — while ensuring a robust environment with the requisite fairness and transparency that will best accentuate the power of the Bittensor network as we unlock a new chapter in network-learning models.

---

### Miners Installation

- The miner will call the official public API to retrieve account-related metadata such as balance, equity, PnL, and drawdown, which are generated from the user's trading activities on the platform [t.signalplus.com](https://t.signalplus.com).
- This data is then passed to the validator for evaluating the strategy's performance.
- During transmission, asymmetric encryption is used to ensure the data remains untampered with, guaranteeing fairness and integrity.
- You can find detailed instructions on how to become a miner via the following link: <p> [how-to-join-the-greatest-tournament-of-crypto](docs/Introduction/HowToJoin.md)
- [running_miner_on_mainnet](docs/running_on_mainnet.md)

---

### Validator Installation

- The validator locally synchronizes the latest blockchain and retrieves all metadata uploaded by the corresponding miners.
- Initially, it verifies the authenticity of the data using asymmetric encryption.
- Once validated, the validator applies a Ranking Model to calculate the miner's weight and updates the results on the blockchain. This will determine the amount of rewards the miner can receive in the next cycle.
- During this process, risk control checks are conducted, and if any fraudulent activity is detected, penalties may be imposed, including disqualification from the competition.
- [running_validator_on_testnet](docs/running_on_testnet.md)
- [running_validator_on_mainnet](docs/running_on_mainnet.md)

---

### Registration Fee for Miners

Each miner wishing to participate in the Efficient Frontier subnet is required to pay a registration fee of **1 TAO** to Bittensor. This amount may be adjusted in the future based on the subnet's weight. Recognizing that our target miners are primarily quantitative trading teams and individuals engaged in complex derivatives trading—who may not be familiar with Bittensor or DeFi and might not have their own crypto wallets—we aim to simplify the onboarding process.

To lower the entry barrier, **SignalPlus** will directly charge miners in **USDT** and exchange it for TAO on their behalf, handling the cross-chain payment to Bittensor. Considering the current value of TAO is approximately **\$450 USD**, plus additional cross-chain and network gas fees, we plan to initially charge a registration fee of **\$500 USD**. This fee will be periodically adjusted to reflect any significant changes in TAO's market price.

If there is any surplus from the registration fee after paying the required 1 TAO to Bittensor, we will allocate the excess USDT as follows:

1. **Price Fluctuation Buffer**: To hedge against potential losses if TAO's price increases sharply before we can adjust the USDT registration fee.
2. **Community Rewards**: Periodically distribute the surplus directly to participating miners as rewards.

By handling the TAO acquisition and payment process, we aim to make it as easy as possible for miners to join the subnet, allowing them to focus on what they do best—trading.

---

### What are the expected operations for a miner?

- You need to operate with a certain capital base, be actively trading, with a goal of maximizing your return against the lowest possible drawdowns via the [t.signalplus.com](https://t.signalplus.com) platform.
- Your scores will be judged based on a 'drawdown-adjusted' return (as defined above), with rewards based on your daily rankings.

---

### Do I need a GPU to run a miner or validator?

- No, you don't.

---

### Does SignalPlus require KYC?

- KYC is not required for our new SignalPlus users as our platform does not touch customer assets at any point of the workflow; however, the platform requires a CEX account API to work as most derivative trading liquidity is still aggregated on CEX.


*README source used for excerpts: `https://raw.githubusercontent.com/EfficientFrontier-SignalPlus/EfficientFrontier/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


*Empty — no description bytes set in `SubnetIdentity`.*

## On-chain identity — additional field


*Empty — no additional field set, or identity missing.*

## Registered contact & links


- **GitHub:** [https://github.com/EfficientFrontier-SignalPlus/EfficientFrontier](https://github.com/EfficientFrontier-SignalPlus/EfficientFrontier)

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103642 | 0.005988661 |
| 8103690 | 0.005994415 |
| 8103738 | 0.005994525 |
| 8103786 | 0.005995744 |
| 8103834 | 0.005995856 |
| 8103882 | 0.005996144 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** GitHub - EfficientFrontier-SignalPlus/EfficientFrontier · GitHub
- **Meta / og:description:** Contribute to EfficientFrontier-SignalPlus/EfficientFrontier development by creating an account on GitHub.
- **Fetched from:** [https://github.com/EfficientFrontier-SignalPlus/EfficientFrontier](https://github.com/EfficientFrontier-SignalPlus/EfficientFrontier)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

