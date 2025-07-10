# Software Name: Data_Integrity_Analyzer
# Category: Data
# Description: The Data Integrity Analyzer is a software application that analyzes and evaluates the integrity of data sets, helping users identify and address data quality issues. It performs checks on data consistency, accuracy, completeness, and validity, providing users with a comprehensive assessment of the overall data integrity.

import pandas as pd

class DataIntegrityAnalyzer:
    """
    Analyzes and evaluates the integrity of data sets, identifying data quality issues.
    """

    def __init__(self, data):
        """
        Initializes the DataIntegrityAnalyzer with the input data.

        Args:
            data: A pandas DataFrame containing the data to analyze.
        """
        self.data = data

    def check_consistency(self, column1, column2, condition):
        """
        Checks for data consistency between two columns based on a given condition.

        Args:
            column1 (str): The name of the first column.
            column2 (str): The name of the second column.
            condition (function): A function that takes two values (from column1 and column2)
                                  and returns True if the condition is met, False otherwise.

        Returns:
            pandas.DataFrame: A DataFrame containing the rows where the consistency check failed.
        """
        inconsistent_data = self.data[~self.data.apply(lambda row: condition(row[column1], row[column2]), axis=1)]
        return inconsistent_data

    def check_accuracy(self, column, expected_values, accuracy_threshold=0.95):
        """
        Checks the accuracy of a column by comparing its values to expected values.

        Args:
            column (str): The name of the column to check.
            expected_values (list): A list of expected values for the column.
            accuracy_threshold (float): Minimum acceptable percentage of matching values.

        Returns:
             float: Percentage of matching values in the given column against expected values.
        """
        valid_count = self.data[self.data[column].isin(expected_values)].shape[0]
        accuracy = valid_count / len(self.data)
        return accuracy

    def check_completeness(self, column):
        """
        Checks for missing values (NaN) in a specified column.

        Args:
            column (str): The name of the column to check for completeness.

        Returns:
            float: The percentage of missing values in the column.
        """
        missing_percentage = self.data[column].isnull().sum() / len(self.data)
        return missing_percentage

    def check_validity(self, column, validation_function):
        """
        Checks the validity of data in a column using a custom validation function.

        Args:
            column (str): The name of the column to validate.
            validation_function (function): A function that takes a value from the column and
                                           returns True if the value is valid, False otherwise.

        Returns:
            pandas.DataFrame: A DataFrame containing the rows where the validation check failed.
        """
        invalid_data = self.data[~self.data[column].apply(validation_function)]
        return invalid_data

    def analyze_data_integrity(self):
          """
          Executes all defined integrity checks and returns the results.  Placeholder to demonstrate function call. Users should define specific checks based on their data.

          Returns:
            dict: A dictionary containing the results of the data integrity checks.
          """
          results = {}
          # Example usage (replace with your specific checks)
          # results['consistency_check'] = self.check_consistency('columnA', 'columnB', lambda a, b: a <= b)
          # results['accuracy_check'] = self.check_accuracy('columnC', ['value1', 'value2'])
          # results['completeness_check'] = self.check_completeness('columnD')
          # results['validity_check'] = self.check_validity('columnE', lambda x: isinstance(x, int) and x > 0)
          return results
if __name__ == '__main__':
    # Example usage
    data = {'ID': [1, 2, 3, 4, 5],
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Age': [25, 30, None, 22, 35],
            'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']}
    df = pd.DataFrame(data)

    analyzer = DataIntegrityAnalyzer(df)

    # Completeness check on 'Age' column
    missing_age_percentage = analyzer.check_completeness('Age')
    print(f"Missing percentage in Age column: {missing_age_percentage}")

    # Validity check on 'Age' column (age should be a positive integer)
    invalid_age_data = analyzer.check_validity('Age', lambda x: isinstance(x, (int, float)) and (x > 0) if x is not None else True)
    print(f"Invalid Age data:\n{invalid_age_data}")