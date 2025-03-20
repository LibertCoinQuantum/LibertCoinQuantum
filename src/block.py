import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calcula o hash do bloco."""
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "nonce": self.nonce
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def __repr__(self):
        return f"Block({self.index}, {self.hash})"
      
