# Software Name: MiniLab_Assistant
# Category: Science
# Description: A software application that assists science students in conducting experiments in a virtual laboratory setting, offering simulated experiments, tutorials, and real-time feedback.

import random
import time

class VirtualLab:
    def __init__(self, name, description, experiments):
        self.name = name
        self.description = description
        self.experiments = experiments

    def display_lab_info(self):
        print(f"Welcome to the {self.name} Virtual Lab!")
        print(self.description)
        print("\nAvailable Experiments:")
        for i, experiment in enumerate(self.experiments):
            print(f"{i+1}. {experiment.name}")

    def select_experiment(self):
        while True:
            try:
                choice = int(input("Enter the number of the experiment you want to perform (or 0 to exit): "))
                if choice == 0:
                    return None
                if 1 <= choice <= len(self.experiments):
                    return self.experiments[choice - 1]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class Experiment:
    def __init__(self, name, description, procedure, expected_result, tutorial=None):
        self.name = name
        self.description = description
        self.procedure = procedure
        self.expected_result = expected_result
        self.tutorial = tutorial

    def display_experiment_info(self):
        print(f"\nExperiment: {self.name}")
        print(self.description)

    def run_tutorial(self):
        if self.tutorial:
            print("\nTutorial:")
            for step in self.tutorial:
                print(step)
                time.sleep(1) # Simulate time passing
        else:
            print("No tutorial available for this experiment.")

    def perform_experiment(self):
        print("\nPerforming the experiment...")
        for step in self.procedure:
            print(step)
            time.sleep(2) # Simulate experiment steps

        # Simulate results with some randomness
        success = random.random() > 0.2  # 80% chance of success
        if success:
            print("\nExperiment completed successfully!")
            print(f"Expected Result: {self.expected_result}")
        else:
            print("\nExperiment failed. Please review the procedure and try again.")

class LabAssistant:
    def __init__(self, lab):
        self.lab = lab

    def run(self):
        self.lab.display_lab_info()
        while True:
            experiment = self.lab.select_experiment()
            if experiment is None:
                print("Exiting the virtual lab.")
                break

            experiment.display_experiment_info()
            
            tutorial_choice = input("Do you want to view the tutorial? (y/n): ").lower()
            if tutorial_choice == 'y':
                experiment.run_tutorial()

            perform_choice = input("Do you want to perform the experiment? (y/n): ").lower()
            if perform_choice == 'y':
                experiment.perform_experiment()
            else:
                print("Returning to experiment selection.")


if __name__ == "__main__":
    # Define some example experiments
    experiment1 = Experiment(
        name="Titration Experiment",
        description="Determine the concentration of an acid using titration.",
        procedure=[
            "1. Prepare the burette with the titrant (NaOH).",
            "2. Add a known volume of the analyte (HCl) to a flask.",
            "3. Add an indicator to the flask.",
            "4. Slowly add titrant to the flask while stirring.",
            "5. Stop adding titrant when the indicator changes color.",
            "6. Record the volume of titrant added.",
            "7. Calculate the concentration of the analyte."
        ],
        expected_result="The concentration of HCl is approximately 0.1 M.",
        tutorial=[
            "Step 1: Make sure the burette is clean.",
            "Step 2: Fill the burette with NaOH solution.",
            "Step 3: Carefully read the initial volume of NaOH.",
        ]
    )

    experiment2 = Experiment(
        name="Simple Circuit Experiment",
        description="Build a simple circuit with a battery, resistor, and LED.",
        procedure=[
            "1. Connect the positive terminal of the battery to the resistor.",
            "2. Connect the other end of the resistor to the positive (longer) leg of the LED.",
            "3. Connect the negative (shorter) leg of the LED to the negative terminal of the battery.",
            "4. Observe if the LED lights up."
        ],
        expected_result="The LED should light up.",
        tutorial=[
            "Step 1: Make sure the battery is properly connected.",
            "Step 2: Check the resistor value to ensure it is appropriate for the LED.",
            "Step 3: Verify the LED polarity."
        ]
    )

    # Create a virtual lab
    chemistry_lab = VirtualLab(
        name="Virtual Chemistry Lab",
        description="Welcome to the virtual chemistry lab! Here, you can perform various chemistry experiments in a safe and controlled environment.",
        experiments=[experiment1, experiment2]
    )

    # Create a lab assistant and run the simulation
    assistant = LabAssistant(chemistry_lab)
    assistant.run()