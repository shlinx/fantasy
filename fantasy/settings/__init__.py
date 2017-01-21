try:
    from .local import ENVIRONMENT
except ImportError:
    ENVIRONMENT = 'production'

if ENVIRONMENT == 'production':
    from .production import *
elif ENVIRONMENT == 'dev':
    from .dev import *
