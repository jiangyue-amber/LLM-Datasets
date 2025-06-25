# Software Name: Retail_Simulator
# Category: Management_Game
# Description: Retail Simulator is a management game software that allows players to experience the challenges and rewards of running a virtual retail store. Players start with a small storefront and must make strategic decisions to attract customers and optimize sales. They can choose the types of products to sell, manage inventory, set prices, design and optimize store layout, conduct marketing campaigns, and hire and train employees. The aim is to grow the business, increase profitability, and become a successful retail entrepreneur.

```python
import random

class RetailSimulator:
    def __init__(self, starting_funds=10000, starting_inventory_capacity=100):
        self.funds = starting_funds
        self.inventory_capacity = starting_inventory_capacity
        self.inventory = {}  # {product_name: quantity}
        self.employees = []
        self.store_layout = "Basic"  # Can be upgraded
        self.customer_traffic = 0
        self.marketing_effectiveness = 0
        self.day = 1

    def choose_products(self, available_products):
        """Allows the player to choose which products to sell.
        Args:
            available_products: A list of dictionaries, where each dictionary
                                 represents a product and contains its name and cost.
        Returns:
            A list of product names the player wants to sell.
        """
        print("Available Products:")
        for i, product in enumerate(available_products):
            print(f"{i+1}. {product['name']} - Cost: ${product['cost']}")

        selected_products = []
        while True:
            choice = input("Enter the number of a product to add to your inventory (or 'done'): ")
            if choice.lower() == 'done':
                break
            try:
                index = int(choice) - 1
                if 0 <= index < len(available_products):
                    selected_products.append(available_products[index]['name'])
                    print(f"Added {available_products[index]['name']} to your selection.")
                else:
                    print("Invalid product number.")
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
        return selected_products

    def manage_inventory(self, products_to_sell, product_prices):
        """Allows the player to buy more of the products they have selected.
           product_prices: Dictionary of {product_name: cost_per_item}
        """
        print(f"Current Funds: ${self.funds}")
        print("Current Inventory:")
        for product, quantity in self.inventory.items():
            print(f"- {product}: {quantity}")

        for product in products_to_sell:
             while True:
                try:
                    quantity_to_buy = int(input(f"How many of {product} would you like to buy? (Cost: ${product_prices[product]}) (Enter 0 to skip): "))
                    if quantity_to_buy < 0:
                        print("Invalid quantity. Please enter a non-negative number.")
                        continue
                    cost = quantity_to_buy * product_prices[product]
                    if cost > self.funds:
                        print("Insufficient funds.")
                        continue
                    if sum(self.inventory.values()) + quantity_to_buy > self.inventory_capacity:
                        print("Not enough inventory space.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
             if quantity_to_buy > 0:
                self.funds -= cost
                if product in self.inventory:
                    self.inventory[product] += quantity_to_buy
                else:
                    self.inventory[product] = quantity_to_buy
                print(f"Bought {quantity_to_buy} of {product}.")
                print(f"Remaining Funds: ${self.funds}")

    def set_prices(self, products_to_sell):
         """Sets the selling prices for each product."""
         product_prices = {}
         print("Set the selling price for each product:")
         for product in products_to_sell:
            while True:
                try:
                    price = float(input(f"Enter the selling price for {product}: $"))
                    if price <= 0:
                        print("Price must be positive.")
                        continue
                    product_prices[product] = price
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
         return product_prices
    def design_store_layout(self):
        """Allows the player to upgrade their store layout."""
        layout_options = {
            "Basic": {"cost": 0, "customer_increase": 0},
            "Organized": {"cost": 2000, "customer_increase": 0.1},
            "Premium": {"cost": 5000, "customer_increase": 0.25},
        }

        print("Available Store Layouts:")
        for layout, details in layout_options.items():
            print(f"- {layout}: Cost ${details['cost']}, Customer Increase: {details['customer_increase'] * 100}%")

        while True:
            layout_choice = input("Enter the name of the layout you want to purchase (or 'cancel'): ")
            if layout_choice.lower() == 'cancel':
                break
            if layout_choice in layout_options:
                cost = layout_options[layout_choice]['cost']
                if cost <= self.funds:
                    self.funds -= cost
                    self.store_layout = layout_choice
                    self.customer_traffic += layout_options[layout_choice]['customer_increase'] * 100
                    print(f"Upgraded to {layout_choice} layout.")
                    break
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid layout choice.")

    def conduct_marketing_campaign(self):
        """Allows the player to conduct a marketing campaign."""
        campaign_options = {
            "Social Media": {"cost": 500, "effectiveness_increase": 0.05},
            "Local Ads": {"cost": 1000, "effectiveness_increase": 0.1},
            "Influencer Marketing": {"cost": 3000, "effectiveness_increase": 0.2},
        }

        print("Available Marketing Campaigns:")
        for campaign, details in campaign_options.items():
            print(f"- {campaign}: Cost ${details['cost']}, Effectiveness Increase: {details['effectiveness_increase'] * 100}%")

        while True:
            campaign_choice = input("Enter the name of the campaign you want to conduct (or 'cancel'): ")
            if campaign_choice.lower() == 'cancel':
                break
            if campaign_choice in campaign_options:
                cost = campaign_options[campaign_choice]['cost']
                if cost <= self.funds:
                    self.funds -= cost
                    self.marketing_effectiveness += campaign_options[campaign_choice]['effectiveness_increase']
                    print(f"Conducted {campaign_choice} campaign.")
                    break
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid campaign choice.")

    def hire_employee(self):
        """Allows the player to hire an employee."""
        employee_options = {
            "Sales Associate": {"salary": 1000},
            "Marketing Specialist": {"salary": 2000},
            "Inventory Manager": {"salary": 1500},
        }

        print("Available Employees:")
        for employee, details in employee_options.items():
            print(f"- {employee}: Salary ${details['salary']}")

        while True:
            employee_choice = input("Enter the name of the employee you want to hire (or 'cancel'): ")
            if employee_choice.lower() == 'cancel':
                break
            if employee_choice in employee_options:
                self.employees.append({"role": employee_choice, "salary": employee_options[employee_choice]['salary']})
                print(f"Hired a {employee_choice}.")
                break
            else:
                print("Invalid employee choice.")

    def train_employee(self):
        """Allows the player to train an existing employee."""
        if not self.employees:
            print("No employees to train.")
            return

        print("Available Employees:")
        for i, employee in enumerate(self.employees):
            print(f"{i+1}. {employee['role']}")

        while True:
            try:
                employee_index = int(input("Enter the number of the employee you want to train (or 'cancel'): ")) - 1
                if 0 <= employee_index < len(self.employees):
                    training_cost = 500  # Fixed training cost
                    if training_cost <= self.funds:
                        self.funds -= training_cost
                        print(f"Trained {self.employees[employee_index]['role']}.")
                        # Add training effect here (e.g., increase sales, reduce waste)
                        break
                    else:
                        print("Insufficient funds for training.")
                        break
                else:
                    print("Invalid employee number.")
            except ValueError:
                print("Invalid input. Please enter a number or 'cancel'.")
            if input("Enter 'cancel' to skip training.").lower() == 'cancel':
                break

    def simulate_day(self, product_prices):
        """Simulates a day of running the retail store."""
        print(f"\n--- Day {self.day} ---")

        # Calculate customer traffic
        base_traffic = 50
        traffic = base_traffic + self.customer_traffic  # Start with base traffic and add layout bonuses
        traffic = int(traffic * (1 + self.marketing_effectiveness))  # Apply marketing effectiveness

        # Simulate sales
        revenue = 0
        for product, quantity in self.inventory.items():
            # Simulate demand (random with some influence from price)
            demand = random.randint(0, int(traffic * (1.5 - (product_prices[product]/10))))  # Lower price, higher demand
            sales = min(quantity, demand)
            revenue += sales * product_prices[product]
            self.inventory[product] -= sales

        # Pay employee salaries
        salary_expenses = sum(employee['salary'] for employee in self.employees)

        # Calculate profit
        profit = revenue - salary_expenses

        # Update funds
        self.funds += profit

        # Print results
        print(f"Customer Traffic: {traffic}")
        print(f"Revenue: ${revenue}")
        print(f"Salary Expenses: ${salary_expenses}")
        print(f"Profit: ${profit}")
        print(f"Current Funds: ${self.funds}")

        self.day += 1

    def run_game(self, available_products, product_prices):
        """Runs the main game loop."""
        products_to_sell = self.choose_products(available_products)

        while True:
            print("\n--- Options ---")
            print("1. Manage Inventory")
            print("2. Set Prices")
            print("3. Design Store Layout")
            print("4. Conduct Marketing Campaign")
            print("5. Hire Employee")
            print("6. Train Employee")
            print("7. Simulate Day")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.manage_inventory(products_to_sell, product_prices)
            elif choice == '2':
                product_prices = self.set_prices(products_to_sell)
            elif choice == '3':
                self.design_store_layout()
            elif choice == '4':
                self.conduct_marketing_campaign()
            elif choice == '5':
                self.hire_employee()
            elif choice == '6':
                self.train_employee()
            elif choice == '7':
                self.simulate_day(product_prices)
            elif choice == '8':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice.")

if __name__ == '__main__':
    available_products = [
        {"name": "T-Shirt", "cost": 5},
        {"name": "Mug", "cost": 3},
        {"name": "Hat", "cost": 7},
        {"name": "Bag", "cost": 10},
    ]
    # Initialize with default prices
    product_prices = {product["name"]: product["cost"] * 2 for product in available_products}

    game = RetailSimulator()
    game.run_game(available_products, product_prices)
```