import logging.config
from pathlib import Path

DEPARTMENT_NAME = 'osa'
SERVER_LOGS_PATH = Path('/var/log').joinpath(DEPARTMENT_NAME)
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'logfmt': {
            'format': 'ts=%(asctime)s level=%(levelname)s msg="%(message)s"',
            'datefmt': '%Y-%m-%dT%H:%M:%S',
        },
        'logfmt_debug': {
            'format': 'ts=%(asctime)s level=%(levelname)s module="%(name)s" '
                      'msg="%(message)s"',
            'datefmt': '%Y-%m-%dT%H:%M:%S',
        },
    },
    'handlers': {
        'stdout_info': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'logfmt',
            'stream': 'ext://sys.stdout',
        },
        'stdout_debug': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'logfmt_debug',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'root': {'level': 'INFO', 'handlers': ['stdout_info']},
    },
}


def get_logfile_path(name):
    path = SERVER_LOGS_PATH  # logpath for server
    if not path.exists():
        path = Path(__file__).parent.joinpath('logs')  # local logs dirrectory
    path = path.joinpath(name)
    path.mkdir(parents=True, exist_ok=True)
    return path.joinpath(f'{name}.log')


def init_logger(name, verbose=False, nologfile=False):
    root_handlers = LOGGING_CONFIG['loggers']['root']['handlers']
    logfile = not nologfile
    if logfile:
        logfile_conf = {'class': 'logging.handlers.RotatingFileHandler',
                        'level': 'DEBUG',
                        'formatter': 'logfmt',
                        'backupCount': 2,
                        'filename': get_logfile_path(name)}
        LOGGING_CONFIG['handlers'].update(logfile=logfile_conf)
        root_handlers.append('logfile')
    if verbose:
        LOGGING_CONFIG['loggers']['root'].update(level='DEBUG')
        root_handlers[root_handlers.index('stdout_info')] = 'stdout_debug'
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(name)
    return logger
