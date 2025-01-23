# user_services.py

from sqlmodel import Session, select, and_
from models.db_models import *
from schemas.user_schemas import *

def add_user(db: Session, user: UserCreate):
    query = select(User).where(User.email == user.email)
    db_user = db.exec(query).first()

    if db_user:
        raise ValueError('correo utilizado')
    
    if user.password != user.password_valide:
        raise ValueError('password no coincide')
    
    new_user = User(
        nick = user.nick,
        email = user.email,
        password = user.password
    )

    try: 
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise ValueError(f'error add_user {e}')
    
def update_user(db: Session, user_update: UserUpdate):
    query = select(User).where(User.id == user_update.id)
    db_user = db.exec(query).first()
    
    if not db_user:
        raise ValueError('usuario no encontrado')
    
    db_user.money = user_update.money
    db_user.elo = user_update.elo
    db_user.wins = user_update.wins
    db_user.lost = user_update.lost
    db_user.tied = user_update.tied
    db_user.money_up = user_update.money_up
    db_user.money_down = user_update.money_down
    db_user.allin = user_update.allin
    db_user.calls = user_update.calls
    db_user.check = user_update.check
    db_user.folds = user_update.folds


    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise ValueError(f'error update_user {e}')
    
def log_user(db: Session, user: UserBase):
    query = select(User).where(
        and_(
            User.email == user.email,
            User.password == user.password
        )
    )
    db_user = db.exec(query).first()

    if not db_user:
        raise ValueError('usuario no encontrado')

    # desenpaquetado del objeto user como parametros a userstat
    user_stat = UserStat(**db_user.__dict__)

    return user_stat

def get_user(db: Session, user_id: id):
    query = select(User).where(User.id == user_id)
    db_user = db.exec(query).first()
    
    if not db_user:
        raise ValueError('usuario no encontrado')

    return db_user


def out_user(db: Session, user_id: int):
    query = select(User).where(User.id == user_id)
    db_user = db.exec(query).first()

    if not db_user:
        raise ValueError('usuario no encontrado')

    try:
        db.delete(db_user)
        db.commit()
        print(f'user eliminado: {user_id}')
    except Exception as e:
        db.rollback()
        raise ValueError(f'error delete_user {e}')