"""
Consensus Layer: Proof-of-Work (Nakamoto Consensus)
"""
import hashlib

def proof_of_work(block, difficulty):
    prefix = '0' * difficulty
    nonce = 0
    while True:
        block.nonce = nonce
        hash_result = block.calculate_hash()
        if hash_result.startswith(prefix):
            return nonce, hash_result
        nonce += 1
