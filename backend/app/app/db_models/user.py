from sqlalchemy import Enum, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
import enum


class Roles(str, enum.Enum):
    entrepreneur = "entrepreneur"
    investor = "investor"


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(Roles), nullable=False)

    passport = relationship("Passport", back_populates="user", uselist=False)
    entrepreneur = relationship("Entrepreneur", back_populates="user", uselist=False)
    investor = relationship("Investor", back_populates="user", uselist=False)
