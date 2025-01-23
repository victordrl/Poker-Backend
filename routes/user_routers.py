# user_routes.py

from fastapi import APIRouter, Depends
from sqlmodel import Session
from core.connection_DB import get_session
from schemas.user_schemas import *
from controllers.user_controller import *

router = APIRouter(
    prefix = '/users',
    tags = ['users']
)

@router.post("/add/")
def root_create_user(user: UserCreate, db: Session = Depends(get_session)):
    return create_user_controller(db = db, user = user)

@router.post("/update/")
def root_update_user(user: UserStat, db: Session = Depends(get_session)):
    return update_user_controller(db = db, user_update = user)

@router.post("/log/")
def root_login_user(user: UserBase, db: Session = Depends(get_session)):
    return login_user_controller(db = db, user = user)

@router.get("/get/{user_id}")
def root_get_user(user_id: int, db: Session = Depends(get_session)):
    return get_user_controller(db = db, user_id = user_id)

@router.delete("/out/{user_id}")
def root_delete_user(user_id: int, db: Session = Depends(get_session)):
    return delete_user_controller(db =db, user_id = user_id)
