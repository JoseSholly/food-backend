from .common import *


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

database_url= os.getenv("DATABASE_URL")

DATABASES["default"] = dj_database_url.parse(database_url)

ALLOWED_HOSTS = ['127.0.0.1',]
