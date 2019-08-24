from datetime import timedelta

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.core import config
from app.core.jwt import create_access_token
from app.core.security import get_password_hash
from app.db_models.user import User as DBUser, Roles
# from app.models.msg import Msg
from app.models.token import Token
from app.models.user import User, UserCreate

router = APIRouter()


@router.post("/login/access-token", response_model=Token, tags=["login"])
def login_access_token(
        *, db: Session = Depends(get_db), email: str, hash_password: str
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        db, email=email, password_hash=hash_password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": user.id, "role": user.role}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/register", response_model=Token, tags=["login"])
def register(
        *,
        db: Session = Depends(get_db),
        user_in: UserCreate
):
    created_user = crud.user.create(db, user_in=user_in)
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": created_user.id, "role": None}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
#
# @router.post("/login/test-token", tags=["login"], response_model=User)
# def test_token(current_user: DBUser = Depends(get_current_user)):
#     """
#     Test access token
#     """
#     return current_user
