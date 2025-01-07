from ..database import get_db
from fastapi import APIRouter, Depends
from ..schemas import User, ShowUser
from sqlalchemy.orm.session import Session
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.post('', response_model=ShowUser)
def create_user(request: User, db:Session = Depends(get_db)):
    # Function that creates new user
    return user.create_user(request, db)



@router.get('/{id}', response_model=ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    # Retrieve user based on given id
    return user.get_users(id, db)