#app/api/routes.py
from fastapi import APIRouter
from .query import get_nfl_team_data, get_nfl_player_data, get_schedule_by_team

router = APIRouter()

@router.get("/player_data")
async def get_player_data(player_id: str, team_id: str, pos_id: str):
    return get_nfl_player_data(player_id, team_id, pos_id)
