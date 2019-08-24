# Import all the models, so that Base has them before being
# imported by Alembic

from app.db.base_class import Base  # noqa
# from app.db_models import *
from app.db_models.user import User  # noqa
from app.db_models.startup import Startup
from app.db_models.investor import Investor
from app.db_models.document import Document
from app.db_models.entrepreneur import Entrepreneur
from app.db_models.invenstment import Investment
from app.db_models.investor_investment_history import InvestorInvestmentHistory
from app.db_models.passport import Passport
from app.db_models.startup import Startup
from app.db_models.tag import Tag
