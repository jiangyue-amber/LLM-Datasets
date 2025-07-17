# Software Name: Customer_Feedback_Tracker
# Category: Business
# Description: Customer Feedback Tracker is a business software application that allows businesses to collect and analyze customer feedback. The software provides a user-friendly interface for businesses to create and manage feedback forms, distribute them to customers via email or social media platforms, and collect responses. It also offers data visualization tools to analyze feedback data, identify trends and patterns, and generate actionable insights for improving products and services.

import pandas as pd
import matplotlib.pyplot as plt

class CustomerFeedbackTracker:
    def __init__(self):
        self.feedback_forms = {}
        self.feedback_data = pd.DataFrame()

    def create_feedback_form(self, form_name, questions):
        """
        Creates a new feedback form.

        Args:
            form_name (str): The name of the feedback form.
            questions (list): A list of questions for the feedback form.
        """
        self.feedback_forms[form_name] = questions
        print(f"Feedback form '{form_name}' created successfully.")

    def distribute_feedback_form(self, form_name, customers, distribution_channel="email"):
        """
        Distributes a feedback form to a list of customers.

        Args:
            form_name (str): The name of the feedback form to distribute.
            customers (list): A list of customer email addresses or social media handles.
            distribution_channel (str): The channel to distribute the form (default: "email").
        """
        if form_name not in self.feedback_forms:
            print(f"Error: Feedback form '{form_name}' not found.")
            return

        print(f"Distributing feedback form '{form_name}' to {len(customers)} customers via {distribution_channel}.")
        # Simulate sending the form (replace with actual email/social media integration)
        for customer in customers:
            print(f"Sending form to: {customer}")

    def collect_feedback(self, form_name, customer_id, responses):
        """
        Collects feedback data from a customer.

        Args:
            form_name (str): The name of the feedback form.
            customer_id (str): The unique identifier for the customer.
            responses (dict): A dictionary of responses to the feedback form questions.
                             Keys should match the questions in the form.
        """
        if form_name not in self.feedback_forms:
            print(f"Error: Feedback form '{form_name}' not found.")
            return

        form_questions = self.feedback_forms[form_name]
        if not all(q in responses for q in form_questions):
            print("Error: Incomplete feedback. Please answer all questions.")
            return

        new_feedback = {'form_name': form_name, 'customer_id': customer_id}
        new_feedback.update(responses)  # Add responses to the dictionary
        self.feedback_data = pd.concat([self.feedback_data, pd.DataFrame([new_feedback])], ignore_index=True)

        print(f"Feedback from customer '{customer_id}' for form '{form_name}' collected.")

    def analyze_feedback(self, question):
        """
        Analyzes the collected feedback data for a specific question.

        Args:
            question (str): The question to analyze.

        Returns:
            pandas.Series: A series containing the value counts for the question.
        """
        if question not in self.feedback_data.columns:
            print(f"Error: Question '{question}' not found in feedback data.")
            return None

        return self.feedback_data[question].value_counts()

    def visualize_feedback(self, question, chart_type="bar"):
        """
        Visualizes the collected feedback data for a specific question using matplotlib.

        Args:
            question (str): The question to visualize.
            chart_type (str): The type of chart to use (default: "bar"). Options: "bar", "pie".
        """
        analysis = self.analyze_feedback(question)
        if analysis is None:
            return

        if chart_type == "bar":
            analysis.plot(kind="bar")
            plt.title(f"Feedback Analysis: {question}")
            plt.xlabel("Response")
            plt.ylabel("Frequency")
            plt.show()
        elif chart_type == "pie":
            analysis.plot(kind="pie", autopct='%1.1f%%')
            plt.title(f"Feedback Analysis: {question}")
            plt.ylabel("")  # Remove default ylabel
            plt.show()
        else:
            print("Error: Invalid chart type. Choose 'bar' or 'pie'.")

    def generate_report(self, filename="feedback_report.txt"):
        """
        Generates a text report summarizing the collected feedback.

        Args:
            filename (str): The name of the file to save the report to (default: "feedback_report.txt").
        """
        with open(filename, "w") as f:
            f.write("Customer Feedback Report\n")
            f.write("------------------------\n")
            if self.feedback_data.empty:
                f.write("No feedback data available.\n")
            else:
                for form_name in self.feedback_forms:
                    f.write(f"\nFeedback Form: {form_name}\n")
                    f.write("------------------------\n")
                    for question in self.feedback_forms[form_name]:
                        f.write(f"\nQuestion: {question}\n")
                        analysis = self.analyze_feedback(question)
                        if analysis is not None:
                            f.write(analysis.to_string() + "\n")
                        else:
                            f.write("No data for this question.\n")
        print(f"Feedback report generated and saved to '{filename}'.")


if __name__ == '__main__':
    # Example Usage
    tracker = CustomerFeedbackTracker()

    # Create a feedback form
    questions = ["How satisfied are you with our product?", "How likely are you to recommend us?", "Any suggestions for improvement?"]
    tracker.create_feedback_form("Product Satisfaction Survey", questions)

    # Distribute the form to customers
    customers = ["customer1@example.com", "customer2@example.com", "customer3@example.com"]
    tracker.distribute_feedback_form("Product Satisfaction Survey", customers)

    # Collect feedback
    tracker.collect_feedback(
        "Product Satisfaction Survey",
        "customer1@example.com",
        {"How satisfied are you with our product?": "Very satisfied",
         "How likely are you to recommend us?": "Likely",
         "Any suggestions for improvement?": "None"}
    )

    tracker.collect_feedback(
        "Product Satisfaction Survey",
        "customer2@example.com",
        {"How satisfied are you with our product?": "Satisfied",
         "How likely are you to recommend us?": "Neutral",
         "Any suggestions for improvement?": "Improve customer support"}
    )

    tracker.collect_feedback(
        "Product Satisfaction Survey",
        "customer3@example.com",
        {"How satisfied are you with our product?": "Very satisfied",
         "How likely are you to recommend us?": "Very likely",
         "Any suggestions for improvement?": "Add more features"}
    )

    # Analyze feedback
    satisfaction_analysis = tracker.analyze_feedback("How satisfied are you with our product?")
    print("\nSatisfaction Analysis:")
    print(satisfaction_analysis)

    # Visualize feedback
    tracker.visualize_feedback("How satisfied are you with our product?", chart_type="pie")

    # Generate a report
    tracker.generate_report()