from utils import format_amount, print_line


# -------------------------------
# Add Expense
# -------------------------------

def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ").strip()

        if category == "":
            print("Category cannot be empty.")
            return

        description = input("Enter description: ").strip()

        if description == "":
            print("Description cannot be empty.")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


# -------------------------------
# View Expenses
# -------------------------------

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n===== YOUR EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(
            i,
            "|", format_amount(expense["amount"]),
            "|", expense["category"],
            "|", expense["description"]
        )


# -------------------------------
# Search Expenses
# -------------------------------

def search_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    search = input("Enter category to search: ").strip()

    found = False

    print("\n===== SEARCH RESULTS =====")

    for i, expense in enumerate(expenses, start=1):

        if expense["category"].lower() == search.lower():

            print(
                i,
                "|", format_amount(expense["amount"]),
                "|", expense["category"],
                "|", expense["description"]
            )

            found = True

    if found == False:
        print("No expenses found in this category.")


# -------------------------------
# Spending Summary
# -------------------------------

def spending_summary(expenses):
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    total = 0
    categories = {}

    for expense in expenses:

        total = total + expense["amount"]

        category = expense["category"]

        if category in categories:
            categories[category] = (
                categories[category] + expense["amount"]
            )
        else:
            categories[category] = expense["amount"]

    average = total / len(expenses)

    print("\n===== SPENDING SUMMARY =====")

    print(
        "Total Spending:",
        format_amount(total)
    )

    print(
        "Number of Expenses:",
        len(expenses)
    )

    print(
        "Average Expense:",
        format_amount(average)
    )

    print("\n===== CATEGORY-WISE SPENDING =====")

    for category in categories:

        print(
            category,
            ":",
            format_amount(categories[category])
        )


# -------------------------------
# Delete Expense
# -------------------------------

def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n===== YOUR EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):

        print(
            i,
            "|", format_amount(expense["amount"]),
            "|", expense["category"],
            "|", expense["description"]
        )

    try:

        number = int(
            input("\nEnter expense number to delete: ")
        )

        if number >= 1 and number <= len(expenses):

            deleted = expenses.pop(number - 1)

            print(
                "Deleted:",
                deleted["category"],
                "-",
                format_amount(deleted["amount"])
            )

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# -------------------------------
# Main Program
# -------------------------------

def main():

    expenses = []

    print("================================")
    print("     STUDENT EXPENSE TRACKER")
    print("================================")

    while True:

        print_line()

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Spending Summary")
        print("5. Delete Expense")
        print("6. Exit")

        print_line()

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            add_expense(expenses)

        elif choice == "2":

            view_expenses(expenses)

        elif choice == "3":

            search_expenses(expenses)

        elif choice == "4":

            spending_summary(expenses)

        elif choice == "5":

            delete_expense(expenses)

        elif choice == "6":

            print("\nThank you for using Student Expense Tracker!")
            break

        else:

            print("Invalid choice. Please select 1-6.")


# -------------------------------
# Start Program
# -------------------------------

if __name__ == "__main__":
    main()