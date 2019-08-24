from sqlalchemy import Table, Date, Boolean, Column, Enum, Binary, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from .investor_tag import investor_tag


class Investor(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    link = Column(String)
    min_investment = Column(DECIMAL)
    max_investment = Column(DECIMAL)

    history = relationship("InvestorInvestmentHistory", back_populates="investor")

    tags = relationship("Tag", secondary=investor_tag, backref="investors")
