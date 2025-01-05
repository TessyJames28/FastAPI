from passlib.context import CryptContext


# For password hashing
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


# Class to handle password hashing


class Hash():
    def bcrypt(password:str):
        hashed_pwd = pwd_context.hash(password)
        return hashed_pwd