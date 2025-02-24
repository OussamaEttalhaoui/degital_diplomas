#interact_with_blockchain.py
from web3 import Web3
import os
from dotenv import load_dotenv

import json

load_dotenv()

# Connexion à la blockchain locale
blockchain_url = os.getenv("BLOCKCHAIN_URL")
web3 = Web3(Web3.HTTPProvider(blockchain_url))
contract_address = os.getenv("CONTRACT_ADDRESS")



# Obtenez le chemin absolu du fichier interact_with_blockchain.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construisez le chemin relatif vers le fichier DiplomaRegistry.json
contract_path = os.path.join(current_dir, '../build/contracts/DiplomaRegistry.json')

# Charger l'ABI à partir du fichier JSON généré par Truffle
with open(contract_path) as f:
    contract_json = json.load(f)
    abi = contract_json['abi']

contract = web3.eth.contract(address=contract_address, abi=abi)


def store_diploma_on_chain(student_data):
    tx = contract.functions.registerDiploma(
        student_data['nom'],
        student_data['prenom'],
        student_data['cne'],
        student_data['cin'],
        student_data['diplome'],
        student_data['specialization'],
        student_data['university'],
        student_data['year'],  # L'année convertie en entier
        student_data['mention']  
    ).transact({'from': web3.eth.accounts[0]})
    receipt = web3.eth.wait_for_transaction_receipt(tx)
    print("Diplôme enregistré sur la blockchain")

    # Retourner l'ID de la transaction (hash de la transaction)
    return receipt['transactionHash'].hex()

