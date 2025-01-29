# websocket_schemas.py

from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class Jugada(BaseModel):
    hand: int = 0
    card_high: int = 0
    bet: int = 0
    action: str = ''

class Player(Jugada):
    card: Dict[int, str] = {}
    turn_on: bool = False

class PlayerInfo(Player):
    id: int
    nick: str
    money: int

class MesaInfo(BaseModel):
    user: List[PlayerInfo] = []
    card: Dict[int, str] = {}
    pote: int = 0
    turn_id: int = 0
    bet_min: int
    round: int = 0