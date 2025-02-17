# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('heightsWeight.csv')  # Ensure the file is in the working directory

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Calculate summary statistics
summary_stats = df.describe().loc[['mean', 'min', 'max', 'std']]
print("\nSummary Statistics:")
print(summary_stats)

# Create a scatter plot of Height vs. Weight
plt.figure(figsize=(10, 6))
plt.scatter(df['Height'], df['Weight'], alpha=0.5, color='blue', edgecolors='k')
plt.title('Height vs. Weight')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.grid(True)
plt.show()
