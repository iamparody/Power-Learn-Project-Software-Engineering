1. Setup and Data Loading
 Copyimport pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nData types and missing values:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

2. Data Cleaning
 Copy# Drop rows with missing values (if any)
df_clean = df.dropna()
print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())

3. Basic Data Analysis
 Copy# Basic statistics
print("\nBasic statistics:")
print(df_clean.describe())

# Group by species and compute mean
print("\nMean of numerical columns by species:")
print(df_clean.groupby('species').mean())

4. Data Visualization
 Copy# Set style for plots
sns.set_style("whitegrid")

# Line chart (example: sepal length trend by index)
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_clean, x=df_clean.index, y='sepal length (cm)', hue='species')
plt.title("Trend of Sepal Length by Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend(title='Species')
plt.show()

# Bar chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(data=df_clean, x='species', y='petal length (cm)', ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# Histogram: Distribution of sepal width
plt.figure(figsize=(8, 5))
sns.histplot(data=df_clean, x='sepal width (cm)', kde=True, hue='species')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Sepal length vs. Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_clean, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()

5. Error Handling (Example)
 Copytry:
    # Attempt to load a CSV file (replace with your file path)
    custom_df = pd.read_csv("your_dataset.csv")
    print("\nCustom dataset loaded successfully!")
except FileNotFoundError:
    print("\nError: File not found. Please check the file path.")
except Exception as e:
    print(f"\nAn error occurred: {e}")

#6. Observations and Findings

# Sepal Length vs. Petal Length: There is a clear positive correlation between sepal length and petal length, especially for the species virginica and versicolor.
# Average Petal Length: Setosa has the smallest average petal length, while virginica has the largest.
# Sepal Width Distribution: Setosa has a wider sepal width compared to the other species.
