from fastapi import APIRouter

router=APIRouter(prefix='/blog',tags=['blog'])
@router.post('/new')
def creat_post():
	return {'massage':'ok'}
