from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'Fantasy NZ <no-reply@fantasynz.com>'


ALLOWED_HOSTS = [
    'www.fantasynz.com'
]

try:
    from .local import *
except ImportError:
    pass
