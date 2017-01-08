from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%7gj_r)rc52n_t^=7%=2r2+z#^c2%%f#5-n8+7*^f-4-#$sv7w'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '[::1]',
    '0.0.0.0',
    'fantasynz.shawn-lin.com'
]

try:
    from .local import *
except ImportError:
    pass
