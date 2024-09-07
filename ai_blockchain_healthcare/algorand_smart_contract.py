from algosdk.v2client import algod
from algosdk.transaction import PaymentTxn

# Use Nodely TestNet endpoint (no token required)
ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""  # No token required

# Initialize the algod client
algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

def send_healthcare_data_to_blockchain(sender_private_key, sender_address, data):
    """Send healthcare data to the Algorand blockchain."""
    params = algod_client.suggested_params()

    # Create a transaction with the required parameters
    txn = PaymentTxn(
        sender=sender_address,
        sp=params,
        receiver=sender_address,
        amt=1000,
        note=data.encode()
    )
    
    # Sign the transaction
    signed_txn = txn.sign(sender_private_key)
    
    # Send the transaction
    txid = algod_client.send_transaction(signed_txn)
    
    # Wait for the transaction confirmation
    return f"Transaction ID: {txid}"
