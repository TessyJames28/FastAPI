from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {
                        "check_same_thread": False})


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()


# The function helps to make the Session pased to the db on create func pydantic
# Thanks to the use of Depends from fastapi which allows the error-free starting of the server
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
