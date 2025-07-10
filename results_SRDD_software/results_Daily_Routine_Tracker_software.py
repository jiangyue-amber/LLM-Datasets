# Software Name: Daily_Routine_Tracker
# Category: Personalisation
# Description: A personalization software application that helps users track and optimize their daily routines and habits. Users can input their routines and the software provides personalized recommendations for improvements to help users optimize their daily schedules. The software also offers features like progress tracking and reminders to help users stay consistent with their routines.

import datetime

class DailyRoutineTracker:
    def __init__(self):
        self.routines = {}

    def add_routine(self, routine_name, tasks, optimal_time=None):
        """
        Adds a new routine to the tracker.

        Args:
            routine_name (str): The name of the routine (e.g., "Morning Routine").
            tasks (list): A list of tasks in the routine.
            optimal_time (int, optional): The ideal duration for the routine in minutes. Defaults to None.
        """
        self.routines[routine_name] = {"tasks": tasks, "optimal_time": optimal_time, "history": []}
        print(f"Routine '{routine_name}' added successfully.")

    def view_routine(self, routine_name):
        """
        Displays the tasks associated with a specific routine.

        Args:
            routine_name (str): The name of the routine.
        """
        if routine_name in self.routines:
            print(f"Routine: {routine_name}")
            print("Tasks:")
            for i, task in enumerate(self.routines[routine_name]["tasks"]):
                print(f"{i+1}. {task}")
            if self.routines[routine_name]["optimal_time"]:
                print(f"Optimal Time: {self.routines[routine_name]['optimal_time']} minutes")
        else:
            print(f"Routine '{routine_name}' not found.")

    def record_completion(self, routine_name, actual_time):
        """
        Records the completion of a routine and the time taken.

        Args:
            routine_name (str): The name of the routine.
            actual_time (int): The actual time taken to complete the routine in minutes.
        """
        if routine_name in self.routines:
            timestamp = datetime.datetime.now()
            self.routines[routine_name]["history"].append({"timestamp": timestamp, "actual_time": actual_time})
            print(f"Routine '{routine_name}' completion recorded at {timestamp} (Time taken: {actual_time} minutes).")
        else:
            print(f"Routine '{routine_name}' not found.")

    def get_average_completion_time(self, routine_name):
        """
        Calculates the average completion time for a routine based on historical data.

        Args:
            routine_name (str): The name of the routine.

        Returns:
            float: The average completion time in minutes, or None if no data is available.
        """
        if routine_name in self.routines:
            history = self.routines[routine_name]["history"]
            if history:
                total_time = sum(entry["actual_time"] for entry in history)
                average_time = total_time / len(history)
                return average_time
            else:
                print(f"No completion history found for routine '{routine_name}'.")
                return None
        else:
            print(f"Routine '{routine_name}' not found.")
            return None

    def suggest_improvements(self, routine_name):
        """
        Provides personalized recommendations for improving a routine.

        Args:
            routine_name (str): The name of the routine.
        """
        if routine_name in self.routines:
            average_time = self.get_average_completion_time(routine_name)
            optimal_time = self.routines[routine_name]["optimal_time"]

            if average_time is not None and optimal_time is not None:
                if average_time > optimal_time:
                    difference = average_time - optimal_time
                    print(f"Your average completion time for '{routine_name}' is {average_time:.2f} minutes, which is {difference:.2f} minutes longer than the optimal time of {optimal_time} minutes.")
                    print("Suggestions:")
                    print("- Analyze each task in the routine to identify time-consuming steps.")
                    print("- Consider breaking down larger tasks into smaller, more manageable steps.")
                    print("- Eliminate distractions during the routine.")
                    print("- Experiment with different task order to find a more efficient flow.")
                elif average_time < optimal_time:
                    difference = optimal_time - average_time
                    print(f"Your average completion time for '{routine_name}' is {average_time:.2f} minutes, which is {difference:.2f} minutes shorter than the optimal time of {optimal_time} minutes.")
                    print("Suggestions:")
                    print("- You might want to incorporate a short relaxing activity into your routine, such as stretching.")
                    print("- Use the extra time to do some extra prep.")

                else:
                    print(f"Your average completion time for '{routine_name}' is in line with the optimal time.")

            else:
                print("Not enough data to provide personalized suggestions. Please record more completions of this routine.")
        else:
            print(f"Routine '{routine_name}' not found.")

    def set_reminder(self, routine_name, time):
        """
        Sets a reminder for the given routine. This is a placeholder, as actual reminder implementation depends on system capabilities.

        Args:
            routine_name (str): The name of the routine.
            time (str): The time to set the reminder (e.g., "07:00").
        """
        if routine_name in self.routines:
            print(f"Reminder set for '{routine_name}' at {time}.")
            # In a real application, this would involve using a scheduling library or system service
        else:
            print(f"Routine '{routine_name}' not found.")

# Example usage:
if __name__ == "__main__":
    tracker = DailyRoutineTracker()

    tracker.add_routine("Morning Routine", ["Wake up", "Brush teeth", "Drink water", "Exercise"], optimal_time=30)
    tracker.add_routine("Evening Routine", ["Dinner", "Read a book", "Plan next day", "Sleep"], optimal_time=60)

    tracker.view_routine("Morning Routine")

    tracker.record_completion("Morning Routine", 35)
    tracker.record_completion("Morning Routine", 28)
    tracker.record_completion("Morning Routine", 40)

    avg_time = tracker.get_average_completion_time("Morning Routine")
    if avg_time:
        print(f"Average completion time for Morning Routine: {avg_time:.2f} minutes")

    tracker.suggest_improvements("Morning Routine")

    tracker.set_reminder("Evening Routine", "21:00")