import logging.config
import os

debug=os.environ.get('DEBUG','false')
if debug=='true':
    log_level=logging.DEBUG
else:
    log_level=logging.INFO

def getLogger(name):
    logging_config = dict(
        version = 1,
        disable_existing_loggers = False,
        formatters = {
            'f': {'format':
                  '%(levelname)s-%(asctime)s-%(module)s-%(funcName)s-%(lineno)d: %(message)s'
            }
        },
        handlers = {
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': log_level}
        },
        root = {
            'handlers': ['h'],
            'level': log_level,
        },
    )
    logging.config.dictConfig(logging_config)
    logger=logging.getLogger(name)
    logger.setLevel(log_level)
    return logger
