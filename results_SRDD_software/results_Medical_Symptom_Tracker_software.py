# Software Name: Medical_Symptom_Tracker
# Category: Medical
# Description: A software application that allows users to track and monitor their symptoms over time, enabling them to identify patterns and potential triggers. Users can log symptoms, severity, duration, and associated factors such as food, stress, or environment to gain insights into their health and make informed decisions.

import datetime

class SymptomTracker:
    def __init__(self):
        self.entries = []

    def add_entry(self, symptom, severity, duration, factors, date=None):
        """
        Adds a new symptom entry to the tracker.

        Args:
            symptom (str): The name of the symptom.
            severity (int): The severity of the symptom (e.g., 1-10).
            duration (str): The duration of the symptom (e.g., "1 hour", "all day").
            factors (list): A list of associated factors (e.g., ["food", "stress"]).
            date (datetime.date, optional): The date of the symptom. Defaults to today's date.
        """
        if date is None:
            date = datetime.date.today()
        entry = {
            "date": date,
            "symptom": symptom,
            "severity": severity,
            "duration": duration,
            "factors": factors,
        }
        self.entries.append(entry)

    def get_entries_by_date(self, date):
        """
        Retrieves all symptom entries for a specific date.

        Args:
            date (datetime.date): The date to retrieve entries for.

        Returns:
            list: A list of symptom entries for the specified date.
        """
        return [entry for entry in self.entries if entry["date"] == date]

    def get_entries_by_symptom(self, symptom):
          """
          Retrieves all symptom entries for a specific symptom.
          Args:
              symptom (str): The symptom to retrieve entries for.
          Returns:
              list: A list of symptom entries for the specified symptom.
          """
          return [entry for entry in self.entries if entry["symptom"] == symptom]

    def get_entries_by_factor(self, factor):
        """
        Retrieves all symptom entries associated with a specific factor.

        Args:
            factor (str): The factor to retrieve entries for.

        Returns:
            list: A list of symptom entries associated with the specified factor.
        """
        return [entry for entry in self.entries if factor in entry["factors"]]


    def get_all_entries(self):
        """
        Retrieves all symptom entries.

        Returns:
            list: A list of all symptom entries.
        """
        return self.entries

    def display_entry(self, entry):
        """
        Displays a single symptom entry in a user-friendly format.

        Args:
            entry (dict): The symptom entry to display.
        """
        print(f"Date: {entry['date']}")
        print(f"Symptom: {entry['symptom']}")
        print(f"Severity: {entry['severity']}")
        print(f"Duration: {entry['duration']}")
        print(f"Factors: {', '.join(entry['factors'])}")
        print("-" * 20)

    def display_entries(self, entries):
        """
        Displays a list of symptom entries.

        Args:
            entries (list): A list of symptom entries to display.
        """
        if not entries:
            print("No entries found.")
            return

        for entry in entries:
            self.display_entry(entry)

    def run(self):
        """
        Runs the symptom tracker application.
        """
        while True:
            print("\nMedical Symptom Tracker")
            print("1. Add Symptom Entry")
            print("2. View Entries by Date")
            print("3. View Entries by Symptom")
            print("4. View Entries by Factor")
            print("5. View All Entries")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                symptom = input("Enter symptom: ")
                severity = int(input("Enter severity (1-10): "))
                duration = input("Enter duration: ")
                factors_str = input("Enter factors (comma-separated): ")
                factors = [f.strip() for f in factors_str.split(",")]
                self.add_entry(symptom, severity, duration, factors)
                print("Entry added successfully!")

            elif choice == "2":
                date_str = input("Enter date (YYYY-MM-DD): ")
                try:
                    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                    entries = self.get_entries_by_date(date)
                    self.display_entries(entries)
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

            elif choice == "3":
                symptom = input("Enter symptom: ")
                entries = self.get_entries_by_symptom(symptom)
                self.display_entries(entries)

            elif choice == "4":
                factor = input("Enter factor: ")
                entries = self.get_entries_by_factor(factor)
                self.display_entries(entries)

            elif choice == "5":
                entries = self.get_all_entries()
                self.display_entries(entries)

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    tracker = SymptomTracker()
    tracker.run()