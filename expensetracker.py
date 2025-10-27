#expense tracker

expenses = {}

def choice1():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses[category] = amount
    print("Expense added.")

def choice2():
    for category, amount in expenses.items():
        print(f"{category}: {amount}")

def choice3():
    total = sum(expenses.values())
    print(f"Total expenses: {total}")

print("\nWelcome to the Expense Tracker!" \
"\n1. Add Expense" \
"\n2. View Expenses" \
"\n3. View Total Expenses" \
"\n4. Exit")

condition = True

while True:
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        choice1()
    elif choice == '2':
        choice2()
    elif choice == '3':
        choice3()
    elif choice == '4':
        print("Exiting the Expense Tracker. Goodbye!")
        condition = False
        break
    else:
        print("Invalid choice. Please try again.")
