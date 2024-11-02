from .common import *


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'