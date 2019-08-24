from sqlalchemy import Boolean, Column, Enum, Binary, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from enum import Enum, auto

from app.db.base_class import Base


class DocTypeEnum(Enum):
    entrepreneur_passport = auto()
    startup_business_plan = auto()


class Document(Base):
    id = Column(Integer, primary_key=True)
    type = Column(Enum(DocTypeEnum))
    document_name = Column(String)
    file = Column(Binary)

    # startup = relationship("Startup", back_populates="documents", uselist=False)
