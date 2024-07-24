import os
from decouple import config
from django.core.wsgi import get_wsgi_application



if config('ENVIRONMENT') == 'DEVELOPMENT':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aob.settings.development')
elif config('ENVIRONMENT') == 'PRODUCTION':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aob.settings.production')
elif config('ENVIRONMENT') == 'WORKSPACE':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aob.settings.workspace')
elif os.environ.get('ENVIRONMENT') == 'WORKSPACE':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aob.settings.workspace')
else:
    try:
        from django.core.exceptions import ImproperlyConfigured
    except ImproperlyConfigured:
        raise ImproperlyConfigured(
        "Couldn't detect current environment."
        "Please set the ENVIRONMENT variable to either 'DEVELOPMENT', 'PRODUCTION', or 'WORKSPACE'"
    )
    

application = get_wsgi_application()
