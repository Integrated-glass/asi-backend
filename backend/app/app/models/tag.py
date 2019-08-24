from typing import Optional, List

from .base import Base


class TagBase(Base):
    name: str


class TagInDB(TagBase):
    id: int


class TagOrm(TagBase):
    pass
