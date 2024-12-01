#app/api/routes.py
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from io import BytesIO
from .query import get_nfl_player_data, get_player_headshot


router = APIRouter()

@router.get("/player_data")
async def get_player_data(player_id: str, team_id: str, pos_id: str):
    return get_nfl_player_data(player_id, team_id, pos_id)

@router.get("/player_headshot")
async def get_headshot(url: str):
    image_data = get_player_headshot(url)
    
    return StreamingResponse(BytesIO(image_data), media_type="image/png")