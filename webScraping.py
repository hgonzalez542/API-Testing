import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage content
url = 'https://www.scrapethissite.com/pages/forms/'
response = requests.get(url)

response.raise_for_status()  # Ensure the request was successful, always do this to make sure step by step my code is processing/rendering

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Locate the table rows containing team data
team_rows = soup.find_all('tr', class_='team')

# Step 4: Extract data for the first 25 teams
data = []
for row in team_rows[:25]:
    cols = row.find_all('td')
    team_name = cols[0].text.strip() #Required Data
    year = cols[1].text.strip() # Required Data
    wins = cols[2].text.strip() # Required Data
    losses = cols[3].text.strip() # Required Data
    data.append([team_name, year, wins, losses])

# Step 5: Create a DataFrame **
df = pd.DataFrame(data, columns=['Team Name', 'Year', 'Wins', 'Losses'])

# Display the DataFrame
print(df)