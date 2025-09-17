# Snowchain

Snowchain is a layered blockchain implementation in Python, inspired by Bitcoin's architecture. It features:

- Peer-to-peer network for decentralization
- Proof-of-Work consensus (Nakamoto)
- Immutable blockchain data structure (linked list of hashes)
- UTXO transaction model
- Block structure with header and body

## Project Structure
- `network/` — Peer-to-peer node logic
- `consensus/` — Proof-of-Work implementation
- `data/` — Blockchain and block data structures
- `transaction/` — UTXO model and transaction logic
- `main.py` — Entry point for running a node

## Getting Started
1. Clone or download the repository.
2. Install Python 3.8+.
3. Run `main.py` to start a node.

## Documentation
See `.github/copilot-instructions.md` for workspace-specific instructions.