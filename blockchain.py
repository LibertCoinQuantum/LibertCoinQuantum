from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Cria o bloco inicial da blockchain."""
        genesis_block = Block(0, "0", [], 0)
        self.chain.append(genesis_block)

    def add_block(self, transactions, nonce):
        """Adiciona um novo bloco à cadeia."""
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, transactions, nonce)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Verifica a integridade da blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Testando a blockchain
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block(["Fagner enviou 10 LQC para João"], 100)
    blockchain.add_block(["Maria enviou 5 LQC para Ana"], 200)

    for block in blockchain.chain:
        print(block)
