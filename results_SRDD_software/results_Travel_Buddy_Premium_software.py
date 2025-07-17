# Software Name: Travel_Buddy_Premium
# Category: Travel
# Description: b
import datetime
import random

class TravelBuddyPremium:
    def __init__(self):
        self.attractions_data = {}
        self.accommodations_data = {}
        self.local_experiences_data = {}
        self.transportation_data = {}
        self.weather_data = {}
        self.event_data = {}
        self.user_preferences = {}

    def load_data(self, attractions, accommodations, local_experiences, transportation, weather, events):
        self.attractions_data = attractions
        self.accommodations_data = accommodations
        self.local_experiences_data = local_experiences
        self.transportation_data = transportation
        self.weather_data = weather
        self.event_data = events

    def get_user_preferences(self):
        self.user_preferences['destination'] = input("Enter your destination: ")
        self.user_preferences['dates'] = input("Enter your travel dates (YYYY-MM-DD to YYYY-MM-DD): ")
        self.user_preferences['budget'] = input("Enter your budget: ")
        self.user_preferences['interests'] = input("Enter your interests (comma-separated): ").split(',')
        self.user_preferences['themes'] = input("Enter your desired themes (comma-separated, e.g., culinary, adventure, cultural): ").split(',')
        self.user_preferences['accommodation_type'] = input("Enter preferred accommodation type (hotel, hostel, Airbnb): ")
        return self.user_preferences
    
    def filter_by_destination(self, data, destination):
        return {k: v for k, v in data.items() if v.get('location') == destination}
    
    def filter_by_interests(self, data, interests):
        filtered_data = {}
        for key, value in data.items():
            if any(interest.strip().lower() in [tag.lower() for tag in value.get('tags', [])] for interest in interests):
                filtered_data[key] = value
        return filtered_data

    def filter_by_themes(self, data, themes):
        filtered_data = {}
        for key, value in data.items():
            if any(theme.strip().lower() in [tag.lower() for tag in value.get('themes', [])] for theme in themes):
                filtered_data[key] = value
        return filtered_data

    def filter_by_budget(self, data, budget):
        try:
            budget_value = float(budget)
            filtered_data = {}
            for key, value in data.items():
                if 'price' in value and isinstance(value['price'], (int, float)) and value['price'] <= budget_value:
                    filtered_data[key] = value
            return filtered_data
        except ValueError:
            print("Invalid budget format. Please enter a number.")
            return data

    def get_weather_forecast(self, destination, date):
        if destination in self.weather_data:
            return self.weather_data[destination].get(date, "Weather data not available for this date.")
        else:
            return "Weather data not available for this destination."

    def get_local_events(self, destination, date):
        if destination in self.event_data:
            return self.event_data[destination].get(date, [])
        else:
            return []

    def generate_itinerary(self, user_preferences):
        destination = user_preferences['destination']
        interests = [i.strip() for i in user_preferences['interests']]
        themes = [t.strip() for t in user_preferences['themes']]
        budget = user_preferences['budget']

        attractions = self.filter_by_destination(self.attractions_data, destination)
        accommodations = self.filter_by_destination(self.accommodations_data, destination)
        local_experiences = self.filter_by_destination(self.local_experiences_data, destination)

        attractions = self.filter_by_interests(attractions, interests)
        accommodations = self.filter_by_interests(accommodations, interests)
        local_experiences = self.filter_by_interests(local_experiences, interests)

        attractions = self.filter_by_themes(attractions, themes)
        accommodations = self.filter_by_themes(accommodations, themes)
        local_experiences = self.filter_by_themes(local_experiences, themes)

        attractions = self.filter_by_budget(attractions, budget)
        accommodations = self.filter_by_budget(accommodations, budget)
        local_experiences = self.filter_by_budget(local_experiences, budget)

        start_date_str, end_date_str = user_preferences['dates'].split(" to ")
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
        num_days = (end_date - start_date).days + 1

        itinerary = {}
        current_date = start_date

        for day in range(num_days):
            date_str = current_date.strftime("%Y-%m-%d")
            itinerary[date_str] = {
                'weather': self.get_weather_forecast(destination, date_str),
                'events': self.get_local_events(destination, date_str),
                'attractions': random.sample(list(attractions.keys()), min(2, len(attractions))),
                'accommodation': random.choice(list(accommodations.keys())) if accommodations else None,
                'local_experience': random.choice(list(local_experiences.keys())) if local_experiences else None
            }
            current_date += datetime.timedelta(days=1)

        return itinerary

    def display_itinerary(self, itinerary):
        for date, details in itinerary.items():
            print(f"Date: {date}")
            print(f"  Weather: {details['weather']}")
            print(f"  Events: {details['events']}")
            print(f"  Attractions: {details['attractions']}")
            print(f"  Accommodation: {details['accommodation']}")
            print(f"  Local Experience: {details['local_experience']}")
            print("-" * 20)

