#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config


def main():
    """Run administrative tasks."""

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
        
        
        
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
