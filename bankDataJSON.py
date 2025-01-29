import json
import pandas as pd

# Define file path
file_path = "banksdata.json"  # Change to your JSON file name

try:
    # Open and load JSON file
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Display JSON content
    print("JSON Loaded Successfully:")
    print(json.dumps(data, indent=4))  # Pretty-print JSON

    # Convert JSON to DataFrame (if applicable)
    if isinstance(data, list):  # Ensure JSON is a list of dictionaries
        df = pd.DataFrame(data)
        print("\nDataFrame Head:")
        print(df.head())
    else:
        print("\nJSON data is not a list of dictionaries, cannot convert to DataFrame.")

except FileNotFoundError:
    print("Error: The file was not found. Check the file path.")
except json.JSONDecodeError:
    print("Error: The file is not a valid JSON format.")
except Exception as e:
    print(f"Unexpected error: {e}")