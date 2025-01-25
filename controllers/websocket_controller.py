# backend/controllers/websocket_controller.py
from fastapi import WebSocket, WebSocketDisconnect
from services.websocket_service import *
from schemas.websocket_schemas import *

manager = WebSocketManager()

async def websocket_controller(websocket: WebSocket, user_id: int):
    try:
        await manager.connect(websocket, user_id)

        if user_id not in manager.connections:
            return
        
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(f'mesaje recibido {message}')
    except WebSocketDisconnect:
        await manager.disconnect(user_id)
