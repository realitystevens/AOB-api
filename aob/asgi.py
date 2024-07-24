import os
from decouple import config
from django.core.asgi import get_asgi_application



if config('ENVIRONMENT') == 'DEVELOPMENT':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aob.settings.development')
elif config('ENVIRONMENT') == 'PRODUCTION':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aob.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aob.settings.staging')


application = get_asgi_application()
