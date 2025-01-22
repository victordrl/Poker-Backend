# config_DB.py

# Configuración de la base de datos MySQL
DB_CONFIG = {
    "user": "root",       
    "password": "1709",
    "host": "Localhost",        
    "port": 3306,               
    "database": "POKER"
}

base_url_connection = (
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}"
)


url_connection = (
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)