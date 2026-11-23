from storage import load_transactions, save_transactions
from transactions import (
    get_transaction_type,
    get_positive_amount,
    get_non_empty_text,
    generate_transaction_id,
    find_transaction_by_id,
    create_transaction,
    update_transaction,
    delete_transaction,
    calculate_summary
)
from display import format_rupiah, display_summary, display_transactions

def main():
    transactions = load_transactions()
    
    if transactions is None:
        print("FinTrack cannot start because data is invalid.")
        return

    print(f"{len(transactions)} transaction(s) loaded.")
    
    while True:
        print("\n===== FINTRACK =====")
        print("1. Add Transaction")
        print("2. View Transaction")
        print("3. Financial Summary")
        print("4. Search Transaction")
        print("5. Update Transaction")
        print("6. Delete Transaction")
        print("7. Exit")
        
        choice = input("choose menu (1-7): ").strip()
        
        if choice == "1":
            transaction = create_transaction(transactions)
            transactions.append(transaction)
            
            save_transactions(transactions)
            
            print("\nTransaction successfully added.")
        elif choice == "2":
            display_transactions(transactions)
        elif choice == "3":
            summary = calculate_summary(transactions)
            display_summary(summary)
        elif choice == "4":
            transaction_id = get_positive_amount("Transaction ID:")
            transaction = find_transaction_by_id(transactions, transaction_id)
            
            if transaction is None:
                print("Transaction not found.")
            else:
                display_transactions([transaction]) 
                
        elif choice == "5":
            update_transaction(transactions)
            save_transactions(transactions)
            
        elif choice == "6":
            delete_transaction(transactions)
            save_transactions(transactions)
            
        elif choice == "7":
            print("Thank you for using FinTrack")
            break
        
        else:
            print("Invalid menu. Please choose 1-7.")
    
if __name__ == "__main__":
    main()