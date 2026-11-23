def get_transaction_type():
    while True:
        transaction_type = input("Transaction Type (income/expense): ").strip().lower()
        if transaction_type == "income" or transaction_type == "expense":
            return transaction_type
        print("Invalid type. Enter income or expense.")

def get_positive_amount(prompt="Amount: "):
    while True:
        amount_text = input(prompt).strip()
        try:
            amount = int(amount_text)
        except ValueError:
            print("Amount must be a whole number")
            continue
        
        if amount > 0:
            return amount
        
        print("Amount must be greater than zero")

def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        
        if value != "":
            return value
        
        print("Input cannot be empty")
        
def generate_transaction_id(transactions):
    if len(transactions) == 0:
        return 1
    
    last_id = max(transaction["id"] for transaction in transactions)
    
    return last_id + 1

def find_transaction_by_id(transactions, transaction_id):
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return transaction
        
    return None

def create_transaction(transactions):
    print("\n--- ADD NEW TRANSACTION ---")
    
    transaction_id = generate_transaction_id(transactions)
    transaction_type = get_transaction_type()
    amount = get_positive_amount()
    category = get_non_empty_text("Category: ")
    description = get_non_empty_text("Description: ")
    
    transaction = {
        "id": transaction_id,
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description
    }
    
    return transaction
    
def update_transaction(transactions):
    print("\n--- UPDATE TRANSACTION ---")
    
    transaction_id = get_positive_amount("Transaction ID: ")
    transaction = find_transaction_by_id(transactions, transaction_id)
    
    if transaction is None:
        print("Tranaction not found.")
        return
    
    print("Leave input empty to keep the current value.")
    
    new_amount = input(f"Amount [{transaction['amount']}]:").strip()
    if new_amount != "":
        try: 
            amount = int(new_amount)
        
            if amount > 0:
                transaction["amount"] = amount
            else:
                print("Amount must be greater than zero.")
            
        except ValueError:
            print("Invalid amount. Old value retained")
            
    new_category = input(f"Category [{transaction['category']}]:").strip()
    if new_category != "":
        transaction["category"] = new_category
        
    new_description = input(f"Description [{transaction['description']}]:").strip()
    if new_description != "":
        transaction["description"] = new_description
        
    print("Transaction update process completed.")
    
def delete_transaction(transactions):
    print("\n--- DELETE TRANSACTION ---")

    transaction_id = get_positive_amount("Transaction ID: ")

    transaction = find_transaction_by_id(
        transactions, transaction_id
    )

    if transaction is None:
        print("Transaction not found.")
        return

    print(f"Transaction: {transaction['description']}")

    confirmation = input(
        "Delete this transaction? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        transactions.remove(transaction)
        print("Transaction successfully deleted.")
    else:
        print("Deletion cancelled.")


def calculate_summary(transactions):
    total_income = 0
    total_expense = 0

    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]

        elif transaction["type"] == "expense":
            total_expense += transaction["amount"]

    balance = total_income - total_expense

    summary = {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }

    return summary
