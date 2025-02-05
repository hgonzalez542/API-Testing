import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"

    try:
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            return data.get("fact", "No fact found.")
        else:
            return f"Error {response.status_code}: {response.text}"

    except requests.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    cat_fact = get_cat_fact()
    print("🐱 Cat Fact:", cat_fact)
