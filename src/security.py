from pqcrypto.sign.falcon import generate_keypair, sign, verify

class Security:
    def __init__(self):
        self.public_key, self.private_key = generate_keypair()

    def sign_transaction(self, message):
        """Assina a transação usando FALCON"""
        return sign(message.encode(), self.private_key)

    def verify_signature(self, message, signature):
        """Verifica a assinatura"""
        return verify(message.encode(), signature, self.public_key)
