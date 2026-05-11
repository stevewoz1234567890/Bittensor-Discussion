# btcli Command Reference & Staking Guide

Quick reference for the **Bittensor CLI** (`btcli`) command tree, common staking workflows, and community DCA tooling.

## Full command tree

```
btcli
├── config
│   ├── set              # Set persistent config values
│   ├── get              # Show current config
│   └── clear            # Reset config to defaults
├── wallet
│   ├── list             # List all local wallets
│   ├── create           # Create a new wallet (coldkey + hotkey)
│   ├── new-coldkey       # Generate a new coldkey only
│   ├── new-hotkey        # Generate a new hotkey only
│   ├── regen-coldkey     # Regenerate coldkey from mnemonic
│   ├── regen-coldkeypub  # Regenerate coldkey public info
│   ├── regen-hotkey      # Regenerate hotkey from mnemonic
│   ├── swap-hotkey       # Swap hotkey associated with a coldkey
│   ├── balance           # Show TAO balance
│   ├── overview          # Wallet overview across subnets
│   ├── transfer          # Transfer TAO between coldkeys
│   ├── faucet            # Testnet faucet (test TAO only)
│   ├── set-identity      # Set on-chain identity metadata
│   ├── get-identity      # Query on-chain identity
│   └── sign              # Sign a message with a key
├── stake
│   ├── add              # Stake TAO to a hotkey (on a subnet)
│   ├── remove           # Unstake TAO from a hotkey
│   ├── list             # List current stakes
│   ├── move             # Move stake between hotkeys
│   ├── transfer         # Transfer staked TAO
│   ├── swap             # Swap stake between subnets
│   └── child
│       ├── get          # View child hotkey delegations
│       ├── set          # Set child hotkey delegation
│       ├── revoke       # Revoke child hotkey
│       └── take         # Set child-key take rate
├── sudo
│   ├── set              # Set subnet hyperparameter (owner only)
│   ├── get              # Query subnet hyperparameter
│   ├── senate           # View senate members
│   ├── proposals        # View governance proposals
│   ├── senate-vote      # Vote on a proposal
│   ├── set-take         # Set validator take percentage
│   └── get-take         # Query validator take
└── subnets
    ├── list             # List all subnets
    ├── show             # Show detail for a specific subnet
    ├── hyperparameters  # Dump all hyperparameters for a subnet
    ├── create           # Register a new subnet (burn cost)
    ├── register         # Register a neuron (UID) on a subnet
    ├── pow-register     # Register via proof-of-work
    ├── burn-cost        # Show current subnet creation burn cost
    └── price            # Show current alpha/TAO price for a subnet
```

---

## Staking operations

### Add stake to a subnet

```bash
btcli stake add \
  --amount <TAO_AMOUNT> \
  --wallet-name <wallet> \
  --wallet-hotkey <hotkey> \
  --netuid <SUBNET_ID>
```

- `--netuid` is optional; omitting it prompts you to choose interactively.
- Staking routes TAO into the subnet's AMM pool, receiving alpha tokens in return.
- Your alpha position earns emissions proportional to your share of the subnet's staked alpha.

### Remove stake

```bash
btcli stake remove \
  --amount <TAO_AMOUNT> \
  --wallet-name <wallet> \
  --wallet-hotkey <hotkey> \
  --netuid <SUBNET_ID>
```

### Move stake between hotkeys

```bash
btcli stake move \
  --wallet-name <wallet> \
  --origin-hotkey <from_hotkey> \
  --dest-hotkey <to_hotkey>
```

### View stakes

```bash
btcli stake list --wallet-name <wallet>
```

### Swap stake across subnets

```bash
btcli stake swap \
  --wallet-name <wallet> \
  --wallet-hotkey <hotkey> \
  --origin-netuid <FROM_SUBNET> \
  --dest-netuid <TO_SUBNET> \
  --amount <TAO_AMOUNT>
```

---

## Child hotkey delegation

Child hotkeys let a parent validator delegate a fraction of their stake weight to another hotkey (useful for multi-machine setups or delegated mining).

```bash
btcli stake child set \
  --wallet-name <wallet> \
  --wallet-hotkey <hotkey> \
  --netuid <SUBNET_ID> \
  --child <CHILD_HOTKEY_SS58> \
  --proportion <0.0-1.0>

btcli stake child get --wallet-name <wallet> --wallet-hotkey <hotkey>
btcli stake child revoke --wallet-name <wallet> --wallet-hotkey <hotkey> --child <CHILD_SS58>
btcli stake child take --wallet-name <wallet> --wallet-hotkey <hotkey> --take <PERCENTAGE>
```

---

## DCA (Dollar-Cost Averaging) into subnets

Manually staking at regular intervals is tedious. Community scripts automate this:

### dtao-dca.py

A Python script that periodically stakes a fixed TAO amount into one or more subnets on a schedule.

- **Repository:** [mcjkula/bittensor-scripts — dtao-dca.py](https://github.com/mcjkula/bittensor-scripts/blob/main/dtao-dca.py)
- Allows setting interval, amount per stake, and target subnet(s)
- Requires a funded wallet with `btcli` configured locally

### DynamicBot

A more full-featured bot for automated staking and rebalancing strategies on dTAO subnets.

- **Repository:** [unconst/DynamicBot](https://github.com/unconst/DynamicBot)
- Built by a core Bittensor contributor (unconst / Const)
- Supports dynamic rebalancing across multiple subnets

> **Warning:** Automated staking bots hold or access wallet keys. Audit the code, use a dedicated wallet with limited funds, and never expose mnemonics.

---

## Useful shortcuts

```bash
btcli wallet balance                       # Quick balance check
btcli subnets list                         # All active subnets
btcli subnets price --netuid <ID>          # Current α price
btcli wallet overview --wallet-name <name> # Stakes + UIDs across subnets
btcli subnets hyperparameters --netuid <ID> # Full hyperparameter dump
```

## References

- [Bittensor docs: staking](https://docs.bittensor.com/staking-and-delegating/)
- [btcli source (opentensor/btcli)](https://github.com/opentensor/btcli)
- [Learn Bittensor](https://learnbittensor.org/)
