# Software Name: BudgetMaster
# Category: Budgeting
# Description: BudgetMaster is a budgeting software application that helps individuals effectively manage their finances by providing comprehensive budgeting features. It allows users to input their income and expenses, categorize them, and set budget goals. The software provides visual representations of budget breakdowns and generates reports to track spending patterns. With BudgetMaster, users can make informed financial decisions and stay on track to achieve their financial goals.

class BudgetMaster:
    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.budget_goals = {}
        self.categories = set()

    def add_income(self, source, amount):
        """Adds an income source and its amount."""
        if source in self.income:
            self.income[source] += amount
        else:
            self.income[source] = amount
        print(f"Income added: {source} - ${amount}")

    def add_expense(self, category, item, amount):
        """Adds an expense to a specific category."""
        if category not in self.categories:
            self.categories.add(category)
            self.expenses[category] = {}

        if item in self.expenses[category]:
            self.expenses[category][item] += amount
        else:
            self.expenses[category][item] = amount
        print(f"Expense added: {category} - {item} - ${amount}")


    def set_budget_goal(self, category, amount):
        """Sets a budget goal for a specific category."""
        self.budget_goals[category] = amount
        print(f"Budget goal set for {category}: ${amount}")

    def get_total_income(self):
        """Calculates and returns the total income."""
        total = sum(self.income.values())
        return total

    def get_total_expenses(self):
        """Calculates and returns the total expenses."""
        total = 0
        for category in self.expenses:
            for item in self.expenses[category]:
                total += self.expenses[category][item]
        return total

    def get_category_expenses(self, category):
        """Calculates and returns total expenses for a specific category."""
        if category in self.expenses:
            total = sum(self.expenses[category].values())
            return total
        else:
            return 0

    def generate_report(self):
        """Generates a report of income, expenses, and budget goals."""
        print("\n--- Budget Report ---")
        print("Income:")
        for source, amount in self.income.items():
            print(f"  {source}: ${amount}")
        print(f"Total Income: ${self.get_total_income()}")

        print("\nExpenses:")
        for category in self.expenses:
            print(f"  {category}:")
            for item, amount in self.expenses[category].items():
                print(f"    {item}: ${amount}")
            print(f"    Total {category}: ${self.get_category_expenses(category)}")
        print(f"Total Expenses: ${self.get_total_expenses()}")

        print("\nBudget Goals:")
        for category, amount in self.budget_goals.items():
            print(f"  {category}: ${amount}")

        remaining_budget = self.get_total_income() - self.get_total_expenses()
        print(f"\nRemaining Budget: ${remaining_budget}")

    def visualize_budget(self):
        """Placeholder for budget visualization."""
        print("\nBudget Visualization (Placeholder):")
        print("  Visualization feature coming soon!")

# Example usage:
if __name__ == "__main__":
    budget = BudgetMaster()

    budget.add_income("Salary", 5000)
    budget.add_income("Freelance", 1000)

    budget.add_expense("Housing", "Rent", 1500)
    budget.add_expense("Food", "Groceries", 300)
    budget.add_expense("Food", "Dining Out", 200)
    budget.add_expense("Transportation", "Gas", 150)
    budget.add_expense("Transportation", "Public Transport", 50)

    budget.set_budget_goal("Food", 500)
    budget.set_budget_goal("Transportation", 200)

    budget.generate_report()
    budget.visualize_budget()