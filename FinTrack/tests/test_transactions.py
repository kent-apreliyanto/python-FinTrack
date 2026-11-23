import unittest

from transactions import (
    generate_transaction_id,
    find_transaction_by_id,
    calculate_summary
)

class testTransactionFunctions(unittest.TestCase):
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
        
if __name__ == "__main__":
    unittest.main()