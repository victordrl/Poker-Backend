# table_controller.py

from fastapi import HTTPException, status
from sqlmodel import Session
from schemas.table_schemas import *
from services.table_services import *

def create_table_controller(db: Session, table: TableCreate):
    try:
        add_table(db, table)
        return {'message': 'mesa creada', 'table': table}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')
    
def login_table_controller(db: Session, table: TableInfo):
    try:
        log_table(db, table)
        return {'message': 'login correcto', 'table': table}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')

def get_table_controller(db: Session):
    try:
        list = get_table(db)
        return {'message': 'mesa encontrada', 'list_table': list}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')
    
def get_user_table_controller(db: Session, table_code: str):
    try:
        list_u_t = get_user_table(db, table_code)
        return {'message': 'mesa encontrada', 'lista': list_u_t}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')
    
def delete_table_controller(db: Session, table_code: str):
    try:
        out_table(db, table_code)
        return {'message': 'mesa eliminada', 'table': table_code}
    except ValueError as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'error interno')
    
