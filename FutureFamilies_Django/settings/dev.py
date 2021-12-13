from .base import *


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'future_families',

        'USER': 'ps',

        'PASSWORD': '<password>',

        'HOST': 'localhost',

        'PORT': '5432',
    }
}