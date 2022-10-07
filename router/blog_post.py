from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
router=APIRouter(prefix='/blog',tags=['blog'])

class BlogModel(BaseModel):
	title:str
	content:str
	nb_comments:int
	publisher:Optional[bool]


@router.post('/new')
def creat_post(blog:BlogModel):
	return {'massage':'ok','data':blog}
