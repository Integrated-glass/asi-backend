from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.entrepreneur import EntrepreneurOrm
from app.db_models.entrepreneur import Entrepreneur as EntrepreneurDB
import app.crud.entrepreneur

from app.api.utils.db import get_db
from app.api.utils.security import get_current_entrepreneur

router = APIRouter()


@router.get('/me', response_model=EntrepreneurOrm)
def getme(
        db: Session = Depends(get_db),
        current_entrepreneurship: EntrepreneurDB = Depends(get_current_entrepreneur)
):
    return current_entrepreneurship
