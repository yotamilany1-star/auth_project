from sqlalchemy import Column, Integer, String, Boolean
from database import Base
#create a User model that inherits from the Base class
class User(Base):
    __tablename__ = "users"
#create columns for the User model
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="user")  # Added role column with default value "user"