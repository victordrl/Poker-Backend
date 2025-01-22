# db_models.py

from sqlmodel import SQLModel, Field

class User(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    nick: str = Field(nullable = False)
    email: str = Field(nullable = False, unique = True)
    password: str = Field(nullable = False)
    money: int = Field(default = 1000)
    elo: int = Field(default = 300)
    wins: int = Field(default = 0)
    lost: int = Field(default = 0)
    tied: int = Field(default = 0)
    money_up: int = Field(default = 0)
    money_down: int = Field(default = 0)
    allin: int = Field(default = 0)
    calls: int = Field(default = 0)
    check: int = Field(default = 0)
    folds: int = Field(default = 0)

class Table(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    code: str = Field(nullable = False, unique = True, max_length = 5)
    password: str = Field(default = '0')

class Table_User(SQLModel, table = True):
    user_id: int = Field(foreign_key = 'user.id', primary_key = True)
    table_id: int = Field(foreign_key = 'table.id', primary_key = True)