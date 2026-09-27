# Expense Tracker

A command-line Python application for recording and analyzing personal expenses.

## Overview
Expense Tracker helps users record expenses, view saved records, calculate total spending, analyze spending by category, find the highest expense, and compare spending with a monthly budget.

Expense records are stored locally in `expense.txt`, allowing data to remain available after the program is closed.

## Features
- Add expense
- View all expenses
- Calculate total spending
- Category-wise spending analysis
- Find highest expense
- Set monthly budget
- View budget status
- Persistent local file storage
- Input validation and error handling

## Technologies Used
- Python 3
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- File handling
- Exception handling

## Project Structure
```text
Expense Tracker/
├── Expense_Tracker.py
├── expense.txt
├── README.md
├── statement.md
└── Expense_Tracker_Project_Report.pdf
```

## Requirements
- Python 3.x
- No external Python libraries are required.

## How to Run
Open a terminal in the project folder and run:
```bash
python Expense_Tracker.py
```

## Data Storage
Each record in `expense.txt` follows:
```text
Expense Name | Amount | Category
```

## Input Validation
The program handles invalid menu choices, invalid amounts and budgets, zero/negative values, empty names/categories, missing files, and invalid stored amounts.

## Sample Test Data
| Expense | Amount | Category |
|---|---:|---|
| College Canteen | ₹120 | FOOD |
| Bus Pass | ₹200 | TRAVEL |
| Notebook | ₹180 | EDUCATION |
| Movie | ₹250 | ENTERTAINMENT |
| Lunch | ₹150 | FOOD |

Monthly budget: ₹2000  
Expected total: ₹900  
Expected remaining budget: ₹1100

## Limitations
- Command-line interface only.
- Monthly budget is maintained for the current program session.
- Text-file storage is intended for a small project.
- No login or multi-user functionality.

## Future Enhancements
- Date/month field
- Search and filtering
- Monthly reports
- CSV export
- Spending charts
- Database storage
- Persistent monthly budgets

## Author
Student project developed as part of the Python Essentials course project.
