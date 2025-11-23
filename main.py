# main.py - The entry point for PocketSaver
# I am connecting the ledger and budget modules here

import ledger
import budget

def print_menu():
    print("\n--- Student Pocket Money Tracker ---")
    print("1. Add New Expense")
    print("2. Check Total Spending")
    print("3. Save & Exit")

def main():
    # 1. Load data from the file as soon as app starts
    my_expenses = ledger.history()
    print(f"Welcome back! Loaded {len(my_expenses)} past expenses.")

    while True:
        print_menu()
        choice = input("Select an option (1-3): ")

        if choice == "1":
            # Taking input
            # We need try/except here in case user types text instead of a number
            try:
                amt_input = int(input("Enter amount spent: "))
                cat_input = input("Enter category (e.g., Food, Travel): ")

                # 2. Use budget.py to package this data
                new_item = budget.entry(amt_input, cat_input)
                
                my_expenses.append(new_item)
                print("Expense recorded.")
            except ValueError:
                print("Error: Please enter a valid number for the amount.")

        elif choice == "2":
            print("\n--- Spending Summary ---")
            
            # 3. Use budget.py to do the math
            total_spent = budget.total_spending(my_expenses)
            status_msg = budget.check_status(total_spent)
            
            print(f"Total Spent So Far: Rs. {total_spent}")
            print(status_msg)
            
            # Optional: Print the list if you want
            print("\nRecent Transactions:")
            for x in my_expenses:
                print(f" - Rs.{x['amt']} on {x['cat']}")

        elif choice == "3":
            # 4. Use ledger.py to save
            ledger.expense(my_expenses)
            print("Data saved successfully. Exiting...")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
