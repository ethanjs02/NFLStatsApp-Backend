import os
import requests
import certifi
from dotenv import load_dotenv

#Load environment variables
load_dotenv()

headers = {
        "x-rapidapi-key": os.getenv("API_KEY"),
        "x-rapidapi-host": "nfl-api-data.p.rapidapi.com"
    }       

def get_nfl_player_data(player_id, team_id, pos_id):
    if(pos_id == "8"):
        return get_qb_stats(player_id, team_id)
    elif(pos_id in ["1", "7"] ):
        return get_wr_stats(player_id, team_id)
    elif(pos_id == "9"):
        return get_rb_stats(player_id, team_id)
    elif(pos_id == "22"):
        return get_k_stats(player_id, team_id)
    

def get_qb_stats(player_id, team_id):
    None

def get_wr_stats(player_id, team_id):
    None

def get_rb_stats(player_id, team_id):
    None

def get_k_stats(player_id, team_id):
    None


def get_player_stats(player_id):
    None

def get_team_stats(team_id):
    None

def get_schedule(team_id):
    None    
    
    
    # url = "https://nfl-api-data.p.rapidapi.com/nfl-player-listing/v1/data"
    
    # # querystring = {"id":"15035","year":"2024"}
    # querystring = {"id": 25}
    
    # try:
    #     response = requests.get(url, headers=headers, params=querystring, verify=certifi.where())
    #     response.raise_for_status()
    #     return response.json()
    # except requests.RequestException as e:
    #     print(f"An error occurred: {e}")
    #     return None