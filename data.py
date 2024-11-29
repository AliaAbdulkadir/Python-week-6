# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
# Try to load the dataset and handle errors
try:
    # Load dataset (You can replace this with the path to your own CSV file)
    df = pd.read_csv('your_dataset.csv')

    # Display the first few rows to inspect the data
    print("First few rows of the dataset:")
    print(df.head())

    # Explore the structure of the dataset
    print("\nData Types and Missing Values:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing values in the dataset:")
    print(df.isnull().sum())
    
    # Clean the dataset (Fill missing values with the mean for numerical columns)
    df.fillna(df.mean(), inplace=True)
    print("\nMissing values after filling with mean:")
    print(df.isnull().sum())

except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
# Basic statistics for numerical columns
print("\nBasic Statistics:")
print(df.describe())

# Perform groupings and compute the mean for a categorical column (e.g., 'species')
if 'species' in df.columns:  # Check if 'species' column exists for the example
    print("\nAverage values grouped by 'species':")
    print(df.groupby('species').mean())

# Task 3: Data Visualization
# Set the style for the plots using Seaborn
sns.set(style="whitegrid")

# 1. Line Chart - Showing trends over time (replace 'date_column' and 'value_column' with actual columns)
plt.figure(figsize=(10, 6))
df['date_column'] = pd.to_datetime(df['date_column'])  # Ensure the date column is in datetime format
plt.plot(df['date_column'], df['value_column'], label='Value over Time', color='blue')
plt.title('Trend of Value Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Chart - Comparing numerical value across categories (e.g., Average Petal Length per Species)
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.show()

# 3. Histogram - Distribution of a numerical column (e.g., Petal Length)
plt.figure(figsize=(8, 6))
sns.histplot(df['petal_length'], bins=20, kde=True, color='green')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot - Relationship between two numerical columns (e.g., Sepal Length vs. Petal Length)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend(title='Species')
plt.show()

# Additional Observations or Findings
print("\nAnalysis Observations:")
# You can add your own insights based on the data analysis and visualizations above.

