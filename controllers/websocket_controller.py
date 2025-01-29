# backend/controllers/websocket_controller.py
from fastapi import WebSocket, WebSocketDisconnect
from services.websocket_service import *
from schemas.websocket_schemas import *

manager = WebSocketManager()

game = GameLoop()

async def websocket_controller(websocket: WebSocket, user_id: int):
    try:
        await manager.connect(websocket, user_id)

        if user_id not in manager.connections:
            return
        
        game.add_player(user_id)
        
        while True:
            game.start()
            message = await websocket.receive_json()
            if user_id == game.turn:
                jugada = Jugada(**message)
                game.update_jugada(user_id, jugada)
                game.next_turn()

    except WebSocketDisconnect:
        await manager.disconnect(user_id) 
