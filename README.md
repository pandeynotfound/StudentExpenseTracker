# Student Expense Tracker

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

No external Python libraries are required to run the application.

## Project Structure

```text
StudentExpenseTracker/
│
├── main.py
├── utils.py
├── test_expenses.py
├── statement.md
├── README.md
├── .gitignore
│
└── docs/
    ├── flowchart.png
    ├── use_case_diagram.png
    ├── sequence diagram.png
    ├── system_architecture.png
    ├── component_diagram.png
    ├── sample_output.png
    └── test_results.txt
```

## How to Run

Open a terminal inside the `StudentExpenseTracker` folder.

Run the application:

```bash
python main.py
```

Use the menu:

```text
1. Add Expense
2. View Expenses
3. Search Expenses
4. Spending Summary
5. Delete Expense
6. Exit
```

## Testing

Run:

```bash
python test_expenses.py
```

The current test suite checks:
- Adding expense data
- Multiple expenses
- Category-wise calculation
- Total spending calculation
- Expense deletion

The current test run passes all five tests.

## Example

```text
===== SPENDING SUMMARY =====

Total Spending: INR 900.0
Number of Expenses: 4
Average Expense: INR 225.0

===== CATEGORY-WISE SPENDING =====

Food : INR 320.0
Transport : INR 80.0
Shopping : INR 500.0
```

## Design Documentation

The `docs` folder contains:
- Flowchart
- Use Case Diagram
- Sequence Diagram
- System Architecture Diagram
- Component Diagram
- Sample Output
- Test Results

## Limitations

- Expenses are stored only while the program is running.
- Data is lost when the application is closed.
- The application currently uses a command-line interface.
- Expenses do not currently contain dates.
- No database is used.
- No user account system is included.

## Future Enhancements

Possible future improvements include:
- Permanent storage using files
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
