# Software Name: FlexiSchedule
# Category: Schedule
# Description: FlexiSchedule is a schedule software application that allows users to create flexible schedules based on their availability and preferences. It provides a user-friendly interface where users can input their tasks, set priorities, and allocate time slots. FlexiSchedule also offers customization options, allowing users to define their work hours, breaks, and recurring activities. The software provides reminders and notifications to keep users on track with their schedule. Additionally, FlexiSchedule offers a visual representation of the schedule, allowing users to easily manage their tasks and optimize their productivity.

import datetime
import time
import tkinter as tk
from tkinter import ttk, messagebox

class FlexiSchedule:
    def __init__(self, master):
        self.master = master
        master.title("FlexiSchedule")

        self.tasks = []
        self.preferences = {
            'work_hours_start': 9,
            'work_hours_end': 17,
            'break_duration': 30,
            'recurring_activities': []
        }

        # UI elements
        self.task_label = ttk.Label(master, text="Task:")
        self.task_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.task_entry = ttk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        self.priority_label = ttk.Label(master, text="Priority (1-High, 3-Low):")
        self.priority_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.priority_var = tk.IntVar(value=2)
        self.priority_scale = tk.Scale(master, from_=1, to=3, orient=tk.HORIZONTAL, variable=self.priority_var)
        self.priority_scale.grid(row=1, column=1, padx=5, pady=5)

        self.duration_label = ttk.Label(master, text="Duration (minutes):")
        self.duration_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.duration_entry = ttk.Entry(master, width=10)
        self.duration_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.duration_entry.insert(0, "60") # Default duration

        self.add_button = ttk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.schedule_button = ttk.Button(master, text="Generate Schedule", command=self.generate_schedule)
        self.schedule_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.task_listbox = tk.Listbox(master, width=50, height=10)
        self.task_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.preferences_button = ttk.Button(master, text="Preferences", command=self.open_preferences_window)
        self.preferences_button.grid(row=6, column=0, columnspan=2, pady=10)

    def add_task(self):
        task_name = self.task_entry.get()
        priority = self.priority_var.get()
        try:
            duration = int(self.duration_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid duration. Please enter a number.")
            return

        if task_name:
            self.tasks.append({'name': task_name, 'priority': priority, 'duration': duration})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task name.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['name']} - Priority: {task['priority']} - Duration: {task['duration']} minutes")

    def generate_schedule(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks to schedule.")
            return

        # Basic scheduling logic (prioritize by priority, then add in order)
        self.tasks.sort(key=lambda x: x['priority'])  # Sort tasks by priority (lower is higher)

        schedule = []
        current_time = datetime.datetime.now().replace(hour=self.preferences['work_hours_start'], minute=0, second=0, microsecond=0)
        end_time = datetime.datetime.now().replace(hour=self.preferences['work_hours_end'], minute=0, second=0, microsecond=0)

        for task in self.tasks:
            task_duration_minutes = task['duration']
            task_end_time = current_time + datetime.timedelta(minutes=task_duration_minutes)

            if task_end_time <= end_time:
                schedule.append({'task': task['name'], 'start': current_time.strftime("%H:%M"), 'end': task_end_time.strftime("%H:%M")})
                current_time = task_end_time
            else:
                messagebox.showinfo("Info", f"Not enough time to schedule all tasks within work hours. Task '{task['name']}' skipped.")
                break  # Stop scheduling if we run out of time

        # Display the schedule (can be improved for better UI)
        schedule_text = "Schedule:\n"
        for item in schedule:
            schedule_text += f"{item['start']} - {item['end']}: {item['task']}\n"
        messagebox.showinfo("Schedule", schedule_text)

    def open_preferences_window(self):
        preferences_window = tk.Toplevel(self.master)
        preferences_window.title("Preferences")

        # Work Hours
        work_hours_label = ttk.Label(preferences_window, text="Work Hours (HH):")
        work_hours_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        start_hour_label = ttk.Label(preferences_window, text="Start:")
        start_hour_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.start_hour_entry = ttk.Entry(preferences_window, width=5)
        self.start_hour_entry.grid(row=0, column=2, padx=5, pady=5)
        self.start_hour_entry.insert(0, str(self.preferences['work_hours_start']))

        end_hour_label = ttk.Label(preferences_window, text="End:")
        end_hour_label.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        self.end_hour_entry = ttk.Entry(preferences_window, width=5)
        self.end_hour_entry.grid(row=0, column=4, padx=5, pady=5)
        self.end_hour_entry.insert(0, str(self.preferences['work_hours_end']))

        # Break Duration
        break_duration_label = ttk.Label(preferences_window, text="Break Duration (minutes):")
        break_duration_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.break_duration_entry = ttk.Entry(preferences_window, width=5)
        self.break_duration_entry.grid(row=1, column=1, padx=5, pady=5)
        self.break_duration_entry.insert(0, str(self.preferences['break_duration']))

        save_button = ttk.Button(preferences_window, text="Save Preferences", command=lambda: self.save_preferences(preferences_window))
        save_button.grid(row=2, column=0, columnspan=5, pady=10)

    def save_preferences(self, preferences_window):
        try:
            start_hour = int(self.start_hour_entry.get())
            end_hour = int(self.end_hour_entry.get())
            break_duration = int(self.break_duration_entry.get())

            if 0 <= start_hour <= 23 and 0 <= end_hour <= 23 and start_hour < end_hour and break_duration >= 0:
                self.preferences['work_hours_start'] = start_hour
                self.preferences['work_hours_end'] = end_hour
                self.preferences['break_duration'] = break_duration
                messagebox.showinfo("Success", "Preferences saved.")
                preferences_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid preference values. Please check the input.")

        except ValueError:
            messagebox.showerror("Error", "Invalid preference values. Please enter numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    flexi_schedule = FlexiSchedule(root)
    root.mainloop()