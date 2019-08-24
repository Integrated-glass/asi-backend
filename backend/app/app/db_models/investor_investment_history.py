from sqlalchemy import Column,  Integer, ForeignKey, String, DECIMAL
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class InvestorInvestmentHistory(Base):
    id = Column(Integer, primary_key=True, index=True)

    investor_id = Column(Integer, ForeignKey("investor.id"))
    investor = relationship("Investor", back_populates="history")

    project_name = Column(String)
    link = Column(String)
    money_invested = Column(DECIMAL)
