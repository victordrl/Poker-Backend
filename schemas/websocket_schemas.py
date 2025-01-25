# backend/schemas/websocket_schemas.py
from pydantic import BaseModel

class UserConnection(BaseModel):
    user_id: int
