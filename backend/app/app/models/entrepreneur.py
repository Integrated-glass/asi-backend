from typing import Optional, List

from .base import Base
from .startup import StartupOrm


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
