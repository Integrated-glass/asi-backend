from sqlalchemy import  Column, Enum, Binary, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
import enum

from app.db.base_class import Base


class DocTypeEnum(enum.Enum):
    entrepreneur_passport = "entrepreneur_passport"
    startup_business_plan = "startup_business_plan"


class Document(Base):
    id = Column(Integer, primary_key=True)
    type = Column(Enum(DocTypeEnum))
    document_name = Column(String)
    file = Column(Binary)

    # startup = relationship("Startup", back_populates="documents", uselist=False)
