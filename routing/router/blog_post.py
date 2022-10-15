from fastapi import APIRouter,Query,Body,Path
from pydantic import BaseModel
from typing import Optional,List
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
#Path is a integer validator
@router.post('/new/{id}/comment/{comment_id}')
def creat_comment(
									id:int,
                  blog:BlogModel,
                  comment_title:int=
											Query(default=None,
                      title='Title Text!',
                      description='Description Text',
                      alias='Comment Title',
                      deprecated=False),
                  contetnt:str=Body(Ellipsis,
                                    min_length=10,
                                    max_length=20,
                                    regex='^[A-Z].*'),
                  version:Optional[List[str]]=Query(None),
                  comment_id:int=Path(None,
                                      gt=5)):
# great than ----GT-----
# great or equal-----GE----
# less than-------LT-----
# less or equal------LE-----
	
	return {'blog':blog,
	        'id':id,
	        'comment_title':comment_title,
	        'contetnt':contetnt,
					'version':version,
	        'comment_id':comment_id
	        }
#body is a way to complete docs for user,Ellipsis means not use default value for content and user have to
#enter it.
#reqex help to make a format for inputs
