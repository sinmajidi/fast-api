from fastapi import APIRouter,Query
from pydantic import BaseModel
from typing import Optional
router=APIRouter(prefix='/blog',tags=['blog'])

#it's a model for store articles in database
class BlogModel(BaseModel):
	title:str
	content:str
	nb_comments:int
	publisher:Optional[bool]


@router.post('/new/{id}')
def creat_post(blog:BlogModel,id:int,version:int):
	return {'massage':'ok','data':blog,'id':id,'version':version}
#Query is a way to complete docs for user,alias is for change query variables name
#for example   alias='Comment ID' change comment_id to Comment ID for shpwing to users
#deprecated is for make an api expired or not
@router.post('/new/{id}/comment')
def creat_comment(id:int,blog:BlogModel,comment_id:int=
Query(None,
      title='Title Text!',
      description='Description Text',
      alias='Comment ID',
      deprecated=False)):
	
	return {'blog':blog,
	        'id':id,
	        'comment_id':comment_id}
