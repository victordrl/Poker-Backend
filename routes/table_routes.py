# table_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from core.connection_DB import get_session
from schemas.table_schemas import *
from controllers.table_controller import *

router = APIRouter(
    prefix = '/table',
    tags = ['table']
)

@router.post("/add/")
def root_create_table(table: TableCreate , db: Session = Depends(get_session)):
    return create_table_controller(db, table)

@router.post("/log/")
def root_login_table(table: TableCreate, db: Session = Depends(get_session)):
    return login_table_controller(db, table)

@router.get("/get_list/")
def root_get_table(db: Session = Depends(get_session)):
    return get_table_controller(db)

@router.delete("/out/{table_code}")
def root_delete_table(table_code: str, db: Session = Depends(get_session)):
    return delete_table_controller(db, table_code)


