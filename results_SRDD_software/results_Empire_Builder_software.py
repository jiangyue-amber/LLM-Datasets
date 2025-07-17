# Software Name: Empire_Builder
# Category: Strategy_Game
# Description: Empire Builder is a strategy game software application where players take on the role of an emperor and must strategically build and expand their own empire. Players will need to allocate resources, construct buildings, train armies, and engage in battles with other empires or AI opponents. The game offers a variety of terrain types, unit types, and strategic challenges to test players

import random

class Empire:
    def __init__(self, name, resources=1000, land=100, army_size=50):
        self.name = name
        self.resources = resources
        self.land = land
        self.army_size = army_size

    def __str__(self):
        return f"Empire: {self.name}\nResources: {self.resources}\nLand: {self.land}\nArmy Size: {self.army_size}"

    def allocate_resources(self, amount):
        if amount > self.resources:
            print("Not enough resources!")
            return False
        self.resources -= amount
        return True

    def construct_building(self, building_type):
        if building_type == "farm":
            cost = 200
            if self.allocate_resources(cost):
                self.land += 10
                print("Farm constructed!")
                return True
            else:
                return False
        elif building_type == "barracks":
            cost = 300
            if self.allocate_resources(cost):
                print("Barracks constructed!")
                return True
            else:
                return False
        else:
            print("Unknown building type.")
            return False

    def train_army(self, num_units):
        if not hasattr(self, 'has_barracks') and not self.construct_building("barracks"):
            print("You need a barracks to train units.")
            self.has_barracks = True # Set it to True after attempt to build to prevent infinite recursion
            return False
        cost_per_unit = 50
        total_cost = num_units * cost_per_unit
        if self.allocate_resources(total_cost):
            self.army_size += num_units
            print(f"Trained {num_units} units!")
            return True
        else:
            return False

    def engage_battle(self, other_empire):
        print(f"{self.name} is engaging in battle with {other_empire.name}!")
        self_strength = self.army_size * random.uniform(0.8, 1.2)
        other_strength = other_empire.army_size * random.uniform(0.8, 1.2)

        if self_strength > other_strength:
            print(f"{self.name} won the battle!")
            land_taken = min(other_empire.land // 4, self.land // 4)
            self.land += land_taken
            other_empire.land -= land_taken
            army_loss = int(self.army_size * random.uniform(0.1, 0.3))
            self.army_size -= army_loss
            other_army_loss = int(other_empire.army_size * random.uniform(0.3, 0.6))
            other_empire.army_size -= other_army_loss
            self.resources += 100
            other_empire.resources = max(0, other_empire.resources - 50) #reduce resources
            print(f"{self.name} lost {army_loss} units and gained {land_taken} land.")
            print(f"{other_empire.name} lost {other_army_loss} units and {land_taken} land.")
        elif self_strength < other_strength:
            print(f"{other_empire.name} won the battle!")
            land_taken = min(self.land // 4, other_empire.land // 4)
            other_empire.land += land_taken
            self.land -= land_taken
            army_loss = int(self.army_size * random.uniform(0.3, 0.6))
            self.army_size -= army_loss
            other_army_loss = int(other_empire.army_size * random.uniform(0.1, 0.3))
            other_empire.army_size -= other_army_loss
            other_empire.resources += 100
            self.resources = max(0, self.resources - 50) #reduce resources
            print(f"{self.name} lost {army_loss} units and {land_taken} land.")
            print(f"{other_empire.name} lost {other_army_loss} units and gained {land_taken} land.")
        else:
            print("The battle was a draw!")
            army_loss1 = int(self.army_size * random.uniform(0.2, 0.4))
            self.army_size -= army_loss1
            army_loss2 = int(other_empire.army_size * random.uniform(0.2, 0.4))
            other_empire.army_size -= army_loss2
            print(f"Both Empires lost units. {self.name} lost {army_loss1}, and {other_empire.name} lost {army_loss2}")

def main():
    player_name = input("Enter your empire's name: ")
    player_empire = Empire(player_name)
    ai_empire = Empire("AI Empire", resources=800, land=120, army_size=60)

    while True:
        print("\n--- Empire Builder ---")
        print(player_empire)
        print("\nChoose an action:")
        print("1. Construct building (farm/barracks)")
        print("2. Train army")
        print("3. Engage in battle with AI Empire")
        print("4. View AI Empire")
        print("5. End turn")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            building_type = input("Enter building type (farm/barracks): ")
            player_empire.construct_building(building_type)
        elif choice == "2":
            num_units = int(input("Enter number of units to train: "))
            player_empire.train_army(num_units)
        elif choice == "3":
            player_empire.engage_battle(ai_empire)
        elif choice == "4":
            print(ai_empire)
        elif choice == "5":
            #AI Turn
            if ai_empire.resources < 500:
               ai_empire.construct_building("farm")
            elif ai_empire.army_size < player_empire.army_size:
                ai_empire.train_army(20)
            elif random.random() < 0.3:
                ai_empire.engage_battle(player_empire)
            else:
                ai_empire.train_army(10)


        elif choice == "6":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()