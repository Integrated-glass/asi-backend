from sqlalchemy import Boolean, Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Passport(Base):
    id = Column(Integer, primary_key=True, index=True)
    series = Column(String(4))
    number = Column(String(6), unique=True)
    issued_code = Column(String(6))
    issued_date = Column(Date)

    user_id = Column(Integer, ForeignKey("User.id"))
    user = relationship("User", back_populates="passport")
