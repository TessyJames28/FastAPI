from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # The login func is where the oauth2 will get the token from

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Cound not validate credentials",
        headers = {'WWW-Authenticate': "Bearer"}
    )

    return token.verify_token(data, credentials_exception)