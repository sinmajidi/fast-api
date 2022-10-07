from fastapi import FastAPI
import uvicorn
app=FastAPI()
@app.get('/')
def index():
	return 'homes'
@app.get('/blogs')
def get_blogs(page_size,count):
	return {'message':f'{page_size} ---- {count}'}
@app.get('/blog/{id}')
def get_blog(id):
	if id.isnumeric():
		return {'message':'blogs!','id':f'{id}'}
	else:
		return {'message': 'your entrance should be integer'}


uvicorn.run(app)

