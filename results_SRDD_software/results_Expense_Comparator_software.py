# Software Name: Expense_Comparator
# Category: Finance
# Description: Expense Comparator is a finance software application that helps users compare their expenses across different time periods. Users can input their expenses and categorize them into different categories such as groceries, transportation, entertainment, etc. The application will provide a visual representation of their expenses through charts and graphs, allowing users to easily compare their spending habits between different timeframes. Users can also set custom date ranges for comparison. The main function of the software is to provide users with a clear understanding of their spending patterns and identify areas where they can make adjustments to improve their financial well-being.

import matplotlib.pyplot as plt
import pandas as pd

class ExpenseComparator:
    def __init__(self):
        self.expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

    def add_expense(self, date, category, amount):
        """Adds an expense to the expense tracker."""
        new_expense = pd.DataFrame([[date, category, amount]], columns=['Date', 'Category', 'Amount'])
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
        self.expenses['Amount'] = pd.to_numeric(self.expenses['Amount'], errors='coerce')
        self.expenses['Date'] = pd.to_datetime(self.expenses['Date'], errors='coerce')

    def get_expenses_by_date_range(self, start_date, end_date):
        """Returns expenses within a specified date range."""
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        date_filtered_expenses = self.expenses[(self.expenses['Date'] >= start_date) & (self.expenses['Date'] <= end_date)]
        return date_filtered_expenses

    def calculate_total_expenses(self, start_date=None, end_date=None):
        """Calculates the total expenses, optionally within a date range."""
        if start_date and end_date:
            expenses = self.get_expenses_by_date_range(start_date, end_date)
        else:
            expenses = self.expenses
        return expenses['Amount'].sum()

    def calculate_expenses_by_category(self, start_date=None, end_date=None):
        """Calculates expenses grouped by category, optionally within a date range."""
        if start_date and end_date:
            expenses = self.get_expenses_by_date_range(start_date, end_date)
        else:
            expenses = self.expenses

        if expenses.empty:
            return pd.Series()
        else:
            return expenses.groupby('Category')['Amount'].sum()

    def generate_expense_summary(self, start_date=None, end_date=None):
          """Generates and prints a summary of expenses."""
          total_expenses = self.calculate_total_expenses(start_date, end_date)
          category_expenses = self.calculate_expenses_by_category(start_date, end_date)

          print("Expense Summary:")
          if start_date and end_date:
            print(f"  From {start_date} to {end_date}:")
          print(f"  Total Expenses: ${total_expenses:.2f}")
          print("\n  Expenses by Category:")
          if category_expenses.empty:
            print("    No expenses found for the specified period.")
          else:
            for category, amount in category_expenses.items():
                print(f"    {category}: ${amount:.2f}")

    def visualize_expenses_by_category(self, start_date=None, end_date=None):
        """Visualizes expenses by category using a bar chart."""
        category_expenses = self.calculate_expenses_by_category(start_date, end_date)

        if category_expenses.empty:
            print("No data to visualize for the selected period.")
            return

        category_expenses.plot(kind='bar', title='Expenses by Category', figsize=(10, 6))
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def visualize_expenses_over_time(self, category=None):
        """Visualizes expenses over time using a line chart."""
        if self.expenses.empty:
            print("No expense data available.")
            return

        if category:
            expenses = self.expenses[self.expenses['Category'] == category].copy()
        else:
            expenses = self.expenses.copy()

        if expenses.empty:
            print(f"No expenses found for category: {category}" if category else "No expenses found.")
            return


        expenses = expenses.sort_values('Date')
        expenses.set_index('Date', inplace=True)
        expenses['Amount'].plot(kind='line', title=f'Expenses Over Time (Category: {category})' if category else 'Expenses Over Time', figsize=(10, 6))
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    expense_comparator = ExpenseComparator()

    # Example Usage
    expense_comparator.add_expense('2023-01-01', 'Groceries', 100)
    expense_comparator.add_expense('2023-01-05', 'Transportation', 50)
    expense_comparator.add_expense('2023-01-10', 'Entertainment', 30)
    expense_comparator.add_expense('2023-02-01', 'Groceries', 120)
    expense_comparator.add_expense('2023-02-15', 'Transportation', 60)

    # Get expenses for January
    january_expenses = expense_comparator.get_expenses_by_date_range('2023-01-01', '2023-01-31')
    print("January Expenses:\n", january_expenses)

    # Calculate total expenses in January
    total_january_expenses = expense_comparator.calculate_total_expenses('2023-01-01', '2023-01-31')
    print("\nTotal Expenses in January:", total_january_expenses)

    # Calculate expenses by category
    expenses_by_category = expense_comparator.calculate_expenses_by_category()
    print("\nExpenses by Category:\n", expenses_by_category)

    # Generate expense summary
    expense_comparator.generate_expense_summary('2023-01-01', '2023-01-31')

    # Visualize expenses by category
    expense_comparator.visualize_expenses_by_category()

    # Visualize expenses over time
    expense_comparator.visualize_expenses_over_time()

    # Visualize expenses over time for a specific category
    expense_comparator.visualize_expenses_over_time(category='Groceries')