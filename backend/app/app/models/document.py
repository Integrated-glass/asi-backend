from typing import Optional, List
import enum

from .base import Base


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
