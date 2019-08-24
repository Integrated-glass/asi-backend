from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_superuser = Column(Boolean(), default=False)
    role = Column(String, nullable=False)

    passport = relationship("Passport", back_poplates="user", uselist=False)
    entrepreneur = relationship("Entrepreneur", back_populates="user",  uselist=False)
