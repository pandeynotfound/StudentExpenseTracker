# Student Expense Tracker

## 1. Problem Statement

College students make many small expenses during their daily academic and personal activities. These expenses may include food, transportation, shopping, stationery, entertainment, and other miscellaneous purchases. When these expenses are not recorded properly, it can become difficult to determine how much money has been spent and which categories consume the most money.

The **Student Expense Tracker** is a Python-based, menu-driven application designed to provide a simple solution to this problem. The application allows users to record their expenses, view previously recorded expenses, search for expenses by category, analyze their spending, and delete incorrect or unnecessary records.

The project applies fundamental problem-solving and programming concepts from CSE1021, including variables, input/output, conditional statements, loops, functions, lists, dictionaries, searching, counting, and summation.

---

## 2. Objectives

The main objectives of the Student Expense Tracker are:

1. To develop a simple application for recording daily student expenses.
2. To apply fundamental Python programming concepts to a real-world problem.
3. To demonstrate the use of lists and dictionaries for storing and organizing data.
4. To implement searching and basic data-processing algorithms.
5. To calculate useful spending statistics such as total and average expenses.
6. To provide category-wise spending information.
7. To implement basic input validation and error handling.
8. To develop a modular and understandable Python program.

---

## 3. Scope of the Project

The project focuses on managing expenses through a command-line interface.

The current version of the application provides the following functionality:

- Adding new expenses
- Viewing all recorded expenses
- Searching for expenses by category
- Calculating total spending
- Calculating the average expense
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

---

## 4. Target Users

The primary target users of the application are:

- College students
- Hostel students
- Students who want to monitor their daily spending
- Students who want a simple way to categorize expenses
- Beginners learning Python programming and problem solving

---

## 5. Functional Requirements

### FR1: Add Expense

The system shall allow the user to add a new expense.

The user must provide:

- Expense amount
- Expense category
- Expense description

The system shall validate the entered information before adding the expense.

---

### FR2: View Expenses

The system shall display all recorded expenses.

Each expense shall contain:

- Expense number
- Amount
- Category
- Description

---

### FR3: Search Expenses

The system shall allow the user to search for expenses using a category.

The search shall be case-insensitive so that inputs such as:

```text
Food
food
FOOD