import os
import tempfile
import unittest

from unittest.mock import patch
from storage import load_transactions, save_transactions

class TestStorageFunctions(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = os.path.join(
            self.temp_dir.name,
            "test_transactions.json"
        )
        
        self.patcher = patch("storage.DATA_FILE", self.data_file)
        self.patcher.start()
        
    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()
        
    def test_save_and_load_transaction(self):
        transactions = [
            {
                "id": 1,
                "type": "income",
                "amount": 10000,
                "category": "Food",
                "description": "Lunch"
            }
        ]
        
        save_transactions(transactions)
        
        result = load_transactions()
        
        self.assertEqual(result, transactions)
        
    def test_load_transactions_file_not_found(self):
        result = load_transactions()
        
        self.assertEqual(result, [])
        
    def test_load_invalid_json(self):
        with open(self.data_file, "w", encoding="utf-8") as file:
            file.write("{ invalid json }")
            
        result = load_transactions()
        
        self.assertIsNone(result)
        
if __name__ == "__main__":
    unittest.main()
