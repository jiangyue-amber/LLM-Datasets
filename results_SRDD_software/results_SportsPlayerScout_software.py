# Software Name: SportsPlayerScout
# Category: Sports
# Description: A software application that allows scouts and coaches to analyze and track the performance of individual athletes in various sports. Users can input performance data such as speed, agility, accuracy, and endurance for each athlete. The software generates detailed reports and provides insights on the strengths and weaknesses of the athletes. It also allows users to compare the performance of multiple athletes side by side, helping scouts and coaches make informed decisions on player recruitment and team composition.

class Athlete:
    def __init__(self, name, sport, speed=0, agility=0, accuracy=0, endurance=0):
        self.name = name
        self.sport = sport
        self.speed = speed
        self.agility = agility
        self.accuracy = accuracy
        self.endurance = endurance

    def __str__(self):
        return f"Name: {self.name}, Sport: {self.sport}, Speed: {self.speed}, Agility: {self.agility}, Accuracy: {self.accuracy}, Endurance: {self.endurance}"

    def update_performance(self, speed=None, agility=None, accuracy=None, endurance=None):
        if speed is not None:
            self.speed = speed
        if agility is not None:
            self.agility = agility
        if accuracy is not None:
            self.accuracy = accuracy
        if endurance is not None:
            self.endurance = endurance

    def get_performance_summary(self):
        return {
            "Speed": self.speed,
            "Agility": self.agility,
            "Accuracy": self.accuracy,
            "Endurance": self.endurance
        }


class SportsPlayerScout:
    def __init__(self):
        self.athletes = {}

    def add_athlete(self, athlete):
        if athlete.name not in self.athletes:
            self.athletes[athlete.name] = athlete
            return True
        else:
            return False

    def get_athlete(self, name):
        return self.athletes.get(name)

    def update_athlete_performance(self, name, speed=None, agility=None, accuracy=None, endurance=None):
         athlete = self.get_athlete(name)
         if athlete:
             athlete.update_performance(speed, agility, accuracy, endurance)
             return True
         else:
             return False

    def generate_report(self, name):
        athlete = self.get_athlete(name)
        if athlete:
            return str(athlete)
        else:
            return "Athlete not found."

    def compare_athletes(self, names):
        if not all(name in self.athletes for name in names):
            return "One or more athletes not found."

        comparison_data = {}
        for name in names:
            comparison_data[name] = self.athletes[name].get_performance_summary()

        return comparison_data


if __name__ == '__main__':
    # Example usage:
    scout = SportsPlayerScout()

    # Add athletes
    athlete1 = Athlete("John Doe", "Basketball", speed=8, agility=9, accuracy=7, endurance=6)
    athlete2 = Athlete("Jane Smith", "Soccer", speed=7, agility=8, accuracy=9, endurance=8)

    scout.add_athlete(athlete1)
    scout.add_athlete(athlete2)

    # Get athlete report
    print(scout.generate_report("John Doe"))

    # Update athlete performance
    scout.update_athlete_performance("John Doe", accuracy=8)
    print(scout.generate_report("John Doe"))

    # Compare athletes
    comparison = scout.compare_athletes(["John Doe", "Jane Smith"])
    print(comparison)

    #Try to add existing athlete
    athlete3 = Athlete("John Doe", "Basketball", speed=5, agility=5, accuracy=5, endurance=5) # different attributes
    print(scout.add_athlete(athlete3))

    #Try to get report for non-existing athlete
    print(scout.generate_report("Non Existing Athlete"))

    #Try to compare non existing athletes
    print(scout.compare_athletes(["John Doe", "Non Existing Athlete"]))