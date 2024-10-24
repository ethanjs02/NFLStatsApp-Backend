#app/api/routes.py
from fastapi import APIRouter
from .query import get_nfl_team_data

router = APIRouter()

@router.get("/nfl-team-data")
async def get_data():
    return get_nfl_team_data()