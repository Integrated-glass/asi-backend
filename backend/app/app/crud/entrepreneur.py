from typing import Optional

from sqlalchemy.orm import Session

from app.db_models.entrepreneur import Entrepreneur
from app.models import EntrepreneurCreate


def get(db_session: Session, *, user_id: int) -> Optional[Entrepreneur]:
    return db_session.query(Entrepreneur).filter(Entrepreneur.id == user_id).first()


def create(db_session: Session,
           entrepreneur_to_create: EntrepreneurCreate) -> Entrepreneur:
    entrepreneur = Entrepreneur(**entrepreneur_to_create)
    return entrepreneur
