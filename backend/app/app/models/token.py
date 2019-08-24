from pydantic import BaseModel
from .base import Base


class Token(Base):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    user_id: int = None
