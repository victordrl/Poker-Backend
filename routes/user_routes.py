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
    return create_user_controller(db, user )

@router.post("/update/")
def root_update_user(user_update: UserUpdate, db: Session = Depends(get_session)):
    return update_user_controller(db, user_update)

@router.post("/log/")
def root_login_user(user: UserBase, db: Session = Depends(get_session)):
    return login_user_controller(db, user )

@router.get("/get/{user_id}")
def root_get_user(user_id: int, db: Session = Depends(get_session)):
    return get_user_controller(db, user_id)

@router.get("/get_rank/")
def root_get__user_rank(db: Session = Depends(get_session)):
    return get_users_rank_controller(db)

@router.delete("/out/{user_id}")
def root_delete_user(user_id: int, db: Session = Depends(get_session)):
    return delete_user_controller(db, user_id)
