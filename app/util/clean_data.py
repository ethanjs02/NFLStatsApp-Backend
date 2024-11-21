
def clean_qb_data(player_data):
    data = player_data['statistics']['splits']['categories']

    player_stats = {
        "gamesPlayed": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "gamesPlayed"),
        "fumblesLost": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "fumblesLost"),
        "totalPassingYards": next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "passingYards"),
        "avgPassingYards": next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "passingYardsPerGame"),
        "totalPassingTDs": next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "passingTouchdowns"),
        "totalPassAttempts": next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "passingAttempts"),
        "totalRushingYards": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYards"),
        "avgRushingYards": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYardsPerGame"),
        "totalRushingTDs": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingTouchdowns"),
        "totalRushAttempts": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingAttempts"),
        "avgRushAttempts": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "yardsPerRushAttempt"),
        "totalInterceptions": next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "interceptions"),
    }

    return player_stats


def clean_wr_data(player_data, team_data):
    data = player_data['statistics']['splits']['categories']
    
    player_stats = {
        "totalReceivingYards": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingYards"),
        "receivingYardsPerGame": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingYardsPerGame"),
        "totalReceivingTDs": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTouchdowns"),
        "totalTargets": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTargets"),
        "totalRushingYards": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYards"),
        "totalRushingTDs": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingTouchdowns"),
        "totalFumbles": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "fumbles"),
    }

    data = team_data['statistics']['splits']['categories']

    team_stats = { "teamPassAttempts": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTargets") }

    return {**player_stats, **team_stats}


def clean_rb_data(player_data, team_data):
    data = player_data['statistics']['splits']['categories']
    
    player_stats = {
        "totalRushingYards": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYards"),
        "rushingYardsPerGame": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYardsPerGame"),
        "totalRushingTDs": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingTouchdowns"),
        "totalRushAttempts": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingAttempts"),
        "totalReceivingYards": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingYards"),
        "receivingYardsPerGame": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingYardsPerGame"),
        "totalReceivingTDs": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTouchdowns"),
        "totalTargets": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTargets"),
        "totalFumbles": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "fumbles"),
    }

    data = team_data['statistics']['splits']['categories']

    team_stats = {
        "teamPassAttempts": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTargets"),
        "teamRushAttempts": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingAttempts"), 
    }
    
    return {**player_stats, **team_stats}


def clean_k_data(player_data):
    data = player_data['statistics']['splits']['categories']
    
    player_stats = {
        "extraPointAttempts": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "extraPointAttempts"),
        "extraPointPct": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "extraPointPct"),
        "extraPointsMade": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "extraPointsMade"),
        "fieldGoalAttempts": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts"),
        "fieldGoalAttempts1_19": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts1_19"),
        "fieldGoalAttempts20_29": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts20_29"),
        "fieldGoalAttempts30_39": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts30_39"),
        "fieldGoalAttempts40_49": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts40_49"),
        "fieldGoalAttempts50_59": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts50_59"),
        "fieldGoalAttempts60_99": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts60_99"),
        "fieldGoalPct": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalPct"),
        "fieldGoalsMade": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalsMade"),
        "fieldGoalsMade1_19": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalsMade1_19"),
        "fieldGoalsMade20_29": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalsMade20_29"),
        "fieldGoalsMade30_39": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalsMade30_39"),
        "fieldGoalsMade40_49": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalsMade40_49"),
        "fieldGoalsMade50_59": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalsMade50_59"),
        "fieldGoalsMade60_99": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalsMade60_99"),
        "longFieldGoalMade": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "longFieldGoalMade")
    }

    return player_stats
