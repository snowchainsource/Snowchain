"""
Transaction Layer: UTXO Model (inputs & outputs)
"""

TOTAL_SUPPLY = 590_589_899_658_545.2  # Total supply of Snowchain
import hashlib

class TransactionInput:
    def __init__(self, txid, output_index, signature):
        self.txid = txid
        self.output_index = output_index
        self.signature = signature

class TransactionOutput:
    def __init__(self, amount, recipient):
        self.amount = amount
        self.recipient = recipient

class Transaction:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        self.txid = self.calculate_txid()

    def calculate_txid(self):
        input_str = ''.join([f"{inp.txid}{inp.output_index}{inp.signature}" for inp in self.inputs])
        output_str = ''.join([f"{out.amount}{out.recipient}" for out in self.outputs])
        return hashlib.sha256((input_str + output_str).encode()).hexdigest()
