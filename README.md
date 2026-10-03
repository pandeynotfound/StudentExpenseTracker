# Student Expense Tracker

**Student:** Rohitashwa Pandey  
**Registration No.:** 26BAI10095  
**Institution:** VIT Bhopal University  
**Course:** CSE1021 — Introduction to Problem Solving and Programming

A simple Python-based expense tracking application designed for students.

## Overview

The **Student Expense Tracker** is a menu-driven Python application that helps students record and manage their daily expenses.

The application allows users to add expenses, view recorded expenses, search expenses by category, analyze spending, and delete expenses.

The project demonstrates fundamental problem-solving and Python programming concepts such as functions, lists, dictionaries, loops, conditional statements, searching, counting, summation, and error handling.

## Features

- Add an expense
- View all expenses
- Search expenses by category
- Calculate total spending
- Calculate average expense
- View category-wise spending
- Delete an expense
- Input validation
- Error handling
- Simple command-line interface

## Technologies Used

- Python 3
- Python Lists
- Python Dictionaries
- Python Functions
- Conditional Statements
- `for` and `while` Loops
- String Operations
- Exception Handling

No external Python libraries are required.

## Project Structure

```text
StudentExpenseTracker/
│
├── main.py
├── utils.py
├── test_expenses.py
├── statement.md
└── README.md
```

### `main.py`

Contains the main application logic, menu system, and expense-management functions. The program includes the student project identification in its header and menu.

### `utils.py`

Contains reusable utility functions used by the main program.

### `test_expenses.py`

Contains tests for important expense-management and calculation operations.

### `statement.md`

Contains the problem statement, objectives, scope, requirements, and technical description.

### `README.md`

Contains project information, features, setup instructions, usage instructions, and testing instructions.

## How to Run

### Step 1: Open the Project Folder

Open a terminal inside the `StudentExpenseTracker` folder.

### Step 2: Run the Application

```bash
python main.py
```

### Step 3: Use the Menu

```text
1. Add Expense
2. View Expenses
3. Search Expenses
4. Spending Summary
5. Delete Expense
6. Exit
```

## Example Usage

### Adding an Expense

```text
Enter your choice: 1

Enter expense amount: 150
Enter category: Food
Enter description: Lunch

Expense added successfully!
```

### Viewing Expenses

```text
Enter your choice: 2

===== YOUR EXPENSES =====

1 | INR 150.0 | Food | Lunch
```

### Searching Expenses

```text
Enter your choice: 3

Enter category to search: Food

===== SEARCH RESULTS =====

1 | INR 150.0 | Food | Lunch
```

### Spending Summary

```text
Enter your choice: 4

===== SPENDING SUMMARY =====

Total Spending: INR 230.0
Number of Expenses: 2
Average Expense: INR 115.0

===== CATEGORY-WISE SPENDING =====

Food : INR 150.0
Transport : INR 80.0
```

### Deleting an Expense

```text
Enter your choice: 5

===== YOUR EXPENSES =====

1 | INR 150.0 | Food | Lunch
2 | INR 80.0 | Transport | Bus

Enter expense number to delete: 1

Deleted: Food - INR 150.0
```

## Input Validation

The application validates user input.

For example:

```text
Enter expense amount: abc

Please enter a valid amount.
```

For a negative or zero amount:

```text
Enter expense amount: -100

Amount must be greater than zero.
```

The program also prevents empty categories and descriptions.

## Testing

The project contains a testing file:

```text
test_expenses.py
```

Run the tests using:

```bash
python test_expenses.py
```

Expected output:

```text
==============================
   STUDENT EXPENSE TESTS
==============================

Test 1 passed: Add Expense
Test 2 passed: Multiple Expenses
Test 3 passed: Category Calculation
Test 4 passed: Total Calculation
Test 5 passed: Delete Expense

==============================
   ALL TESTS PASSED!
==============================
```

## Project Objective

The objective of this project is to apply fundamental problem-solving and Python programming concepts to a simple real-world problem faced by students.

The application demonstrates how data can be represented using Python lists and dictionaries and processed using functions, loops, conditions, searching, counting, and summation.

## Limitations

- Expenses are stored only while the program is running.
- Data is lost when the application is closed.
- The application currently uses a command-line interface.
- Expenses do not currently contain dates.
- No database is used.
- No user account system is included.

## Future Enhancements

Possible future improvements include:

- Permanent expense storage using files
- Date and time for expenses
- Monthly and weekly reports
- Budget limits
- Budget alerts
- Graphical spending charts
- Exporting reports
- Graphical user interface
- Database integration
- User accounts
- Mobile application support

## Conclusion

The Student Expense Tracker is a simple application that demonstrates the practical use of fundamental Python programming and problem-solving concepts.

It provides basic expense-management functionality while maintaining a simple and understandable design suitable for a beginner-level programming project.
