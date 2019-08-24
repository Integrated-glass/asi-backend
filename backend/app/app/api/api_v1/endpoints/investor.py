from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.api.utils.security import get_current_user
from app.api.utils.db import get_db
from app.db_models.user import User
import app.crud.investor as crud
from app.models import InvestorProfile, InvestorForInvestorsListForIvestorsSearchByFiltersProxyFactoryAwareInvestorsSingletonFactory


router = APIRouter()


@router.get("/",
  response_model=InvestorProfile,
)
def get_by_investor_id(
  db: Session = Depends(get_db),
  current_user: User = Depends(get_current_user),
  *,
  investor_id: int,
):
  return crud.get(db, investor_id)

@router.get("/by_filters", response_model=List[InvestorForInvestorsListForIvestorsSearchByFiltersProxyFactoryAwareInvestorsSingletonFactory])
def get_by_tags(
  db: Session = Depends(get_db),
  current_user: User = Depends(get_current_user),
  *
  tags: List[int],
):
  pass


# @router.get("/by_startup_id", response_model=List[Item])
# def get_by_startup_id(
#   db: Session = Depends(get_db),
#   current_user: User = Depends(get_current_user),
#   *,
#   startup_id: int,
# ):
#   pass
