import os
import requests
import certifi
from dotenv import load_dotenv

#Load environment variables
load_dotenv()

def get_nfl_team_data():
    url = "https://nfl-api-data.p.rapidapi.com/nfl-team-listing/v1/data"

    headers = {
        "x-rapidapi-key": os.getenv("API_KEY"),
        "x-rapidapi-host": "nfl-api-data.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers, verify=certifi.where())
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    data = get_nfl_team_data()
    if data:
        print(data)
    else:
        print("Failed to retrieve NFL team data.")