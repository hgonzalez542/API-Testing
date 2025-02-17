# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "WineQT.csv"  # Ensure the correct path
df = pd.read_csv(file_path)

# Display basic info
print("Dataset Information:\n")
print(df.info())

# Display first few rows
print("\nFirst 5 Rows of Dataset:\n", df.head())

# Summary statistics of all variables
print("\nSummary Statistics:\n", df.describe())

# Summary statistics for alcohol grouped by quality
grouped_stats = df.groupby("quality")["alcohol"].describe()
print("\nGrouped Statistics - Alcohol by Quality:\n", grouped_stats)

# Correlation matrix
correlation_matrix = df.corr()
print("\nCorrelation Matrix:\n", correlation_matrix)

# Set seaborn style
sns.set(style="whitegrid")

# Scatter plot: Alcohol vs. Quality
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="alcohol", y="quality", hue="quality", palette="coolwarm", alpha=0.7)
plt.title("Alcohol Content vs. Wine Quality")
plt.xlabel("Alcohol Content (%)")
plt.ylabel("Wine Quality")
plt.legend(title="Quality")
plt.show()

# Histogram of alcohol content
plt.figure(figsize=(10, 6))
sns.histplot(df["alcohol"], bins=20, kde=True, color="blue")
plt.title("Distribution of Alcohol Content in Wine")
plt.xlabel("Alcohol Content (%)")
plt.ylabel("Frequency")
plt.show()

# Heatmap of correlation matrix ~ Was not going to add cause of the complications but figure it out
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Heatmap of Feature Correlations")
plt.show()

# Question: How does sulphate concentration vary across different wine quality ratings?

# Boxplot of sulphates by wine quality
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="quality", y="sulphates", palette="coolwarm")
plt.title("Sulphates Concentration Across Wine Quality Ratings")
plt.xlabel("Wine Quality")
plt.ylabel("Sulphates Concentration")
plt.show()
