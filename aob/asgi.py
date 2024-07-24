import os
from decouple import config
from django.core.asgi import get_asgi_application



if config('ENVIRONMENT') == 'PRODUCTION':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aob.settings.production')
elif os.environ.get('ENVIRONMENT') == 'STAGING' or config('ENVIRONMENT') == 'STAGING' or config('ENVIRONMENT') == 'DEVELOPMENT':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aob.settings.development')
else:
    try:
        from django.core.exceptions import ImproperlyConfigured
    except ImproperlyConfigured:
        raise ImproperlyConfigured(
        "Couldn't detect current environment."
        "Please set the ENVIRONMENT variable to either 'DEVELOPMENT', 'PRODUCTION', or 'STAGING'"
    )


application = get_asgi_application()
