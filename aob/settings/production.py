from aob.settings.main import *
import cloudinary
import cloudinary.api
import cloudinary.uploader
import dj_database_url
from decouple import config




DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DATABASES = {
    'default':dj_database_url.parse(os.getenv("DATABASE_URL") or config('DATABASE_URL'))
}


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUDNAME') or os.environ.get('CLOUDINARY_CLOUDNAME'),
    'API_KEY': config('CLOUDINARY_APIKEY') or os.environ.get('CLOUDINARY_APIKEY'),
    'API_SECRET': config('CLOUDINARY_APISECRET') or os.environ.get('CLOUDINARY_APISECRET'),
}

cloudinary.config(
    cloud_name = config('CLOUDINARY_CLOUDNAME'),
    api_key = config('CLOUDINARY_APIKEY'),
    api_secret = config('CLOUDINARY_APISECRET'),
)