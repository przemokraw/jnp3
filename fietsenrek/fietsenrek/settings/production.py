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
        'ENGINE': 'django_postgrespool',
        'NAME': 'fietsenrek',
        'USER': 'mrozek',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DATABASE_POOL_ARGS = {
    'max_overflow': 10,
    'pool_size': 5,
    'recycle': 300,
}
