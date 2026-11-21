from pydantic import BaseModel , ConfigDict, EmailStr , conint , Field
from ruamel.yaml import Optional 
from datetime import datetime
from typing import Annotated


class Food(BaseModel):
    title: str
    menu: str
    publish : bool = True  




class Postbase(BaseModel):
    title: str
    menu: str
    publish : bool = True   


class PostCreate(Postbase):
    pass


class Userout(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime   

class postresponse(Postbase):
    owner_id : int
    owner : Userout
    model_config = ConfigDict(from_attributes=True)
    


class UserCreate(BaseModel):
    email: EmailStr
    password: str     


class Userresponse(BaseModel):
    id: int
    email: EmailStr


class Userlogin(BaseModel):
    email: EmailStr
    password: str    

 

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None       


class Vote(BaseModel):
    post_id: int
    dir:  Annotated[int, Field(ge=0, le=1)]