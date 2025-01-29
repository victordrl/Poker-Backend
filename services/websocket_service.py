# websocket_service.py

from fastapi import WebSocket
from typing import Dict
from schemas.websocket_schemas import *

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
            try:
                websocket = self.connections.pop(user_id)
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

class GameLoop:
    def __init__(self):
        self.players: Dict[int, Player] = {}
        self.order: List[int] = []
        self.end: int = True
        self.turn_start: int = 0
        self.turn: int = 0
        self.round: int = 0
        self.pote: int = 0
        self.bet_min: int = 1

    def add_player(self, user_id: int):
        if user_id not in self.players:
            self.players[user_id] = Player()
            
            if len(self.players) == 1:
                self.turn_start = user_id
                self.turn = self.turn_start
                print({'message': 'turn start', 'user': self.turn_start})

            print({'message': 'player added', 'user': user_id})
        else:
            print({'message': 'player exists', 'user': user_id})

    def start(self):
        if len(self.players) >= 2 and self.round == 0 and self.end:
            self.round: int = 0
            self.pote: int = 0
            self.bet_min: int = 1
            self.order.clear()
            self.order.extend(self.players.keys())
            self.end = False

            print({'message': 'game started', 'order': self.order})
        else:
            if len(self.players) < 2:
                print({'messaje': 'players incompled', 'players': len(self.players)})
            if self.round == 0:
                print({'message': 'game not started', 'round': self.round})

    def all_bet(self):
        all_bet = all(self.players[user_id].bet >= self.bet_min for user_id in self.order)

        if all_bet:
            self.round += 1
            print({'message': 'round incremented', 'new_round': self.round})
            self.turn = self.turn_start

            if self.round > 4:
                self.round = 0
        
        return all_bet

    def next_turn(self):
        if not self.order:
            print({'message': 'no players in the game'})
            return

        if self.turn in self.order:
            index = self.order.index(self.turn)
            next_index = (index + 1) % len(self.order)
            self.turn = self.order[next_index]

        print({'message': 'next turn', 'current_turn': self.turn})

    def update_jugada(self, user_id: int, jugada: Jugada):
        if user_id in self.players:
            self.players[user_id].hand = jugada.hand
            self.players[user_id].card_high = jugada.card_high
            self.players[user_id].bet = jugada.bet
            self.players[user_id].action = jugada.action

            if jugada.bet > self.bet_min:
                self.bet_min = jugada.bet
                print({'message': 'new bet_min', 'bet': self.bet_min})
            
            self.pote += jugada.bet

            if self.players[user_id].action == 'fold':
                self.order.pop(user_id)
            # else:
            #     self.next_turn()    

            print({'message': 'jugada updated', 'user': user_id, 'jugada': jugada})
            print({'message': 'pote update', 'pote': self.pote})
        else:
            print({'message': 'player not found', 'user': user_id})
    
    def get_players(self):
        for user_id, player in self.players.items():
            print({'players': f'{user_id}: {player}'})

        return self.players
