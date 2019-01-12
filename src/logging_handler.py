
import logging
import graypy
from configs import *

logger = logging.getLogger(PROJECT_NAME)

if ENVIRONMENT != 'production':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

if GRAYLOG_ENABLED:
    handler = graypy.GELFHandler(host=GRAYLOG_HOST,
                                 port=GRAYLOG_PORT)
else:
    handler = logging.StreamHandler()

logger.addHandler(handler)
logger = logging.LoggerAdapter(logger, EXTRA_FIELDS)
