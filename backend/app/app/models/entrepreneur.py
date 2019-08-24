from typing import Optional


from .base import Base


class EntrepreneurBase(Base):
    first_name: str
    last_name: str
    patronymic: Optional[str]

