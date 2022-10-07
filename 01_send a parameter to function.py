from fastapi import FastAPI,Response,status
import uvicorn
app=FastAPI()
@app.get('/')
def index():
	return 'homes'
@app.get('/blogs')
def get_blogs(page_size,count):
	return {'message':f'{page_size} ---- {count}'}
@app.get('/blog/{id}',status_code=status.HTTP_200_OK)
def get_blog(id,response:Response):
	if id.isnumeric():
		if int(id)<10:
			return {'message':'blogs!','id':f'{id}'}
		else:
			response.status_code=status.HTTP_404_NOT_FOUND
			return {'message': f'blog {id} not founde'}
	else:
		return {'message': 'your entrance should be integer'}


uvicorn.run(app)

