from fastapi import FastAPI,Response,status,HTTPException, Depends,APIRouter
from fastapi import Body
from .. import models , schemas , utils , oauth
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from ..database import engine  ,get_db
from sqlalchemy.orm import Session
from typing import List , Optional

router = APIRouter(tags=['Posts'])


while True:
    
    try:
       conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='6382***REVTIr', cursor_factory=RealDictCursor)
       cursor = conn.cursor()
       print("Database connection was successful")
       break
    except Exception as error:
       print("Connecting to database failed")
       print("Error: ", error)               
       time.sleep(2)  # Wait for 2 seconds before retrying             

my_posts = [{"title": "mukuls post", "menu": "mukuls menu", "rate": 5},
            {
    "title": "mukuls post2", "menu": "mukuls menu2", "rate": 4},
    {"title": "mukuls post3", "menu": "mukuls menu3", "rate": 3
}]    



@router.get("/posts")
async def root():
    posts = cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()   
    print(posts)
    return posts



@router.post("/posts", status_code=status.HTTP_201_CREATED)
def root(posts: schemas.Food):
    cursor.execute("INSERT INTO posts (title, menu, publish) VALUES (%s, %s, %s) RETURNING *""", 
                   (posts.title, posts.menu, posts.publish))
    new_post = cursor.fetchone()
    conn.commit()
    return new_post



@router.post("/posts1S", status_code=status.HTTP_201_CREATED , response_model=schemas.postresponse)
def root(post: dict, db: Session = Depends(get_db)):
    model_post = models.Post(**post)    
    db.add(model_post)
    db.commit()
    db.refresh(model_post)
    return model_post


@router.post("/posts_leatest", status_code=status.HTTP_201_CREATED)
async def root(foodies : schemas.Food):
    food_dict = foodies.dict()  
    food_dict['rate'] = randrange(0, 1000000)
    my_posts.append(food_dict)
    return food_dict


@router.get("/posts/latest")
def get_latest():
    post = my_posts[len(my_posts) - 1]
    return post

@router.get("/sqlalchemy", response_model=list[schemas.postresponse])
def test_posts(
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(oauth.get_current_user) , limit : int = 10, search: Optional[str] =  ""
):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).all()

    results = db.query(models.Post).join(
    models.Vote,
    models.Vote.post_id == models.Post.rate)
    print(results)
    return posts


@router.get("/posts/{rate}")
def get_post(rate: int, response: Response):
    cursor.execute("""SELECT * FROM posts WHERE rate = %s""", (str(rate)))
    post = cursor.fetchone()
    return  post
        
#    response.status_code = status.HTTP_404_NOT_FOUND
#    return {"message": "Post not found"}
     
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Post with rate {rate} not found")


@router.delete("/posts/{rate}")
def delete_post(rate: int):
    for index, post in enumerate(my_posts):
        if post['rate'] == rate:
            my_posts.pop(index)
            return {"message": f"Post with rate {rate} has been deleted"}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Post with rate {rate} not found")    


@router.put("/posts/{rate}")
def update_post(rate: int, updated_post: schemas.Food):
    cursor.execute("""UPDATE posts SET title = %s, menu = %s, publish = %s where rate = %s RETURNING *""", 
                   (updated_post.title, updated_post.menu, updated_post.publish, str(rate)))
    up_post = cursor.fetchone()
    conn.commit()

    if up_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with rate {rate} not found")
    return {"message": f"Post with rate {rate} has been updated", "updated_post": up_post}



@router.post("/postsjwt", status_code=status.HTTP_201_CREATED , response_model=schemas.postresponse)
def create_post(updated_post: schemas.PostCreate, db: Session = Depends(get_db),user_id: int = Depends(oauth.get_current_user)):
   
   print("User ID from token:", user_id.id) 
   new_post = models.Post(owner_id = user_id.id, **updated_post.dict())
   db.add(new_post)     
   db.commit()
   db.refresh(new_post)
   return new_post
    