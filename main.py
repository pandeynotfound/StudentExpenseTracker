"""
Student Expense Tracker
Student: Rohitashwa Pandey
Registration No.: 26BAI10095
VIT Bhopal University
"""

from utils import format_amount, print_line

my_expenses = []
expenses = my_expenses

CATEGORIES = [
    "Food",
    "Travel",
    "Conveyance",
    "College",
    "Shopping",
    "Entertainment",
]


def add_expense():
    """Add a new expense to the in-memory list."""
    print("\n--- Add Expense ---")

    try:
        amount_text = input("Enter amount (INR): ").strip()
        if not amount_text:
            print("Amount cannot be empty.")
            return

        amount = float(amount_text)
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid numeric amount.")
        return

    description = input("Enter description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    print("\nSelect Category:")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")
    print(f"{len(CATEGORIES) + 1}. Other")

    try:
        category_choice = int(input("Enter category choice: "))
    except ValueError:
        print("Please enter a valid category number.")
        return

    if 1 <= category_choice <= len(CATEGORIES):
        category = CATEGORIES[category_choice - 1]
    elif category_choice == len(CATEGORIES) + 1:
        category = input("Enter your custom category: ").strip()
        if not category:
            print("Category cannot be empty.")
            return
    else:
        print("Invalid category choice.")
        return

    expense = {
        "amount": amount,
        "description": description,
        "category": category,
    }

    my_expenses.append(expense)

    print("\nExpense added successfully!")
    print(f"Amount: {format_amount(amount)}")
    print(f"Description: {description}")
    print(f"Category: {category}")


def view_expenses():
    """Display all stored expenses in a clear format."""
    print("\n--- All Expenses ---")

    if not my_expenses:
        print("No expenses recorded.")
        return

    print_line()

    for counter, expense in enumerate(my_expenses, start=1):
        print(
            f"{counter}. INR {expense['amount']:.2f} | "
            f"{expense['category']} | {expense['description']}"
        )

    print_line()


def search_expenses():
    """Search expenses by keyword in their description or category."""
    print("\n--- Search Expenses ---")

    if not my_expenses:
        print("No expenses recorded.")
        return

    keyword = input("Enter keyword to search: ").strip().lower()
    if not keyword:
        print("Search keyword cannot be empty.")
        return

    matches_found = False
    print_line()

    for index, expense in enumerate(my_expenses, start=1):
        description = expense["description"].lower()
        category = expense["category"].lower()
        if keyword in description or keyword in category:
            print(
                f"{index}. INR {expense['amount']:.2f} | "
                f"{expense['category']} | {expense['description']}"
            )
            matches_found = True

    print_line()

    if not matches_found:
        print("No matching expenses found.")


def spending_summary():
    """Show total, average, and category-wise spending."""
    print("\n--- Spending Summary ---")

    if not my_expenses:
        print("No expenses recorded.")
        return

    total = sum(expense["amount"] for expense in my_expenses)
    count = len(my_expenses)
    average = total / count if count else 0

    print(f"Total Spending: {format_amount(total)}")
    print(f"Number of Expenses: {count}")
    print(f"Average Expense: {format_amount(average)}")

    category_totals = {}
    for expense in my_expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print("\nCategory-wise Spending:")
    for category_name, category_total in category_totals.items():
        print(f"{category_name}: {format_amount(category_total)}")


def delete_expense():
    """Delete a specific expense from the list."""
    print("\n--- Delete Expense ---")

    if not my_expenses:
        print("No expenses recorded.")
        return

    view_expenses()

    try:
        number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(my_expenses):
        print("Invalid expense number.")
        return

    removed = my_expenses.pop(number - 1)

    print("\nExpense deleted successfully!")
    print(
        f"Deleted: INR {removed['amount']:.2f} | "
        f"{removed['category']} | {removed['description']}"
    )


def main():
    """Run the expense tracker menu."""
    while True:
        print("\n" + "=" * 45)
        print("       STUDENT EXPENSE TRACKER")
        print("       Rohitashwa Pandey")
        print("       26BAI10095")
        print("=" * 45)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Spending Summary")
        print("5. Delete Expense")
        print("6. Exit")
        print("=" * 45)

        user_choice = input("Enter your choice: ").strip()

        if user_choice == "1":
            add_expense()
        elif user_choice == "2":
            view_expenses()
        elif user_choice == "3":
            search_expenses()
        elif user_choice == "4":
            spending_summary()
        elif user_choice == "5":
            delete_expense()
        elif user_choice == "6":
            print("\nThank you for using Student Expense Tracker!")
            break
        else:
            print("\nInvalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()