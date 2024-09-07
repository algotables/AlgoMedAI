from algosdk.v2client import algod
from algosdk.future import transaction as future_transaction

# Use Nodely TestNet endpoint (no token required)
ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""  # No token required

# Initialize the algod client
algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

def send_healthcare_data_to_blockchain(sender_private_key, sender_address, data):
    """Send healthcare data to the Algorand blockchain."""
    params = algod_client.suggested_params()

    # Create a transaction with the required parameters
    txn = future_transaction.PaymentTxn(
        sender=sender_address,  # Sender's address
        sp=params,              # Suggested params from the network (includes gh)
        receiver=sender_address, # Send to self for PoC
        amt=1000,               # Sending 1000 microAlgos (0.001 ALGO)
        note=data.encode()       # Encode healthcare data as a note
    )
    
    # Sign the transaction
    signed_txn = txn.sign(sender_private_key)
    
    # Send the transaction
    txid = algod_client.send_transaction(signed_txn)
    
    # Wait for the transaction confirmation
    return f"Transaction ID: {txid}"
