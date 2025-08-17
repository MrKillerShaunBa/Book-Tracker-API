from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from . import schemas, models, utils, database
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth",tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    from jose import JWTError,jwt
    try:
        payload = jwt.decode(token, utils.SECRET_KEY, algorithms=[utils.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.post("/register",response_model=schemas.UserOut,summary="Register a new user",description="Create a new user account with a username and password.")
def register_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
    hashed_pwd = utils.hash_password(user.password)
    db_user = models.User(username=user.username, password = hashed_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login",response_model=schemas.TokenOut,summary="User Login",description="Login with your username and password to receive a JWT access token.\nSet \"grant_type\" to \"password\", username and password as they are and rest of the fields blank.")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not utils.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    access_token = utils.create_access_token(data={"sub":user.username},expires_delta=timedelta(minutes=30))
    return {"access_token":access_token, "token_type":"bearer"}