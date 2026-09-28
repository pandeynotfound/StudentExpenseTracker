# Student Expense Tracker

**Student:** Rohitashwa Pandey  
**Registration No.:** 26BAI10095  
**Institution:** VIT Bhopal University  
**Course:** CSE1021 — Introduction to Problem Solving and Programming

## 1. Problem Statement

College students make many small expenses during their daily academic and personal activities. These expenses may include food, transportation, shopping, stationery, entertainment, and other miscellaneous purchases. When these expenses are not recorded properly, it can become difficult to determine how much money has been spent and which categories consume the most money.

The **Student Expense Tracker** is a Python-based, menu-driven application designed to provide a simple solution to this problem. The application allows users to record their expenses, view previously recorded expenses, search for expenses by category, analyze their spending, and delete incorrect or unnecessary records.

The project applies fundamental problem-solving and programming concepts from CSE1021, including variables, input/output, conditional statements, loops, functions, lists, dictionaries, searching, counting, and summation.

## 2. Objectives

1. To develop a simple application for recording daily student expenses.
2. To apply fundamental Python programming concepts to a real-world problem.
3. To demonstrate the use of lists and dictionaries for storing and organizing data.
4. To implement searching and basic data-processing algorithms.
5. To calculate useful spending statistics such as total and average expenses.
6. To provide category-wise spending information.
7. To implement basic input validation and error handling.
8. To develop a modular and understandable Python program.

## 3. Scope of the Project

The project focuses on managing expenses through a command-line interface.

The current version provides:
- Adding new expenses
- Viewing all recorded expenses
- Searching for expenses by category
- Calculating total spending
- Calculating average expense
- Calculating category-wise spending
- Deleting an existing expense
- Validating user input
- Handling invalid inputs and choices

The current project uses temporary memory through Python lists and dictionaries. Expenses are not permanently stored after the program is closed.

The project does not currently include:
- User accounts
- Database connectivity
- Online synchronization
- Cloud storage
- Graphical user interface
- Mobile application functionality

These features may be considered as future enhancements.

## 4. Target Users

The primary target users are:
- College students
- Hostel students
- Students who want to monitor their daily spending
- Students who want a simple way to categorize expenses
- Beginners learning Python programming and problem solving

## 5. Functional Requirements

### FR1: Add Expense
The system shall allow the user to add a new expense by providing:
- Expense amount
- Expense category
- Expense description

The system shall validate the entered information before adding the expense.

### FR2: View Expenses
The system shall display all recorded expenses, including:
- Expense number
- Amount
- Category
- Description

### FR3: Search Expenses
The system shall allow the user to search for expenses using a category. The search shall be case-insensitive.

### FR4: Spending Summary
The system shall calculate and display:
- Total number of expenses
- Total spending
- Average expense
- Category-wise spending

### FR5: Delete Expense
The system shall allow the user to delete an expense by selecting its expense number.

### FR6: Input Validation
The system shall validate:
- Expense amount must be greater than zero.
- Expense amount must be numeric.
- Category cannot be empty.
- Description cannot be empty.
- Expense number must be valid.
- Menu choices must be between 1 and 6.

### FR7: Exit
The system shall provide an option for the user to exit the application.

## 6. Non-Functional Requirements

### NFR1: Usability
The application should provide a simple menu-driven interface that is easy for a student to understand and operate.

### NFR2: Reliability
The application should continue running when users enter invalid menu choices or invalid numerical input instead of terminating unexpectedly.

### NFR3: Maintainability
The program should be divided into functions so that individual operations can be modified or tested independently.

### NFR4: Error Handling
The system should handle invalid numerical input, invalid expense numbers, empty fields, and invalid menu choices.

### NFR5: Resource Efficiency
The application should use basic Python data structures and algorithms without requiring unnecessary external libraries or resources.

## 7. High-Level System Workflow

```text
Start
  |
  v
Display Main Menu
  |
  v
User Selects an Option
  |
  +----> Add Expense
  |
  +----> View Expenses
  |
  +----> Search Expenses
  |
  +----> Spending Summary
  |
  +----> Delete Expense
  |
  +----> Exit
  |
  v
Return to Main Menu
  |
  v
Continue Until Exit
```

## 8. Data Representation

The application uses a Python list to store multiple expenses. Each individual expense is represented using a Python dictionary.

Example:

