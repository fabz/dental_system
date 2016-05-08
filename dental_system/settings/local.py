from .base import *  # @UnusedWildImport

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dental_system',                      # Or path to database file if using sqlite3.
        'USER': 'dentaville',                      # Not used with sqlite3.
        'PASSWORD': 'dental123',  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DEBUG = True

NFS_PATH = '/mnt/nfs/'

IMAGE_URL_SPLITTER = 'localhost:81/'

# django-debug-toolbar requirements
INTERNAL_IPS = ('127.0.0.1',)
DATABASE_ENGINE = DATABASES['default']['ENGINE'].split('.')[-1]
# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
# }

# Trade Gecko
TG_TOKEN = "0dc2ef5847542168bb3af8788bc3381febb14c7b03353806fe2d1ccccf5c7fe2"

MIDDLEWARE_HOSTNAME = 'http://localhost:9999'
RECIPIENT_EMAIL_LIST = ['it_dev@gmail.co.id']
