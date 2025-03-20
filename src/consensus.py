import randomx
import os

class Miner:
    def __init__(self):
        self.vm = randomx.RandomXVM()

    def mine_block(self, data):
        """Simula mineração RandomX"""
        nonce = 0
        while True:
            hash_result = self.vm.calculate_hash(f"{data}-{nonce}")
            if hash_result.startswith("0000"):  # Dificuldade ajustável
                return nonce, hash_result
            nonce += 1
          
