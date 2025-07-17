# Software Name: Data_Integrity_Analyzer
# Category: Data
# Description: The Data Integrity Analyzer is a software application that analyzes and evaluates the integrity of data sets, helping users identify and address data quality issues. It performs checks on data consistency, accuracy, completeness, and validity, providing users with a comprehensive assessment of the overall data integrity.

import pandas as pd

class DataIntegrityAnalyzer:
    def __init__(self, data):
        """
        Initializes the DataIntegrityAnalyzer with a pandas DataFrame.

        Args:
            data (pd.DataFrame): The data to be analyzed.
        """
        self.data = data

    def check_missing_values(self):
        """
        Checks for missing values in the DataFrame.

        Returns:
            pd.DataFrame: A DataFrame showing the number and percentage of missing values for each column.
        """
        missing_counts = self.data.isnull().sum()
        missing_percentages = (missing_counts / len(self.data)) * 100
        missing_data = pd.DataFrame({'Missing Count': missing_counts, 'Missing Percentage': missing_percentages})
        return missing_data.sort_values(by='Missing Count', ascending=False)

    def check_duplicate_rows(self):
        """
        Checks for duplicate rows in the DataFrame.

        Returns:
            int: The number of duplicate rows.
        """
        return self.data.duplicated().sum()

    def check_data_types(self):
        """
        Checks the data types of each column in the DataFrame.

        Returns:
            pd.Series: A Series showing the data type of each column.
        """
        return self.data.dtypes

    def check_value_ranges(self, column, min_value=None, max_value=None):
        """
        Checks if values in a specified column fall within a given range.

        Args:
            column (str): The name of the column to check.
            min_value (float or int, optional): The minimum allowed value. Defaults to None.
            max_value (float or int, optional): The maximum allowed value. Defaults to None.

        Returns:
            pd.Series: A boolean Series indicating whether each value is within the specified range.
        """
        if column not in self.data.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")

        if min_value is not None and max_value is not None:
            return (self.data[column] >= min_value) & (self.data[column] <= max_value)
        elif min_value is not None:
            return self.data[column] >= min_value
        elif max_value is not None:
            return self.data[column] <= max_value
        else:
            raise ValueError("Either min_value or max_value must be provided.")

    def check_categorical_values(self, column, allowed_values):
        """
        Checks if categorical values in a specified column are within a set of allowed values.

        Args:
            column (str): The name of the column to check.
            allowed_values (list): A list of allowed values for the column.

        Returns:
            pd.Series: A boolean Series indicating whether each value is in the allowed values.
        """
        if column not in self.data.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        return self.data[column].isin(allowed_values)

    def run_all_checks(self, column_ranges=None, column_categories=None):
        """
        Runs all defined checks and returns a dictionary of results.

        Args:
            column_ranges (dict, optional): A dictionary specifying column ranges (column_name: (min_value, max_value)). Defaults to None.
            column_categories (dict, optional): A dictionary specifying column allowed categories (column_name: [allowed_values]). Defaults to None.

        Returns:
            dict: A dictionary containing the results of all checks.
        """
        results = {}
        results['missing_values'] = self.check_missing_values()
        results['duplicate_rows'] = self.check_duplicate_rows()
        results['data_types'] = self.check_data_types()

        if column_ranges:
            results['value_range_checks'] = {}
            for column, (min_value, max_value) in column_ranges.items():
                try:
                    results['value_range_checks'][column] = self.check_value_ranges(column, min_value, max_value)
                except ValueError as e:
                    results['value_range_checks'][column] = str(e)
        if column_categories:
            results['categorical_checks'] = {}
            for column, allowed_values in column_categories.items():
                try:
                    results['categorical_checks'][column] = self.check_categorical_values(column, allowed_values)
                except ValueError as e:
                    results['categorical_checks'][column] = str(e)

        return results

if __name__ == '__main__':
    # Example Usage
    data = {'col1': [1, 2, 3, 4, 5, None],
            'col2': ['A', 'B', 'A', 'C', 'B', 'A'],
            'col3': [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]}
    df = pd.DataFrame(data)

    analyzer = DataIntegrityAnalyzer(df)

    # Run specific checks
    missing_data = analyzer.check_missing_values()
    duplicate_count = analyzer.check_duplicate_rows()
    data_types = analyzer.check_data_types()
    col1_range_check = analyzer.check_value_ranges('col1', min_value=1, max_value=5)
    col2_category_check = analyzer.check_categorical_values('col2', ['A', 'B', 'C'])

    print("Missing Data:\n", missing_data)
    print("\nDuplicate Row Count:", duplicate_count)
    print("\nData Types:\n", data_types)
    print("\nCol1 Range Check (1-5):\n", col1_range_check)
    print("\nCol2 Category Check (A, B, C):\n", col2_category_check)

    #Run all checks
    all_results = analyzer.run_all_checks(column_ranges={'col3': (15.0, 55.0)}, column_categories={'col2': ['A', 'B']})
    print("\nAll Results:\n", all_results)