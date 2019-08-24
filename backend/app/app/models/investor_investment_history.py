from .base import Base
from pydantic import UrlStr
from decimal import Decimal


class InvestorInvestmentHistoryBase(Base):
    project_name: str
    link: UrlStr
    money_invested: Decimal


class InvestorInvestmentHistoryInDB(InvestorInvestmentHistoryBase):
    id: int


class InvestorInvestmentHistoryOrm(InvestorInvestmentHistoryBase):
    pass
