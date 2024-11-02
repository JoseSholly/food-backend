from .common import *


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

database_url= os.getenv("DATABASE_URL")

DATABASES["default"] = dj_database_url.parse(database_url)

ALLOWED_HOSTS = ['127.0.0.1',]

STATIC_URL = '/static/'


# This production code might break development mode, so we check # This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
    WHITENOISE_AUTOREFRESH = True
    WHITENOISE_USE_FINDERS = True
    WHITENOISE_COMPRESS = True
    WHITENOISE_MANIFEST_STRICT = True 
