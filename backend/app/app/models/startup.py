from typing import Optional, List

from .base import Base
from .document import DocumentOrm
from .tag import TagOrm


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
