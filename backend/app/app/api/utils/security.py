import jwt
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN

from app import crud
from app.api.utils.db import get_db
from app.core import config
from app.core.jwt import ALGORITHM
from app.db_models.user import User
from app.models.token import TokenPayload

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/login/access-token")


def get_current_investor(
        db: Session = Depends(get_db), token: str = Security(reusable_oauth2)
):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    if token_data.role != "investor":
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="You are not an investor"
        )
    user = crud.investor.get(db, user_id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_entrepreneur(
        db: Session = Depends(get_db), token: str = Security(reusable_oauth2)
):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    if token_data.role != 'entrepreneur':
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="You are not an entrepreneur"
        )
    user = crud.entrepreneur.get(db, user_id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

