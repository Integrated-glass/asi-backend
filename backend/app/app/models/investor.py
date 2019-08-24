from typing import  List
from decimal import Decimal

from .base import Base
from .investor_investment_history import InvestorInvestmentHistoryOrm
from .tag import TagOrm


class InvestorBase(Base):
    name: str
    link: str
    min_investment: Decimal
    max_investment: Decimal

    history: List[InvestorInvestmentHistoryOrm]
    tags: List[TagOrm]


class InvestorInDB(InvestorBase):
    id: int


class InvestorOrm(InvestorBase):
    pass
