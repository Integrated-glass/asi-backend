from sqlalchemy import Table, Date, Boolean, Column, Enum, Binary, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Investment(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    link = Column(String)
    min_money = Column(DECIMAL)
    max_money = Column(DECIMAL)
