# Software Name: QuickDelivery
# Category: Restaurants_Delivery
# Description: QuickDelivery is a Restaurants&Delivery software application that focuses on providing fast and efficient delivery services for users. It allows users to easily browse through a curated selection of popular dishes from local restaurants and place orders for delivery. Users can track the progress of their orders in real-time and benefit from seamless payment options.

import json
from datetime import datetime

class QuickDelivery:
    def __init__(self):
        self.restaurants = {}
        self.users = {}
        self.orders = {}
        self.next_order_id = 1

    def add_restaurant(self, restaurant_id, name, menu):
        """Adds a restaurant to the system."""
        if restaurant_id not in self.restaurants:
            self.restaurants[restaurant_id] = {"name": name, "menu": menu}
            return True
        else:
            return False

    def add_user(self, user_id, name, address, payment_info):
        """Adds a user to the system."""
        if user_id not in self.users:
            self.users[user_id] = {"name": name, "address": address, "payment_info": payment_info}
            return True
        else:
            return False

    def get_restaurant_menu(self, restaurant_id):
        """Retrieves the menu for a given restaurant."""
        if restaurant_id in self.restaurants:
            return self.restaurants[restaurant_id]["menu"]
        else:
            return None

    def place_order(self, user_id, restaurant_id, items):
        """Places an order for a user from a restaurant."""
        if user_id in self.users and restaurant_id in self.restaurants:
            order_id = self.next_order_id
            self.next_order_id += 1
            order = {
                "order_id": order_id,
                "user_id": user_id,
                "restaurant_id": restaurant_id,
                "items": items,
                "order_time": datetime.now().isoformat(),
                "status": "pending"
            }
            self.orders[order_id] = order
            return order_id
        else:
            return None

    def get_order_status(self, order_id):
        """Retrieves the status of an order."""
        if order_id in self.orders:
            return self.orders[order_id]["status"]
        else:
            return None

    def update_order_status(self, order_id, status):
        """Updates the status of an order."""
        if order_id in self.orders:
            self.orders[order_id]["status"] = status
            return True
        else:
            return False

    def get_user_orders(self, user_id):
        """Retrieves all orders for a given user."""
        user_orders = [order for order in self.orders.values() if order["user_id"] == user_id]
        return user_orders

    def get_all_restaurants(self):
        """Retrieves all restaurants in the system."""
        restaurant_list = []
        for restaurant_id, restaurant_data in self.restaurants.items():
            restaurant_list.append({"restaurant_id": restaurant_id, "name": restaurant_data["name"]})
        return restaurant_list

    def to_json(self):
        """Serializes the QuickDelivery object to a JSON string."""
        data = {
            "restaurants": self.restaurants,
            "users": self.users,
            "orders": self.orders,
            "next_order_id": self.next_order_id
        }
        return json.dumps(data, indent=4)

    def from_json(self, json_string):
        """Deserializes a QuickDelivery object from a JSON string."""
        data = json.loads(json_string)
        self.restaurants = data.get("restaurants", {})
        self.users = data.get("users", {})
        self.orders = data.get("orders", {})
        self.next_order_id = data.get("next_order_id", 1)

if __name__ == '__main__':
    # Example Usage
    delivery_service = QuickDelivery()

    # Add a restaurant
    menu1 = {"Pizza": 12.99, "Burger": 8.99, "Fries": 4.99}
    delivery_service.add_restaurant(1, "Pizza Palace", menu1)

    # Add a user
    delivery_service.add_user(101, "Alice Smith", "123 Main St", "Credit Card")

    # Get the restaurant menu
    menu = delivery_service.get_restaurant_menu(1)
    print("Menu:", menu)

    # Place an order
    order_id = delivery_service.place_order(101, 1, ["Pizza", "Fries"])
    print("Order ID:", order_id)

    # Get the order status
    status = delivery_service.get_order_status(order_id)
    print("Order Status:", status)

    # Update the order status
    delivery_service.update_order_status(order_id, "Delivered")
    print("Order Status Updated:", delivery_service.get_order_status(order_id))

    # Get user orders
    user_orders = delivery_service.get_user_orders(101)
    print("User Orders:", user_orders)

    # Get all restaurants
    all_restaurants = delivery_service.get_all_restaurants()
    print("All Restaurants:", all_restaurants)

    # Serialize to JSON
    json_data = delivery_service.to_json()
    print("JSON Data:\n", json_data)

    # Deserialize from JSON
    new_delivery_service = QuickDelivery()
    new_delivery_service.from_json(json_data)
    print("New Delivery Service Restaurants:", new_delivery_service.restaurants)