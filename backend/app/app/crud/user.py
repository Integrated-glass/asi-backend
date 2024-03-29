from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.db_models.user import User
from app.models import UserCreate, Roles  # , UserUpdate


def get(db_session: Session, *, user_id: int) -> Optional[User]:
    return db_session.query(User).filter(User.id == user_id).first()


def get_by_email(db_session: Session, *, email: str) -> Optional[User]:
    return db_session.query(User).filter(User.email == email).first()


def authenticate(db_session: Session, *, email: str, password_hash: str) -> Optional[User]:
    user = get_by_email(db_session, email=email)
    if not user:
        return None
    if not verify_password(password_hash, user.hashed_password):
        return None
    return user


# def get_multi(db_session: Session, *, skip=0, limit=100) -> List[Optional[User]]:
#     return db_session.query(User).offset(skip).limit(limit).all()


def create(db_session: Session, *, user_in: UserCreate) -> User:
    user = User(
        email=user_in.email,
        hashed_password=user_in.hashed_password,
        role=user_in.role
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

# def update(db_session: Session, *, user: User, user_in: UserUpdate) -> User:
#     user_data = jsonable_encoder(user)
#     update_data = user_in.dict(skip_defaults=True)
#     for field in user_data:
#         if field in update_data:
#             setattr(user, field, update_data[field])
#     if user_in.password:
#         passwordhash = get_password_hash(user_in.password)
#         user.hashed_password = passwordhash
#     db_session.add(user)
#     db_session.commit()
#     db_session.refresh(user)
#     return user
