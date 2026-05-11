# Running Your Own Subtensor Node

Running a local subtensor node removes reliance on public RPCs, gives full chain-state access, and is required for certain archive queries (e.g. historical price probes beyond public RPC retention).

## Option A — Native binary (archive node via PM2)

An **archive node** retains every historical block state. This is the heaviest option but enables arbitrary historical RPC queries.

### Prerequisites

- Compiled `node-subtensor` binary at `./target/production/node-subtensor` (see [opentensor/subtensor build docs](https://github.com/opentensor/subtensor))
- [PM2](https://pm2.keymetrics.io/) process manager (`npm install -g pm2`)
- Finney chain spec at `./chainspecs/raw_spec_finney.json`
- Sufficient disk (archive nodes grow continuously; plan for multi-TB NVMe)

### Launch command

```bash
pm2 start ./target/production/node-subtensor \
  --restart-delay 60000 \
  --name archive-subtensor \
  -- \
  --chain ./chainspecs/raw_spec_finney.json \
  --base-path /root/archive/finney/ \
  --sync=full \
  --pruning archive \
  --port 30333 \
  --max-runtime-instances 32 \
  --rpc-max-response-size 2048 \
  --rpc-cors all \
  --rpc-port 9944 \
  --bootnodes /dns/bootnode.finney.chain.opentensor.ai/tcp/30333/ws/p2p/12D3KooWRwbMb85RWnT8DSXSYMWQtuDwh4LJzndoRrTDotTR5gDC \
  --no-mdns \
  --in-peers 8000 \
  --out-peers 8000 \
  --prometheus-external \
  --rpc-external
```

### Key flags explained

| Flag | Purpose |
|------|---------|
| `--sync=full` | Download and validate every block from genesis (required for archive) |
| `--pruning archive` | Keep all historical state; never prune |
| `--rpc-port 9944` | WebSocket/HTTP RPC endpoint |
| `--rpc-external` | Bind RPC to `0.0.0.0` (expose to network — firewall accordingly) |
| `--rpc-cors all` | Accept cross-origin requests (needed for browser-based tools) |
| `--rpc-max-response-size 2048` | Allow larger RPC responses (MB); useful for bulk queries |
| `--max-runtime-instances 32` | Parallel Wasm executor instances for RPC throughput |
| `--in-peers 8000` / `--out-peers 8000` | High peer count for fast sync and serving |
| `--prometheus-external` | Expose Prometheus metrics for monitoring |
| `--no-mdns` | Disable local multicast discovery (use bootnodes only) |
| `--restart-delay 60000` | PM2 waits 60 s before restarting on crash |

### Monitoring

```bash
pm2 logs archive-subtensor --lines 50
pm2 monit
```

---

## Option B — Docker lite node (warp sync)

A **lite node** warp-syncs to chain head quickly and keeps only recent state. Suitable for RPC forwarding, validator operations, and tools that don't need deep history.

### Full setup script

This single script tears down any previous subtensor containers/images, clones the official repo, patches the compose file for higher RPC connection limits, starts the node, and sets the restart policy.

```bash
#!/usr/bin/env bash
set -euo pipefail

# --- Cleanup old subtensor containers ---
for d in $(docker container ls -a | grep -i subtensor | cut -d ' ' -f1); do
  echo "[ cleaning up container: $d ]"
  docker container rm "$d" -f
  echo
done

for i in $(docker images | grep -i 'subtensor' | cut -d ' ' -f1); do
  echo "[ cleaning up image: $i ]"
  docker rmi "$i"
  echo
done

# --- Clone fresh repo ---
echo "[ cleaning up repository... ]"
cd ~/apps
rm -rf ~/apps/subtensor

echo "[ cloning repository... ]"
git clone https://github.com/opentensor/subtensor.git
cd subtensor

# --- Patch: raise RPC connection limit ---
sed -i 's/--sync warp/--sync warp --rpc-max-connections 2000/g' ./docker-compose.yml

# --- Start lite node on mainnet ---
echo "[ setting up a lite node on the mainnet... ]"
./scripts/run/subtensor.sh -e docker --network mainnet --node-type lite

# --- Set restart=always so it survives reboots ---
for d in $(docker ps -a | grep -i 'subtensor' | cut -d ' ' -f1); do
  echo "[ updating container $d restart=always ]"
  docker update --restart=always "$d"
  echo
done

echo "[ DONE ]"
```

### Prerequisites

- Docker and Docker Compose installed
- `~/apps` directory (or adjust paths)
- Adequate disk for warp-synced state (~100–200 GB as of mid-2026, grows over time)

### Verifying

After the node syncs, test the local RPC:

```bash
curl -s -H "Content-Type: application/json" \
  -d '{"id":1,"jsonrpc":"2.0","method":"system_health","params":[]}' \
  http://127.0.0.1:9944 | python3 -m json.tool
```

---

## Pointing btcli / bittensor SDK at your local node

Once either node is synced and serving on `:9944`:

```bash
btcli wallet balance --subtensor.chain_endpoint ws://127.0.0.1:9944
```

Or in Python:

```python
from bittensor import Subtensor
st = Subtensor(network="ws://127.0.0.1:9944")
print(st.get_current_block())
```

---

## References

- [opentensor/subtensor](https://github.com/opentensor/subtensor) — node source and official Docker scripts
- [Bittensor docs: running a subtensor node](https://docs.bittensor.com/subtensor-nodes/)
- [PM2 docs](https://pm2.keymetrics.io/docs/usage/quick-start/)
