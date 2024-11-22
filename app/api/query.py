import os
import requests
import certifi
from dotenv import load_dotenv
from util.clean_data import clean_qb_data, clean_wr_data, clean_rb_data, clean_k_data

#Load environment variables
load_dotenv()

headers = {
        "x-rapidapi-key": os.getenv("API_KEY"),
        "x-rapidapi-host": "nfl-api-data.p.rapidapi.com"
    }       


def get_nfl_player_data(player_id, team_id, pos_id):
    if(pos_id == "8"):
        return get_qb_stats(player_id)
    elif(pos_id in ["1", "7"] ):
        return get_wr_stats(player_id, team_id)
    elif(pos_id in ["9", "10"]):
        return get_rb_stats(player_id, team_id)
    elif(pos_id == "22"):
        return get_k_stats(player_id)
    

def get_qb_stats(player_id):
    return clean_qb_data(get_player_stats(player_id))


def get_wr_stats(player_id, team_id):
    player_data = get_player_stats(player_id)
    team_data = get_team_stats(team_id)
    
    data = clean_wr_data(player_data, team_data)
        
    return data


def get_rb_stats(player_id, team_id):
    player_data = get_player_stats(player_id)
    team_data = get_team_stats(team_id)
    
    data = clean_rb_data(player_data, team_data)
        
    return data


def get_k_stats(player_id):
    return clean_k_data(get_player_stats(player_id))


def get_player_stats(player_id):
    url = "https://nfl-api-data.p.rapidapi.com/nfl-ath-statistics"

    querystring = {"year":"2024","id":f"{player_id}"}

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


def get_team_stats(team_id):
    url = "https://nfl-api-data.p.rapidapi.com/nfl-team-statistics"

    querystring = {"year":"2023","id":f"{team_id}"}
    
    response = requests.get(url, headers=headers, params=querystring)

    return response


def get_schedule(team_id):
    url = "https://nfl-api-data.p.rapidapi.com/nfl-team-schedule"

    querystring = {"id":f"{team_id}"}

    response = requests.get(url, headers=headers, params=querystring)

    return response