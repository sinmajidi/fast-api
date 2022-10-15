from fastapi import FastAPI,Response,status
import uvicorn
app=FastAPI()
@app.get('/')
def index():
	return 'homes'

# you can add description using this command also and you can see tags,summary and description in /docs
# @app.get('/blogs',tags=['blog'],summary='get all blogs!', description = 'this api is for get all blogs'
# ,response_description='now you can see all the blogs')
@app.get('/blogs',tags=['blog'],summary='get all blogs!',response_description='now you can see all the blogs')
def get_blogs(page_size,count):
	
	"""
	this api is for get all blogs
	- **page_size:** for getting page size
	- **count:** for getting blogs count
	"""
	return {'message':f'{page_size} ---- {count}'}


@app.get('/blog/{id}',status_code=status.HTTP_200_OK,tags=['blog'],summary='get a blog!',description='this api is for '
                                                                                                     'getting blogs')
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

