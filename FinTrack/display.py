
def format_rupiah(amount):
    return f"Rp{amount:,}".replace(",", ".")


def display_transactions(transactions):
    print("\n===== TRANSACTION HISTORY =====")

    if len(transactions) == 0:
        print("No transaction recorded.")
        return

    for transaction in transactions:
        print(f"\nID          : {transaction['id']}")
        print(f"Date        : {transaction.get('date', '-')}")
        print(f"Type        : {transaction['type'].upper()}")
        print(f"Amount      : {format_rupiah(transaction['amount'])}")
        print(f"Category    : {transaction['category']}")
        print(f"Description : {transaction['description']}")
        print("-" * 35)


def display_summary(summary):
    print("\n===== FINANCIAL SUMMARY =====")
    print(f"Total Income  : {format_rupiah(summary['total_income'])}")
    print(f"Total Expense : {format_rupiah(summary['total_expense'])}")
    print(f"Balance       : {format_rupiah(summary['balance'])}")

def display_monthly_summary(summary, month):
    print(f"\n===== MONTHLY FINANCIAL REPORT: {month} =====")
    
    print(f"Transactions    : {summary['transaction_count']}")
    print(f"Total Income    : {format_rupiah(summary['total_income'])}")
    print(f"Total Expense   : {format_rupiah(summary['total_expense'])}")
    print(f"Balance         : {format_rupiah(summary['balance'])}")
    
    if summary["transaction_count"] == 0:
        print("No transactions found for this month.")
    
    