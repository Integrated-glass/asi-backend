from sqlalchemy import Boolean, Column, Integer,ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Entrepreneur(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String, nullable=True)
    bio = Column(String)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="entrepreneur")

    startups = relationship("Startup", uselist=True, back_populates="owner")