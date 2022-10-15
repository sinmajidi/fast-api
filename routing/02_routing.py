from fastapi import FastAPI
import uvicorn
from routing.router import blog_get
from routing.router import blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
	return 'homes'




uvicorn.run(app)

