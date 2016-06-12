"""
Django settings for dental_system project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'dental_system.wsgi.application'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')i)ylmdc1a!2-2@1isx!z_1zm2ta#g^)o1#lasbuy6!p9v-n8y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, '_templates'),
)
# Application definition

ALLOWED_IMAGES = 'image/jpeg,image/png'

THIRD_PARTY_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': []
}
PROJECT_APPS = (
    'homepage',
    'rest_framework',
    'dentists',
    'customers',
    'consumables',
    'medical_records',
    'prices',
    'schedules',
    'transactions',
    'treatments',
    'vendors',
)

INSTALLED_APPS = tuple(set(THIRD_PARTY_APPS).union(set(PROJECT_APPS)))

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dental_system.urls'

WSGI_APPLICATION = 'dental_system.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, '_statics/root/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, '_statics/assets'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

NFS_PATH = ('/mnt/nfs/')
INBOUND_FILE_PATH = (NFS_PATH + 'inventory/inbound/')
OUTBOUND_FILE_PATH = (NFS_PATH + 'inventory/inbound/')
MAX_OUTBOUND_IDX_IN_FILE = 13
MAX_INBOUND_IDX_IN_FILE = 6
