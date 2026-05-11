# Emission Mechanics & Subnet AMM Pool Dynamics

How TAO emissions are allocated across subnets, and the two key factors that drive emission changes under dTAO.

## Background: the subnet AMM pool

Each subnet operates an on-chain **Automated Market Maker (AMM) pool** that pairs **TAO** with the subnet's **alpha token**. The pool follows a constant-product invariant (similar to Uniswap's `x * y = k`):

```
k = tao_in * alpha_in
```

- **`tao_in`** — TAO reserves in the pool
- **`alpha_in`** — Alpha token reserves in the pool
- **`k`** — Liquidity constant (increases when liquidity is added, never decreases from swaps alone)

The **spot price** of one alpha token in TAO terms:

```
price = tao_in / alpha_in
```

This price shifts with every staking, unstaking, or emission event that changes either reserve.

## Two main factors driving emission changes

### 1. How much TAO flows into the subnet AMM pool

TAO enters a subnet pool through:

- **Direct staking** — users call `btcli stake add --netuid <ID>`, which deposits TAO into the pool and receives alpha tokens back.
- **Protocol emission routing** — each epoch, the root network allocates a share of newly minted TAO across subnets. The allocation weights are set by root validators. TAO routed to a subnet enters its AMM pool, increasing `tao_in`.
- **Stake transfers / swaps** — `btcli stake swap` moves TAO out of one subnet pool and into another.

**More TAO flowing in** means:
- `tao_in` rises, pushing `price` up (alpha becomes more expensive in TAO terms)
- Higher `tao_in` signals stronger market demand/confidence in the subnet
- Root validators observing higher `tao_in` relative to other subnets may increase that subnet's weight, compounding the effect

**Less TAO flowing in** (or TAO flowing out via unstaking) means:
- `tao_in` drops, pushing `price` down
- The subnet's share of total emission allocation may shrink if root validators reduce its weight

### 2. How fast subnet miners swap their TAO for alpha tokens

Miners and validators on a subnet receive emissions denominated in **alpha tokens**. To realize profit in TAO, they must swap alpha back to TAO through the pool. This is the sell-side pressure:

- **Fast selling** — miners immediately swap alpha for TAO after each epoch. This floods `alpha_in` back into the pool while draining `tao_in`, pushing the price **down**. If sell pressure exceeds new TAO inflows, the subnet's alpha depreciates and the emission allocation may shrink.
- **Slow selling (holding alpha)** — miners hold their alpha tokens (or re-stake them). Less alpha re-enters the pool, so `alpha_in` stays lower and `tao_in` stays higher, keeping the price **up**. This signals confidence and can attract further staking.

### The feedback loop

These two factors create a **reflexive cycle**:

```
More TAO staked → higher alpha price → more emission share → attracts more stakers
       ↑                                                            |
       └────────────────────────────────────────────────────────────┘

Miners dump alpha → lower alpha price → less emission share → stakers leave
       ↑                                                            |
       └────────────────────────────────────────────────────────────┘
```

Subnets with genuine utility tend to retain miners who hold alpha (because they need it to operate), creating a healthier equilibrium. Subnets with pure mercenary mining see faster alpha dumps and emission decay.

## Emission allocation walkthrough

1. **Global emission** — The Bittensor protocol mints a fixed amount of TAO per block (halving schedule applies).
2. **Root weight voting** — Root validators (NetUID 0) set weights across all subnets. These weights determine what fraction of the global emission each subnet receives.
3. **Per-subnet distribution** — Within a subnet, the allocated TAO is split between:
   - **TAO routed into the pool** (`tao_in_emission`) — increases pool reserves
   - **Alpha minted to miners/validators** (`alpha_out_emission`) — distributed based on Yuma consensus scores
   - **Alpha into pool** (`alpha_in_emission`) — protocol-level pool liquidity contribution
4. **Net effect** — The balance between these three emission streams, plus user staking/unstaking and miner selling, determines the subnet's evolving price trajectory.

## Practical implications for stakers

| Strategy | When it works | Risk |
|----------|--------------|------|
| Stake early in a promising subnet | Pool is small; your TAO buys a large alpha share | Subnet may fail or lose root weight |
| DCA into established subnets | Smooths entry across price fluctuations | May miss early alpha appreciation |
| Hold alpha (no sell) | Maintains price support; benefits from compounding emissions | Opportunity cost if alpha depreciates anyway |
| Sell alpha regularly | Locks in TAO profit | Depresses price; reduces your emission share |

## Related discussions

- [dTAO Alpha Price and Resources](dtao-alpha-price-and-resources.md) — spot price formula, wallet setup, community links
- [btcli Reference & Staking Guide](btcli-reference.md) — command tree, staking commands, DCA bots
- [Subtensor Node Setup](subtensor-node-setup.md) — run your own RPC for reliable chain queries

## References

- [Dynamic TAO (dTAO)](https://learnbittensor.org/explore/concept/dynamic-tao)
- [Subnet emissions](https://learnbittensor.org/explore/concept/emissions)
- [Subnet pool mechanics](https://learnbittensor.org/explore/concept/subnet-pool)
- [Root proportion](https://learnbittensor.org/explore/concept/root-proportion)
- [unconst/DynamicBot](https://github.com/unconst/DynamicBot) — automated rebalancing strategies
- [mcjkula/bittensor-scripts](https://github.com/mcjkula/bittensor-scripts/blob/main/dtao-dca.py) — DCA staking script
