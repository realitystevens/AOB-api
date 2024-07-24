from aob.settings.main import *
import cloudinary
import cloudinary.api
import cloudinary.uploader
import dj_database_url




DEBUG = False


DATABASES = {
    'default':dj_database_url.parse(os.getenv("DATABASE_URL"))
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