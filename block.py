"""
Block Layer: Header & Body
"""
class BlockHeader:
    def __init__(self, previous_hash, merkle_root, timestamp, nonce):
        self.previous_hash = previous_hash
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.nonce = nonce

class BlockBody:
    def __init__(self, transactions):
        self.transactions = transactions
