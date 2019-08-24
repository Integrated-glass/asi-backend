from sqlalchemy import Table, Boolean, Column, Enum, Binary, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from .startup_tag import startup_tag
from .investor_tag import investor_tag


class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    startups = relationship("Startup", secondary=startup_tag, back_populates="startup_tags")
    investors = relationship("Investor", secondary=investor_tag, back_populates="investor_tags")
