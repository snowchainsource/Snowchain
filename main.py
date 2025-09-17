"""
Entry point for Snowchain node
"""
from network.node import Node
from data.blockchain import Blockchain
from consensus.pow import proof_of_work
from transaction.utxo import Transaction, TransactionInput, TransactionOutput
from transaction.utxo import TOTAL_SUPPLY

if __name__ == "__main__":
    # Start network node
    node = Node()
    # Initialize blockchain
    blockchain = Blockchain()
    # Example: Add a block with dummy transaction
    tx_in = TransactionInput(txid="0", output_index=0, signature="sig")
    tx_out = TransactionOutput(amount=10, recipient="user1")
    tx = Transaction(inputs=[tx_in], outputs=[tx_out])
    difficulty = 2
    nonce, block_hash = proof_of_work(blockchain.get_latest_block(), difficulty)
    blockchain.add_block([tx], nonce)
    print(f"Block added with hash: {block_hash}")
    print(f"Blockchain length: {len(blockchain.chain)}")
    print(f"Total supply: {TOTAL_SUPPLY}")
