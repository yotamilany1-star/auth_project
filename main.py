from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
import auth
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) #create the tables in the database
app = FastAPI() #create a FastAPI app instance

def get_db(): #create a dependency to get a database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup", response_model=schemas.userResponse) #endpoint for user signup
def create_user(user: schemas.userCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user: #check if the user already exists in the database
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login") #endpoint for user login
def login(user_credentials: schemas.userCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user or not auth.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": auth.create_access_token(data={"sub": user.email}), "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.userResponse) #endpoint to get the current user
def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user