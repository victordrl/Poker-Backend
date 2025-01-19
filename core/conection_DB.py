# connection_DB.py

import mysql.connector
from mysql.connector import Error
from core.config_DB import DB_CONFIG

def connect_database(use_database):
    try:
        connetion = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            port = DB_CONFIG['port'],
            database=DB_CONFIG['database'] if use_database else None,
        )
        print(f'conexion : {DB_CONFIG['database']}')
        return connetion
    except Error as e:
        print(f'error conexion database: {e}')
        raise