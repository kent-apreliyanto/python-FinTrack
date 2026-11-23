import unittest
from datetime import date
from unittest.mock import patch

from transactions import (
    generate_transaction_id,
    find_transaction_by_id,
    calculate_summary,
    create_transaction,
    filter_transactions_by_category,
    calculate_monthly_summary,
    get_valid_month
)

class TestTransactionFunctions(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            {
                "id": 1,
                "type": "income",
                "amount": 10000,
                "category": "Food",
                "description": "Lunch"
            },
            {
                "id": 2,
                "type": "expense",
                "amount": 20000,
                "category": "Drink",
                "description": "Coffee"
            },
            {
                "id": 3,
                "type": "income",
                "amount": 25000,
                "category": "Drink",
                "description": "Tea"
            },
            {
                "id": 4,
                "type": "expense",
                "amount": 20000,
                "category": "Food",
                "description": "Dessert"
            }
        ]
    @patch("builtins.input", side_effect=["2026-11"])    
    def test_get_valid_month(self, mock_input):
        result = get_valid_month()
        
        self.assertEqual(result, "2026-11")
        
    @patch("builtins.input", side_effect=[
        "2026-13",
        "November",
        "2026-11"
    ])
    def test_get_valid_month_invalid_input(self, mock_input):
        result = get_valid_month()
        
        self.assertEqual(result, "2026-11")
        self.assertEqual(mock_input.call_count, 3)
        
    @patch("builtins.input", side_effect=[
        "expense",
        "15000",
        "Food",
        "Nasi Goreng"
        ])
    def test_create_transaction_includes_date(self, mock_input):
        result = create_transaction(self.transactions)
        
        self.assertEqual(
            result["date"],
            date.today().isoformat()
        )
        
    def test_generate_transaction_id(self):
        result = generate_transaction_id(self.transactions)
        self.assertEqual(result, 5)
        
    def test_generate_transaction_id_empty(self):
        result = generate_transaction_id([])
        self.assertEqual(result, 1)
        
    def test_find_transaction_by_id(self):
        result = find_transaction_by_id(self.transactions, 2)
        self.assertEqual(result, self.transactions[1])
        
    def test_find_transaction_not_found(self):
        result = find_transaction_by_id(self.transactions, 99)
        self.assertIsNone(result)
        
    def test_calculate_summary(self):
        result = calculate_summary(self.transactions)
        
        self.assertEqual(result["total_income"], 35000)
        self.assertEqual(result["total_expense"], 40000)
        self.assertEqual(result["balance"], -5000)
        
    def test_calculate_summary_empty(self):
        result = calculate_summary([])
        
        self.assertEqual(result["total_income"], 0)
        self.assertEqual(result["total_expense"], 0)
        self.assertEqual(result["balance"], 0)
        
    def test_generate_transaction_id_unsorted(self):
        transactions = [
            {"id": 4},
            {"id": 1},
            {"id": 7}
        ]
        
        result = generate_transaction_id(transactions)
        self.assertEqual(result, 8)
        
    def test_filter_transactions_by_category(self):
        result = filter_transactions_by_category(self.transactions, "FOOD")
        
        self.assertEqual(len(result), 2)
        
    def test_filter_transactions_category_not_found(self):
        result = filter_transactions_by_category(self.transactions, "Electronics")
        
        self.assertEqual(result, [])
     
    def test_calculate_monthly_summary_empty(self):
        result = calculate_monthly_summary([], "2026-11")

        self.assertEqual(result["total_income"], 0)
        self.assertEqual(result["total_expense"], 0)
        self.assertEqual(result["balance"], 0)
        self.assertEqual(result["transaction_count"], 0)
       
    def test_calculate_monthly_summary(self):
        transactions = [
            {
                "id": 1,
                "date": "2026-11-05",
                "type": "income",
                "amount": 100000
            },
            {
                "id": 2,
                "date": "2026-11-12",
                "type": "expense",
                "amount": 25000
            },
            {
                "id": 3,
                "date": "2026-10-30",
                "type": "income",
                "amount": 50000
            },
            {
                "id": 4,
                "type": "expense",
                "amount": 10000
            }
        ]

        result = calculate_monthly_summary(
            transactions,
            "2026-11"
        )

        self.assertEqual(result["total_income"], 100000)
        self.assertEqual(result["total_expense"], 25000)
        self.assertEqual(result["balance"], 75000)
        self.assertEqual(result["transaction_count"], 2)
           
if __name__ == "__main__":
    unittest.main()