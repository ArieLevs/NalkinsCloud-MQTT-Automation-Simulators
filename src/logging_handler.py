
import logging
from configs import *

logger = logging.getLogger()

if ENVIRONMENT != 'production':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger = logging.LoggerAdapter(logger, LOGGING_EXTRA_FIELDS)
