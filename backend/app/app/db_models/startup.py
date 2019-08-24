from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from .startup_tag import startup_tag


class Startup(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    logo = Column(String)  # base64

    document_id = Column(Integer, ForeignKey("document.id"))
    documents = relationship("Document", uselist=True)

    owner_id = Column(Integer, ForeignKey("entrepreneur.id"))
    owner = relationship("Entrepreneur", back_populates="startups")

    tags = relationship("Tag", secondary=startup_tag, backref='startups')
