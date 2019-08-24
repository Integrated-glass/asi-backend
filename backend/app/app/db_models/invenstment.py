from sqlalchemy import Table, Date, DECIMAL, Column, Enum, Binary, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Investment(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    link = Column(String, nullable=True)
    min_money = Column(DECIMAL, nullable=True)
    max_money = Column(DECIMAL, nullable=True)
