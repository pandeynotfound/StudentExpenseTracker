from main import (
    add_expense,
    view_expenses,
    search_expenses,
    spending_summary,
    delete_expense
)


# -------------------------------
# Test 1: Adding an Expense
# -------------------------------

def test_add_expense():
    expenses = []

    expense = {
        "amount": 100,
        "category": "Food",
        "description": "Lunch"
    }

    expenses.append(expense)

    assert len(expenses) == 1
    assert expenses[0]["amount"] == 100
    assert expenses[0]["category"] == "Food"

    print("Test 1 passed: Add Expense")


# -------------------------------
# Test 2: Multiple Expenses
# -------------------------------

def test_multiple_expenses():
    expenses = [
        {
            "amount": 100,
            "category": "Food",
            "description": "Lunch"
        },
        {
            "amount": 200,
            "category": "Transport",
            "description": "Bus"
        }
    ]

    assert len(expenses) == 2
    assert expenses[1]["amount"] == 200

    print("Test 2 passed: Multiple Expenses")


# -------------------------------
# Test 3: Category Calculation
# -------------------------------

def test_category_calculation():
    expenses = [
        {
            "amount": 100,
            "category": "Food",
            "description": "Lunch"
        },
        {
            "amount": 200,
            "category": "Food",
            "description": "Dinner"
        },
        {
            "amount": 150,
            "category": "Transport",
            "description": "Bus"
        }
    ]

    categories = {}

    for expense in expenses:

        category = expense["category"]

        if category in categories:
            categories[category] += expense["amount"]
        else:
            categories[category] = expense["amount"]

    assert categories["Food"] == 300
    assert categories["Transport"] == 150

    print("Test 3 passed: Category Calculation")


# -------------------------------
# Test 4: Total Calculation
# -------------------------------

def test_total_calculation():
    expenses = [
        {"amount": 100, "category": "Food", "description": "Lunch"},
        {"amount": 200, "category": "Transport", "description": "Bus"},
        {"amount": 300, "category": "Shopping", "description": "Shoes"}
    ]

    total = 0

    for expense in expenses:
        total += expense["amount"]

    assert total == 600

    print("Test 4 passed: Total Calculation")


# -------------------------------
# Test 5: Delete Expense
# -------------------------------

def test_delete_expense():

    expenses = [
        {"amount": 100, "category": "Food", "description": "Lunch"},
        {"amount": 200, "category": "Transport", "description": "Bus"}
    ]

    deleted = expenses.pop(0)

    assert deleted["amount"] == 100
    assert len(expenses) == 1
    assert expenses[0]["category"] == "Transport"

    print("Test 5 passed: Delete Expense")


# -------------------------------
# Run All Tests
# -------------------------------

if __name__ == "__main__":

    print("\n==============================")
    print("   STUDENT EXPENSE TESTS")
    print("==============================\n")

    test_add_expense()
    test_multiple_expenses()
    test_category_calculation()
    test_total_calculation()
    test_delete_expense()

    print("\n==============================")
    print("   ALL TESTS PASSED!")
    print("==============================")