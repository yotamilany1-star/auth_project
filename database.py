from sqlalchemy import create_engine #pipe to the database
from sqlalchemy.orm import declarative_base, sessionmaker
 #sessionmaker #create a session to interact with the database
#declarative_base #create a base class for our models
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db" #what type of database we are using and where it is located
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) #create an engine to connect to the database


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #create a session to interact with the database

Base = declarative_base() #create a base class for our models

def get_db(): #create a dependency to get a database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()