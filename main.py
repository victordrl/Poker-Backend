# main.py

from core.create_DB import *
from core.connection_DB import *
from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.table_routes import router as table_router
from routes.websocket_routes import router as websocket_router

app = FastAPI()

@app.on_event("startup")
def startup_event():
    database_valide()
    test_connection()
    
@app.get('/')
def welcome():
    return {'message': 'API POKER'}

app.include_router(user_router)
app.include_router(table_router)

app.include_router(websocket_router)


