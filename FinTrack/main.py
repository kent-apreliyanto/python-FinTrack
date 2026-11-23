from storage import load_transactions, save_transactions, export_transactions_to_csv
from transactions import (
    get_transaction_type,
    get_positive_amount,
    get_non_empty_text,
    generate_transaction_id,
    find_transaction_by_id,
    create_transaction,
    update_transaction,
    delete_transaction,
    calculate_summary,
    filter_transactions_by_category,
    get_valid_month,
    calculate_monthly_summary
)
from display import format_rupiah, display_summary, display_transactions, display_monthly_summary

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
        print("7. Filter by Category")
        print("8. Monthly Financial Report")
        print("9. Export Transaction to CSV")
        print("10. Exit")
        
        choice = input("choose menu (1-10): ").strip()
        
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
            print("\n--- FILTER BY CATEGORY")  
            
            category = get_non_empty_text("Category: ")
            
            filtered_transactions = filter_transactions_by_category(
                transactions,
                category
            )
            
            display_transactions(filtered_transactions)
          
        elif choice == "8":
            month = get_valid_month()
            
            summary = calculate_monthly_summary(transactions, month)
            
            display_monthly_summary(summary, month)
            
        elif choice == "9":
            export_transactions_to_csv(transactions)
            
        elif choice == "10":
            print("Thank you for using FinTrack")
            break
        
        else:
            print("Invalid menu. Please choose 1-7.")
    
if __name__ == "__main__":
    main()