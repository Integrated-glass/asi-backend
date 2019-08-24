from typing import Optional

from pydantic import BaseModel
import enum

from .base import Base
from .entrepreneur import EntrepreneurOrm
from .investor import InvestorOrm


class Roles(str, enum.Enum):
    entrepreneur = "entrepreneur"
    investor = "investor"


# Shared properties
class UserBase(Base):
    email: Optional[str] = None
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


class UserOrm(UserBase):
    entrepreneur: Optional[EntrepreneurOrm]
    investor: Optional[InvestorOrm]
