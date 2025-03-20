import os
import json
from security import Security

class Wallet:
    def __init__(self):
        self.security = Security()
        self.balance = 0
        self.address = os.urandom(16).hex()  # Gerando um endereço aleatório

    def sign_transaction(self, transaction):
        """Assina a transação"""
        return self.security.sign_transaction(json.dumps(transaction))

    def __repr__(self):
        return f"Wallet(Address: {self.address}, Balance: {self.balance})"
      
