# dTAO: Alpha Token Price and Further Reading

**Summary:** On dynamic-TAO subnets, the instantaneous **price** of a subnet alpha token versus TAO reserves in the pool is tied to reserves. Practical concepts and official/community links below.

## Price / rate of alpha tokens

### Ideal (spot) price

For each subnet, **price** is a function of TAO in reserve **τ<sub>in</sub>** over alpha in reserve **α<sub>in</sub>**:

**Price = τ<sub>in</sub> / α<sub>in</sub>**

Interpret this as **TAO per unit of alpha** implied by pool reserves before fees and slip.

### Example

If for subnet ε the subnet pool has **τ<sub>in</sub> = 1000** TAO and **α<sub>in</sub> = 16 000** alpha units:

**R = τ<sub>in</sub> / α<sub>in</sub> = 1000 / 16 000 = 0.0625**

So **1 ε = 0.0625 TAO** at that snapshot (conceptually analogous to saying one alpha buys 0.0625 TAO at the marginal pool rate described by the reserves).

This exchange rate **can change every block** when staking, unstaking, or emissions alter reserves on that subnet.

## Getting started (wallets & testnet)

- [Bittensor docs: wallets and basic setup](https://docs.bittensor.com/getting-started/wallets)
- The rest of the official docs covers other core concepts worth skimming once you’re past wallets.
- For experimentation, prefer **testnet** (e.g. `--subtensor.network test`, `--netuid 168`) over mainnet so you are not risking real TAO while learning.

## Concept overviews & data

### dTAO

- [Dynamic TAO (dTAO)](https://learnbittensor.org/explore/concept/dynamic-tao)

### Subnet emissions

- [Subnet emissions (Learn Bittensor)](https://learnbittensor.org/explore/concept/emissions)
- [Subnets primer (TAOStats docs)](https://docs.taostats.io/docs/subnets-1)

### Root proportion & pool mechanics

- [Root proportion](https://learnbittensor.org/explore/concept/root-proportion)
- [Subnet pool](https://learnbittensor.org/explore/concept/subnet-pool)

## Commentary & tools (third party)

Community strategy threads (not protocol specs—verify independently):

- [dTAO-related thread (@badenglishtea)](https://x.com/badenglishtea/status/1889719115620966712)
- [Related thread (@Old_Samster)](https://x.com/Old_Samster/status/1890071216645603802)

Dashboard / ancillary tool:

- [taopill.ai](https://taopill.ai)

*(Obsidian vault reference: diagram `![[Pasted image 20250404032216.png]]` — add under `assets/` and link here if you want the image version-controlled in this repo.)*

## Sources / further reading

Primary protocol behavior should always be validated against **current** [Bittensor documentation](https://docs.bittensor.com), chain state, and your client version; formulas above describe the conceptual reserve ratio framing from community/docs material summarized here.
