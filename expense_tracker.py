import pandas as pd
import os

EXPENSE_FILE = "expenses.csv"

# Function to add an expense
def add_expense(category, amount, description):
    data = {"Category": category, "Amount": amount, "Description": description}
    df = pd.DataFrame([data])
    
    if os.path.exists(EXPENSE_FILE):
        df.to_csv(EXPENSE_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(EXPENSE_FILE, index=False)
    
    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    if os.path.exists(EXPENSE_FILE):
        df = pd.read_csv(EXPENSE_FILE)
        print(df.to_markdown())
    else:
        print("No expenses recorded yet.")

# Main Menu
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        add_expense(category, amount, description)
    
    elif choice == "2":
        view_expenses()
    
    elif choice == "3":
        break

    else:
        print("Invalid choice. Try again.")
