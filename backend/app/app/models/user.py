from typing import Optional

from pydantic import BaseModel
import enum

from .base import Base


class Roles(str, enum.Enum):
    entrepreneur = "entrepreneur"
    investor = "investor"


# Shared properties
class UserBase(Base):
    email: Optional[str] = None
    is_superuser: Optional[bool] = False
    role: Roles


class UserBaseInDB(UserBase):
    id: int = None


# Properties to receive via API on creation
class UserCreate(UserBaseInDB):
    email: str
    hashed_password: str


# Additional properties to return via API
class User(UserBaseInDB):
    pass


# Additional properties stored in DB
class UserInDB(UserBaseInDB):
    hashed_password: str
