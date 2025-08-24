# Expense-tracker
A simple Python-based CLI Expense Tracker that stores expenses in CSV. Features: add, view, filter, monthly total, and category-based search.
## ✨ Features
- Add new expense with amount, category, date, and optional note  
- Show all recorded expenses  
- Calculate total spending (all-time)  
- View monthly spending for a given year and month  
- Search expenses by category  
- Input validation for clean and correct data  
- Data stored automatically in `file.csv`
### Run the program  
git clone https://github.com/Shrey-ja/expense-tracker.git
cd expense-tracker
### Run the main program:
python project.py
### Categories
1 → Food
2 → Travel
3 → Studies
4 → Medical
5 → Personal
6 → Others
## Project Structure
Expense-Tracker/
│── LICENSE        # License file
│── README.md      # Documentation
│── Tracker.py     # ExpenseTracker class (handles file operations & calculations)
│── file.csv       # Stores expenses (auto-created if missing)
│── project.py     # Main program (menu, input handling)
