"""
Data Layer: Blockchain as a linked list of hashes
"""
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), [], 0)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions, nonce):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=previous_block.index + 1,
            previous_hash=previous_block.hash,
            timestamp=time.time(),
            transactions=transactions,
            nonce=nonce
        )
        self.chain.append(new_block)
