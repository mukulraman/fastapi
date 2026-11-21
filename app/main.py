from fastapi import FastAPI,Response,status,HTTPException, Depends
from fastapi import Body
from . import models , schemas , utils
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .database import engine  ,get_db
from sqlalchemy.orm import Session
from typing import List
from .routers import post , user , auth , votes
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)



@app.get("/")
def root():
    return {"message": "FastAPI is running"}






