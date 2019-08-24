from sqlalchemy.orm import Session

from app.db_models.investor import Investor
from app.models.investor import InvestorCreate


def get(db: Session, investor_id: int):
  return db.query(Investor).filter(Investor.id == investor_id).first()


def create(db: Session, investor_to_create: InvestorCreate):
  investor = Investor(**investor_to_create)

  db.add(investor)
  db.commit()
  db.refresh(investor)
  return investor
