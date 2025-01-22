# connection_DB.py

from sqlmodel import Session, create_engine
from core.config_DB import DB_CONFIG, url_connection

engine = create_engine(url_connection, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def test_connection():
    try:
        with engine.connect() as connection:
            print(f"Conexión exitosa: {connection}")
            return {"status": "success", "details": f"Connected: {connection}"}
    except Exception as e:
        print(f"Error al conectar database: {e}")
        return {"status": "error", "details": str(e)}

