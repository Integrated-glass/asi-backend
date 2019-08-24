from typing import Optional, List
import enum
from pydantic import BaseModel
from pydantic import UrlStr
from decimal import Decimal


class Base(BaseModel):
    class Config:
        orm_mode = True


class Roles(str, enum.Enum):
    entrepreneur = "entrepreneur"
    investor = "investor"


class UserBase(Base):
    email: Optional[str] = None
    role: Roles


class DocumentTypes(str, enum.Enum):
    entrepreneur_passport = "entrepreneur_passport"
    startup_business_plan = "startup_business_plan"


class DocumentBase(Base):
    type: DocumentTypes
    document_name: str
    file: bytes


class DocumentInDB(DocumentBase):
    id: int


class DocumentOrm(DocumentBase):
    pass


class TagBase(Base):
    name: str


class TagInDB(TagBase):
    id: int


class TagOrm(TagBase):
    pass


class StartupBase(Base):
    name: str
    description: str
    logo: str  # base64
    documents: List[DocumentOrm]
    tags: List[TagOrm]


class StartupInDB(StartupBase):
    id: int


class StartupOrm(StartupBase):
    pass


class EntrepreneurBase(Base):
    first_name: str
    last_name: str
    patronymic: Optional[str]
    bio: str


class EntrepreneurWithRelations(EntrepreneurBase):
    startups: List[StartupOrm]


class EntrepreneurInDB(EntrepreneurWithRelations):
    id: int


class EntrepreneurCreate(EntrepreneurBase):
    user_id: int


class EntrepreneurOrm(EntrepreneurBase):
    pass


class Token(Base):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    user_id: int = None


class InvestorInvestmentHistoryBase(Base):
    project_name: str
    link: UrlStr
    money_invested: Decimal


class InvestorInvestmentHistoryInDB(InvestorInvestmentHistoryBase):
    id: int


class InvestorInvestmentHistoryOrm(InvestorInvestmentHistoryBase):
    pass


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


# Shared properties


class UserBaseInDB(UserBase):
    id: int = None


# Properties to receive via API on creation
class UserCreate(UserBaseInDB):
    email: str
    hashed_password: str


# Additional properties to return via API
class User(UserBaseInDB):
    pass


# Additional properties stored in DB
class UserInDB(UserBaseInDB):
    hashed_password: str


class UserOrm(UserBase):
    entrepreneur: Optional[EntrepreneurOrm]
    investor: Optional[InvestorOrm]
