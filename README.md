# FinTrack – Personal Finance Tracker

FinTrack is a simple command-line personal finance application built with Python. It helps users record and manage their income and expenses, view transaction history, and calculate their financial balance.

This project was created as a Python learning portfolio project, focusing on functions, modular programming, JSON file handling, and unit testing.

## Features

- **Add Transactions** – Record income and expenses.
- **View Transactions** – Display transaction history.
- **Search Transactions** – Find transactions using their ID.
- **Update Transactions** – Edit transaction details.
- **Delete Transactions** – Remove transactions with confirmation.
- **Financial Summary** – Calculate total income, total expenses, and balance.
- **Data Persistence** – Save and load transaction data using JSON.
- **Input Validation** – Validate transaction types, amounts, and text inputs.
- Automatic Transaction Date
- Filter Transactions by Category
- Monthly Financial Reports
- Export Transactions to CSV
- Automated Unit Testing with unittest

## Technologies

- Python 3
- JSON
- unittest

No third-party Python packages are required.

## Project Structure

```text
.
├── FinTrack/
│   ├── tests/
│   │   ├── test_transactions.py
│   │   └── test_storage.py
│   ├── main.py
│   ├── transactions.py
│   ├── storage.py
│   └── display.py
├── .gitignore
└── README.md
```

### Module Description

| File | Description |
|---|---|
| `main.py` | Main application flow and menu |
| `transactions.py` | Transaction logic and input validation |
| `storage.py` | Loading, saving, and validating JSON data |
| `display.py` | Formatting and displaying transaction information |
| `tests/` | Automated unit tests |
| `transactions.json` | Local transaction data |

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kent-apreliyanto/python-FinTrack.git
```

### 2. Navigate to the Project Folder

```bash
cd python-FinTrack/FinTrack
```

### 3. Run the Application

```bash
python main.py
```

The application starts with an empty transaction list if no `transactions.json` file exists. Transaction data is saved locally when changes are saved through the application.

## Running Tests

To run all automated tests, execute:

```bash
python -m unittest discover -s tests -v
```

The tests cover transaction functions and JSON storage operations.

## Data and Privacy

Transaction data is stored locally in `transactions.json`.

This file is excluded from Git tracking through `.gitignore` to help prevent personal financial data from being uploaded to a public repository.

## Learning Objectives

This project demonstrates practical use of:

- Python functions and modules
- Lists and dictionaries
- CRUD operations
- Exception handling
- JSON file operations
- Input validation
- Unit testing with `unittest`

## Future Improvements

- Add transaction filtering by category.
- Add transaction history by date.
- Add monthly financial reports.
- Improve input validation and error handling.
- Add a graphical user interface.

## Author

Created as a personal Python portfolio project.