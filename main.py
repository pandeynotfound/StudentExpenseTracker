"""
Student Expense Tracker
CSE1021 — Introduction to Problem Solving and Programming

Student: Rohitashwa Pandey
Registration No.: 26BAI10095
VIT Bhopal University
"""

from utils import format_amount, print_line


# Student: Rohitashwa Pandey | Registration No.: 26BAI10095
expenses = []

CATEGORIES = [
    "Food",
    "Travel",
    "Conveyance",
    "College",
    "Shopping",
    "Entertainment"
]


def add_expense():
    """Add a new expense to the in-memory expense list."""
    print("\n--- Add Expense ---")

    try:
        amount = float(input("Enter amount (INR): "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        description = input("Enter description: ").strip()

        if not description:
            print("Description cannot be empty.")
            return

        print("\nSelect Category:")
        for i, category in enumerate(CATEGORIES, 1):
            print(f"{i}. {category}")
        print(f"{len(CATEGORIES) + 1}. Other")

        try:
            category_choice = int(input("Enter category choice: "))

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

        except ValueError:
            print("Please enter a valid category number.")
            return

        expense = {
            "amount": amount,
            "description": description,
            "category": category
        }

        expenses.append(expense)

        print("\nExpense added successfully!")
        print(f"Amount: {format_amount(amount)}")
        print(f"Description: {description}")
        print(f"Category: {category}")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    """Display all recorded expenses."""
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded.")
        return

    print_line()

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. INR {expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )

    print_line()


def search_expenses():
    """Search expenses by description or category."""
    print("\n--- Search Expenses ---")

    if not expenses:
        print("No expenses recorded.")
        return

    keyword = input("Enter keyword to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    found = False
    print_line()

    for i, expense in enumerate(expenses, 1):
        if (
            keyword in expense["description"].lower()
            or keyword in expense["category"].lower()
        ):
            print(
                f"{i}. INR {expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['description']}"
            )
            found = True

    print_line()

    if not found:
        print("No matching expenses found.")


def spending_summary():
    """Display total, average, count, and category-wise spending."""
    print("\n--- Spending Summary ---")

    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(expense["amount"] for expense in expenses)
    count = len(expenses)
    average = total / count

    print(f"Total Spending: {format_amount(total)}")
    print(f"Number of Expenses: {count}")
    print(f"Average Expense: {format_amount(average)}")

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        category_totals[category] = (
            category_totals.get(category, 0) + expense["amount"]
        )

    print("\nCategory-wise Spending:")
    for category, amount in category_totals.items():
        print(f"{category}: {format_amount(amount)}")


def delete_expense():
    """Delete an expense by its displayed number."""
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses recorded.")
        return

    view_expenses()

    try:
        number = int(input("Enter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        removed = expenses.pop(number - 1)

        print("\nExpense deleted successfully!")
        print(
            f"Deleted: INR {removed['amount']:.2f} | "
            f"{removed['category']} | "
            f"{removed['description']}"
        )

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Run the Student Expense Tracker menu."""
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

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            spending_summary()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("\nThank you for using Student Expense Tracker!")
            break
        else:
            print("\nInvalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
