# user_controller.py

from fastapi import HTTPException, status
from sqlmodel import Session
from schemas.user_schemas import *
from services.user_services import *

def create_user_controller(db: Session, user: UserCreate):
    try:
        new_user = add_user(db, user)
        return {'message': 'usuario creado', 'user': new_user}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')

def update_user_controller(db: Session, user_update: UserUpdate):
    try:
        update_user(db, user_update)
        return {'message': 'usuario actualizado', 'user': user_update}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')
    
def login_user_controller(db: Session, user: UserBase):
    try:
        result = log_user(db, user)
        return {'message': 'usuario comprovado', 'user': result}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')
    
def get_user_controller(db: Session, user_id: int):
    try:
        get_user(db, user_id)
        return {'message': 'usuario encontrado', 'user': user_id}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')
    
def delete_user_controller(db: Session, user_id: int):
    try:
        out_user(db, user_id)
        return {'message': 'usuario eliminado', 'user': user_id}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')
    