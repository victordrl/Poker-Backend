# user_schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    nick: str
    email: EmailStr
    password: str

class UserCreate(UserBase):
    password_valide: str

class UserInfo(BaseModel):
    id: int
    nick: str
    email: EmailStr

class UserStat(UserInfo):
    money: Optional[int] = None
    elo: Optional[int] = None
    wins: Optional[int] = None
    lost: Optional[int] = None
    tied: Optional[int] = None
    money_up: Optional[int] = None
    money_down: Optional[int] = None
    allin: Optional[int] = None
    calls: Optional[int] = None
    check: Optional[int] = None
    folds: Optional[int] = None

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    id: int
    money: Optional[int] = None
    elo: Optional[int] = None
    wins: Optional[int] = None
    lost: Optional[int] = None
    tied: Optional[int] = None
    money_up: Optional[int] = None
    money_down: Optional[int] = None
    allin: Optional[int] = None
    calls: Optional[int] = None
    check: Optional[int] = None
    folds: Optional[int] = None

    class Config:
        orm_mode = True