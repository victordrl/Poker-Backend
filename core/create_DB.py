# create_DB.PY
from core.config_DB import DB_CONFIG
from core.conection_DB import connect_database

def create_database():
    try:
        # Conexión al servidor MySQL (sin base de datos específica)
        connection = connect_database(use_database=False)
        cursor = connection.cursor()

        # Verifica si la base de datos existe
        cursor.execute(f"SHOW DATABASES LIKE '{DB_CONFIG['database']}'")
        result = cursor.fetchone()
        
        if not result:
            print(f"La base de datos '{DB_CONFIG['database']}' no existe. Creándola...")
            cursor.execute(f"CREATE DATABASE {DB_CONFIG['database']}")
            print(f"Base de datos '{DB_CONFIG['database']}' creada con éxito.")
        else:
            print(f"La base de datos '{DB_CONFIG['database']}' ya existe.")

        cursor.close()
        connection.close()

        # Crear tablas
        create_tables()
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")
        raise

def create_tables():
    try:
        # Conexión a la base de datos específica
        connection = connect_database(use_database=True)
        cursor = connection.cursor()
        
        # Crear la tabla 'user'
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nick VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            money INT DEFAULT 1000,
            elo INT DEFAULT 300,
            wins INT DEFAULT 0,
            lost INT DEFAULT 0,
            tied INT DEFAULT 0,
            money_up INT DEFAULT 0,
            money_down INT DEFAULT 0,
            allin INT DEFAULT 0,
            calls INT DEFAULT 0,
            checks INT DEFAULT 0,
            folds INT DEFAULT 0
        )
        ''')
        print('Tabla "user" creada o ya existe.')

        # Crear la tabla 'tables'
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tables (
            id INT PRIMARY KEY AUTO_INCREMENT,
            code VARCHAR(5) NOT NULL UNIQUE,
            password VARCHAR(255) DEFAULT '0'
        )
        ''')
        print('Tabla "tables" creada o ya existe.')

        # Crear la tabla 'tables_users'
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tables_users (
            user_id INT NOT NULL,
            table_id INT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user(id),
            FOREIGN KEY (table_id) REFERENCES tables(id)
        )
        ''')
        print('Tabla "tables_users" creada o ya existe.')

        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error al crear las tablas: {e}")
        raise
