def clean_qb_data(player_data):
    data = player_data['statistics']['splits']['categories']

    player_stats = {
        "gamesPlayed": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "gamesPlayed"),
        "totalPassingYards": next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "passingYards"),
        "avgPassingYards": round(next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "passingYardsPerGame"), 2),
        "totalPassingTDs": next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "passingTouchdowns"),
        "totalPassAttempts": next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "passingAttempts"),
        "totalRushingYards": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYards"),
        "avgRushingYards": round(next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYardsPerGame"), 2),
        "totalRushingTDs": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingTouchdowns"),
        "totalRushAttempts": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingAttempts"),
        "avgRushAttempts": round(next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "yardsPerRushAttempt"), 2),
        "totalInterceptions": next(stat["value"] for stat in data[1]["stats"] if stat["name"] == "interceptions"),
        "fumblesLost": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "fumblesLost"),
    }

    return player_stats


def clean_wr_data(player_data, team_data):
    data = player_data['statistics']['splits']['categories']
    
    player_stats = {
        "gamesPlayed": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "gamesPlayed"),
        "totalReceivingYards": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingYards"),
        "receivingYardsPerGame": round(next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingYardsPerGame"), 2),
        "totalReceivingTDs": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTouchdowns"),
        "totalReceptions": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTargets"),
        "totalRushingYards": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYards"),
        "totalRushingTDs": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingTouchdowns"),
        "totalFumbles": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "fumbles"),
    }

    data = team_data['statistics']['splits']['categories']

    team_stats = { "teamPassAttempts": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTargets") }

    player_stats["targetShare"] = str(round((float(player_stats["totalReceptions"]) / float(team_stats["teamPassAttempts"])) * 100, 2))


    return player_stats


def clean_rb_data(player_data, team_data):
    data = player_data['statistics']['splits']['categories']
    
    player_stats = {
        "gamesPlayed": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "gamesPlayed"),
        "totalRushingYards": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYards"),
        "rushingYardsPerGame": round(next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingYardsPerGame"), 2),
        "totalRushingTDs": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingTouchdowns"),
        "totalRushAttempts": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingAttempts"),
        "totalReceivingYards": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingYards"),
        "receivingYardsPerGame": round(next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingYardsPerGame"), 2),
        "totalReceivingTDs": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTouchdowns"),
        "totalReceptions": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTargets"),
        "totalFumbles": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "fumbles"),
    }

    data = team_data['statistics']['splits']['categories']

    team_stats = {
        "teamPassAttempts": next(stat["value"] for stat in data[3]["stats"] if stat["name"] == "receivingTargets"),
        "teamRushAttempts": next(stat["value"] for stat in data[2]["stats"] if stat["name"] == "rushingAttempts"), 
    }
    

    player_stats["targetShare"] = str(round((float(player_stats["totalReceptions"]) / float(team_stats["teamPassAttempts"])) * 100, 2))
    player_stats["rushShare"] = str(round((float(player_stats["totalRushAttempts"]) / float(team_stats["teamRushAttempts"])) * 100, 2))

    return player_stats


def clean_k_data(player_data):
    data = player_data['statistics']['splits']['categories']
    
    player_stats = {
        "gamesPlayed": next(stat["value"] for stat in data[0]["stats"] if stat["name"] == "gamesPlayed"),
        "extraPointAttempts": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "extraPointAttempts"),
        "extraPointPct": round(next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "extraPointPct"), 2),
        "extraPointsMade": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "extraPointsMade"),
        "fieldGoalAttempts": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts"),
        "fieldGoalAttempts1_19": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts1_19"),
        "fieldGoalAttempts20_29": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts20_29"),
        "fieldGoalAttempts30_39": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts30_39"),
        "fieldGoalAttempts40_49": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts40_49"),
        "fieldGoalAttempts50_59": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts50_59"),
        "fieldGoalAttempts60_99": next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalAttempts60_99"),
        "fieldGoalPct": round(next(stat["value"] for stat in data[4]["stats"] if stat["name"] == "fieldGoalPct"), 2),
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