from .database import Base
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import TEXT, TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Boolean , ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts1"

    rate = Column(Integer, primary_key=True, nullable=False)
    title= Column(String, nullable=False)
    menu= Column(String, nullable=False)
    publish = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))  
    owner_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    owner = relationship("user")    


class user(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)  
    email= Column(String, nullable=False, unique=True)
    password= Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))   
    phone_number1 = Column(String) 

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts1.rate", ondelete="CASCADE"), primary_key=True)
