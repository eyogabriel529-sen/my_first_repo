from expense import Expense
import calendar
import datetime

def main():
    print(f'🎯 Running Expense Tracker')
    expense_file_path = "expenses.csv"
    budget = 50000

    # Get user to input their expense.
    expense = get_usr_expense()


    # write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # read file and summarize expense.
    summarize_expenses(expense_file_path, budget)



def get_usr_expense():
    print(f'🎯 Getting User Expense')
    expense_name = input('Enter Expense Name: ')
    expense_amount = float(input('Enter Expense Amount: '))
    expense_categories = [
        '🍔Food',
        '🏠Home',
        '🏢Work',
        '🎉Fun',
        '✨Misc'
    ]

    while True:
        print('Select a category: ')
        for i, category_name in enumerate(expense_categories):
            print(f"    {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f'Enter a category number{value_range}: ')) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print('Invalind category. Please try again!')


def save_expense_to_file(expense: Expense, expense_file_path):
    #used a type hint here (": Expense")
    print(f'🎯 Saving User Expense: {expense} to {expense_file_path}')
    with open(expense_file_path, "a", encoding="utf-8") as f:
        #so that python can save the file in UTF-8 encoding which supports emojis and all unicode characters
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")
   

def summarize_expenses(expense_file_path, budget):
    print(f'🎯 Summarizing User Expense')
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(',')
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
      
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
            
    print("Expenses by Category📈:")        
    for key, amount in amount_by_category.items():
        print(f'  {key}: N{amount:.2f}')

    total_spent = sum([ex.amount for ex in expenses])
    print(f"💵Total Spent: N{total_spent:.2f}")
    
    remaining_budget = budget - total_spent
    print(f"✅Budget Remaining: N{remaining_budget:.2f}")
    
    # Get the current date
    now = datetime.datetime.now()
    
    # Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    
    # Calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day    
    
    daily_budget = remaining_budget / remaining_days
    print(f"👉Budget per day: N{daily_budget:.2f}") 
    
'''    
# To add colour to the terminal output

def color_text(text, color):
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"
'''

if __name__ == '__main__':
    main()
    

