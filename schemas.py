from pydantic import BaseModel, EmailStr, Field

class userCreate(BaseModel): #builder for user creation
    email: EmailStr
    password: str = Field(..., max_length=72)

class userResponse(BaseModel): #builder for user response
    id: int
    email: EmailStr
    is_active: bool
    role: str

    class Config:
        from_attributes = True  # enable our Pydantic model to read data from SQLAlchemy models