from fastapi import FastAPI
from routing.router import blog_get
from routing.router import blog_post
from ORM_SQLALCHEMY.database import models
from ORM_SQLALCHEMY.database.db import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
models.Base.metadata.create_all(engine)

@app.get('/')
def hello():
    return 'hello world'