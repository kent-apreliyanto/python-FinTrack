import os
import tempfile
import unittest
import csv

from unittest.mock import patch
from storage import load_transactions, save_transactions, export_transactions_to_csv

class TestStorageFunctions(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_file = os.path.join(
            self.temp_dir.name,
            "test_transactions.json"
        )
        
        self.patcher = patch("storage.DATA_FILE", self.data_file)
        self.patcher.start()
        
        self.csv_file = os.path.join(self.temp_dir.name, "test_export.csv")
        
        self.csv_patcher = patch("storage.CSV_FILE", self.csv_file)
        self.csv_patcher.start()
        
    def tearDown(self):
        self.csv_patcher.stop()
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
        
    def test_export_transactions_to_csv(self):
        transactions = [
            {
                "id": 1,
                "date": "2026-11-23",
                "type": "expense",
                "amount": 15000,
                "category": "Food",
                "description": "Nasi Goreng"
            }
        ]
        
        result = export_transactions_to_csv(transactions)
        
        self.assertTrue(result)
        
        with open(self.csv_file, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["date"], "2026-11-23")
        self.assertEqual(rows[0]["amount"], "15000")
        
    def test_export_empty_transactions(self):
        result = export_transactions_to_csv([])
        
        self.assertTrue(result)
        
        with open(self.csv_file, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            
        self.assertEqual(len(rows), 0)
        
if __name__ == "__main__":
    unittest.main()
