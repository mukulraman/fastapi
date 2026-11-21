from fastapi import FastAPI,Response,status,HTTPException, Depends,APIRouter
from fastapi import Body
from .. import models , schemas , utils
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from ..database import engine  ,get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(tags=['Users'])

@router.post("/users", status_code=status.HTTP_201_CREATED , response_model=schemas.Userresponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Hash the password before storing it in the database
    hashed_password = utils.hash_password(user.password)
    user.password = hashed_password
    new_user = models.user(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user     


@router.get("/users/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with id {id} not found")
    return user