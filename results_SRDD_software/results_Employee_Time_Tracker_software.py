# Software Name: Employee_Time_Tracker
# Category: Business
# Description: Employee Time Tracker is a software application that allows businesses to track and manage employee working hours and attendance. It provides features for employees to log their working hours, record time off, and request leave. The application also offers functionalities for managers to approve and manage time off requests, monitor attendance and punctuality, and generate time and attendance reports.

```python
import datetime

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.time_logs = []
        self.time_off_requests = []

    def log_time(self, start_time, end_time, description=""):
        """Logs working hours for the employee."""
        self.time_logs.append({"start_time": start_time, "end_time": end_time, "description": description})

    def request_time_off(self, start_date, end_date, reason):
        """Requests time off for the employee."""
        self.time_off_requests.append({"start_date": start_date, "end_date": end_date, "reason": reason, "status": "pending"})

    def get_time_logs(self):
        """Returns the employee's time logs."""
        return self.time_logs

    def get_time_off_requests(self):
        """Returns the employee's time off requests."""
        return self.time_off_requests

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}"


class Manager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.managed_employees = []

    def add_employee(self, employee):
        """Adds an employee to the manager's list of managed employees."""
        self.managed_employees.append(employee)

    def approve_time_off(self, employee, request_index):
        """Approves a time off request for an employee."""
        if 0 <= request_index < len(employee.time_off_requests):
            employee.time_off_requests[request_index]["status"] = "approved"
        else:
            print("Invalid request index.")

    def reject_time_off(self, employee, request_index):
        """Rejects a time off request for an employee."""
        if 0 <= request_index < len(employee.time_off_requests):
            employee.time_off_requests[request_index]["status"] = "rejected"
        else:
            print("Invalid request index.")

    def generate_attendance_report(self, employee, start_date, end_date):
         """Generates an attendance report for an employee within a date range."""
         report = f"Attendance Report for {employee.name} ({employee.employee_id})\n"
         report += f"From: {start_date}, To: {end_date}\n\n"
         total_hours = 0
         for log in employee.time_logs:
              log_start_time = log['start_time']
              log_end_time = log['end_time']
              if start_date <= log_start_time.date() <= end_date:
                  duration = log_end_time - log_start_time
                  total_hours += duration.total_seconds() / 3600
                  report += f"Date: {log_start_time.date()}, Start Time: {log_start_time.time()}, End Time: {log_end_time.time()}, Description: {log['description']}\n"

         report += f"\nTotal Hours Worked: {total_hours:.2f}"
         return report

    def __str__(self):
        return f"Manager ID: {self.manager_id}, Name: {self.name}"


class TimeTracker:
    def __init__(self):
        self.employees = {}
        self.managers = {}

    def add_employee(self, employee):
        """Adds an employee to the time tracker system."""
        self.employees[employee.employee_id] = employee

    def add_manager(self, manager):
        """Adds a manager to the time tracker system."""
        self.managers[manager.manager_id] = manager

    def get_employee(self, employee_id):
        """Retrieves an employee by their ID."""
        return self.employees.get(employee_id)

    def get_manager(self, manager_id):
        """Retrieves a manager by their ID."""
        return self.managers.get(manager_id)
    def display_all_employees(self):
        """Displays details of all employees."""
        if not self.employees:
            print("No employees found.")
        else:
            print("List of Employees:")
            for employee_id, employee in self.employees.items():
                print(employee)

    def display_all_managers(self):
        """Displays details of all managers."""
        if not self.managers:
            print("No managers found.")
        else:
            print("List of Managers:")
            for manager_id, manager in self.managers.items():
                print(manager)


# Example Usage:
if __name__ == "__main__":
    # Initialize Time Tracker
    time_tracker = TimeTracker()

    # Create Employees
    employee1 = Employee("E001", "Alice Smith")
    employee2 = Employee("E002", "Bob Johnson")

    # Create Manager
    manager1 = Manager("M001", "Carol Williams")

    # Add Employees and Manager to Time Tracker
    time_tracker.add_employee(employee1)
    time_tracker.add_employee(employee2)
    time_tracker.add_manager(manager1)

    # Manager adds employees under her management
    manager1.add_employee(employee1)
    manager1.add_employee(employee2)

    # Employee logs time
    employee1.log_time(datetime.datetime(2024, 1, 22, 9, 0), datetime.datetime(2024, 1, 22, 17, 0), "Project work")
    employee2.log_time(datetime.datetime(2024, 1, 22, 8, 30), datetime.datetime(2024, 1, 22, 16, 30), "Meeting and coding")

    # Employee requests time off
    employee1.request_time_off(datetime.date(2024, 2, 15), datetime.date(2024, 2, 16), "Personal leave")

    # Manager approves time off
    manager1.approve_time_off(employee1, 0)

    # Generate attendance report
    report = manager1.generate_attendance_report(employee1, datetime.date(2024, 1, 1), datetime.date(2024, 1, 31))
    print(report)

    #Display all employees and managers
    time_tracker.display_all_employees()
    time_tracker.display_all_managers()

    # Accessing Employee and Manager objects through TimeTracker
    retrieved_employee = time_tracker.get_employee("E001")
    if retrieved_employee:
        print(f"Retrieved Employee: {retrieved_employee.name}")

    retrieved_manager = time_tracker.get_manager("M001")
    if retrieved_manager:
        print(f"Retrieved Manager: {retrieved_manager.name}")

    # Example of Time Off request being rejected.
    employee2.request_time_off(datetime.date(2024, 3, 1), datetime.date(2024, 3, 5), "Vacation")
    manager1.reject_time_off(employee2, 0)
    print(employee2.get_time_off_requests())
```