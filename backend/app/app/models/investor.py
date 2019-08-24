from typing import  List
from decimal import Decimal

from .base import Base
from .investor_investment_history import InvestorInvestmentHistoryOrm
from .tag import TagOrm
from .user import UserBase


class InvestorBase(Base):
    name: str
    link: str
    min_investment: Decimal
    max_investment: Decimal


class InvestorWithRelations(InvestorBase):
    history: List[InvestorInvestmentHistoryOrm]
    tags: List[TagOrm]
    user: UserBase


class InvestorInDB(InvestorWithRelations):
    id: int
    user_id: int


class InvestorOrm(InvestorWithRelations):
    pass


class InvestorProfile(InvestorBase):
    history: List[InvestorInvestmentHistoryOrm]


class InvestorCreate(InvestorBase):
    user_id: int
