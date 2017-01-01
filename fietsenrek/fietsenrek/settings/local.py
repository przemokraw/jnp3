from .base import *

DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
