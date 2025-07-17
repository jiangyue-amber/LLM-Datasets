# Software Name: Sport_Event_Organizer
# Category: Sport_Game
# Description: The Sport Event Organizer software is designed to help organizers plan and manage sports events efficiently. It allows users to input event details such as date, time, location, and type of sport. The software then generates a schedule, assigns teams and referees, and provides real-time updates on game progress. Additionally, it has features to track participant registration, manage team rosters, and generate event reports.

import datetime

class SportEvent:
    def __init__(self, name, date, time, location, sport_type):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.sport_type = sport_type
        self.teams = []
        self.referees = []
        self.schedule = []
        self.participants = {} # {participant_name: team_name}
        self.game_progress = {} # {game_id: status} , status examples: "Scheduled", "In Progress", "Completed"

    def add_team(self, team_name):
        self.teams.append(team_name)

    def add_referee(self, referee_name):
        self.referees.append(referee_name)

    def create_schedule(self):
        # Placeholder for schedule generation logic
        # This would involve algorithms to pair teams, allocate referees, and set game times
        print("Generating schedule...")
        self.schedule = ["Game 1: Team A vs Team B - Referee: Referee 1", "Game 2: Team C vs Team D - Referee: Referee 2"] # Example
        print("Schedule generated.")

    def register_participant(self, participant_name, team_name):
         if team_name in self.teams:
            self.participants[participant_name] = team_name
         else:
            print(f"Error: Team '{team_name}' does not exist in the event.")

    def update_game_progress(self, game_id, status):
        self.game_progress[game_id] = status

    def generate_event_report(self):
        report = f"""
        Event Report: {self.name}
        Date: {self.date}
        Location: {self.location}
        Sport: {self.sport_type}

        Teams: {', '.join(self.teams)}
        Referees: {', '.join(self.referees)}
        Participants: {self.participants}
        Schedule: {self.schedule}
        Game Progress: {self.game_progress}
        """
        return report

class SportEventOrganizer:
    def __init__(self):
        self.events = {}

    def create_event(self, name, date, time, location, sport_type):
        if name not in self.events:
            self.events[name] = SportEvent(name, date, time, location, sport_type)
            print(f"Event '{name}' created successfully.")
        else:
            print(f"Error: Event '{name}' already exists.")

    def get_event(self, event_name):
        if event_name in self.events:
            return self.events[event_name]
        else:
            print(f"Error: Event '{event_name}' not found.")
            return None

    def delete_event(self, event_name):
        if event_name in self.events:
            del self.events[event_name]
            print(f"Event '{event_name}' deleted successfully.")
        else:
            print(f"Error: Event '{event_name}' not found.")

# Example Usage
if __name__ == "__main__":
    organizer = SportEventOrganizer()

    # Create an event
    organizer.create_event("Annual Soccer Tournament", datetime.date(2024, 12, 25), datetime.time(9, 0), "City Stadium", "Soccer")

    # Get the event
    event = organizer.get_event("Annual Soccer Tournament")

    if event:
        # Add teams and referees
        event.add_team("Team A")
        event.add_team("Team B")
        event.add_referee("Referee 1")
        event.add_referee("Referee 2")

        # Register participants
        event.register_participant("Alice", "Team A")
        event.register_participant("Bob", "Team B")

        # Generate a schedule
        event.create_schedule()

        # Update game progress
        event.update_game_progress("Game 1", "In Progress")

        # Generate a report
        report = event.generate_event_report()
        print(report)

    # Delete the event
    organizer.delete_event("Annual Soccer Tournament")