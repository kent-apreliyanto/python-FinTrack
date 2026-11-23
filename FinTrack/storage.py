import json

DATA_FILE = "transaction.json"

def validate_transactions(transactions):
    if not isinstance(transactions, list):
        return False
    
    required_keys = {"id","type","amount","category","description"}
    
    for transaction in transactions:
        if not isinstance(transaction, dict):
            return False
        if not required_keys.issubset(transaction):
            return False
        if type(transaction["id"]) is not int or transaction["id"] <= 0:
            return False
        if transaction["type"] not in ("income", "expense"):
            return False
        if type(transaction["amount"]) is not int or transaction["amount"] <= 0:
            return False
        if not isinstance(transaction["category"], str):
            return False
        if not transaction["category"].strip():
            return False
        if not isinstance(transaction["description"], str):
            return False
        if not transaction["description"].strip():
            return False
        
    return True

def load_transactions():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            transactions = json.load(file)
            
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
        return None
    
    if not validate_transactions(transactions):
        print("Error: Invalid transaction data.")
        return None
    
    return transactions

def save_transactions(transactions):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(transactions, file, indent=4, ensure_ascii=False)
        print("Transaction data saved successfully.")
        
    except OSError as error:
        print(f"Error saving transaction data: {error}")