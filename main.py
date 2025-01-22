# main.py

from core.create_DB import *
from core.connection_DB import *
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def startup_event():
    database_valide()
    test_connection()
    
@app.get('/')
def welcome():
    return {'message': 'API POKER'}

