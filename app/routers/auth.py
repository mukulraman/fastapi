from fastapi import FastAPI,Response,status,HTTPException, Depends,APIRouter

from sqlalchemy.orm import Session
from .. import models , schemas , utils , database , oauth

router = APIRouter(tags=['Authentication'])

@router.post("/login" , response_model=schemas.Token)
def login(user_credentials: schemas.Userlogin, db: Session = Depends(database.get_db)):
    user = db.query(models.user).filter(models.user.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    #create and return a token or session here if needed

    access_token = oauth.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}  # Replace with actual token generation logic






