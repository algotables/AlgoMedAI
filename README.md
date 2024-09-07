# AlgoMedAI

**AlgoMedAI** is a Python-based proof-of-concept (PoC) project that integrates AI for healthcare data validation with the Algorand blockchain. It demonstrates how validated healthcare data can be securely stored on the blockchain after being processed by a machine learning model.

## Overview

This project validates healthcare data (age, severity of symptoms, and presence of pre-existing conditions) using a logistic regression model. Once the data is validated, it is sent to the Algorand TestNet where the transaction stores the data on-chain.

## Features

1. **AI-Powered Healthcare Data Validation**: 
   - A logistic regression model is used to assess the validity of healthcare data.
   - Data includes the patient's age, symptom severity (on a scale of 1-10), and pre-existing conditions.

2. **Blockchain Storage via Algorand**:
   - If the healthcare data is valid, it is encoded and stored as a transaction note on the Algorand TestNet.

## Example Transaction

You can view a real transaction that was executed as part of this project on the Algorand TestNet Explorer:

[View Transaction on Algorand TestNet](https://testnet.explorer.perawallet.app/tx/IY3TDBN5E5HCASFIJAQCYO2GKEGQLHCJXC7SH3X3UYHVLFLUZOPQ)

- **Transaction ID**: IY3TDBN5E5HCASFIJAQCYO2GKEGQLHCJXC7SH3X3UYHVLFLUZOPQ
- **Blockchain**: Algorand TestNet
- **Data Stored**: Age, symptom severity, and condition status

## Requirements

- Python 3.x
- Algorand SDK (`py-algorand-sdk`)
- Scikit-learn (`scikit-learn`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/algotables/AlgoMedAI.git
2. Navigate to the project directory:
   ```bash
   cd AlgoMedAI
3. Install Requirements
   ```bash
   pip install -r requirements.txt
4. Navigate to the project subdirectory:
   ```bash
   cd ai_blockchain_healthcare

## How to Run
1. Replace the mnemonic and address placeholders in main.py with your own Algorand TestNet account details:
   ```bash
   mnemonic_phrase = "your_mnemonic_here"
   address = "your_address_here"
2. Run the script:
   ```bash
   python3 ai_blockchain_healthcare/main.py
3. Follow the prompts to input patient data and send the validated data to the Algorand blockchain.

## Screenshots
<img src="https://github.com/user-attachments/assets/3f0614fd-bdfe-452f-a0e1-1d5222e7bc43" alt="Transaction Example in CLI"/>
<br>
<br>
<img src="https://github.com/user-attachments/assets/1b752c20-6560-41a1-9925-5900de0779ac" alt="Pera Explorer Showing of Transaction"/>
