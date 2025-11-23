# PocketSaver: Student Expense Tracker

## Project Description
PocketSaver is a CLI (Command Line Interface) tool built to help university students manage their monthly pocket money. I often find myself losing track of small expenses like food, printouts, and travel, leading to budget issues at the end of the month. This program solves that by allowing users to log every expense, calculate the total spent, and check if they are within their safety limit.

## Theme
Finance & Banking

## Course
CSE1003 - Introduction to Problem Solving & Programming

## Features
* **Expense Logging:** Quickly add an amount and a category (e.g., "50 for Coffee").
* **Budget Logic:** The system sums up all expenses and warns the user if they exceed their monthly limit (set to Rs. 5000).
* **Data Persistence:** Uses File I/O to save records to `my_expenses.txt`, ensuring data is kept safe even after closing the program.
* **Error Handling:** Includes checks to ensure users enter valid numbers for amounts.

## Project Structure
I followed a modular design approach, splitting the code into three Python files:

1.  **`main.py`** (The Interface):
    * Contains the main menu loop.
    * Handles user input and error checking (try/except blocks).
    * Connects the logic module with the storage module.

2.  **`ledger.py`** (The Storage):
    * Handles reading and writing to the text file.
    * `save_expense()`: Converts the integer amounts to strings and saves them with a `|` separator.
    * `load_history()`: Reads the file and converts the data back into a list of dictionaries.

3.  **`budget.py`** (The Logic):
    * Handles the mathematical calculations.
    * `get_total_spending()`: Iterates through the list to calculate the sum.
    * `check_budget_status()`: Uses conditional logic (`if/elif/else`) to determine if the user is safe or over budget.

## How to Run
1.  Make sure Python is installed on your system.
2.  Download the repository files to a single folder.
3.  Open the terminal/command prompt in that folder.
4.  Run the application:
    ```bash
    python main.py
    ```
5.  Follow the menu prompts to add or view expenses.

## Data Format
The program stores data in a simple text file (`my_expenses.txt`) in the following format:
`Amount|Category`
Example:
```text
100|Breakfast
50|Auto Rickshaw
