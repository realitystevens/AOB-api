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