from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
]


INSTALLED_APPS += [
    'django.contrib.postgres',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fietsenrek',
        'USER': 'mrozek',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