if __name__ == '__main__':
    # Sample data (replace with actual data loading)
    attractions_data = {
        "Eiffel Tower": {"location": "Paris", "tags": ["landmark", "cultural"], "themes": ["cultural"], "price": 20},
        "Louvre Museum": {"location": "Paris", "tags": ["museum", "art", "cultural"], "themes": ["cultural"], "price": 17},
        "Great Wall": {"location": "Beijing", "tags": ["landmark", "historical"], "themes":["cultural"], "price": 15},
        "Forbidden City": {"location": "Beijing", "tags": ["historical", "cultural"], "themes": ["cultural"], "price": 12},
        "Himalayas": {"location": "Nepal", "tags": ["mountain", "adventure"], "themes": ["adventure"], "price": 0},
        "Annapurna Trek": {"location": "Nepal", "tags": ["trekking", "adventure"], "themes": ["adventure"], "price": 50}
    }

    accommodations_data = {
        "Hotel Plaza": {"location": "Paris", "tags": ["hotel", "luxury"], "themes": [], "price": 300},
        "Airbnb Paris Center": {"location": "Paris", "tags": ["airbnb", "apartment"], "themes": [], "price": 150},
        "Beijing Hotel": {"location": "Beijing", "tags": ["hotel", "comfortable"], "themes": [], "price": 100},
        "Nepal Tea House": {"location": "Nepal", "tags": ["tea house", "mountain"], "themes": ["adventure"], "price": 30}
    }

    local_experiences_data = {
        "Paris Cooking Class": {"location": "Paris", "tags": ["cooking", "culinary"], "themes": ["culinary"], "price": 80},
        "Beijing Duck Dinner": {"location": "Beijing", "tags": ["food", "culinary"], "themes": ["culinary"], "price": 60},
        "Mount Everest Flight": {"location": "Nepal", "tags": ["flight", "adventure"], "themes": ["adventure"], "price": 200}
    }

    transportation_data = {}
    weather_data = {
        "Paris": {"2024-01-01": "Sunny", "2024-01-02": "Cloudy"},
        "Beijing": {"2024-01-01": "Snowy", "2024-01-02": "Hazy"},
        "Nepal": {"2024-01-01": "Clear", "2024-01-02": "Windy"}
    }
    event_data = {
        "Paris": {"2024-01-01": ["New Year's Day Parade"], "2024-01-02": []},
        "Beijing": {"2024-01-01": [], "2024-01-02": []},
        "Nepal": {"2024-01-01": [], "2024-01-02": []}
    }
    
    travel_buddy = TravelBuddyPremium()
    travel_buddy.load_data(attractions_data, accommodations_data, local_experiences_data, transportation_data, weather_data, event_data)

    user_preferences = travel_buddy.get_user_preferences()
    itinerary = travel_buddy.generate_itinerary(user_preferences)
    travel_buddy.display_itinerary(itinerary)