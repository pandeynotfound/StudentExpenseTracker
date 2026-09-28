"""
Automated tests for Student Expense Tracker.

Student: Rohitashwa Pandey
Registration No.: 26BAI10095
"""

from main import expenses


def test_add_expense():
    expenses.clear()
    expense = {
        "amount": 250.0,
        "description": "Lunch",
        "category": "Food"
    }
    expenses.append(expense)

    assert len(expenses) == 1
    assert expenses[0]["amount"] == 250.0
    assert expenses[0]["description"] == "Lunch"
    assert expenses[0]["category"] == "Food"


def test_multiple_expenses():
    expenses.clear()

    expenses.extend([
        {"amount": 100.0, "description": "Bus", "category": "Conveyance"},
        {"amount": 200.0, "description": "Lunch", "category": "Food"},
        {"amount": 300.0, "description": "Books", "category": "College"}
    ])

    assert len(expenses) == 3


def test_category_total():
    expenses.clear()

    expenses.extend([
        {"amount": 100.0, "description": "Lunch", "category": "Food"},
        {"amount": 150.0, "description": "Dinner", "category": "Food"},
        {"amount": 200.0, "description": "Bus", "category": "Conveyance"}
    ])

    food_total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"] == "Food"
    )
    conveyance_total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"] == "Conveyance"
    )

    assert food_total == 250.0
    assert conveyance_total == 200.0


def test_total_expenses():
    expenses.clear()

    expenses.extend([
        {"amount": 100.0, "description": "Lunch", "category": "Food"},
        {"amount": 200.0, "description": "Bus", "category": "Conveyance"},
        {"amount": 300.0, "description": "Books", "category": "College"}
    ])

    total = sum(expense["amount"] for expense in expenses)
    assert total == 600.0


def test_delete_expense():
    expenses.clear()

    expenses.extend([
        {"amount": 100.0, "description": "Lunch", "category": "Food"},
        {"amount": 200.0, "description": "Bus", "category": "Conveyance"}
    ])

    deleted = expenses.pop(0)

    assert deleted["amount"] == 100.0
    assert deleted["description"] == "Lunch"
    assert len(expenses) == 1


def run_tests():
    test_add_expense()
    test_multiple_expenses()
    test_category_total()
    test_total_expenses()
    test_delete_expense()
    print("ALL TESTS PASSED!")


if __name__ == "__main__":
    run_tests()
