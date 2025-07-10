# Software Name: Quest_Companion
# Category: Role_Playing_Game
# Description: A software application that assists role-playing game players in completing quests by providing step-by-step guidance and tracking their progress. It offers quest-specific tips, strategies, and objectives, helping players navigate through challenging quests. The application allows users to mark completed objectives, track their overall progress, and view detailed quest information. A user-friendly interface with customizable categories and tags ensures easy organization and accessibility of quests.

import json

class Quest:
    def __init__(self, name, description, objectives, tips=None, strategies=None, tags=None, category=None):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.tips = tips or []
        self.strategies = strategies or []
        self.tags = tags or []
        self.category = category
        self.completed_objectives = [False] * len(objectives)

    def mark_objective_complete(self, objective_index):
        if 0 <= objective_index < len(self.objectives):
            self.completed_objectives[objective_index] = True
        else:
            print("Invalid objective index.")

    def get_progress(self):
        completed_count = sum(self.completed_objectives)
        return completed_count / len(self.objectives) if len(self.objectives) > 0 else 1.0

    def display_quest_details(self):
        print(f"Quest Name: {self.name}")
        print(f"Description: {self.description}")
        print("Objectives:")
        for i, objective in enumerate(self.objectives):
            status = "[X]" if self.completed_objectives[i] else "[ ]"
            print(f"  {i+1}. {status} {objective}")
        if self.tips:
            print("Tips:")
            for tip in self.tips:
                print(f"  - {tip}")
        if self.strategies:
            print("Strategies:")
            for strategy in self.strategies:
                print(f"  - {strategy}")
        if self.tags:
            print(f"Tags: {', '.join(self.tags)}")
        if self.category:
            print(f"Category: {self.category}")
        print(f"Progress: {self.get_progress()*100:.2f}%")

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'objectives': self.objectives,
            'tips': self.tips,
            'strategies': self.strategies,
            'tags': self.tags,
            'category': self.category,
            'completed_objectives': self.completed_objectives
        }

    @classmethod
    def from_dict(cls, data):
        quest = cls(
            name=data['name'],
            description=data['description'],
            objectives=data['objectives'],
            tips=data.get('tips', []),
            strategies=data.get('strategies', []),
            tags=data.get('tags', []),
            category=data.get('category'),
        )
        quest.completed_objectives = data.get('completed_objectives', [False] * len(quest.objectives))
        return quest


class QuestCompanion:
    def __init__(self):
        self.quests = {}

    def add_quest(self, quest):
        if quest.name not in self.quests:
            self.quests[quest.name] = quest
        else:
            print(f"Quest with name '{quest.name}' already exists.")

    def get_quest(self, quest_name):
        return self.quests.get(quest_name)

    def list_quests(self):
        if not self.quests:
            print("No quests available.")
        else:
            print("Available Quests:")
            for name in self.quests:
                print(f"- {name}")

    def delete_quest(self, quest_name):
        if quest_name in self.quests:
            del self.quests[quest_name]
            print(f"Quest '{quest_name}' deleted.")
        else:
            print(f"Quest '{quest_name}' not found.")

    def save_data(self, filename="quests.json"):
        data = {name: quest.to_dict() for name, quest in self.quests.items()}
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")

    def load_data(self, filename="quests.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.quests = {name: Quest.from_dict(quest_data) for name, quest_data in data.items()}
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty quest list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Starting with an empty quest list.")
            self.quests = {}

def main():
    companion = QuestCompanion()
    companion.load_data()

    while True:
        print("\nQuest Companion Menu:")
        print("1. Add Quest")
        print("2. View Quest")
        print("3. List Quests")
        print("4. Delete Quest")
        print("5. Mark Objective Complete")
        print("6. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter quest name: ")
            description = input("Enter quest description: ")
            objectives_str = input("Enter objectives (comma-separated): ")
            objectives = [obj.strip() for obj in objectives_str.split(",")]
            tips_str = input("Enter tips (comma-separated, or leave blank): ")
            tips = [tip.strip() for tip in tips_str.split(",")] if tips_str else []
            strategies_str = input("Enter strategies (comma-separated, or leave blank): ")
            strategies = [strategy.strip() for strategy in strategies_str.split(",")] if strategies_str else []
            tags_str = input("Enter tags (comma-separated, or leave blank): ")
            tags = [tag.strip() for tag in tags_str.split(",")] if tags_str else []
            category = input("Enter category (or leave blank): ") or None

            new_quest = Quest(name, description, objectives, tips, strategies, tags, category)
            companion.add_quest(new_quest)

        elif choice == '2':
            name = input("Enter quest name to view: ")
            quest = companion.get_quest(name)
            if quest:
                quest.display_quest_details()
            else:
                print("Quest not found.")

        elif choice == '3':
            companion.list_quests()

        elif choice == '4':
            name = input("Enter quest name to delete: ")
            companion.delete_quest(name)

        elif choice == '5':
             name = input("Enter quest name: ")
             quest = companion.get_quest(name)
             if quest:
                 quest.display_quest_details()
                 objective_index = int(input("Enter the number of the objective to mark complete: ")) - 1
                 quest.mark_objective_complete(objective_index)
                 print("Objective marked complete.")
                 quest.display_quest_details()

             else:
                 print("Quest not found")

        elif choice == '6':
            companion.save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()