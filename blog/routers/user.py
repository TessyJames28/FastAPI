from ..database import get_db
from fastapi import APIRouter, Depends, status, HTTPException
from ..hashing import Hash
from ..schemas import User, ShowUser
from sqlalchemy.orm.session import Session
from .. import models


router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.post('', response_model=ShowUser)
def create_user(request: User, db:Session = Depends(get_db)):
    # Function that creates new user
    hashed_pwd = Hash.bcrypt(request.password)
    new_user = models.User(name = request.name, email = request.email, password = hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get('/{id}', response_model=ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    # Retrieve user based on given id
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"User with the id {id} not found")
    return user