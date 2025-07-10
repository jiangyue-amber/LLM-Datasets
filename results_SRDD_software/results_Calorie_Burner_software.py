# Software Name: Calorie_Burner
# Category: Health_Fitness
# Description: Calorie Burner is a software application that allows users to track and monitor the number of calories burned during physical activities and workouts. Users can select from a list of common activities or input custom activities to calculate the calories burned. The app provides real-time tracking of calories burned and displays an overview of the user

class CalorieBurner:
    def __init__(self):
        self.activity_calories = {
            "running": 10,  # Calories per minute
            "walking": 5,
            "swimming": 8,
            "cycling": 7,
        }
        self.tracked_calories = 0

    def select_activity(self):
        print("Available activities:")
        for activity in self.activity_calories:
            print(f"- {activity}")
        activity = input("Enter activity name (or 'custom'): ").lower()
        return activity

    def get_activity_duration(self):
        while True:
            try:
                duration = float(input("Enter duration in minutes: "))
                if duration > 0:
                    return duration
                else:
                    print("Duration must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def calculate_calories(self, activity, duration):
        if activity in self.activity_calories:
            calories_per_minute = self.activity_calories[activity]
            calories_burned = calories_per_minute * duration
            return calories_burned
        else:
            print("Activity not found.")
            return None

    def custom_activity(self):
      activity_name = input("Enter custom activity name: ")
      while True:
          try:
              calories_per_minute = float(input("Enter calories burned per minute: "))
              if calories_per_minute > 0:
                  self.activity_calories[activity_name] = calories_per_minute
                  break
              else:
                print("Calories burned per minute must be positive.")
          except ValueError:
            print("Invalid input. Please enter a number.")
      duration = self.get_activity_duration()
      calories_burned = self.activity_calories[activity_name] * duration
      return calories_burned

    def track_activity(self):
        activity = self.select_activity()

        if activity == "custom":
            calories_burned = self.custom_activity()
            if calories_burned is not None:
              self.tracked_calories += calories_burned
              print(f"Calories burned: {calories_burned:.2f}")
        elif activity in self.activity_calories:
            duration = self.get_activity_duration()
            calories_burned = self.calculate_calories(activity, duration)
            if calories_burned is not None:
                self.tracked_calories += calories_burned
                print(f"Calories burned: {calories_burned:.2f}")
        else:
            print("Invalid activity.")

    def display_overview(self):
        print(f"Total calories burned: {self.tracked_calories:.2f}")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Track activity")
            print("2. Display overview")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.track_activity()
            elif choice == "2":
                self.display_overview()
            elif choice == "3":
                print("Exiting Calorie Burner.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    calorie_burner = CalorieBurner()
    calorie_burner.run()