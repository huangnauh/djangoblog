"""
Django settings for django_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#from __future__ import absolute_import
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^&za0z9dnwny6vpfee#&xb8%%z!4-b$*#ty1ltv39#a7q_0*e+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGGING_CONFIG = None

# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'bootstrap_toolkit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
    'address',
    'djcelery',
    'celerytest',
    'book',
    'gunicorn',
    'postgresqltest',
)

TEMPLATE_DIRS = (
        './templates',
#        os.path.join(BASE_DIR,'templates').replace('\\','/'),
        )
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS +(
        'django.core.context_processors.request',)
BOOTSTRAP_ADMIN_SIDEBAR_MEMU = True

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'django_blog.urls'

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db.psycopg2',
        'USER': "ubuntu",
        "PASSWORD": "huanglibo",
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR,'static_resources').replace('\\','/')
#STATICFILES_DIRS = (
#       os.path.join(BASE_DIR,'static').replace('\\','/'), 
#       )
STATICFILES_FINDERS = (  
    'django.contrib.staticfiles.finders.FileSystemFinder',     
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',   
    )   
STATIC_URL = '/static/'

#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'huanglibo2010@gmail.com'
EMAIL_HOST_PASSWORD = 'lcnxpgxjikptsszn'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


import djcelery
djcelery.setup_loader()
BROKER_HOST = "0.0.0.0"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"
CELERY_IMPORTS=("celerytest.task")
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

