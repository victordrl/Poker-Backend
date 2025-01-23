from sqlmodel import SQLModel, create_engine, text
from core.config_DB import DB_CONFIG, base_url_connection, url_connection
from models.db_models import User, Table

def database_valide():
    base_engine = create_engine(base_url_connection)

    try:
        with base_engine.connect() as connection:
            result = connection.execute(text(f"SHOW DATABASES LIKE '{DB_CONFIG['database']}'"))
            if not result.fetchone():
                print(f"database '{DB_CONFIG['database']}' no existe, creando...")
                connection.execute(text(f"CREATE DATABASE {DB_CONFIG['database']}"))
                print(f"database '{DB_CONFIG['database']}' creada correctamente.")
                create_tables()
            else:
                print(f"database '{DB_CONFIG['database']}' ya existe.")
    except Exception as e:
        print(f"error al validar o crear la base de datos: {e}")
        raise

def create_tables():
    engine = create_engine(url_connection)
    try:
        SQLModel.metadata.create_all(engine)
        print("tablas creadas correctamente.")
    except Exception as e:
        print(f"error al crear las tablas: {e}")
        raise
