# main.py

from core.create_DB import *
from core.connection_DB import *
from fastapi import FastAPI
from routes.user_routers import router as user_router
app = FastAPI()

@app.on_event("startup")
def startup_event():
    database_valide()
    test_connection()
    
@app.get('/')
def welcome():
    return {'message': 'API POKER'}

app.include_router(user_router)


