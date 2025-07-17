# Software Name: Culture_Facts
# Category: Culture
# Description: Culture Facts is a software application that provides users with interesting and educational facts about different cultures from around the world.

import json
import random

class CultureFacts:
    def __init__(self, data_file="culture_facts.json"):
        self.data_file = data_file
        self.facts = self.load_facts()

    def load_facts(self):
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save_facts(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.facts, f, indent=4)

    def add_fact(self, culture, fact):
        if culture not in self.facts:
            self.facts[culture] = []
        self.facts[culture].append(fact)
        self.save_facts()

    def get_random_fact(self, culture=None):
        if not self.facts:
            return "No culture facts available."

        if culture:
            if culture in self.facts:
                if self.facts[culture]:
                    return random.choice(self.facts[culture])
                else:
                    return f"No facts available for {culture}."
            else:
                return f"Culture '{culture}' not found."
        else:
            all_facts = []
            for culture_name, facts_list in self.facts.items():
                all_facts.extend(facts_list)
            if all_facts:
                return random.choice(all_facts)
            else:
                return "No culture facts available."

    def get_cultures(self):
        return list(self.facts.keys())

    def remove_fact(self, culture, fact_index):
        if culture in self.facts:
            if 0 <= fact_index < len(self.facts[culture]):
                del self.facts[culture][fact_index]
                self.save_facts()
                return True
            else:
                return False
        else:
            return False

# Example Usage (This won't be executed when you just return the class definition)
if __name__ == '__main__':
    culture_facts = CultureFacts()

    # Add some facts
    culture_facts.add_fact("Japanese", "Eating noodles noisily is considered polite in Japan.")
    culture_facts.add_fact("Indian", "The cow is considered a sacred animal in Hinduism.")
    culture_facts.add_fact("Italian", "Italians use a lot of hand gestures when they speak.")

    # Get a random fact
    print("Random fact:", culture_facts.get_random_fact())

    # Get a random fact about a specific culture
    print("Random Japanese fact:", culture_facts.get_random_fact("Japanese"))

    #List all cultures
    print("Available cultures: ", culture_facts.get_cultures())

    #Remove a fact
    if culture_facts.remove_fact("Japanese", 0):
        print("Fact removed successfully.")
    else:
        print("Failed to remove fact.")

    # Get a random fact
    print("Random fact:", culture_facts.get_random_fact())