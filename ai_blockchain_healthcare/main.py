from model import validate_healthcare_data
from algorand_smart_contract import send_healthcare_data_to_blockchain
from algosdk import mnemonic

def main():
    print("Welcome to AlgoMedAI!")

    # Get user input
    age = int(input("Enter patient age: "))
    severity = int(input("Enter symptom severity (1-10): "))
    conditions = int(input("Existing conditions (0 = no, 1 = yes): "))

    # Validate healthcare data using AI
    is_valid = validate_healthcare_data(age, severity, conditions)

    # Placeholder for mnemonic and address (replace with actual values locally)
    mnemonic_phrase = "your_mnemonic_here"
    address = "your_address_here"
    
    # Extract private key from mnemonic
    private_key = mnemonic.to_private_key(mnemonic_phrase)

    if is_valid:
        print("Healthcare data is valid. Sending to the Algorand blockchain...")

        # Send data to the blockchain
        data = f"Age: {age}, Severity: {severity}, Conditions: {conditions}"
        tx_id = send_healthcare_data_to_blockchain(private_key, address, data)

        print(f"Data sent successfully! Transaction ID: {tx_id}")
    else:
        print("Invalid healthcare data. Please recheck the input.")

if __name__ == "__main__":
    main()
