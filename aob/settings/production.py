from aob.settings.main import *
import cloudinary
import cloudinary.api
import cloudinary.uploader




DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'live.sqlite3'),
    }
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUDNAME'),
    'API_KEY': config('CLOUDINARY_APIKEY'),
    'API_SECRET': config('CLOUDINARY_APISECRET'),
}

cloudinary.config(
    cloud_name = config('CLOUDINARY_CLOUDNAME'),
    api_key = config('CLOUDINARY_APIKEY'),
    api_secret = config('CLOUDINARY_APISECRET'),
)