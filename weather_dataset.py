import pandas as pd

# Load the dataset
df = pd.read_csv('weather-data.csv')

# Inspect the first few rows of the dataset
print(df.head())
# Get basic information about the dataset
print(df.info())

# Get summary statistics for numerical columns
print(df.describe())
# Check for missing values
print(df.isnull().sum())

# Example: Fill missing values with the mean of the column
df.fillna(df.mean(), inplace=True)

# Alternatively, you can drop rows with missing values
# df.dropna(inplace=True)
