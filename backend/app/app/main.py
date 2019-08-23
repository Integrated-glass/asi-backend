from fastapi import FastAPI
from starlette.requests import Request

from app.api.api_v1.api import api_router
from app.core import config
from app.db.session import Session

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = FastAPI(title=config.PROJECT_NAME)

app.include_router(api_router, prefix=config.API_V1_STR)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next ):
    logger.debug("Entered middleware")
    request.state.db = Session()
    logger.debug(f"call_next type: {type(call_next)}, __name__ {call_next.__func__.__name__}")
    logger.debug("Before calling call_next")
    response = await call_next(request)  # TODO: Проблема с возвращаемыми типами: Приходит ORM модель, которая не dict
    logger.debug(f"Response: class - {type(response)} - {response}")
    request.state.db.close()
    logger.debug(f"Response: class - {type(response)} - {response}")
    return response

