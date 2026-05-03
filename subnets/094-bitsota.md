# NetUID 94 — Bitsota (`ᚄ`)

## Overview

Decentralized SoTA Research

https://discord.gg/jkJWJtPuw7

**From crawled page (site or GitHub):** BitSota main repository. Contribute to AlveusLabs/SN94-BitSota development by creating an account on GitHub.

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
- **`difficulty` (PoW field on info view):** 18446744073709551615
- **`immunity_period` (blocks):** 5000
- **Registration recycle cost snapshot (`burn`):** τ0.000500000
- **Owner SS58 (`owner_ss58`):** `5EZRCK9op9piMhQvHqrEL1SNQU8ENU8s9aqGnRKNsUxmPYP2`

### Consensus hyperparameters (`SubnetHyperparameters` snapshot)

- **Registration allowed:** `True`
- **`min_burn` / `max_burn` (RAO envelope):** τ0.000500000 / τ100.000000000
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

## Miner / validator compute notes (README excerpts)

### For Miners

**Desktop GUI (Recommended):**
1. Download from [bitsota.ai](https://bitsota.ai)
2. Install for your platform
3. Import your Bittensor hotkey
4. Choose mining mode (Direct or Pool)
5. Start mining

See detailed setup guides:
- [Direct Mining Setup](docs/mining.md#setup)
- [Pool Mining Setup](docs/pool-mining.md#setup)

---

### For Validators

```bash
git clone https://github.com/AlveusLabs/BitSota.git
cd BitSota
pip install -r requirements.txt
pip install -e .

cp validator_config.yaml.example validator_config.yaml

---

# Edit validator_config.yaml with your wallet and burn_hotkey

python neurons/validator_node.py
```

**[→ Full Validator Setup](docs/validation.md#setup)**

---

## Requirements

**Minimum:**
- Python 3.10+
- 4GB RAM
- 2GB storage
- Stable internet connection

**For Validation:**
- 16GB RAM
- 8+ CPU cores


*README source used for excerpts: `https://raw.githubusercontent.com/AlveusLabs/SN94-BitSota/main/README.md`.*

*Headings were selected heuristically (hardware / miner / validator / requirements). Always read the full README in the repo.*

## On-chain identity — description


Decentralized SoTA Research

## On-chain identity — additional field


https://discord.gg/jkJWJtPuw7

## Registered contact & links


- **GitHub:** [https://github.com/AlveusLabs/SN94-BitSota](https://github.com/AlveusLabs/SN94-BitSota)
- **Discord (handle / invite hint):** `dev.alveuslabs`
- **Logo URL:** [https://bitsota.ai/logo.png](https://bitsota.ai/logo.png)
- **Contact:** info@bitsota.ai

## Alpha price vs TAO (history)


### Short window — on-chain α price (public RPC state retention)

Most public Finney RPC nodes discard state after only **hundreds of blocks**, so this is a **true** but **very short** slice of history (samples every **48** blocks out to roughly **576** blocks).
| Block | α price (TAO) |
|------:|----------------:|
| 8103690 | 0.005070998 |
| 8103738 | 0.005071234 |
| 8103786 | 0.005091045 |
| 8103834 | 0.005091322 |
| 8103882 | 0.00509676 |

### Extended history — TAOStats pool price (daily)

Provide **`TAOSTATS_API_KEY`** in the environment (or **`--taostats-api-key`**) to pull roughly **weekly–monthly** cadence historical prices from TAOStats. Without a key, only the abbreviated on-chain samples above populate automatically.


## Web crawl (supplementary)


- **Document title:** GitHub - AlveusLabs/SN94-BitSota: BitSota main repository · GitHub
- **Meta / og:description:** BitSota main repository. Contribute to AlveusLabs/SN94-BitSota development by creating an account on GitHub.
- **Fetched from:** [https://github.com/AlveusLabs/SN94-BitSota](https://github.com/AlveusLabs/SN94-BitSota)

---

*Snapshot: Subtensor `finney`, head block **8103882**, 2026-05-03 15:06 UTC. Regenerate via `scripts/generate_subnet_pages.py`. Chain excerpts are authoritative for protocol fields; README parsing is heuristic; TAOStats history requires API access.*

