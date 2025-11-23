# budget.py - This file handles the math and logic for my expenses

def entry(amount_num, cat_text):
    # Bundling the two inputs into a dictionary
    # amount_num should be an integer here
    new_expense = {
        'amt': amount_num,
        'cat': cat_text
    }
    return new_expense

def total_spending(expense_list):
    # We need to loop through the list and add up all the 'amt' values
    total_money = 0
    
    for item in expense_list:
        cost = item['amt']
        # Accumulating the sum
        total_money = total_money + cost
        
    return total_money

def check_status(current_total):
    # I set my monthly pocket money limit to 5000
    limit = int(input("Enter the budget: "))
    
    if current_total > limit:
        return "Warning: You have exceeded your budget!"
    elif (limit-current_total)< 500:
        return "Careful: You are almost out of money."
    else:
        remaining = limit - current_total
        return f"Status: Safe. You have {remaining} left to spend."
