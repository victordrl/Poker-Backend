# table_services.py

from sqlmodel import Session, select, and_
from models.db_models import *
from schemas.table_schemas import *

def add_table(db: Session, table: TableCreate):
    query = select(Table).where(Table.code == table.code)
    db_table = db.exec(query).first()

    if db_table:
        raise ValueError('codigo de la mesa utilizado')
    
    new_table = Table(
        code = table.code,
        state = table.state,
        password = table.password,
        ciega = table.ciega
    )

    try:
        db.add(new_table)
        db.commit()
        db.refresh(new_table)
        return new_table
    except Exception as e:
        db.rollback()
        raise ValueError(f'error add_table {e}')
    
def log_table(db: Session, table: TableInfo):
    query = select(Table).where(
        and_(
            Table.code == table.code,
            Table.password == table.password
        )
    )
    db_table = db.exec(query).first()

    if not db_table:
        raise ValueError('code o password incorrectos')
    
    return db_table

def get_table(db: Session):
    query = select(Table)
    db_table = db.exec(query).all()

    return db_table

def out_table(db: Session, table_code: str):
    query = select(Table).where(Table.code == table_code)
    db_table = db.exec(query).first()

    if not db_table:
        raise ValueError('mesa no encontrada')
        
    try:
        db.delete(db_table)
        db.commit()
        print(f'mesa eliminada {db_table}')
    except Exception as e:
        db.rollback()
        raise ValueError(f'error out_table {e}')
