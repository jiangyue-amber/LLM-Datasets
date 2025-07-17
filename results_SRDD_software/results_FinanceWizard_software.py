# Software Name: FinanceWizard
# Category: Management_Game
# Description: FinanceWizard is a management game software that allows players to step into the role of a financial manager. Players are tasked with making strategic financial decisions to ensure the profitability and growth of a virtual company. They can analyze financial data, create and manage budgets, make investment decisions, and analyze market trends. The goal is to maximize profits, minimize expenses, and achieve financial success.

import random

class FinanceWizard:
    def __init__(self, company_name="Acme Corp", initial_capital=100000):
        self.company_name = company_name
        self.capital = initial_capital
        self.expenses = 0
        self.revenue = 0
        self.profit = 0
        self.market_trend = "stable"  # Can be "stable", "growth", "recession"

    def generate_random_value(self, base, variation):
        return base + random.uniform(-variation, variation)

    def update_market_trend(self):
        trends = ["stable", "growth", "recession"]
        self.market_trend = random.choice(trends)

    def calculate_expenses(self, employees, rent, materials, marketing):
        self.expenses = employees + rent + materials + marketing
        return self.expenses

    def calculate_revenue(self, sales_volume, price_per_unit):
        # Revenue influenced by market trend
        if self.market_trend == "growth":
            revenue_multiplier = 1.2
        elif self.market_trend == "recession":
            revenue_multiplier = 0.8
        else:
            revenue_multiplier = 1.0

        self.revenue = sales_volume * price_per_unit * revenue_multiplier
        return self.revenue

    def calculate_profit(self):
        self.profit = self.revenue - self.expenses
        self.capital += self.profit
        return self.profit

    def make_investment(self, investment_amount, expected_return_rate):
        # Simplified investment logic
        if investment_amount <= self.capital:
            self.capital -= investment_amount
            potential_return = investment_amount * expected_return_rate
            # Simulate investment outcome (success or failure)
            if random.random() > 0.3:  # 70% chance of success
                self.capital += potential_return
                return True, potential_return
            else:
                return False, 0 #Investment Failure
        else:
            return False, "Insufficient funds for investment"

    def run_simulation(self, num_periods=12):
        for period in range(num_periods):
            print(f"--- Period {period + 1} ---")
            self.update_market_trend()
            print(f"Market trend: {self.market_trend}")

            # Simulate some basic financial decisions
            employees = int(self.generate_random_value(30000, 10000))
            rent = int(self.generate_random_value(10000, 3000))
            materials = int(self.generate_random_value(20000, 7000))
            marketing = int(self.generate_random_value(15000, 5000))

            self.calculate_expenses(employees, rent, materials, marketing)

            sales_volume = int(self.generate_random_value(5000, 1500))
            price_per_unit = self.generate_random_value(25, 5)

            self.calculate_revenue(sales_volume, price_per_unit)
            self.calculate_profit()

            print(f"Expenses: {self.expenses:.2f}")
            print(f"Revenue: {self.revenue:.2f}")
            print(f"Profit: {self.profit:.2f}")
            print(f"Capital: {self.capital:.2f}")

            #Investment decision
            if self.capital > 50000:
                investment_amount = self.generate_random_value(10000, 5000)
                success, return_value = self.make_investment(investment_amount, 0.10)

                if success:
                    print(f"Successful investment of {investment_amount:.2f}, returned {return_value:.2f}")
                elif return_value == "Insufficient funds for investment":
                    print("Insufficient funds for investment")
                else:
                    print(f"Investment of {investment_amount:.2f} failed.")
                print(f"Capital: {self.capital:.2f}")

            if self.capital <= 0:
                print("Game Over! Company bankrupt.")
                return

        print("Simulation finished!")
        if self.capital > 200000:
            print("Congratulations! You achieved significant financial success.")
        elif self.capital > 100000:
            print("Good job! The company is profitable.")
        else:
            print("The company faced some challenges. There is room for improvement in financial management.")

# Example usage:
if __name__ == "__main__":
    game = FinanceWizard("TechSolutions Inc.", 150000)
    game.run_simulation()