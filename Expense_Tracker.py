expenses = []

# Load previously saved expenses
try:
    with open("expense.txt", "r") as file:
        for line in file:
            parts = line.split("|")
            if len(parts) == 3:
                parts[0] = parts[0].strip()
                parts[1] = parts[1].strip()
                parts[2] = parts[2].strip()
                try:
                    parts[1] = float(parts[1])
                    expenses.append(parts)
                except ValueError:
                    pass
except FileNotFoundError:
    pass


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense[1]
    return total


def save_expenses(expenses):
    with open("expense.txt", "w") as file:
        for expense in expenses:
            file.write(expense[0] + " | " + str(expense[1]) + " | " + expense[2] + "\n")


budget = 0
choice = 0

while choice != 8:

    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Category-wise Spending")
    print("5. View Highest Expense")
    print("6. Set Monthly Budget")
    print("7. View Budget Status")
    print("8. Exit")
    print("=====================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        ex_name = input("Enter expense name: ").strip()

        if ex_name == "":
            print("Expense name cannot be empty.")
            continue

        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid amount.")
            continue

        category = input("Enter category: ").strip()

        if category == "":
            print("Category cannot be empty.")
            continue

        category = category.upper()
        expense = [ex_name, amount, category]
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")

    elif choice == 2:
        if expenses == []:
            print("No expenses added yet.")
        else:
            print("\n----------- ALL EXPENSES -----------")
            count = 1
            for expense in expenses:
                print(count, ".", expense[0], "| ₹", expense[1], "|", expense[2])
                count += 1
            print("------------------------------------")

    elif choice == 3:
        if expenses == []:
            print("No expenses added yet.")
        else:
            total = calculate_total(expenses)
            print("\nTotal Spending: ₹", total)

    elif choice == 4:
        if expenses == []:
            print("No expenses added yet.")
        else:
            category_expenses = {}
            for expense in expenses:
                if expense[2] in category_expenses:
                    category_expenses[expense[2]] += expense[1]
                else:
                    category_expenses[expense[2]] = expense[1]

            print("\n------ CATEGORY-WISE SPENDING ------")
            for category in category_expenses:
                print(category, ": ₹", category_expenses[category])
            print("------------------------------------")

    elif choice == 5:
        if expenses == []:
            print("No expenses added yet.")
        else:
            highest_expense = expenses[0]
            for expense in expenses:
                if expense[1] > highest_expense[1]:
                    highest_expense = expense

            print("\n--------- HIGHEST EXPENSE ----------")
            print("Expense Name :", highest_expense[0])
            print("Amount       : ₹", highest_expense[1])
            print("Category     :", highest_expense[2])
            print("------------------------------------")

    elif choice == 6:
        try:
            new_budget = float(input("Enter your monthly budget: "))
            if new_budget <= 0:
                print("Budget must be greater than zero.")
                continue
            budget = new_budget
            print("Monthly budget set successfully!")
        except ValueError:
            print("Please enter a valid budget amount.")

    elif choice == 7:
        if budget == 0:
            print("Please set your budget first.")
        else:
            total = calculate_total(expenses)
            print("\n----------- BUDGET STATUS ----------")
            print("Monthly Budget :", budget)
            print("Total Spending :", total)

            if total > budget:
                print("Budget exceeded by ₹", total - budget)
            elif total == budget:
                print("Budget fully used.")
            else:
                print("Remaining amount : ₹", budget - total)

            print("------------------------------------")

    elif choice == 8:
        print("\nThank you for using Expense Tracker!")
        print("Exiting...")

    else:
        print("Invalid choice. Please select 1 to 8.")
