from expense import Expense

def main():
    print(f'🎯 Running Expense Tracker')
    expense_file_path = "expenses.csv"

    #Get user to input their expense.
    expense = get_usr_expense()


    #write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    #read file and summarize expense.
    summarize_expenses(expense_file_path)



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
   

def summarize_expenses():
   


if __name__ == '__main__':
    main()
    

