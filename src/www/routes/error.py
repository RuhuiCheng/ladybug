import logging
from werkzeug.exceptions import HTTPException
logger = logging.getLogger(__name__)


def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    logger.exception(e)