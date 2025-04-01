from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app.core.database import get_db
from app.core.security import create_access_token
from app.schemas.user import UserCreate, UserRead

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 60


@router.post('/register', response_model=UserRead)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = crud.user.get_user_by_email(db, user_in.email)
    if user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return crud.user.create_user(db, user_in)


@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    user = crud.user.authenticate_user(
        db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Invalid credentials')

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': str(user.id)}, expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'bearer'}
