# websocket_service.py

from fastapi import WebSocket
from typing import Dict

class WebSocketManager:
    def __init__(self):
        self.connections: Dict[int, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user_id: int):
        if user_id in self.connections:
            await websocket.close()
            print({'message': 'connection denied', 'details':'user ya conectado', 'user': user_id})
            return
        
        if len(self.connections) < 8:
            await websocket.accept()
            self.connections[user_id] = websocket
            print({'message': 'connection succes', 'total conectados': len(self.connections), 'new user': user_id})
        else:
            await websocket.close()
            print({'message': 'connection denied', 'details':'limite de conexiones', 'user': user_id})
    
    async def disconnect(self, user_id: int):
        if user_id in self.connections:
            websocket = self.connections.pop(user_id)
            try:
                # await websocket.close()
                print({'message': 'connection closed', 'total connected': len(self.connections), 'old user': user_id})
            except Exception as e:
                print({'message': 'error closing connection', 'error': str(e)})
        else:
            print({'message': 'connection not found', 'user': user_id})

    async def all_message(self, message: str):
        for user_id, websocket in self.connections.items():
            await websocket.send_text(f'{user_id}: {message}')

    async def get_user(self):
        return list(self.connections.keys())