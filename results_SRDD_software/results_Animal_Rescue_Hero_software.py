# Software Name: Animal_Rescue_Hero
# Category: Simulation_Game
# Description: Animal Rescue Hero is a simulation game software where players can rescue and care for abandoned and injured animals. Manage the operations of the rescue center, including fundraising, volunteer coordination, and community outreach. Make critical decisions to ensure the well-being and happiness of the animals under your care.

import random

class Animal:
    def __init__(self, name, species, health=100, happiness=50):
        self.name = name
        self.species = species
        self.health = health
        self.happiness = happiness

    def __str__(self):
        return f"{self.name} ({self.species}) - Health: {self.health}, Happiness: {self.happiness}"

    def heal(self, amount):
        self.health = min(100, self.health + amount)
        print(f"{self.name} healed. Health is now {self.health}")

    def play(self, duration):
        self.happiness = min(100, self.happiness + duration * 5)
        print(f"{self.name} played. Happiness is now {self.happiness}")

    def feed(self, food_quality):
        if food_quality == "good":
            self.health = min(100, self.health + 10)
            self.happiness = min(100, self.happiness + 5)
            print(f"{self.name} fed good quality food. Health: {self.health}, Happiness: {self.happiness}")
        elif food_quality == "bad":
            self.health = max(0, self.health - 5)
            self.happiness = max(0, self.happiness - 2)
            print(f"{self.name} fed bad quality food. Health: {self.health}, Happiness: {self.happiness}")


class RescueCenter:
    def __init__(self, name, funds=1000, reputation=50):
        self.name = name
        self.funds = funds
        self.reputation = reputation
        self.animals = []
        self.volunteers = 0

    def __str__(self):
        return f"{self.name} - Funds: {self.funds}, Reputation: {self.reputation}, Animals: {len(self.animals)}, Volunteers: {self.volunteers}"

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} added to the rescue center.")

    def remove_animal(self, animal):
        self.animals.remove(animal)
        print(f"{animal.name} removed from the rescue center.")

    def show_animals(self):
        if not self.animals:
            print("No animals in the rescue center.")
            return

        print("Animals in the rescue center:")
        for animal in self.animals:
            print(animal)

    def add_funds(self, amount):
        self.funds += amount
        print(f"Funds increased by {amount}. Total funds: {self.funds}")

    def deduct_funds(self, amount):
        if self.funds >= amount:
            self.funds -= amount
            print(f"Funds decreased by {amount}. Total funds: {self.funds}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def improve_reputation(self, amount):
          self.reputation = min(100, self.reputation + amount)
          print(f"Reputation increased by {amount}. Total reputation: {self.reputation}")

    def degrade_reputation(self,amount):
          self.reputation = max(0, self.reputation - amount)
          print(f"Reputation decreased by {amount}. Total reputation: {self.reputation}")

    def adopt_animal(self, animal):
        if animal in self.animals:
            if self.reputation >= 70:
               print(f"{animal.name} has been successfully adopted!")
               self.remove_animal(animal)
               self.improve_reputation(5)
            else:
                print("Reputation is too low for adoption. Improve it by fundraising or community outreach.")
        else:
            print(f"{animal.name} is not in the rescue center.")

    def recruit_volunteers(self, number):
        cost = number * 50
        if self.deduct_funds(cost):
            self.volunteers += number
            print(f"Recruited {number} volunteers. Total volunteers: {self.volunteers}")

    def community_outreach(self):
        cost = 200
        if self.deduct_funds(cost):
            self.improve_reputation(10)
            print("Community outreach successful. Reputation increased.")


def main():
    print("Welcome to Animal Rescue Hero!")
    center_name = input("Enter the name of your rescue center: ")
    rescue_center = RescueCenter(center_name)

    while True:
        print("\n--- Menu ---")
        print("1. Add Animal")
        print("2. Show Animals")
        print("3. Heal Animal")
        print("4. Play with Animal")
        print("5. Feed Animal")
        print("6. Adopt Animal")
        print("7. Fundraise")
        print("8. Recruit Volunteers")
        print("9. Community Outreach")
        print("10. View Rescue Center Status")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter animal name: ")
            species = input("Enter animal species: ")
            rescue_center.add_animal(Animal(name, species))

        elif choice == '2':
            rescue_center.show_animals()

        elif choice == '3':
             rescue_center.show_animals()
             if rescue_center.animals:
                 animal_name = input("Enter the name of the animal to heal: ")
                 animal_to_heal = next((animal for animal in rescue_center.animals if animal.name == animal_name), None)
                 if animal_to_heal:
                     heal_amount = int(input("Enter heal amount: "))
                     if rescue_center.deduct_funds(heal_amount * 2):
                        animal_to_heal.heal(heal_amount)
                     else:
                        print("Not enough fund to proceed.")
                 else:
                     print("Animal not found.")

        elif choice == '4':
            rescue_center.show_animals()
            if rescue_center.animals:
                animal_name = input("Enter the name of the animal to play with: ")
                animal_to_play = next((animal for animal in rescue_center.animals if animal.name == animal_name), None)
                if animal_to_play:
                    play_duration = int(input("Enter play duration: "))
                    animal_to_play.play(play_duration)
                else:
                    print("Animal not found.")

        elif choice == '5':
            rescue_center.show_animals()
            if rescue_center.animals:
                animal_name = input("Enter the name of the animal to feed: ")
                animal_to_feed = next((animal for animal in rescue_center.animals if animal.name == animal_name), None)
                if animal_to_feed:
                    food_quality = input("Enter food quality (good/bad): ")
                    animal_to_feed.feed(food_quality)
                else:
                    print("Animal not found.")

        elif choice == '6':
            rescue_center.show_animals()
            if rescue_center.animals:
                animal_name = input("Enter the name of the animal to adopt: ")
                animal_to_adopt = next((animal for animal in rescue_center.animals if animal.name == animal_name), None)
                if animal_to_adopt:
                    rescue_center.adopt_animal(animal_to_adopt)
                else:
                    print("Animal not found.")

        elif choice == '7':
            amount = int(input("Enter fundraising amount: "))
            rescue_center.add_funds(amount)
            rescue_center.improve_reputation(amount // 100)

        elif choice == '8':
            number = int(input("Enter number of volunteers to recruit: "))
            rescue_center.recruit_volunteers(number)

        elif choice == '9':
            rescue_center.community_outreach()

        elif choice == '10':
            print(rescue_center)

        elif choice == '11':
            print("Thank you for playing Animal Rescue Hero!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()