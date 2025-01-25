# backend/routes/websocket_routes.py
from fastapi import APIRouter, WebSocket
from controllers.websocket_controller import *
from schemas.websocket_schemas import *

router = APIRouter()

@router.websocket("/test/{user_id}")
async def websocket_test(websocket: WebSocket, user_id: int):
    await websocket_controller(websocket, user_id)