```python
expense = {
    "amount": 120,
    "category": "Food",
    "description": "Dinner"
}
```

Multiple expenses are stored inside a list:

```python
expenses = [
    {
        "amount": 120,
        "category": "Food",
        "description": "Dinner"
    },
    {
        "amount": 80,
        "category": "Transport",
        "description": "Bus"
    }
]
```

## 9. Algorithms Used

### 9.1 Expense Addition
The user provides expense details. The program validates the information, creates a dictionary containing the expense data, and adds it to the expense list.

### 9.2 Expense Searching
The program iterates through the expense list and compares each expense category with the category entered by the user. The comparison is case-insensitive.

### 9.3 Total Spending
The program initializes a total value to zero and iterates through every expense, adding each expense amount to the total.

### 9.4 Average Expense
The average expense is calculated using:

```text
Average = Total Spending / Number of Expenses
```

### 9.5 Category-wise Spending
A dictionary is used to group expenses according to their categories. If a category already exists, the new amount is added to its existing total; otherwise, a new category is created.

### 9.6 Expense Deletion
The user selects an expense number. The program converts this number into the corresponding list index and removes the selected expense.

## 10. Technologies Used

- Python 3
- Python Lists
- Python Dictionaries
- Python Functions
- Conditional Statements
- `for` and `while` Loops
- String Operations
- Exception Handling
- Basic Algorithmic Problem Solving

No external Python libraries are required.

## 11. Project Structure

```text
StudentExpenseTracker/
│
├── main.py
├── app.py
├── utils.py
├── test_expenses.py
├── statement.md
└── README.md
```

### main.py
Contains the main application logic, menu system, and expense-management functions.

### app.py
Provides a simple Python launcher for the main application.

### utils.py
Contains small reusable utility functions used by the main program.

### test_expenses.py
Contains basic tests for important expense-management and calculation operations.

### statement.md
Contains the project statement, scope, requirements, objectives, and technical description.

### README.md
Contains project information, features, setup instructions, usage instructions, and testing instructions.

## 12. Expected Input

The application accepts:
- Numeric expense amounts
- Text-based categories
- Text-based descriptions
- Numerical menu choices
- Numerical expense numbers for deletion

Example:

```text
Enter expense amount: 150
Enter category: Food
Enter description: Lunch
```

## 13. Expected Output

After adding an expense:

```text
Expense added successfully!
```

Example expense list:

```text
===== YOUR EXPENSES =====

1 | INR 150 | Food | Lunch
2 | INR 80 | Transport | Bus
```

Example spending summary:

```text
===== SPENDING SUMMARY =====

Total Spending: INR 230
Number of Expenses: 2
Average Expense: INR 115

===== CATEGORY-WISE SPENDING =====

Food : INR 150
Transport : INR 80
```

## 14. Error Handling Strategy

The application uses validation and exception handling to prevent incorrect input from causing the program to terminate unexpectedly.

Examples include:
- Non-numeric expense amounts
- Negative or zero amounts
- Empty categories
- Empty descriptions
- Invalid expense numbers
- Invalid menu choices

Example:

```text
Please enter a valid amount.
```

## 15. Testing

The project includes a testing file named `test_expenses.py`.

The tests cover:
- Adding an expense
- Handling multiple expenses
- Category-wise calculation
- Total spending calculation
- Deleting an expense

Run the tests using:

```bash
python test_expenses.py
```

Successful execution produces:

```text
ALL TESTS PASSED!
```

## 16. Limitations

1. Expenses are stored only while the program is running.
2. Closing the application removes the stored expense data.
3. The application does not have a graphical interface.
4. Users cannot currently specify dates for expenses.
5. The application does not provide graphical charts.
6. There is no user authentication or account system.

## 17. Future Enhancements

Possible future improvements include:
- Permanent storage using files
- Date and time for every expense
- Monthly and weekly reports
- Budget limits
- Budget alerts
- Graphical spending charts
- Exporting reports
- Graphical user interface
- Database integration
- User accounts
- Mobile application support

## 18. Conclusion

The Student Expense Tracker demonstrates how fundamental programming concepts can be applied to solve a simple real-world problem.

The project uses Python functions, lists, dictionaries, loops, conditional statements, searching, counting, summation, and error handling to provide basic expense-management functionality.

The project follows a problem-solving approach of identifying a problem, designing a solution, representing data, implementing algorithms, validating inputs, and testing the resulting program.
