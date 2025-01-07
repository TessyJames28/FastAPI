from fastapi import status, HTTPException
from sqlalchemy.orm.session import Session
from ..schemas import User
from .. import models
from ..hashing import Hash


def create_user(request: User, db: Session):
    # Helper function to handle user creation in the database
    hashed_pwd = Hash.bcrypt(request.password)
    new_user = models.User(name = request.name, email = request.email, password = hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(id: int, db: Session):
    # Helper function to handle users retrieval with given id
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"User with the id {id} not found")
    return user