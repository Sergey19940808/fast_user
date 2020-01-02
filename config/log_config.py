"""
This module for declaration config logging for app user
"""
from config.api_config import ApiConfig


class LogConfig:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(message)s',
                'datefmt': '%y %b %d, %H:%M:%S',
            },
        },
        'handlers': {
            'sanic_internal': {
                'level': 'INFO',
                'filename': f'{ApiConfig.BASE_DIR}/logs/sanic_internal.log',
                'formatter': 'simple',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 20,
                'backupCount': 10,
            },
            'sanic_errors': {
                'level': 'INFO',
                'filename': f'{ApiConfig.BASE_DIR}/logs/sanic_errors.log',
                'formatter': 'simple',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 20,
                'backupCount': 10,
            },
            'sanic_access': {
                'level': 'INFO',
                'filename': f'{ApiConfig.BASE_DIR}/logs/sanic_access.log',
                'formatter': 'simple',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 20,
                'backupCount': 10,
            },
        },
        'loggers': {
            'sanic.root': {
                'handlers': ['sanic_internal'],
                'level': 'INFO',
            },
            'sanic.error': {
                'handlers': ['sanic_errors'],
                'level': 'ERROR',
            },
            'sanic.access': {
                'handlers': ['sanic_access'],
                'level': 'INFO',
            },
        }
    }
