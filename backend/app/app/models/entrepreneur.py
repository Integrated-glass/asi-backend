from typing import Optional, List

from .base import Base
from .startup import StartupOrm


class EntrepreneurBase(Base):
    first_name: str
    last_name: str
    patronymic: Optional[str]
    bio: str
    startups: List[StartupOrm]


class EntrepreneurInDB(EntrepreneurBase):
    id: int


class EntrepreneurOrm(EntrepreneurBase):
    pass
