

import ledger
import budget

def print_menu():
    print("\n--- Student Pocket Money Tracker ---")
    print("1. Add New Expense")
    print("2. Check Total Spending")
    print("3. Save & Exit")

def main():
    
    my_expenses = ledger.history()
    print(f"Welcome back! Loaded {len(my_expenses)} past expenses.")

    while True:
        print_menu()
        choice = input("Select an option (1-3): ")

        if choice == "1":
            
            try:
                amt_input = int(input("Enter amount spent: "))
                cat_input = input("Enter category (e.g., Food, Travel): ")

                
                new_item = budget.entry(amt_input, cat_input)
                
                my_expenses.append(new_item)
                print("Expense recorded.")
            except ValueError:
                print("Error: Please enter a valid number for the amount.")

        elif choice == "2":
            print("\n--- Spending Summary ---")
            
            
            total_spent = budget.total_spending(my_expenses)
            status_msg = budget.check_status(total_spent)
            
            print(f"Total Spent So Far: Rs. {total_spent}")
            print(status_msg)
            
            
            print("\nRecent Transactions:")
            for x in my_expenses:
                print(f" - Rs.{x['amt']} on {x['cat']}")

        elif choice == "3":
            
            ledger.expense(my_expenses)
            print("Data saved successfully. Exiting...")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
