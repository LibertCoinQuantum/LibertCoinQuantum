from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine():
    data = request.json
    transactions = data.get('transactions', [])
    nonce = data.get('nonce', 0)

    blockchain.add_block(transactions, nonce)
    return jsonify({"message": "Bloco minerado!", "block": blockchain.chain[-1].__dict__}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify([block.__dict__ for block in blockchain.chain]), 200

if __name__ == "__main__":
    app.run(port=5000)
