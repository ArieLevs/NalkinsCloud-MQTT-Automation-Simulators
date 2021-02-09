
import logging
import graypy
from configs import *

logger = logging.getLogger()

if ENVIRONMENT != 'production':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

if GRAYLOG_ENABLED:
    handler = graypy.GELFUDPHandler(host=GRAYLOG_HOST, port=GRAYLOG_PORT)
else:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s")
    handler.setFormatter(formatter)

logger.addHandler(handler)
logger = logging.LoggerAdapter(logger, EXTRA_FIELDS)
