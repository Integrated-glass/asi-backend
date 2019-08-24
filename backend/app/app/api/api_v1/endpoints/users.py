from typing import Optional

from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_428_PRECONDITION_REQUIRED

from app.api.utils.security import get_current_user
from app.api.utils.db import get_db
from app.models.user import Roles
from app.models.entrepreneur import EntrepreneurCreate
from app.models.investor import InvestorCreate

import app.crud

# from fastapi.encoders import jsonable_encoder
# from pydantic.types import EmailStr
# from sqlalchemy.orm import Session
#
# from app import crud
# from app.api.utils.db import get_db
# from app.api.utils.security import get_current_active_superuser, get_current_active_user
# from app.core import config
# from app.db_models.user import User as DBUser
# from app.models.user import User, UserCreate, UserInDB, UserUpdate

router = APIRouter()


@router.put("/registration_finish")
def registration_finish(
        *,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
        role: Roles = Body(...),
        entrepreneur : Optional[EntrepreneurCreate],
        investor: Optional[InvestorCreate]
):
    if current_user.role is not None:
        raise HTTPException(
            status_code=HTTP_428_PRECONDITION_REQUIRED, detail="You have finished the registration"
        )
    elif current_user.role == Roles.investor:
        app.crud.investor.create(db, investor)
    elif current_user.role == Roles.entrepreneur:
        app.crud.entrepreneur.create(db, entrepreneur)

#
#
# @router.get("/", response_model=List[User])
# def read_users(
#     db: Session = Depends(get_db),
#     skip: int = 0,
#     limit: int = 100,
#     current_user: DBUser = Depends(get_current_active_superuser),
# ):
#     """
#     Retrieve users.
#     """
#     users = crud.user.get_multi(db, skip=skip, limit=limit)
#     return users
#
#
# @router.post("/", response_model=User)
# def create_user(
#     *,
#     db: Session = Depends(get_db),
#     user_in: UserCreate,
#     current_user: DBUser = Depends(get_current_active_superuser),
# ):
#     """
#     Create new user.
#     """
#     user = crud.user.get_by_email(db, email=user_in.email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this username already exists in the system.",
#         )
#     user = crud.user.create(db, user_in=user_in)
#     return user
#
#
# @router.put("/me", response_model=User)
# def update_user_me(
#     *,
#     db: Session = Depends(get_db),
#     password: str = Body(None),
#     full_name: str = Body(None),
#     email: EmailStr = Body(None),
#     current_user: DBUser = Depends(get_current_active_user),
# ):
#     """
#     Update own user.
#     """
#     current_user_data = jsonable_encoder(current_user)
#     user_in = UserUpdate(**current_user_data)
#     if password is not None:
#         user_in.password = password
#     if full_name is not None:
#         user_in.full_name = full_name
#     if email is not None:
#         user_in.email = email
#     user = crud.user.update(db, user=current_user, user_in=user_in)
#     return user
#
#
# @router.get("/me", response_model=User)
# def read_user_me(
#     db: Session = Depends(get_db),
#     current_user: DBUser = Depends(get_current_active_user),
# ):
#     """
#     Get current user.
#     """
#     return current_user
#
#
# @router.post("/open", response_model=User)
# def create_user_open(
#     *,
#     db: Session = Depends(get_db),
#     password: str = Body(...),
#     email: EmailStr = Body(...),
#     full_name: str = Body(None),
# ):
#     """
#     Create new user without the need to be logged in.
#     """
#     if not config.USERS_OPEN_REGISTRATION:
#         raise HTTPException(
#             status_code=403,
#             detail="Open user resgistration is forbidden on this server",
#         )
#     user = crud.user.get_by_email(db, email=email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this username already exists in the system",
#         )
#     user_in = UserCreate(password=password, email=email, full_name=full_name)
#     user = crud.user.create(db, user_in=user_in)
#     return user
#
#
# @router.get("/{user_id}", response_model=User)
# def read_user_by_id(
#     user_id: int,
#     current_user: DBUser = Depends(get_current_active_user),
#     db: Session = Depends(get_db),
# ):
#     """
#     Get a specific user by id.
#     """
#     user = crud.user.get(db, user_id=user_id)
#     if user == current_user:
#         return user
#     if not crud.user.is_superuser(current_user):
#         raise HTTPException(
#             status_code=400, detail="The user doesn't have enough privileges"
#         )
#     return user
#
#
# @router.put("/{user_id}", response_model=User)
# def update_user(
#     *,
#     db: Session = Depends(get_db),
#     user_id: int,
#     user_in: UserUpdate,
#     current_user: UserInDB = Depends(get_current_active_superuser),
# ):
#     """
#     Update a user.
#     """
#     user = crud.user.get(db, user_id=user_id)
#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="The user with this username does not exist in the system",
#         )
#     user = crud.user.update(db, user=user, user_in=user_in)
#     return user
