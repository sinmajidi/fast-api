from fastapi import APIRouter
from fastapi import FastAPI,Response,status

router=APIRouter(prefix='/blog',tags=['blog'])



@router.get('/all', summary='get all blogs!', response_description='now you can see all the blogs')
def get_blogs(page_size, count):
	"""
	this api is for get all blogs
	- **page_size:** for getting page size
	- **count:** for getting blogs count
	"""
	return {'message': f'{page_size} ---- {count}'}


@router.get('/{id}', status_code=status.HTTP_200_OK, summary='get a blog!',
         description='this api is for '
                     'getting blogs')
def get_blog(id, response: Response):
	if id.isnumeric():
		if int(id) < 10:
			return {'message': 'blogs!', 'id': f'{id}'}
		else:
			response.status_code = status.HTTP_404_NOT_FOUND
			return {'message': f'blog {id} not founde'}
	else:
		return {'message': 'your entrance should be integer'}