import pandas as pd
# Comments used by me are more meant for self analyzing of my thought processs

# Attempt to read the CSV with error handling
try:
    df = pd.read_csv("YoutubeCommentsDataSet.csv", on_bad_lines='skip', encoding='utf-8')

    # If the file is empty
    if df.empty:
        print("The CSV file is empty or does not contain valid data.")
    else:
        print("CSV Loaded Successfully:")
        print(df.info())

except FileNotFoundError:
    print("Error: The file was not found. Check the file path.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except pd.errors.ParserError:
    print("Error: The file could not be parsed. Check for formatting issues.")
except Exception as e:
    print(f"Unexpected error: {e}")

# Handling Missing Data
# Fill missing comment values with a placeholder text
df['Comment'].fillna("No Comment", inplace=True)

# Verify missing values are handled
print(df.isnull().sum())

# Normalize text data
df['Comment'] = df['Comment'].str.lower().str.strip()

# Display sample data after normalization
print(df.head())
