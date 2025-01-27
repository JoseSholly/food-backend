from .common import *


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

database_url= os.getenv("DATABASE_URL")

DATABASES["default"] = dj_database_url.parse(database_url)

ALLOWED_HOSTS=['127.0.0.1', 'localhost']

allowed_host_value= os.getenv("ALLOWED_HOSTS")

if allowed_host_value:
    ALLOWED_HOSTS.append(allowed_host_value)


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

SESSION_COOKIE_SECURE= True

CSRF_COOKIE_SECURE= True

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '').split(",")

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS= os.getenv("CSRF_TRUSTED_ORIGINS", '').split(",")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',  # Change the path as needed
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}