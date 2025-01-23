# table_schemas.py

from pydantic import BaseModel
from typing import List

class TableBase(BaseModel):
    code: str

class TableCreate(TableBase):
    state: bool
    password: str
    ciega: int

class TableInfo(TableBase):
    id: int
    state: bool
    password: str
    ciega: int

class Table_User(TableBase):    
    user_id: List[int]


