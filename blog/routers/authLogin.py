from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from datetime import timedelta
from ..database import get_db
from ..hashing import Hash
from ..schemas import Login, Token
from ..token import create_access_token
from .. import models


router = APIRouter(
    tags = ["Authentication"]
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Login function to authenticate user
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Invalid credentials")
    
    # Hashed password verification
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Incorrect password")
    
    # Generate JWT token and return it
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}) #expires_delta=access_token_expires
    
    return Token(access_token=access_token, token_type="bearer")