from aob.settings.main import *
from decouple import config
import os


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': config('SQLITE_DB_ENGINE') or os.environ.get('SQLITE_DB_ENGINE'),
        'NAME': os.path.join(BASE_DIR, config('SQLITE_DB_NAME') or os.environ.get('SQLITE_DB_NAME')),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django_error.log'),
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
